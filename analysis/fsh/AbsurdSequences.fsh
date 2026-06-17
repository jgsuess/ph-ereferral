// =============================================================================
// PH eReferral v0.1 — Absurd / Counter-Intuitive Example Sequences
//
// These FSH instances are profile-CONFORMANT — they compile without error in
// SUSHI and pass FHIR profile validation — but they represent sequences that
// the state machine model forbids, clinical common sense rejects, or both.
//
// Purpose: demonstrate the gap between what the profiles permit and what the
// workflow narrative intends. Each instance is named Absurd-<hole-id>-<label>.
//
// To compile:  cp analysis/fsh/AbsurdSequences.fsh input/fsh/examples/
//              sushi .    # expect 0 Errors
//
// Supporting instances from ERefTaskExamples.fsh are reused where possible.
// Local supporting resources are defined at the bottom of this file.
// =============================================================================

// =============================================================================
// A-01  ZOMBIE REFERRAL
// Task is created directly in "completed" status.
// The receiving facility was never notified. The service was never performed.
// State machine: FAIL  |  Profile validation: PASS
// =============================================================================

Instance: Absurd-A01-ZombieTask
InstanceOf: ERefTask
Usage: #example
Title: "A-01 Zombie Referral — Task created directly completed"
Description: """
  Hole A-01: The Task is created in 'completed' status without ever passing through
  'requested', 'received', or 'accepted'. The output claims the service was performed.
  Profile validator: PASS. State machine: FAIL.
  Real-world risk: falsified audit trail of care delivery.
"""

* status = #completed
* businessStatus = EReferralWorkflowCS#accepted "Accepted"
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* authoredOn = "2026-06-17T09:00:00+08:00"
* lastModified = "2026-06-17T09:01:00+08:00"
* executionPeriod.start = "2026-06-17T09:00:00+08:00"
* executionPeriod.end   = "2026-06-17T09:01:00+08:00"
* output[0].type = EReferralWorkflowCS#consultation-summary "Consultation summary"
* output[=].valueCodeableConcept.text = "Ultrasound performed. Normal findings."
// 60 seconds from creation to completion. The ultrasound was never performed.
// No receiving facility was contacted. The output text is fabricated.


// =============================================================================
// A-02  BACKWARD TRAVERSAL
// Task moves from completed back to requested.
// The ereferral-task-status-valid invariant is #warning only — it does not
// prevent setting status = requested on a previously completed Task.
// State machine: FAIL  |  Profile validation: PASS (with warning)
// =============================================================================

Instance: Absurd-A02-BackwardTask
InstanceOf: ERefTask
Usage: #example
Title: "A-02 Backward Traversal — Task re-opened after completion"
Description: """
  Hole A-02: This snapshot represents a Task that was 'completed' and is now
  being set back to 'requested' — a backward transition. The profile's
  ereferral-task-status-valid invariant is severity #warning and only checks
  the current value, not the direction of travel.
  Real-world risk: invalidation of billing events, audit trail manipulation.
"""

* status = #requested
// Previous value was #completed. This is the re-opened state.
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* authoredOn = "2026-06-17T08:00:00+08:00"
* lastModified = "2026-06-17T11:00:00+08:00"
// lastModified is 3 hours after authoredOn — the Task was created, then
// (presumably) completed, and is now being moved back to requested.
* note[0].text = "Referral completed at 09:30. Status rolled back to requested at 11:00."


// =============================================================================
// A-05  UNMODELED STATUS
// Task uses 'in-progress' — permitted by the invariant but undefined
// in the workflow model. What does an in-progress referral Task mean?
// State machine: FAIL  |  Profile validation: PASS
// =============================================================================

Instance: Absurd-A05-InProgressTask
InstanceOf: ERefTask
Usage: #example
Title: "A-05 Unmodeled Status — Task.status = in-progress"
Description: """
  Hole A-05: 'in-progress' is permitted by ereferral-task-status-valid but is
  not defined in the workflow state machine. The IG provides no guidance on
  what this means for a referral task or how to transition out of it.
"""

* status = #in-progress
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* authoredOn = "2026-06-17T09:00:00+08:00"
// A FHIR validator will accept this. The workflow model has no 'in-progress' state.
// A dashboard querying Task.status will display "in-progress" with no defined meaning.


// =============================================================================
// B-01  CANCELLATION GAP
// ServiceRequest is revoked while Task remains accepted.
// No cross-resource invariant links their statuses.
// State machine: N/A (cross-resource)  |  Both profiles: PASS independently
// =============================================================================

Instance: Absurd-B01-RevokedServiceRequest
InstanceOf: ERefServiceRequest
Usage: #example
Title: "B-01 Cancellation Gap — ServiceRequest revoked"
Description: """
  Hole B-01 (part 1): The ServiceRequest has been revoked (patient withdrew consent).
  The Task that references this SR still shows 'accepted'. No cascade occurs.
"""

* status = #revoked
* intent = #order
* code = $sct#3457005 "Patient referral"
* subject = Reference(Absurd-Patient)
* authoredOn = "2026-06-17T08:30:00+08:00"
* requester = Reference(Absurd-PractitionerRole)
* performer = Reference(Absurd-OrgReceiving)
* reasonCode = $sct#29857009 "Chest pain"

Instance: Absurd-B01-AcceptedTaskForRevokedSR
InstanceOf: ERefTask
Usage: #example
Title: "B-01 Cancellation Gap — Task accepted, SR already revoked"
Description: """
  Hole B-01 (part 2): Task is in 'accepted' status pointing to a revoked
  ServiceRequest. The receiving facility has allocated capacity for a
  referral that no longer exists. Profile validator: PASS on both resources.
"""

* status = #accepted
* businessStatus = EReferralWorkflowCS#accepted "Accepted"
* intent = #order
* focus = Reference(Absurd-B01-RevokedServiceRequest)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* authoredOn = "2026-06-17T08:30:00+08:00"
* lastModified = "2026-06-17T09:15:00+08:00"
// The Task.focus references a revoked ServiceRequest.
// ERefTask has no invariant checking Task.focus.resolve().status.


// =============================================================================
// B-02  PRE-DELIVERY CLOSURE
// ServiceRequest in draft; Task already completed.
// The referral was "completed" before it was sent.
// State machine: FAIL  |  Profile validation: PASS
// =============================================================================

Instance: Absurd-B02-DraftServiceRequest
InstanceOf: ERefServiceRequest
Usage: #example
Title: "B-02 Pre-Delivery Closure — ServiceRequest in draft"
Description: "Hole B-02 (part 1): ServiceRequest is still in draft — not yet sent."

* status = #draft
* intent = #order
* code = $sct#3457005 "Patient referral"
* subject = Reference(Absurd-Patient)
* authoredOn = "2026-06-17T09:00:00+08:00"
* requester = Reference(Absurd-PractitionerRole)

Instance: Absurd-B02-CompletedTaskForDraftSR
InstanceOf: ERefTask
Usage: #example
Title: "B-02 Pre-Delivery Closure — Task completed, SR still draft"
Description: """
  Hole B-02 (part 2): Task is completed while the referenced ServiceRequest is
  still in draft. The workflow 'completed' before the referral order was sent.
  Profile validator: PASS. Clinical reality: impossible.
"""

* status = #completed
* businessStatus = EReferralWorkflowCS#accepted "Accepted"
* intent = #order
* focus = Reference(Absurd-B02-DraftServiceRequest)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* authoredOn = "2026-06-17T09:00:00+08:00"
* lastModified = "2026-06-17T09:00:01+08:00"
* executionPeriod.start = "2026-06-17T09:00:00+08:00"
* executionPeriod.end   = "2026-06-17T09:00:01+08:00"
// 1-second execution period. Draft ServiceRequest. Completed Task.
// A FHIR validator approves all three resources independently.


// =============================================================================
// C-01  STATUS vs BUSINESSSTATUS CONTRADICTION
// Task.status = accepted; Task.businessStatus = rejected.
// Two systems reading different fields get opposite conclusions.
// State machine: FAIL  |  Profile validation: PASS
// =============================================================================

Instance: Absurd-C01-ContradictoryStatus
InstanceOf: ERefTask
Usage: #example
Title: "C-01 Contradictory Status — accepted + rejected simultaneously"
Description: """
  Hole C-01: Task.status = 'accepted' (FHIR canonical field) but
  Task.businessStatus = EReferralWorkflowCS#rejected (eReferral business layer).
  System A reads Task.status → 'accepted'. System B reads Task.businessStatus
  → 'rejected'. Both are reading a conformant resource correctly.
  No cross-field invariant exists to catch this contradiction.
"""

* status = #accepted
* businessStatus = EReferralWorkflowCS#rejected "Rejected"
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* statusReason.text = "Capacity full — but we also accepted it, sort of."
// The status and businessStatus are mutually exclusive in clinical semantics.
// Both pass profile validation independently.


// =============================================================================
// C-02a  DUAL-REJECTED — Genuine rejection
// C-02b  DUAL-REJECTED — Referred onward
// Both use Task.status = rejected. A search on status=rejected returns both.
// State machine: C-02a valid, C-02b valid  |  Both PASS
// =============================================================================

Instance: Absurd-C02a-GenuinelyRejected
InstanceOf: ERefTask
Usage: #example
Title: "C-02a Dual-Rejected — Genuinely rejected (no onward facility)"
Description: """
  Hole C-02 (part a): This Task represents a genuine rejection — the receiving
  facility cannot take the case and no alternative is given.
  Task.status = rejected.
"""

* status = #rejected
* businessStatus = EReferralWorkflowCS#rejected "Rejected"
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* statusReason.text = "Receiving facility cannot take the case. No onward facility identified."

Instance: Absurd-C02b-ReferredOnwardLooksRejected
InstanceOf: ERefTask
Usage: #example
Title: "C-02b Dual-Rejected — Referred onward (uses same Task.status=rejected)"
Description: """
  Hole C-02 (part b): This Task represents a referred-onward case — a different
  clinical outcome — but uses the same Task.status = rejected.
  GET Task?status=rejected returns BOTH this and Absurd-C02a.
  The clinical difference is only visible via businessStatus.
"""

* status = #rejected
* businessStatus = EReferralWorkflowCS#referred-onward "Referred onward"
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* statusReason = EReferralWorkflowCS#capacity-full "Capacity full"
* output[0].type = EReferralWorkflowCS#onward-referral-request "Onward referral request"
* output[=].valueCodeableConcept.text = "Referred to Eastern District Medical Center."
// Note: output value is a CodeableConcept text string, not a FHIR Reference.
// See hole C-04 for the reference resolution problem.


// =============================================================================
// C-04  UNRESOLVABLE OUTPUT REFERENCE
// Task.output for onward referral uses valueCodeableConcept.text instead of
// valueReference. The onward ServiceRequest cannot be dereferenced.
// State machine: N/A  |  Profile validation: PASS
// =============================================================================

Instance: Absurd-C04-UnresolvableOutput
InstanceOf: ERefTask
Usage: #example
Title: "C-04 Unresolvable Output — onward referral identified by text, not Reference"
Description: """
  Hole C-04: Task.output should use valueReference to point to the onward
  ServiceRequest so clients can dereference it. Instead, the example (and the
  profile, which allows value[x]) uses valueCodeableConcept with a text string.
  The onward SR cannot be programmatically retrieved from this output.
"""

* status = #rejected
* businessStatus = EReferralWorkflowCS#referred-onward "Referred onward"
* intent = #order
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* output[0].type = EReferralWorkflowCS#onward-referral-request "Onward referral request"
* output[=].valueCodeableConcept = EReferralWorkflowCS#onward-referral-request
* output[=].valueCodeableConcept.text = "Onward ServiceRequest: Absurd-E03-SR-002"
// "Absurd-E03-SR-002" is just a string. No system can GET it from a FHIR server.
// A valueReference would be: * output[=].valueReference = Reference(Absurd-E03-SR-002)


// =============================================================================
// D-01  ANONYMOUS ACCEPTANCE
// Task.status = accepted with no Task.owner.
// Who accepted this referral? The data does not say.
// State machine: FAIL  |  Profile validation: PASS (owner is 0..1 MS)
// =============================================================================

Instance: Absurd-D01-AnonymouslyAccepted
InstanceOf: ERefTask
Usage: #example
Title: "D-01 Anonymous Acceptance — accepted Task with no owner"
Description: """
  Hole D-01: The Task is accepted but Task.owner is absent. Per the profile,
  Task.owner is 0..1 MS — optional. No invariant requires owner to be set
  when status = accepted. Which facility accepted? Unknown.
  Real-world risk: no responsible party on record; no one to contact.
"""

* status = #accepted
* businessStatus = EReferralWorkflowCS#accepted "Accepted"
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* authoredOn = "2026-06-17T10:00:00+08:00"
// owner is deliberately absent — this passes profile validation
// A care coordinator querying Task.owner gets nothing.


// =============================================================================
// D-02a / D-02b  MULTI-TASK RACE CONDITION
// Two Tasks both accepted for the same ServiceRequest by different facilities.
// Both are profile-conformant. No uniqueness constraint exists.
// =============================================================================

Instance: Absurd-D02a-AcceptedByFacilityA
InstanceOf: ERefTask
Usage: #example
Title: "D-02a Multi-Task Race — Facility A accepts"
Description: """
  Hole D-02 (part a): Facility A creates an accepted Task for SR/obs-002.
"""

* status = #accepted
* businessStatus = EReferralWorkflowCS#accepted "Accepted"
* intent = #order
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* authoredOn = "2026-06-17T10:00:00+08:00"

Instance: Absurd-D02b-AcceptedByFacilityB
InstanceOf: ERefTask
Usage: #example
Title: "D-02b Multi-Task Race — Facility B also accepts (same ServiceRequest)"
Description: """
  Hole D-02 (part b): Facility B creates a SECOND accepted Task for the same
  ServiceRequest. Both D-02a and D-02b reference Absurd-SR-Active.
  A FHIR search GET Task?focus=Absurd-SR-Active returns both Tasks.
  Two facilities claim ownership. The patient is expected at two locations.
"""

* status = #accepted
* businessStatus = EReferralWorkflowCS#accepted "Accepted"
* intent = #order
* focus = Reference(Absurd-SR-Active)    // SAME ServiceRequest as D-02a
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgFacilityB)  // DIFFERENT owner
* authoredOn = "2026-06-17T10:01:00+08:00"


// =============================================================================
// E-02  COMPLETED vs CLOSED SEMANTIC AMBIGUITY
// A rejected referral is closed using status = completed.
// The FHIR semantic of "completed" implies successful task execution.
// =============================================================================

Instance: Absurd-E02-CompletedRejection
InstanceOf: ERefTask
Usage: #example
Title: "E-02 Completed vs Closed — rejected referral marked completed"
Description: """
  Hole E-02: After the referral is rejected, the initiating facility closes the
  workflow by setting Task.status = completed (via the 'complete_rejected'
  transition). FHIR's Task.status = completed conventionally means the task was
  accomplished. Here it means 'we finished processing a rejection'.
  Dashboard impact: this appears in 'completed referrals' counts as a success.
"""

* status = #completed
* businessStatus = EReferralWorkflowCS#rejected "Rejected"
* intent = #order
* code = $sct#3457005 "Patient referral"
* focus = Reference(Absurd-SR-Active)
* for = Reference(Absurd-Patient)
* requester = Reference(Absurd-PractitionerRole)
* owner = Reference(Absurd-OrgReceiving)
* authoredOn = "2026-06-17T08:00:00+08:00"
* lastModified = "2026-06-17T10:30:00+08:00"
* executionPeriod.start = "2026-06-17T08:00:00+08:00"
* executionPeriod.end   = "2026-06-17T10:30:00+08:00"
* statusReason.text = "Receiving facility rejected referral. No onward facility found. Workflow closed."
// Task.status = completed, but the patient was never seen.
// A dashboard query Task?status=completed returns this alongside genuine completions.


// =============================================================================
// E-03  INFINITE ONWARD CHAIN
// Three ServiceRequests in a replaces chain; all active; no termination.
// =============================================================================

Instance: Absurd-E03-SR-001
InstanceOf: ERefServiceRequest
Usage: #example
Title: "E-03 Infinite Chain — Hop 1 ServiceRequest"
Description: "First referral in an infinite onward chain."

* status = #active
* intent = #order
* code = $sct#3457005 "Patient referral"
* subject = Reference(Absurd-Patient)
* authoredOn = "2026-06-17T08:00:00+08:00"
* requester = Reference(Absurd-PractitionerRole)
* performer = Reference(Absurd-OrgReceiving)
* reasonCode = $sct#29857009 "Chest pain"

Instance: Absurd-E03-SR-002
InstanceOf: ERefServiceRequest
Usage: #example
Title: "E-03 Infinite Chain — Hop 2 ServiceRequest (replaces Hop 1)"
Description: "Second referral; Facility A was full, referred onward."

* status = #active
* intent = #order
* replaces = Reference(Absurd-E03-SR-001)
* code = $sct#3457005 "Patient referral"
* subject = Reference(Absurd-Patient)
* authoredOn = "2026-06-17T09:00:00+08:00"
* requester = Reference(Absurd-PractitionerRole)
* performer = Reference(Absurd-OrgFacilityB)
* reasonCode = $sct#29857009 "Chest pain"

Instance: Absurd-E03-SR-003
InstanceOf: ERefServiceRequest
Usage: #example
Title: "E-03 Infinite Chain — Hop 3 ServiceRequest (replaces Hop 2)"
Description: "Third referral; Facility B was also full."

* status = #active
* intent = #order
* replaces = Reference(Absurd-E03-SR-002)
* code = $sct#3457005 "Patient referral"
* subject = Reference(Absurd-Patient)
* authoredOn = "2026-06-17T10:00:00+08:00"
* requester = Reference(Absurd-PractitionerRole)
* performer = Reference(Absurd-OrgFacilityB)
* reasonCode = $sct#29857009 "Chest pain"
// The profile allows any depth. All three are status=active.
// The patient has been waiting since 08:00. It is now 10:00.
// No facility has taken ownership.


// =============================================================================
// SUPPORTING RESOURCES
// Minimal shared instances reused across the absurd examples above.
// =============================================================================

Instance: Absurd-Patient
InstanceOf: PHCorePatient
Usage: #example
Title: "Supporting Patient (Absurd Sequences)"
Description: "Minimal patient for absurd sequence examples."

* identifier.system = "urn:oid:2.16.840.1.113883.2.9.4.3.2"
* identifier.value = "PH-ABSURD-001"
* name.family = "Dela Cruz"
* name.given[0] = "Maria"
* gender = #female
* birthDate = "1988-03-15"

Instance: Absurd-Practitioner
InstanceOf: PHCorePractitioner
Usage: #example
Title: "Supporting Practitioner (Absurd Sequences)"

* identifier.system = "urn:oid:2.16.840.1.113883.2.9.4.3.3"
* identifier.value = "MD-ABSURD-001"
* name.family = "Santos"
* name.given[0] = "Ana"
* name.prefix = "Dr."
* gender = #female

Instance: Absurd-OrgReferring
InstanceOf: PHCoreOrganization
Usage: #example
Title: "Supporting Referring Facility (Absurd Sequences)"

* identifier.system = "http://fhir.nhdr.gov.ph/nhfr/hospcode"
* identifier.value = "RHU-ABSURD-001"
* name = "Rural Health Unit — Test Barangay"

Instance: Absurd-OrgReceiving
InstanceOf: PHCoreOrganization
Usage: #example
Title: "Supporting Receiving Facility A (Absurd Sequences)"

* identifier.system = "http://fhir.nhdr.gov.ph/nhfr/hospcode"
* identifier.value = "HOSP-ABSURD-001"
* name = "Test Receiving Hospital (Facility A)"

Instance: Absurd-OrgFacilityB
InstanceOf: PHCoreOrganization
Usage: #example
Title: "Supporting Receiving Facility B (Absurd Sequences)"

* identifier.system = "http://fhir.nhdr.gov.ph/nhfr/hospcode"
* identifier.value = "HOSP-ABSURD-002"
* name = "Test Receiving Hospital (Facility B)"

Instance: Absurd-PractitionerRole
InstanceOf: PHCorePractitionerRole
Usage: #example
Title: "Supporting PractitionerRole (Absurd Sequences)"

* active = true
* practitioner = Reference(Absurd-Practitioner)
* organization = Reference(Absurd-OrgReferring)
* code = $sct#158965000 "Medical practitioner"

Instance: Absurd-SR-Active
InstanceOf: ERefServiceRequest
Usage: #example
Title: "Supporting Active ServiceRequest (Absurd Sequences)"
Description: "Shared active ServiceRequest referenced by multiple absurd Task examples."

* status = #active
* intent = #order
* code = $sct#3457005 "Patient referral"
* subject = Reference(Absurd-Patient)
* authoredOn = "2026-06-17T09:00:00+08:00"
* requester = Reference(Absurd-PractitionerRole)
* performer = Reference(Absurd-OrgReceiving)
* reasonCode = $sct#29857009 "Chest pain"
