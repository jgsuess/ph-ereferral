### HL7 Standards Lifecycle

Once an Implementation Guide has moved past the rapid agile draft phase, HL7 International provides a well-established framework for developing it further. This framework defines the stages an IG passes through as it gains maturity, the evidence required at each stage transition, and the governance processes that validate progress. Understanding it is essential for planning a realistic path from an initial draft to a published standard.

For context on where this fits in the overall IG evolution, see [IG Evolution](ig-evolution.html).

---

#### Two Dimensions of IG Maturity

IG development progress is tracked along two related but distinct axes:

1. **Ballot / publication status** — the formal HL7 designation assigned to a published version: Draft, STU (Standard for Trial Use), or Normative.
2. **FHIR Maturity Model (FMM) level** — a 0–5 scale that defines *objective, evidence-based criteria* a specification must meet before advancing to the next stage.

An IG progresses by accumulating FMM evidence, and at certain FMM thresholds it becomes eligible for the next ballot status. The two axes are related but not identical: an IG at a given FMM level may or may not yet have gone through the corresponding ballot process.

{% include hl7-ballot-cycle.svg %}

---

#### Stage 1 — Early Development (pre-ballot)

**Ballot status:** CI build only (no formal HL7 status)
**FMM level:** 0–1

At this stage the IG is under active development, published only as a continuous-integration (CI) build. Breaking changes are expected at any time and no formal HL7 approval has been sought.

*FMM criteria:*
- **FMM 0**: The artifact exists and builds cleanly.
- **FMM 1**: The responsible Work Group considers the artifact substantially complete; no unresolved blocking issues remain.

*Who uses this?* Project teams, early adopters, pilots, and teams preparing for Connectathon participation.

---

#### Stage 2 — Ballot

**Ballot status:** Draft ballot or STU ballot
**FMM level:** 2 required for STU ballot

The first formal HL7 community review. Balloting:

- Collects structured comments from HL7 members.
- Requires reconciliation of all negative votes before publication.
- Is mandatory before any official HL7 publication.

A ballot can be a **Draft ballot** (earlier, higher change tolerance) or an **STU ballot** (more mature, intended for real-world trial use). To file an STU ballot the IG must have reached at least **FMM 2**.

*FMM 2 criteria:*
- Successful interoperability demonstrated among at least **three independently developed systems**.
- Testing conducted using realistic scenarios — typically at a **FHIR Connectathon** or equivalent event.
- Results reported to and accepted by the **FHIR Management Group (FMG)**.

> *"Testing must occur one cycle before ballot."* — HL7 IG process guidance.

---

#### Connectathons in the STU Pathway

Connectathons are not optional polish — for FHIR artifacts, interoperability testing is a **formal gating criterion** for FMM advancement, not a post-publication nicety.

A typical STU path looks like this:

```
Draft IG
  ↓
Connectathon testing (FMM 2)
  ↓
STU Ballot
  ↓
STU Publication
```

Connectathon evidence that HL7 accepts:

- **≥ 3 independent implementations** exercising the declared scope (≈80% coverage is the guideline).
- Semi-realistic data and workflows — not just synthetic test cases.
- Results **documented and accepted by FMG**.

For IGs that go through multiple STU cycles, early Connectathons prove basic feasibility; later ones demonstrate stability, convergence, and cross-vendor consistency. This accumulating evidence directly feeds the case for Normative readiness.

---

#### Stage 3 — STU (Standard for Trial Use)

**Ballot status:** STU
**FMM level:** 3–4

STU is the most common "production-ready" state for a FHIR IG. It signals:

- **Official HL7 standard** — the IG has passed ballot and is formally published.
- **Ready for production trial use** — real-world implementations are explicitly invited.
- **Breaking changes still allowed** — later STU releases may introduce incompatible changes.
- **Real-world feedback expected** — the trial use period is a deliberate mechanism for collecting implementation evidence.

An IG commonly goes through multiple STU releases (STU 1, STU 2, STU 3…), each through a new ballot cycle. This is by design: each cycle allows the IG to absorb implementation feedback before the semantic model is locked.

*FMM criteria:*
- **FMM 3**: Passed STU ballot; evidence of broad review with non-trivial changes resulting from external feedback.
- **FMM 4**: Evidence of broad review and multiple independent implementations; breaking changes slowing significantly.

> **Important rule:** An IG cannot be more mature than the least mature core artifact it depends on.

---

#### Stage 4 — Normative Ballot

**Ballot status:** Normative ballot in progress
**FMM level:** 5 required

A Normative ballot signals intent to **lock down the specification**. It requires:

- Multiple completed STU cycles with demonstrated real-world adoption.
- Strong backward-compatibility confidence — the semantic model is stable.
- Governance willingness to commit to long-term stewardship of a locked specification.

The ballot process at this stage is more stringent: all negative votes must be resolved, and final approval passes through the sponsoring Work Group, the FMG, and the Technical Steering Committee (TSC).

---

#### Stage 5 — Normative Publication

**Ballot status:** Normative
**FMM level:** 5

The highest stability level in the HL7/FHIR ecosystem. A Normative IG:

- Has changes **tightly constrained** by HL7 inter-version compatibility rules.
- Establishes **backward compatibility** as the default expectation.
- Is approved through an **ANSI-accredited process**.
- Is safe to build long-lived, regulated, or national infrastructure on.

Normative IGs are rare and slow to emerge — intentionally so. The bar is high because the governance commitment to maintain backward compatibility is real and long-lived.

---

#### The FMM Maturity Ladder

The table below maps each FMM level to its corresponding ballot status and the evidence required to reach it.

{% include fmm-maturity-ladder.svg %}

| Phase | Ballot / Publication Status | FMM Level |
|-------|-----------------------------|-----------|
| Early development | Draft (CI build only) | FMM 0–1 |
| First review | Draft ballot / STU ballot | FMM 2 |
| Trial use | STU | FMM 3–4 |
| Locked specification | Normative | FMM 5 |

---

#### Evidence Required to Move from STU to Normative

Moving to Normative is not just another ballot. It is a **governance decision to lock the specification** permanently. HL7 expects credible, documented evidence across four areas:

**1. Production implementation**

- Named production deployments (not pilots or test environments).
- Public implementation statements, regulator references, or national programme mandates.
- Downstream IGs or certification programmes that depend on this IG.

This evidence is specifically required for the FMM 4 → FMM 5 transition.

**2. Stability across STU cycles**

- Multiple STU releases with evidence that breaking changes have slowed dramatically.
- Issues are predominantly clarifications or edge cases — not redesigns.
- Alignment with the distinction between Trial Use (which allows incompatible changes) and Normative (which severely restricts them).

**3. Broad and diverse review**

- Comments from multiple independent organisations.
- Non-trivial changes made as a result of external feedback.
- Evidence that feedback came from actual implementers, not just the authoring team.

This expectation is stated explicitly at FMM 3 and above, and carries forward to Normative decisions.

**4. Interoperability history**

- Repeated Connectathon participation with stable, consistent results across vendors.
- No unresolved interoperability-blocking issues.

While not always phrased as "attend X Connectathons", the interoperability evidence requirement persists through FMM 4–5.

**Hard prerequisite: FMM 5** requires all of the following:

- Published in ≥ 2 formal release cycles at FMM 1+.
- Implemented in ≥ 5 independent production systems.
- For international IGs: implementations in more than one country.

Even with FMM 5 evidence in hand, a Normative ballot is still required, all negatives must be resolved per ANSI rules, and final approval passes through the WG, FMG, and TSC.

---

#### Governance: Ballot and Approval Chain

Every formal HL7 publication involves a layered governance chain:

| Stage | Approving body |
|-------|---------------|
| Draft / STU ballot submission | Sponsoring Work Group |
| Ballot reconciliation | Work Group + HL7 members |
| STU / Normative publication | FHIR Management Group (FMG) |
| Normative publication (final) | + Technical Steering Committee (TSC) |

The FMG is the body that accepts Connectathon evidence and adjudicates FMM advancement claims. The TSC provides the final governance gate for Normative publications.

---

#### A Practical Note for National IGs

Many national IGs — including AU Base, AU Core, and US Core — **intentionally remain at STU for extended periods** to:

- Absorb ecosystem feedback and align with evolving regulation.
- Avoid premature lock-in that would constrain implementers.
- Build the production evidence base required for a credible Normative claim.

**Normative is a governance commitment, not just a technical milestone.** If an IG still expects semantic churn, evolving slices, or frequent cardinality changes, it is not Normative-ready — and that is entirely appropriate for a maturing standard.

Most successful IGs spend years at STU by design. The PH eReferral IG, currently in agile draft, has a long and productive journey ahead before Normative is the right conversation.
