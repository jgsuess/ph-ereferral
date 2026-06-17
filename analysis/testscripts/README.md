# Hole-Demonstrating TestScript Scenarios

These scenarios describe sequences of FHIR operations that exercise each
specification hole. They are written as narrative TestScript outlines, compatible
with the `fhir-frog` test infrastructure on `upstream/80-workflow-state-machine`.

Each scenario is structured as: **setup → test operations → assertions → verdict**.
The verdict shows what the FHIR server returns vs. what the state machine expects.

The point of each scenario is that **the FHIR server accepts the operations**
(verdict: PASS from the server) but **the state machine forbids the path**
(verdict: FAIL from the model). This is the gap the specification needs to close.

---

## TS-A01 — Zombie Referral (State Skipping)

**Path tested:** [start] → completed (bypassing requested/received/accepted)

```
Setup:
  POST Patient          → Patient/ts-a01-patient
  POST Organization     → Org/ts-a01-referring
  POST Organization     → Org/ts-a01-receiving
  POST Practitioner     → Prac/ts-a01-md
  POST PractitionerRole → PracRole/ts-a01-role

Test:
  1. POST ServiceRequest (status=active, performer=Org/ts-a01-receiving)
     → SR/ts-a01-ref
  2. POST Task (status=completed, focus=SR/ts-a01-ref,
                executionPeriod.start=T, executionPeriod.end=T+1s,
                output[0].type=#consultation-summary,
                output[0].value="Service performed.")
     → Task/ts-a01-ghost

Assert:
  3. GET Task/ts-a01-ghost
     assert Task.status = "completed"                  → PASS (server accepts)
     assert Task.businessStatus = #accepted            → PASS
     assert Task.executionPeriod.end.exists() = true   → PASS

Verdict:
  FHIR server: 201 Created, all assertions pass.
  State machine model: FAIL — no create_draft, send_referral, receive_referral,
    accept_referral transitions occurred; jumped directly to completed.
  Clinical truth: No service was performed. The output text is fabricated.

What a real fix looks like:
  The server SHOULD return 422 Unprocessable Entity if a Task is POSTed
  in status=completed without prior Task state evidence (e.g., no existing
  Task/AuditEvent showing accepted state was reached).
  This requires custom server-side logic, not a FHIR profile invariant.
```

---

## TS-B01 — The Silent Cancellation

**Path tested:** SR active → Task accepted → SR revoked → no Task update

```
Setup: (same supporting resources as TS-A01)

Test:
  1. POST ServiceRequest (status=active) → SR/ts-b01-ref
  2. POST Task (status=requested, focus=SR/ts-b01-ref) → Task/ts-b01-req
  3. PUT Task/ts-b01-req (status=accepted, owner=Org/ts-b01-receiving) → 200 OK
  4. PUT ServiceRequest/ts-b01-ref (status=revoked) → 200 OK
     [No update to Task/ts-b01-req]

Assert:
  5. GET Task/ts-b01-req
     assert Task.status = "accepted"                  → PASS (still accepted!)
     assert Task.focus.resolve().status = "active"    → FAIL (SR is revoked)
                                                         (FHIRPath cross-resource
                                                          assertion; most validators
                                                          will not check this)

Verdict:
  FHIR server: all operations 200 OK; Task still shows accepted.
  State machine: no transition defined for "SR revoked while Task accepted".
  Clinical truth: receiving facility is unaware the referral was cancelled.

What a real fix looks like:
  Option A: An invariant on ERefTask — severity #error:
    "Task.focus.resolve().status != 'revoked' or Task.status = 'cancelled'"
    (Requires a server that evaluates cross-resource FHIRPath.)
  Option B: IG narrative SHALL: "When a ServiceRequest is revoked, any active
    Tasks referencing it MUST be updated to status=cancelled by the cancelling
    system."
  Option C: FHIR Subscription defined in IG — server notifies Task owners
    when SR.status changes to revoked.
```

---

## TS-C01 — The Status Schism

**Path tested:** POST Task with status=accepted AND businessStatus=#rejected

```
Test:
  1. POST Task (status=accepted, businessStatus=#rejected,
                focus=SR/ts-c01-ref, requester=PracRole/ts-c01-role,
                owner=Org/ts-c01-receiving)
     → Task/ts-c01-schism

Assert:
  2. GET Task/ts-c01-schism
     assert Task.status = "accepted"                  → PASS
     assert Task.businessStatus.coding.code = "rejected" → PASS
     [Both assertions pass on the same resource]

Verdict:
  FHIR server: 201 Created, both assertions pass.
  Clinical semantics: one resource carries two opposite conclusions.
  System A (reads status):         patient is accepted, proceed.
  System B (reads businessStatus): patient is rejected, find another facility.

What a real fix looks like:
  Add invariant to ERefTask — severity #error:
    "(Task.status = 'accepted' implies
       Task.businessStatus.coding.where(system='...ereferral-workflow')
         .code = 'accepted')
     and
     (Task.status = 'rejected' implies
       Task.businessStatus.coding.where(system='...ereferral-workflow')
         .code.memberOf('ereferral-receiving-response-rejected'))"
  Define EReferralReceivingResponseRejected value set = {#rejected, #referred-onward}.
```

---

## TS-D02 — Multi-Task Race Condition

**Path tested:** Two different systems POST accepted Tasks for the same ServiceRequest

```
Test:
  1. POST ServiceRequest (status=active) → SR/ts-d02-shared
  2. POST Task (status=requested, focus=SR/ts-d02-shared) → Task/ts-d02-req

  [Simulating two systems acting concurrently:]
  3. POST Task (status=accepted, focus=SR/ts-d02-shared,
                owner=Org/ts-d02-facility-a) → Task/ts-d02-acc-a
  4. POST Task (status=accepted, focus=SR/ts-d02-shared,
                owner=Org/ts-d02-facility-b) → Task/ts-d02-acc-b

Assert:
  5. GET Task?focus=SR/ts-d02-shared
     assert count of Tasks with status=accepted = 2  → PASS
     assert Task/ts-d02-acc-a.owner = Org/ts-d02-facility-a → PASS
     assert Task/ts-d02-acc-b.owner = Org/ts-d02-facility-b → PASS

Verdict:
  FHIR server: both POSTs succeed; search returns 2 accepted Tasks.
  State machine: undefined — the model assumes one Task per referral.
  Clinical truth: patient expected at two facilities simultaneously.

What a real fix looks like:
  IG SHOULD add a conditional create pattern: POST Task with
  If-None-Exist: focus=<SR-id>&status=accepted
  This uses FHIR conditional create to prevent duplicate accepted Tasks.
  Alternatively: a CapabilityStatement-level constraint declaring that
  servers MUST reject a second accepted Task for the same ServiceRequest.
```

---

## TS-F01 — Attachment Overload

**Path tested:** POST a ServiceRequest with many large inline attachments

```
Test:
  1. POST ServiceRequest with supportingInfo containing:
     40 × DocumentReference resources, each with:
       content[0].attachment.contentType = "application/pdf"
       content[0].attachment.data = [base64-encoded 500 KB PDF]
     Total payload: ~20 MB of base64 JSON

Assert:
  2. HAPI server response:
     IF server has no configured body size limit:
       → 201 Created  [server accepted 20 MB payload]
     IF server has default HAPI limit (~10 MB by default):
       → 413 Payload Too Large  [server rejected]
     The IG specifies neither outcome. Behavior is implementation-defined.

Verdict:
  FHIR server: depends entirely on server configuration.
  IG: completely silent on attachment handling.
  National scale (10,000 facilities × 40 refs/day × 20 MB each):
    = 8 TB of attachment data ingested per day.
    = 2.9 PB per year.

What a real fix looks like:
  Option A: IG normative constraint: "Attachments MUST use DocumentReference
    with external URL (content.attachment.url) rather than inline data
    (content.attachment.data) for files exceeding 100 KB."
  Option B: Reference IHE MHD (Mobile Health Documents) profile for
    attachment management with external storage.
  Option C: CapabilityStatement constraint declaring max attachment size.
  Option D: SMART on FHIR Bulk Data export pattern for large clinical summaries.
```
