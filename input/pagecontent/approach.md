### Approach: From WHO SMART Guidelines to FHIR Examples

This page documents the methodology used to produce the FHIR example resources in this Implementation Guide, tracing the path from the WHO SMART Guidelines framework through the Philippine eReferral data dictionary to validated, machine-readable FHIR Shorthand (FSH) instances.

---

#### Source Artefacts and the WHO SMART Guidelines Framework

The [WHO SMART Guidelines](https://www.who.int/teams/digital-health-and-innovation/smart-guidelines) define five layers for turning clinical recommendations into computable health content:

| Layer | Purpose | Philippine eReferral Artefact |
|-------|---------|-------------------------------|
| **L1 – Narrative** | Personas, user scenarios, workflows | `scenario.xml` — *User scenario 3.1: First antenatal care contact* |
| **L2 – Operational** | DAK, process maps, use-case descriptions | *Philippine Health Referral FHIR IG (PeRef): WHO SMART Guideline L2 Operational Guide* (external document) |
| **L3 – Machine-readable** | Data elements, terminology mappings, decision logic | **PeRef Logical Information Model (Data Dictionary)** — the Excel workbook containing 46 data elements (REF-1 … REF-46) |
| **L4 – Executable** | FHIR profiles, FSH source, IG content | This Implementation Guide (`input/fsh/`) |
| **L5 – Dynamic** | Tests, examples, validation results | The 22 FHIR example instances and 2 transaction bundles documented below |

##### The User Scenario (`scenario.xml`)

The scenario describes **Charity**, a 24-year-old pregnant woman visiting a government health centre for the first time.  Three personas interact across two business processes:

* **Process A — Registration**: Clerk **Abraham** collects demographics, identifiers (PhilSys, PhilHealth), address, and contact information.
* **Process B — Routine ANC Contact**: Nurse **Jane** conducts a counselling session, confirms pregnancy, records vital signs and clinical observations, dispenses iron/folic acid tablets, orders laboratory tests, and creates an ultrasound referral to an external imaging centre.

The scenario is modelled after the WHO ANC Digital Adaptation Kit (DAK) user-scenario format and provides the narrative context for every example resource.

##### The Data Dictionary (Excel Workbook)

The **DRAFT Working Copy CDG Consensus – PeRef Logical Information Model (Data Dictionary)** is the authoritative source for data-element definitions.  Key sheets include:

| Sheet | Content |
|-------|---------|
| **PeRef Logical Information Model** | 46 data elements (REF-1 … REF-46) with columns for *Element ID*, *Data Element*, *Clinical Information Group*, *FHIR Profile*, *FHIR Element (R4)*, *Cardinality*, *Data Type*, *Value Set*, and *CDG Status* |
| **Workflow task Consensus** | Mapping of each element to a workflow task (e.g. *Create Referral Request*, *Assess Patient Condition*) |
| **Terminology Mapping** | Placeholder for value-set and code-system bindings (to be populated) |

The 46 elements are organised into seven clinical information groups:

1. **Sending Practitioner** (REF-1 … REF-3)
2. **Sending Facility** (REF-4 … REF-7)
3. **Receiving Practitioner** (REF-8)
4. **Receiving Facility** (REF-9 … REF-10)
5. **Referral Request** (REF-11 … REF-19)
6. **Patient Demographics** (REF-20 … REF-29)
7. **Clinical Information** (REF-30 … REF-40)

Plus logistics (REF-41), referral decision (REF-42), encounter context (REF-43 … REF-44), and navigator roles (REF-45 … REF-46).

---

#### Agile Iteration through the SMART Layers

Rather than treating the five WHO SMART layers as a strict waterfall sequence, this project works through them in **short, incremental cycles**. Each iteration takes a small slice of scope — a handful of new data elements, a scenario extension, or a set of stakeholder corrections — and pushes it through all five layers from narrative (L1) to validated outputs (L5) before circling back.

{% include agile-smart-cycle.svg %}

**Key principles:**

* **Artefacts at every layer are accepted as imperfect.** A first-pass data dictionary will have gaps; initial FSH instances will carry placeholder codes; validation will surface issues. This is expected and welcomed — each cycle tightens the artefacts rather than attempting perfection up front.
* **Every iteration closes with a stakeholder review of L5 outputs.** The published development IG (`/dev/`) is walked through with domain experts, clinicians, and implementers. Concrete examples — not abstract specifications — form the basis of discussion, making it easier to spot misunderstandings and missing elements.
* **Feedback is the fuel for the next cycle.** Observations from the review are captured as scoped items for the following iteration, keeping the loop short and focused.

This approach aligns with agile delivery practices: deliver working software (a published IG with validated examples) frequently, welcome changing requirements, and rely on close collaboration with stakeholders over exhaustive up-front specification.

---

#### Version Control & Traceability

For this iterative approach to remain **auditable and reproducible**, every artefact that feeds the pipeline — the data dictionary (encrypted), scenario XML, CSV exports, FSH sources, generated JSON examples, and utility scripts — **must be committed to the same Git repository as the IG itself**.

If any input artefact lives outside version control (e.g. on a shared drive or in email), the chain from L3 data elements through L4 FSH source to L5 published examples is broken: there is no way to determine which version of the data dictionary produced a given set of FHIR resources, and stakeholder review feedback cannot be traced back to a specific commit.

**Rule:** If it is an input to or output of the pipeline, it belongs in this repository.

*Note:* The data dictionary Excel workbook is stored as a PGP-encrypted file (`.xlsx.gpg`). To decrypt:

```sh
gpg --decrypt \
  "DRAFT Working Copy CDG Consensus - PeRef Logical Information Model (Data Dictionary).xlsx.gpg" \
  > "DRAFT Working Copy CDG Consensus - PeRef Logical Information Model (Data Dictionary).xlsx"
```

---

#### Detailed Documentation

The following pages provide in-depth coverage of each aspect of the project:

* **[Technical Pipeline](technical-pipeline.html)** — the end-to-end data flow from source artefacts to a published IG, including the step-by-step script pipeline and data-dictionary coverage tracking.
* **[Resource Architecture](resource-architecture.html)** — the FHIR resource types, transaction bundles, FHIR design patterns, scenario activity flow, and data-dictionary-to-FHIR mapping diagram.
* **[AI-Assisted Reasoning](ai-reasoning.html)** — how an AI coding assistant was used to accelerate resource identification, terminology selection, and pipeline automation.
* **[Version Management & Publication](version-management.html)** — the two-lane CI/release publication model, how to cut a release, and known limitations.
* **[DD Mapping](dd-mapping.html)** — the element-by-element mapping between the data dictionary and the FHIR example resources.
* **[IG Evolution](ig-evolution.html)** — how the IG graduates from rapid agile drafting to the HL7 formal process, and what signals indicate readiness to transition.
* **[HL7 Standards Lifecycle](hl7-lifecycle.html)** — the HL7 ballot and publication stages, the FHIR Maturity Model (FMM 0–5), Connectathon requirements, and the evidence needed to move from STU to Normative.
* **[Interoperability Matrix Testing](interop-testing.html)** — CI-based automated testing of registered implementation endpoints against each other, the distinction between quality assurance and quality management, and how to subscribe an endpoint.
* **[Testing Companion IG](testing-companion.html)** — the companion IG artefact that holds bulk test examples, SDC interactive forms, demo scripts, and a containerised local stack for hands-on experimentation.