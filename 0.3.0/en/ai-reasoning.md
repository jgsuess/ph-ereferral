# Ai Reasoning - PH eReferral Implementation Guide v0.3.0

## Ai Reasoning

### AI-Assisted Reasoning

An AI coding assistant (GitHub Copilot) was used throughout this project to accelerate the conversion pipeline. This page documents the key decisions made by the AI, all of which were reviewed and confirmed by the IG author. For the broader methodology, see the [Approach](approach.md) page.

-------

#### Scenario Analysis → Resource Identification

The AI parsed `scenario.xml` and identified the personas (Charity, Abraham, Jane), the two business processes, and the clinical actions described in the narrative. From this it proposed the initial list of FHIR resource types needed (Patient, Practitioner, Organization, Encounter, Observation, Condition, ServiceRequest, Task, MedicationAdministration, RelatedPerson).

-------

#### Data Dictionary Extraction and Mapping

Since the data dictionary is an Excel workbook that tooling cannot read directly, the AI created a Python extraction script (`extract-data-dictionary.py`) to dump all sheets to CSV. It then analysed the 46 REF-* elements, their **FHIR Profile** and **FHIR Element (R4)** columns, and mapped each to a concrete resource instance.

Key reasoning steps:

* **REF-1** maps to both `Practitioner.name` and `PractitionerRole` because the DD specifies `PractitionerRole.practitioner → Practitioner.name` — so two resources are needed per practitioner.
* **REF-23 (computed age)** was excluded from persistence because the DD itself recommends computing it from `birthDate`.
* **REF-38 (treatment given)** was mapped to `MedicationAdministration` (rather than `Procedure`) because the scenario specifically describes dispensing IFA tablets.
* **REF-39 (lab results)** was marked **partial** because the scenario describes ordering tests, not receiving results — so `ServiceRequest` is appropriate now, with `DiagnosticReport` deferred.
* **REF-42 (response)** uses `Task.businessStatus` (not `Task.status`) per the DD's own recommendation to separate human-meaningful state from the technical state machine.

-------

#### Terminology Selection

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

-------

#### Synthetic Data Values

Realistic Filipino-context values were generated for the example data:

* **Charity**: female, DOB 2001-08-15 (age 24), address in Barangay Malusog, Quezon City
* **Vital signs**: BP 110/70 mmHg, HR 78 bpm, RR 18/min, SpO₂ 98%, temp 36.8°C, weight 55 kg
* **Facility**: "Barangay Malusog Health Centre" with a synthetic NHFR code

-------

#### Pipeline Automation

The AI created the full script pipeline (`generate-json-from-dd.py` → `validate-all.sh` → `convert-to-fsh.sh` → `update-dd-coverage.py`) so that changes to the data dictionary or scenario can be propagated through to FSH with a single re-run. For details on each pipeline step, see the [Technical Pipeline](technical-pipeline.md) page.

