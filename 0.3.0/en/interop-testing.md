# Interop Testing - PH eReferral Implementation Guide v0.3.0

## Interop Testing

### Interoperability Matrix Testing

As the PH eReferral IG moves from an agile draft towards broader adoption — the Phase 2 described on the [IG Evolution](ig-evolution.md) page — verifying that different implementations actually work together becomes as important as verifying that each implementation individually conforms to the specification. This page describes the approach: **CI-based interoperability matrix testing**.

-------

#### Why Matrix Testing?

A single implementation can be valid against the spec and still fail to interoperate with another valid implementation. The FHIR specification leaves room for interpretation, optional elements, and vendor-specific choices that all conform individually but diverge in practice. The only way to catch these issues is to test implementations **against each other**, not just against a validator.

In Phase 2, when multiple organisations begin building on the IG, the number of untested combinations grows quickly. A matrix approach makes that coverage systematic and visible.

-------

#### Endpoint Subscriptions

The first requirement for matrix testing is a **registry of stable, accessible endpoints**. Any interested party — a hospital system, a vendor, a government programme — can subscribe by registering:

* A stable FHIR server URL (accessible from CI infrastructure).
* An authentication method (open, bearer token, mutual TLS, or similar).
* A FHIR CapabilityStatement declaring which operations and profiles are supported.
* A point of contact for issue notification.

Registered endpoints are stored in the IG repository, and the project commits to including them in every scheduled test run. In return, endpoint owners commit to maintaining availability and notifying the project when their endpoint changes significantly.

> **What "stable" means:** The endpoint does not need to be a production system. It does need to be reliably available during scheduled CI windows and to reflect a genuine implementation of the IG — not a stub or mock that merely returns HTTP 200.

-------

#### How the CI Matrix Works

A scheduled CI job (running nightly, or triggered by a new IG build) executes a defined set of test scenarios against every registered sender/receiver pair. Results are aggregated into a matrix report and published alongside the IG at `/dev/interop-matrix/`, pinned to the IG version that was current when the tests ran.

<?xml version="1.0" encoding="us-ascii" standalone="no"?>

**Test scenarios** cover the core IG workflows:

| | |
| :--- | :--- |
| **Submit referral** | Sender posts a referral`Bundle`(Transaction); receiver accepts and returns a response |
| **Query referral status** | Requester queries`Task`resource by identifier; responder returns current status |
| **Patient demographics lookup** | Sender queries`Patient`by PhilSys ID; responder matches and returns demographics |
| **Subscription notification** | Subscriber registers a FHIR Subscription; publisher fires a notification on referral status change |

Each scenario is defined as a reusable test script, versioned alongside the IG, so results are reproducible and comparable across IG versions.

-------

#### The Interoperability Matrix

The output of each test run is a matrix — implementations as both senders and receivers, with a pass/fail/pending result at each intersection.

<?xml version="1.0" encoding="us-ascii" standalone="no"?>

The matrix is published openly. A failure is not a compliance finding — it is an **early signal** that prompts investigation: is the issue in the sender, the receiver, or an ambiguity in the IG itself? All three are valid outcomes and all three are valuable:

* A sender bug → the sender fixes their implementation.
* A receiver bug → the receiver fixes their implementation.
* An IG ambiguity → the project team tightens the specification.

This feedback loop is the point of the exercise.

-------

#### Quality Assurance, Not Quality Management

It is important to be clear about what CI matrix testing is — and is not.

<?xml version="1.0" encoding="us-ascii" standalone="no"?>

The distinction between **Quality Assurance (QA)** and **Quality Management (QM)** is well captured by Maren Behrendt in [**Quality Management and Quality Assurance — What's the Difference?**](https://www.babtec.com/blog/difference-quality-management-quality-assurance) (Babtec, 2021):

> Quality Management acts as the **navigation system** — it develops the roadmap, specifications, processes, and rules. Quality Assurance acts as the **navigation device in use** — it implements the monitoring and control measures to verify that requirements are actually met.

In IG development terms:

| | | |
| :--- | :--- | :--- |
| **What** | FMM stage criteria, ballot governance, normative policy | CI matrix tests, Connectathon evidence, FHIR validator runs |
| **Who decides** | HL7 Work Groups, FMG, TSC | Project CI, implementers |
| **When** | At stage-transition gates | Continuously, on every build or nightly |
| **Output** | Permission to advance to next maturity level | Pass/fail report pinned to IG version |
| **Nature** | Governance commitment | Automated verification |

**CI matrix testing is a QA activity.** It eliminates the class of defects that automation can find — missing required elements, wrong status codes, incompatible date formats, malformed references — before those defects reach the formal QM gates. It is the difference between arriving at a Connectathon with known-good implementations versus arriving to discover basic incompatibilities that should have been found weeks earlier.

This testing does **not** replace formal compliance testing. It does not grant any certification, badge, or maturity-level advancement. It is a continuous sanity check that reduces waste and improves the quality of evidence that later feeds the formal processes.

-------

#### What This Is Not

To be explicit about scope:

* **Not a certification programme.** Passing all matrix tests carries no regulatory or contractual weight.
* **Not a Connectathon substitute.** Connectathon evidence (≥ 3 independent systems, accepted by FMG) remains the formal gate for FMM 2 advancement, as described on the [HL7 Standards Lifecycle](hl7-lifecycle.md) page.
* **Not a compliance audit.** Formal compliance testing — against national or regulatory requirements — requires accredited processes that this project does not provide.
* **Not exhaustive.** Automated tests cover the scenarios they are programmed to cover. Edge cases, workflow nuances, and clinical correctness still require human review.

-------

#### Subscribing Your Endpoint

If you are implementing or piloting the PH eReferral IG and would like your endpoint included in the matrix:

1. Open an issue in the[project repository](https://github.com/jgsuess/ph-ereferral)with the label`interop-endpoint`.
1. Provide: endpoint URL, authentication details (shared privately via repository secrets), CapabilityStatement link, and contact email.
1. The project team will add the endpoint to the registry and include it in the next scheduled test run.
1. Results will appear in the published matrix at`/dev/interop-matrix/`within 24 hours of the next run.

Endpoints that become unreachable for more than two consecutive weeks will be marked as `inactive` in the registry and excluded from results until restored.

-------

#### Relationship to the Rest of the Documentation

* **[Approach](approach.md)** — the agile development methodology that produces the IG content being tested.
* **[IG Evolution](ig-evolution.md)** — when and why matrix testing becomes relevant (Phase 2 transition).
* **[HL7 Standards Lifecycle](hl7-lifecycle.md)** — the formal FMM and ballot process that CI testing feeds into but does not replace.
* **[Version Management & Publication](version-management.md)** — how IG versions are tagged; matrix results are pinned to the version current at test time.
* **[Testing Companion IG](testing-companion.md)** — the companion IG that supplies bulk test fixtures and SDC forms used to seed and exercise the matrix test endpoints.

