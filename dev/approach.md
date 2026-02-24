# Approach - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* **Approach**

## Approach

### Approach: From WHO SMART Guidelines to FHIR Examples

This page documents the methodology used to produce the FHIR example resources in this Implementation Guide, tracing the path from the WHO SMART Guidelines framework through the Philippine eReferral data dictionary to validated, machine-readable FHIR Shorthand (FSH) instances.

-------

#### Source Artefacts and the WHO SMART Guidelines Framework

The [WHO SMART Guidelines](https://www.who.int/teams/digital-health-and-innovation/smart-guidelines) define five layers for turning clinical recommendations into computable health content:

| | | |
| :--- | :--- | :--- |
| **L1 – Narrative** | Personas, user scenarios, workflows | `scenario.xml`—**User scenario 3.1: First antenatal care contact** |
| **L2 – Operational** | DAK, process maps, use-case descriptions | **Philippine Health Referral FHIR IG (PeRef): WHO SMART Guideline L2 Operational Guide**(external document) |
| **L3 – Machine-readable** | Data elements, terminology mappings, decision logic | **PeRef Logical Information Model (Data Dictionary)**— the Excel workbook containing 46 data elements (REF-1 … REF-46) |
| **L4 – Executable** | FHIR profiles, FSH source, IG content | This Implementation Guide (`input/fsh/`) |
| **L5 – Dynamic** | Tests, examples, validation results | The 22 FHIR example instances and 2 transaction bundles documented below |

##### The User Scenario (scenario.xml)

The scenario describes **Charity**, a 24-year-old pregnant woman visiting a government health centre for the first time. Three personas interact across two business processes:

* **Process A — Registration**: Clerk **Abraham** collects demographics, identifiers (PhilSys, PhilHealth), address, and contact information.
* **Process B — Routine ANC Contact**: Nurse **Jane** conducts a counselling session, confirms pregnancy, records vital signs and clinical observations, dispenses iron/folic acid tablets, orders laboratory tests, and creates an ultrasound referral to an external imaging centre.

The scenario is modelled after the WHO ANC Digital Adaptation Kit (DAK) user-scenario format and provides the narrative context for every example resource.

##### The Data Dictionary (Excel Workbook)

The **DRAFT Working Copy CDG Consensus – PeRef Logical Information Model (Data Dictionary)** is the authoritative source for data-element definitions. Key sheets include:

| | |
| :--- | :--- |
| **PeRef Logical Information Model** | 46 data elements (REF-1 … REF-46) with columns for**Element ID**,**Data Element**,**Clinical Information Group**,**FHIR Profile**,**FHIR Element (R4)**,**Cardinality**,**Data Type**,**Value Set**, and**CDG Status** |
| **Workflow task Consensus** | Mapping of each element to a workflow task (e.g.**Create Referral Request**,**Assess Patient Condition**) |
| **Terminology Mapping** | Placeholder for value-set and code-system bindings (to be populated) |

The 46 elements are organised into seven clinical information groups:

1. **Sending Practitioner**(REF-1 … REF-3)
1. **Sending Facility**(REF-4 … REF-7)
1. **Receiving Practitioner**(REF-8)
1. **Receiving Facility**(REF-9 … REF-10)
1. **Referral Request**(REF-11 … REF-19)
1. **Patient Demographics**(REF-20 … REF-29)
1. **Clinical Information**(REF-30 … REF-40)

Plus logistics (REF-41), referral decision (REF-42), encounter context (REF-43 … REF-44), and navigator roles (REF-45 … REF-46).

-------

#### Agile Iteration through the SMART Layers

Rather than treating the five WHO SMART layers as a strict waterfall sequence, this project works through them in **short, incremental cycles**. Each iteration takes a small slice of scope — a handful of new data elements, a scenario extension, or a set of stakeholder corrections — and pushes it through all five layers from narrative (L1) to validated outputs (L5) before circling back.

**Key principles:**

* **Artefacts at every layer are accepted as imperfect.** A first-pass data dictionary will have gaps; initial FSH instances will carry placeholder codes; validation will surface issues. This is expected and welcomed — each cycle tightens the artefacts rather than attempting perfection up front.
* **Every iteration closes with a stakeholder review of L5 outputs.** The published development IG (`/dev/`) is walked through with domain experts, clinicians, and implementers. Concrete examples — not abstract specifications — form the basis of discussion, making it easier to spot misunderstandings and missing elements.
* **Feedback is the fuel for the next cycle.** Observations from the review are captured as scoped items for the following iteration, keeping the loop short and focused.

This approach aligns with agile delivery practices: deliver working software (a published IG with validated examples) frequently, welcome changing requirements, and rely on close collaboration with stakeholders over exhaustive up-front specification.

-------

#### Technical Pipeline

The diagram below summarises the end-to-end data flow from source artefacts to a published IG.

##### Step-by-step

| | | | |
| :--- | :--- | :--- | :--- |
| **1. Extract data dictionary** | `utils/extract-data-dictionary.py`(Python + openpyxl) | Excel workbook (`.xlsx`) | CSV files in`input/data-dictionary/` |
| **2. Generate JSON skeletons** | `utils/generate-json-from-dd.py` | CSV + scenario narrative | 22 annotated FHIR R4 JSON files in`input/examples-json-source/` |
| **3. Validate JSON** | `utils/validate-all.sh`→`utils/fhir-validate.py` | JSON files + FHIR server | Validation result summaries |
| **4. Convert to FSH** | `utils/convert-to-fsh.sh`→`gofsh` | Validated JSON files | 22 FSH instance files in`input/fsh/examples/` |
| **5. Author bundles** | Manual (FSH) | Individual FSH instances | `registration-transaction-ex.fsh`,`anc-contact-transaction-ex.fsh` |
| **6. Add narrative descriptions** | `utils/update-fsh-descriptions.py` | FSH instance files | FSH files with`Title:`and`Description:`added |
| **7. Generate DD mapping page** | `utils/generate-dd-mapping-page.py` | `dd-coverage.csv` | `input/pagecontent/dd-mapping.md`(pivot tables + narrative) |
| **8. Compile IG** | `sushi .` | All FSH sources + ph-core dependency | `fsh-generated/resources/*.json`(24 resources) |
| **9. Publish IG** | `_genonce.sh`→ IG Publisher | SUSHI output +`publisher.jar` | `output/`(HTML site) |

##### DD Coverage Tracking

Every JSON example resource is annotated with `meta.tag` entries that reference the data dictionary element IDs it satisfies:

```
"meta": {
  "tag": [
    { "system": "https://example.com/peref-dd", "code": "REF-20", "display": "REF-20" },
    { "system": "https://example.com/peref-dd", "code": "REF-21", "display": "REF-21" }
  ]
}

```

A companion script (`utils/update-dd-coverage.py`) scans all JSON examples and regenerates `input/data-dictionary/dd-coverage.csv`, producing this summary:

| | | |
| :--- | :--- | :--- |
| **Covered** | 31 | Fully represented in at least one example resource |
| **Partial** | 1 | REF-39 (lab results) — orders created but no DiagnosticReport yet |
| **Deferred** | 4 | REF-2, REF-3 (signature — Future Release), REF-11 (HCPN — On-Hold), REF-18 (return slip — Excluded from MVP) |
| **Not applicable** | 10 | Elements not relevant to this ANC scenario (e.g. transport mode, receiving encounter, navigators) |

**100 % of applicable elements are covered.**

-------

#### Resource Architecture

The diagram below shows the FHIR resource types used and their relationships.

##### Bundle A — Registration (Process A)

| | | |
| :--- | :--- | :--- |
| Patient | `patient-charity-ex` | REF-20 … REF-27 |
| RelatedPerson | `relatedperson-companion-ex` | REF-28 |
| Organization | `organization-sending-facility-ex` | REF-4 … REF-7 |
| Practitioner | `practitioner-abraham-ex` | REF-1 |
| PractitionerRole | `practitionerrole-abraham-ex` | REF-1 |
| Encounter | `encounter-registration-ex` | REF-43 |

##### Bundle B — ANC Contact (Process B)

| | | |
| :--- | :--- | :--- |
| Practitioner | `practitioner-jane-ex` | REF-1 |
| PractitionerRole | `practitionerrole-jane-ex` | REF-1 |
| Organization | `organization-receiving-facility-ex` | REF-9, REF-10 |
| Encounter | `encounter-anc-ex` | REF-43 |
| Condition | `condition-pregnancy-ex` | REF-40 |
| Observation ×7 | chief complaint, BP, HR, RR, SpO₂, temp, weight | REF-30, REF-32 … REF-37 |
| MedicationAdministration | `medicationadministration-ifa-ex` | REF-38 |
| ServiceRequest ×2 | ultrasound referral, lab orders | REF-12, REF-13, REF-15, REF-31, REF-39 |
| Task | `task-referral-ex` | REF-16, REF-42 |

-------

#### FHIR Design Patterns

The FHIR specification defines a set of reusable [**Design Patterns**](https://build.fhir.org/patterns.html) that standardise how resources behave across clinical, administrative, and workflow domains. The table below shows which patterns this IG relies on and how they map to the eReferral resources.

| | | | |
| :--- | :--- | :--- | :--- |
| **Request** | [Event / Request](https://build.fhir.org/request.html) | ServiceRequest (×2) | The ultrasound referral and laboratory orders follow the**Request**pattern — they capture the intent, priority, and coded reason for a service to be performed. |
| **Event** | [Event](https://build.fhir.org/event.html) | Observation (×7), MedicationAdministration, Encounter (×2), Condition | Clinical acts that have already occurred use the**Event**pattern — vital-sign observations, medication dispensing, encounter records, and the pregnancy condition all carry status, timing, and performer. |
| **Participant** | [Participant](https://build.fhir.org/participant.html) | Patient, Practitioner (×2), PractitionerRole (×2), RelatedPerson, Organization (×2) | People and organisations are modelled with the**Participant**pattern. PractitionerRole links a Practitioner to an Organization and role code, following the[**Participant and RoleEntity pattern**](https://build.fhir.org/participantandentity.html). |
| **Workflow** | [Workflow](https://build.fhir.org/workflow.html) | Task, ServiceRequest | The referral lifecycle uses the**Workflow**pattern: a ServiceRequest expresses the clinical intent, while a Task tracks fulfilment state (`requested → received → accepted`). This follows the[**ServiceRequest + Task**](https://build.fhir.org/workflow-management.html)coordination approach. |
| **Observation** | [Observation](https://build.fhir.org/observation.html) | Observation (×7) | Vital signs and the chief complaint follow the**Observation**pattern with LOINC-coded types and quantity values. Blood pressure uses the[**component pattern**](https://build.fhir.org/observation.html#component)for systolic/diastolic. |
| **Bundle / Transaction** | [Bundle](https://build.fhir.org/bundle.html) | Bundle (×2) | Registration and ANC-contact resources are grouped into**transaction**Bundles, ensuring atomic submission of related resources. |

> **Further reading:** The FHIR [Design Patterns overview](https://build.fhir.org/patterns.html) explains the rationale behind these abstractions and how they promote consistency across implementation guides.

-------

#### Scenario Activity Flow

The following activity diagram traces the clinical workflow through the two business processes.

-------

#### Data Dictionary to FHIR Mapping

The mapping diagram below shows how the seven clinical information groups in the data dictionary map to FHIR resource types.

-------

#### AI-Assisted Reasoning

An AI coding assistant (GitHub Copilot) was used throughout this project to accelerate the conversion pipeline. The following decisions were made by the AI, reviewed and confirmed by the IG author:

##### Scenario Analysis → Resource Identification

The AI parsed `scenario.xml` and identified the personas (Charity, Abraham, Jane), the two business processes, and the clinical actions described in the narrative. From this it proposed the initial list of FHIR resource types needed (Patient, Practitioner, Organization, Encounter, Observation, Condition, ServiceRequest, Task, MedicationAdministration, RelatedPerson).

##### Data Dictionary Extraction and Mapping

Since the data dictionary is an Excel workbook that tooling cannot read directly, the AI created a Python extraction script (`extract-data-dictionary.py`) to dump all sheets to CSV. It then analysed the 46 REF-* elements, their **FHIR Profile** and **FHIR Element (R4)** columns, and mapped each to a concrete resource instance.

Key reasoning steps:

* **REF-1** maps to both `Practitioner.name` and `PractitionerRole` because the DD specifies `PractitionerRole.practitioner → Practitioner.name` — so two resources are needed per practitioner.
* **REF-23 (computed age)** was excluded from persistence because the DD itself recommends computing it from `birthDate`.
* **REF-38 (treatment given)** was mapped to `MedicationAdministration` (rather than `Procedure`) because the scenario specifically describes dispensing IFA tablets.
* **REF-39 (lab results)** was marked **partial** because the scenario describes ordering tests, not receiving results — so `ServiceRequest` is appropriate now, with `DiagnosticReport` deferred.
* **REF-42 (response)** uses `Task.businessStatus` (not `Task.status`) per the DD's own recommendation to separate human-meaningful state from the technical state machine.

##### Terminology Selection

The AI selected LOINC codes for observations and SNOMED CT codes for conditions based on the codes specified in the DD's **Value Set** column where available, falling back to widely-used international codes where the DD had placeholders:

| | | |
| :--- | :--- | :--- |
| Chief complaint | 10154-3 | LOINC |
| Blood pressure panel | 85354-9 | LOINC |
| Heart rate | 8867-4 | LOINC |
| Respiratory rate | 9279-1 | LOINC |
| SpO₂ | 59408-5 | LOINC |
| Temperature | 8310-5 | LOINC |
| Weight | 29463-7 | LOINC |

##### Synthetic Data Values

Realistic Filipino-context values were generated for the example data:

* **Charity**: female, DOB 2001-08-15 (age 24), address in Barangay Malusog, Quezon City
* **Vital signs**: BP 110/70 mmHg, HR 78 bpm, RR 18/min, SpO₂ 98%, temp 36.8°C, weight 55 kg
* **Facility**: "Barangay Malusog Health Centre" with a synthetic NHFR code

##### Pipeline Automation

The AI created the full script pipeline (`generate-json-from-dd.py` → `validate-all.sh` → `convert-to-fsh.sh` → `update-dd-coverage.py`) so that changes to the data dictionary or scenario can be propagated through to FSH with a single re-run.

-------

#### Version Management & Publication

The IG follows a **two-lane publication model** aligned with HL7 IG publishing guidance:

| | | | |
| :--- | :--- | :--- | :--- |
| **CI (dev)** | Push to`main` | `…/dev/` | Yes — always-fresh preview |
| **Release** | Git tag`vX.Y.Z` | `…/X.Y.Z/` | No — immutable once published |

**Key rules:**

1. The`main`branch always carries the**next**development version with a`-draft`suffix (e.g.`0.2.0-draft`).
1. Release versions are derived from**Git tags**— tagging`v0.1.0`produces IG version`0.1.0`.
1. The release workflow patches`sushi-config.yaml`at build time only; the source on`main`is never modified by the pipeline.
1. Published version directories (`/X.Y.Z/`) are**never overwritten**— the workflow refuses to proceed if the directory already exists.
1. `/current/`redirects to the latest release;`/dev/`always reflects the latest CI build from`main`.
1. A`history.html`page and`package-list.json`feed are maintained automatically on the`gh-pages`branch.

The workflows are defined in:

* `.github/workflows/ig-ci-dev.yml` — CI lane (push to `main`)
* `.github/workflows/ig-release.yml` — Release lane (tag `v*`)

##### Publication URLs

| | |
| :--- | :--- |
| `https://jgsuess.github.io/ph-ereferral/dev/` | Development build (latest CI from`main`) |
| `https://jgsuess.github.io/ph-ereferral/X.Y.Z/` | Immutable release |
| `https://jgsuess.github.io/ph-ereferral/current/` | Redirect to latest release |
| `https://jgsuess.github.io/ph-ereferral/history.html` | Publication history |

##### How to Cut a Release

1. Ensure all changes are merged to`main`.
1. Create an annotated tag:`git tag -a v0.1.0 -m "First draft release"`
1. Push the tag:`git push origin v0.1.0`
1. The`ig-release.yml`workflow runs automatically: builds the IG with version`0.1.0`, publishes to`/0.1.0/`, updates`history.html`,`package-list.json`, and`/current/`.
1. After the release, bump the version on`main`to the next draft (e.g.`0.2.0-draft`).

-------

#### Limitations and Future Work

1. **Signature / Provenance**(REF-2, REF-3) — deferred to a future release per CDG consensus.
1. **HCPN**(REF-11) — on hold pending CDG decision on whether it should be computed or manually entered.
1. **Return referral slip**(REF-18) — excluded from MVP; requires DocumentReference modelling.
1. **Lab results**(REF-39) — currently modelled as ServiceRequest (orders); DiagnosticReport will be added when results are available.
1. **Receiving encounter**(REF-44) — belongs to the receiving facility's workflow, not the sending scenario.
1. **Pregnancy-specific elements**— the DD notes a placeholder row for gravidity, parity, fundal height, and immunisation history; these should be added as structured Observations in a future iteration.

