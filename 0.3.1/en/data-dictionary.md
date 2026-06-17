# Data Dictionary - PH eReferral Implementation Guide v0.3.1

## Data Dictionary

# PH eReferral Data Dictionary

This page provides the authoritative data dictionary for the Philippine eReferral Implementation Guide. It maps all Technical Development Group (TDG) data elements to their corresponding FHIR resources, elements, value sets, and cardinality constraints.

## Data Dictionary

The table below shows the complete data dictionary mapping all TDG data elements to their corresponding FHIR resources, elements, value sets, and cardinality constraints.

| | | | | | | | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Create Referral | REF-1 | Name of Referring Practitioner | Printed name of professional | 01 Sending Practitioner (requestor) | Name |   | Yes | agree / comments (UN)put this on hold (JL) | Practitioner.name | ServiceRequest.requester Reference(PractitionerRole.practitioner -> Practitioner) |   |   |
| Create Referral | REF-2 | Practitioner Role | Designation or role of referring professional | 01 Sending Practitioner (requestor) | List | Midwife, District Nurse, District MEdical Officer | Yes |   | PractitionerRole.code | ServiceRequest.requester Reference(PractitionerRole) | PractitionerRole.code├─ Display - PSOC/PHIC├─ Code - Snomed |   |
| Create Referral | REF-3 | Date & Time of Signature | When signed | 01 Sending Practitioner (requestor) | DateTime |   | No |   | Provenance.recorded | ServiceRequest.relevantHistory |   |   |
| Create Referral | REF-4 | Professional Signature | Signature of the professional | 01 Sending Practitioner (requestor) |   |   | No | For TDG: Review datatype for signature | Provenance.signature | ServiceRequest.relevantHistory |   |   |
| Create Referral | REF-5 | Initiating Facility Name | Referring facility official name.Imp: For pregnancy it is Brrangay Name | 02 Sending Facility (requestor) | Text | Dr Alvin to add example of actual Value | Yes | For TDG: Please consider the means of NHFR-based data retrieval | Organization.name | ServiceRequest.requester Reference (PractitionerRole.organization -> Organization) |   |   |
| Create Referral | REF-6 | Initiating Facility NHFR Code | DOH National Health Facility Registry code | 02 Sending Facility (requestor) | Code |   | Yes | Refer to REF-5 | Organization.identifier(NHFR).value | ServiceRequest.requester Reference(PractitionerRole.organization) |   |   |
| Create Referral | REF-7 | Initiating Facility Address | Facility address | 02 Sending Facility (requestor) | Address |   | No | Refer to REF-5 | Organization.address | ServiceRequest.requester Reference(PractitionerRole.organization) |   |   |
| Create Referral | REF-8 | Initiating Facility Contact Number | Facility phone number | 02 Sending Facility (requestor) | Phone Number |   | No | Refer to REF-5 | Organization.telecom | ServiceRequest.requester Reference(PractitionerRole.organization) |   |   |
| Create Referral | REF-9 | Care Navigator | Name of receiving staff/navigator | 03 Recieving Practitioner | Name |   | No |   | Practitioner.name | Task.owner Reference(PractitionerRole.practitioner -> Practitioner Name) |   | All Requesting data is represented by ServiceRequest. These are data elements that remain fixed throughout the referral process (the “root” of the referral). For example: Referring Practitioner, Initiating Facility, Reason for referral. Once established, these values do not change as the referral progresses.All Receiving data is represented by a Task. These are data elements that are moving/dynamic -- may change as the referral is acted upon. For example: Receiving facility, care navigator, time called. Acceptance or rejection of the referral may change these values. |
| Create Referral | REF-10 | Receiving Facility Name | Intended receiving facility | 04 Receiving Facility | Free Text |   | Yes | Refer to REF-5 | Organization.name | Task.owner Reference(PractitionerRole.organization -> Organization) |   |   |
| Create Referral | REF-11 | Receiving Facility NHFR Code | DOH facility code of receiver | 04 Receiving Facility | Code |   | Yes | Refer to REF-5 | Organization.identifier(NHFR).value | Task.owner Reference(PractitionerRole.organization -> Organization) |   |   |
| Create Referral | REF-12 | Health Care Provider Network (HCPN) Name | Name of the Health Care Provider Network for Referrals. Referrals can only be be within Network | 05 Referral Request | Free Text |   | No | For TDG: Please consider the means of HCPN-based data retrieval | Organization.identifier(HCPN).value├─ Slice by .url (new - cannonical) | Task.owner Reference(PractitionerRole.organization -> Organization) |   |   |
| Create Referral | REF-13 | Date of Referral | Date the referral was created | 05 Referral Request | Date |   | Yes |   | ServiceRequest.authoredOn |   |   |   |
| Create Referral | REF-14 | Referral Category | Urgency and setting indicated by the referrer (emergency vs outpatient/routine). | 05 Referral Request | List | Emergency or Outpatient | Yes |   | ServiceRequest.priority | removed asapAlready addressed: https://build.fhir.org/ig/ph-ereferral-organization/ph-ereferral/en/ValueSet-ereferral-priority.htmlNotify Terminology teamurn://example.com/ph-ereferral/fhir/ValueSet/ereferral-priority | ServiceRequest.priority (Required - routine | urgent | removed_asap | stat) | ServiceRequest.priority - drop from the UI side the "asap" and "urgent" code. Ask John if this will work.In the server side, we can opt to reject submissions with "asap". However, in the UI side, if doctors will click this they might ask why this did not work.Next FHIR Path is "ServiceRequest.category" |
| Create Referral | REF-15 | Time Called | This is the date and time when the sending facility called the receiving facility regarding initial inquiry of the referral | 05 Referral Request | DateTime |   | No | Retained definition and REF-17 dependent. Using the tentative decision on REF-17, "Action point: Return". Hence, will record non-successful referrals. | Task.authoredOn | Task.focus Reference(ServiceRequest) |   |   |
| Create Referral | REF-16 | Reason for Referral (service type) | Classification of the requested service | 05 Referral Request | Structured List | ConsultationDiagnosticsTreatment/ProcedureOthers | Yes |   | ServiceRequest.category |   | Terminology Team to Create a ValuesetBase Example: https://hl7.org/fhir/R4/valueset-servicerequest-category.html |   |
| Referral Triage | REF-17 | Action Point: Received | Receiving facility confirms receipt---Action point should reflect the action of the receiver. This data element may be conditional, depending on the receiver's response (accepted, forwarded (to a different facility), or returned/rejected). | 05 Referral Request |   | Task.status =code: receiveddisplay: Received (keep) |   | No | Task.status |   | TaskStatus - use base FHIR |   |
| Referral Triage | REF-18 | Action Point: Referred (Forwarded) | Case redirected to another facility | 05 Referral Request |   | Task.status =code: rejected | No | Refer to REF-17 | Task.status |   |   |   |
| Presenting Patient | REF-21 | Patient Full Name | Patient legal name | 06 Patient Demographics | Name |   | Yes |   | Patient.name |   |   |   |
| Presenting Patient | REF-22 | Sex (Administrative Gender) | Administrative gender of patient | 06 Patient Demographics | Coded List |   | Yes |   | Patient.gender |   |   |   |
| Presenting Patient | REF-23 | Birth Date | Patient date of birth | 06 Patient Demographics | Date |   | Yes |   | Patient.birthDate |   |   |   |
| Presenting Patient | REF-24 | Age (computed) | Derived age at referral | 06 Patient Demographics | Formula / Logic |   | No |   | Patient.birthDate |   |   |   |
| Presenting Patient | REF-25 | Identity Number (PhilSys) | PhilSys National ID number | 06 Patient Demographics | ID |   | No |   | Patient.identifier(PHCorePhilSysID) |   |   |   |
| Presenting Patient | REF-26 | PhilHealth ID | PhilHealth membership number | 06 Patient Demographics | ID |   | No |   | Patient.identifier(PHCorePhilHealthID) |   |   |   |
| Presenting Patient | REF-27 | Patient Address | Current residence address | 06 Patient Demographics | Address |   | Yes |   | Patient.address |   |   |   |
| Presenting Patient | REF-28 | Contact Number | Patient phone | 06 Patient Demographics |   |   | No |   | Patient.telecom |   |   |   |
| Presenting Patient | REF-29 | Accompanied By / Next of Kin | Companion/guardian details | 06 Patient Demographics |   |   | No |   | Patient├─ Patient.contact├─ Patient.contact.name├─ Patient.contact.telecom |   |   |   |
| Presenting Patient | REF-30 | Patient Disability Registration | PWD registration status/ID | 06 Patient Demographics |   |   | No |   | Patient.extension[pwdDisability] |   |   |   |
| Assess Patient Condition | REF-31 | Chief Complaint | Presenting complaint | 07 Clinical Information |   |   | No |   | Condition├─ Condition.code.text├─ Condition.category = problem-list-item | ServiceRequest.reasonReference Reference (Condition) |   |   |
| Attach Clinical Summary | REF-32 | Clinical History | Pertinent history | 07 Clinical Information |   |   | No |   | Observation (see above)├─ Observation.note |   |   |   |
| Attach Clinical Summary | REF-33 | Vital Signs – Blood Pressure | BP at pre-transfer (can we say latest BP, at the time of referral creation??)Do we need all these vitals for all referrals? or Disease Specific---Follow the AU Core Vital Signs approach | 07 Clinical Information | Numeric (systolic/diastolic) |   | No |   | Observation├─ Observation.code - ask Term Team├─ Observation.value[x]├─ Observation.category = vital-signs├─ Observation.component[0] Systolic├─ Observation.component[1] DiastolicSystolic code Term TeamDiastolic code Term Team | ServiceRequest.supportingInfoObservation.value[x] |   |   |
| Attach Clinical Summary | REF-34 | Vital Signs – Heart Rate | Pulse rate | 07 Clinical Information |   |   | No |   | Observation├─ Observation.code - ask Term Team├─ Observation.value[x]├─ Observation.category = vital-signs | ServiceRequest.supportingInfoReference(Observation.value[x]) |   |   |
| Attach Clinical Summary | REF-35 | Vital Signs – Respiratory Rate | Resp rate | 07 Clinical Information | Numeric |   | No |   | Observation├─ Observation.code - ask Term Team├─ Observation.value[x]├─ Observation.category = vital-signs | ServiceRequest.supportingInfoReference(Observation.value[x]) |   |   |
| Attach Clinical Summary | REF-36 | Vital Signs – Oxygen Saturation | SpO2 | 07 Clinical Information | Numeric |   | No |   | Observation├─ Observation.code - ask Term Team├─ Observation.value[x]├─ Observation.category = vital-signs | ServiceRequest.supportingInfoReference(Observation.value[x]) |   |   |
| Attach Clinical Summary | REF-37 | Vital Signs – Temperature | Body temperature | 07 Clinical Information | Numeric |   | No |   | Observation├─ Observation.code - ask Term Team├─ Observation.value[x]├─ Observation.category = vital-signs | ServiceRequest.supportingInfoReference(Observation.value[x]) |   |   |
| Attach Clinical Summary | REF-38 | Vital Signs – Weight | Weight (kg) | 07 Clinical Information | Numeric |   | No |   | Observation├─ Observation.code - ask Term Team├─ Observation.value[x]├─ Observation.category = vital-signs | ServiceRequest.supportingInfoReference(Observation.value[x]) |   |   |
| Attach Clinical Summary | REF-39 | Treatment Given | Stabilization procedures/meds | 07 Clinical Information |   |   | No |   | Procedure.note | ServiceRequest.supportingInfoReference(Procedure.note) |   |   |
| Attach Clinical Summary | REF-40 | Laboratory Results (attachments) | Labs supporting the referral | 07 Clinical Information | File (PDFs, JPEG, etc.) |   | No |   | DiagnositicReport.presentedForm(Attachment.data) | ServiceRequest.supportingInfoReference(DiagnosticReport) |   |   |
| Assess Patient | REF-41 | Working Impression (clinical reason) | Provisional diagnosis/assessment motivating referral | 07 Clinical Information | Text |   | Yes |   | Condition├─ Condition.code├─ Condition.category = encounter-diagnosis | ServiceRequest.supportingInfoReference(Condition.code) |   |   |

> **Note:** The full CSV can also be downloaded for offline use or integration with other tools. See the [Download](#download) section below.

-------

## Download

* [Download data-dictionary.csv](data-dictionary.csv)

-------

## Data Dictionary Structure

The data dictionary covers all profiles defined in the PH eReferral IG and includes the following columns:

| | |
| :--- | :--- |
| **TDG ID** | Technical Development Group identifier (e.g. REF-1 REF-21) |
| **Data Element** | Human-readable name of the data element |
| **Definition** | Clinical or business definition |
| **FHIR Resource** | The FHIR resource that carries this data element |
| **FHIR Path** | The full FHIR element path |
| **Cardinality** | Minimum and maximum occurrences (e.g. 1..1 0..*) |
| **Data Type** | FHIR data type (e.g. Reference CodeableConcept dateTime) |
| **Value Set / Binding** | Bound value set identifier system or fixed value |
| **Must Support** | Whether the element is marked Must Support in the IG |
| **Notes** | Implementation notes references and edge cases |

-------

## Profile Coverage

The data dictionary covers the following eReferral profiles:

| | | |
| :--- | :--- | :--- |
| [EReferral ServiceRequest](StructureDefinition-ereferral-service-request.md) | REF-1 to REF-21 REF-40 REF-96 REF-97 | ServiceRequest |
| [ERefPatient](StructureDefinition-ereferral-patient.md) | REF-21 to REF-30 | Patient |
| [EReferral Task](StructureDefinition-ereferral-task.md) | REF-9 REF-41 to REF-48 REF-91 to REF-93 | Task |
| [EReferral Provenance](StructureDefinition-ereferral-provenance.md) | REF-3 REF-4 REF-76 to REF-83 | Provenance |
| [ERefEncounter](StructureDefinition-ereferral-encounter.md) | REF-49 to REF-53 REF-89 to REF-90 | Encounter |
| [ERefObservation](StructureDefinition-ereferral-observation.md) | REF-31 REF-33 to REF-38 REF-66 to REF-71 REF-94 to REF-95 | Observation |
| [ERefMedicationAdministration](StructureDefinition-ereferral-medication-administration.md) | REF-39 REF-72 to REF-75 | MedicationAdministration |
| [ERefImmunization](StructureDefinition-ereferral-immunization.md) | REF-54 to REF-57 | Immunization |
| [ERefRelatedPerson](StructureDefinition-ereferral-related-person.md) | REF-29 REF-58 to REF-65 | RelatedPerson |
| [ERefPractitionerRole](StructureDefinition-ereferral-practitioner-role.md) | REF-1 REF-2 REF-5 to REF-11 REF-84 to REF-88 | PractitionerRole |

-------

## How to Use the Data Dictionary

### For Implementers

* Use the **TDG ID** column to trace requirements back to the original TDG specification
* Check the **Must Support** column to identify which elements your system must implement
* Review the **Value Set / Binding** column to ensure your coded values conform to the IG

### For IG Authors

* The CSV file serves as the single source of truth for TDG-to-FHIR mappings
* Updates to the CSV should be reflected in the FSH profile definitions
* The CSV is versioned through the IG build process

### For Connectathon Testers

* Reference the data dictionary when validating that test fixtures include all required elements
* Use the **Cardinality** column to verify that required elements are present (1..1) and optional elements are handled correctly

-------

## Maintenance

The data dictionary is maintained by the PH eReferral IG authoring team. Updates are driven by:

* TDG Technical Working Group on Digital Health decisions
* PH Core profile updates
* Connectathon feedback and implementation experience
* National health data standards revisions

For questions or corrections please open an issue in the [PH eReferral repository](https://github.com/ph-ereferral-organization/ph-ereferral/issues).

-------

## See Also

* [EReferral ServiceRequest Profile](StructureDefinition-ereferral-service-request.md)
* [ERefPatient Profile](StructureDefinition-ereferral-patient.md)
* [EReferral Task Profile](StructureDefinition-ereferral-task.md)
* [v0.1 Connectathon Readiness](connectathon-readiness.md)
* [v0.1 Scope and Release Notes](v01-scope.md)

