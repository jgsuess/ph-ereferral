# Resource Architecture - PH eReferral Implementation Guide v0.3.0

## Resource Architecture

### Resource Architecture

This page documents the FHIR resource types used in the eReferral scenario, how they are grouped into transaction bundles, which FHIR design patterns they follow, and how the clinical workflow and data-dictionary mapping are visualised. For the source artefact descriptions and the agile methodology, see the [Approach](approach.md) page.

-------

#### Resource Diagram

The diagram below shows the FHIR resource types used and their relationships.

<?xml version="1.0" encoding="us-ascii" standalone="no"?>

The 22 example resources are split across two transaction bundles that mirror the two business processes in the ANC scenario.

#### Bundle A — Registration (Process A)

Clerk Abraham registers patient Charity during her first visit. This bundle collects the demographic and administrative resources created at the front desk.

| | | |
| :--- | :--- | :--- |
| Patient | `patient-charity-ex` | REF-20 … REF-27 |
| RelatedPerson | `relatedperson-companion-ex` | REF-28 |
| Organization | `organization-sending-facility-ex` | REF-4 … REF-7 |
| Practitioner | `practitioner-abraham-ex` | REF-1 |
| PractitionerRole | `practitionerrole-abraham-ex` | REF-1 |
| Encounter | `encounter-registration-ex` | REF-43 |

#### Bundle B — ANC Contact (Process B)

Nurse Jane conducts the antenatal care contact — recording clinical observations, dispensing medication, ordering lab tests, and creating the ultrasound referral.

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

The following activity diagram traces the clinical workflow through the two business processes, showing how Charity moves from registration with Abraham through to the ANC contact with Jane.

<?xml version="1.0" encoding="us-ascii" standalone="no"?>

-------

#### Data Dictionary to FHIR Mapping Diagram

The mapping diagram below provides a high-level view of how the seven clinical information groups in the data dictionary map to FHIR resource types. For the detailed element-by-element mapping, see the [DD Mapping](dd-mapping.md) page.

<?xml version="1.0" encoding="us-ascii" standalone="no"?>

