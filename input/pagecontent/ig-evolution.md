### IG Evolution: From Agile Draft to HL7 Standard

An Implementation Guide does not emerge complete. It evolves — first rapidly and informally, then more deliberately and with formal governance as it matures. Understanding that evolution helps teams invest the right energy at each stage: moving quickly when the goal is to produce something evaluable, then slowing down to build evidence when the goal is to produce something durable.

---

#### Two Phases of IG Development

IG development naturally falls into two broad phases, each with a distinct purpose and operating rhythm.

{% include ig-evolution-lifecycle.svg %}

---

#### Phase 1 — Agile Draft

The early life of an IG is best served by a **rapid, iterative process**. The goal is not a polished specification but something concrete enough to evaluate: a working, published guide with realistic examples that stakeholders can read, query, and critique.

Short cycles through the WHO SMART Guideline layers (L1–L5) — as described on the [Approach](approach.html) page — allow the team to surface ambiguities early, incorporate domain-expert feedback, and converge on a model that reflects real-world practice. At this stage:

- The IG is published as a **CI build** (`/dev/`) after every push to `main`.
- **Breaking changes are expected and welcomed** — each iteration tightens the artefacts rather than locking them prematurely.
- Stakeholder reviews are based on **concrete examples**, not abstract specifications, making it easier to spot misunderstandings and missing elements.
- Feedback is captured as scoped items for the following iteration, keeping the loop short and focused.

This is where the PH eReferral IG currently stands.

---

#### When Is a Draft Ready to Graduate?

The transition from Phase 1 to Phase 2 is not triggered by a calendar date or a version number. It is triggered by **evidence of stability and stakeholder alignment**:

| Signal | What to look for |
|--------|-----------------|
| **Semantic stability** | Iterations produce clarifications and refinements, not fundamental redesigns |
| **Stakeholder consensus** | Domain experts, clinicians, and implementers agree the model reflects real-world practice |
| **Pilot implementation** | At least one system has consumed or produced examples, even in a test environment |
| **Tooling maturity** | The IG builds cleanly, examples validate, and the CI pipeline is reliable |

When these signals converge, the project is ready to engage with a broader process — one designed to test the IG against a wider community and produce a specification stable enough to build on.

---

#### Phase 2 — HL7 Formal Process

Once the draft IG is sufficiently stable, the operating rhythm changes. Iterations slow down; governance becomes more structured; and the reviewer community expands well beyond the core project team.

At this stage, **HL7 International offers a well-established framework** for advancing the IG through successive maturity levels. The framework includes:

- A **naming convention** for each stage of the lifecycle** — from Draft through Standard for Trial Use (STU) to Normative — so that every published version carries an unambiguous signal about its stability and change tolerance.
- A **FHIR Maturity Model (FMM)** that defines objective, evidence-based criteria for each stage transition. Moving up the FMM requires documented interoperability testing, demonstrated implementations, and formal review results — not just author judgement.
- **Ballot and governance processes** that route the IG through HL7 Work Groups, the FHIR Management Group (FMG), and, for Normative publications, the Technical Steering Committee (TSC).

The HL7 process is not a replacement for agile thinking; it adds **governance checkpoints** that ensure each stage transition is evidence-based and community-validated.

---

#### What Changes in Phase 2?

Moving into the HL7 formal process introduces practices that are not needed — and would be counterproductive — during the rapid draft phase:

| Practice | Phase 1 — Agile Draft | Phase 2 — HL7 Formal |
|----------|-----------------------|----------------------|
| **Iteration speed** | Rapid (days to weeks) | Slower (months per ballot cycle) |
| **Breaking changes** | Expected and welcomed | Progressively restricted |
| **Reviewers** | Core team + domain experts | HL7 work groups, independent implementers |
| **Interoperability testing** | Informal demos and pilots | Formal Connectathon evidence (≥ 3 systems) |
| **Publication** | CI build + tagged draft releases | Formal HL7 publications with ballot status |
| **Governance** | Project team decision | HL7 WG + FMG + TSC approval chain |

The transition is gradual rather than abrupt. A team may begin engaging with HL7 Work Groups and conducting interoperability tests while still iterating on content — the formal ballot submission is the point of no return, not the first conversation.

---

#### The PH eReferral IG on the Evolution Path

This IG is currently in **Phase 1**. The agile approach described on the [Approach](approach.html) page is the right tool for this stage — it produces working, evaluated content quickly and keeps the cost of change low.

When the IG reaches evaluation readiness, the natural next steps are:

1. Engage with the relevant HL7 Work Group (e.g. through HL7 Philippines or an affiliate).
2. Conduct a Connectathon or equivalent interoperability test with ≥ 3 independent systems.
3. File a Draft Ballot or STU Ballot, depending on the FMM level reached.
4. Progress through STU releases based on accumulated implementation evidence.

The HL7 framework provides a proven path from a well-evaluated draft to a published standard. The agile phase builds the foundation that makes that path navigable.

*For the full detail of each HL7 stage, the FHIR Maturity Model, and the evidence required at each transition, see the [HL7 Standards Lifecycle](hl7-lifecycle.html) page.*
