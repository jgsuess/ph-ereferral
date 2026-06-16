# Home - PH eReferral Implementation Guide v0.1.0

## Home

# Philippine eReferral Implementation Guide (PH eReferral IG)

> **Project Status: In Development** This Implementation Guide is under active development and is not yet available for public or production use. Content, data models, and implementation details are subject to change.

## Introduction

The Philippine eReferral Implementation Guide (PH eReferral IG) is a **use case Implementation Guide** that provides a standardized approach for electronic referral workflows within Health Care Provider Networks (HCPNs) in the Philippines. It defines the minimum FHIR-based requirements to support seamless referral of patients between healthcare providers using HL7® FHIR®© standards.

This IG aligns with the **[Universal Health Care Act (Republic Act 11223)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/86448)** and **[DOH Administrative Order 2020-0019](https://drive.google.com/file/d/1Uri9Iov3YPw3rc3AidV6dXjv8y_W7ydr/view)**, which mandates interoperable health information systems for integrated care across HCPNs. It enables FHIR-based referral messaging, patient navigation, and back-referral workflows consistent with the AO's Annex D requirements.

This FHIR IG is provided for testing purposes and is not yet suitable for production systems.

For the narrative and policy foundation of this implementation guide, see [WHO SMART Guidelines L1 Basis for the PH eReferral IG](who-smart-l1.md).

For the minimum v0.1 testing path, build instructions, fixture pack, and release-readiness checklist, see [v0.1 Connectathon Quick-Start, Test Pack, and Release Readiness](connectathon-readiness.md).

## What is a Use Case IG?

A use case Implementation Guide builds upon foundational and core standards to address a specific clinical or administrative workflow. Unlike base or core IGs that establish broad interoperability foundations, a use case IG:

* **Targets a specific workflow** — in this case, the patient referral process between healthcare facilities
* **Profiles core resources for the use case** — constrains and extends PH Core profiles to meet referral-specific requirements
* **Defines actors and interactions** — identifies systems, users, and the exchanges between them
* **Specifies business rules** — documents the rules governing referral lifecycle, status transitions, and required data elements

PH eReferral demonstrates how FHIR resources can be applied to solve a real-world interoperability challenge in the Philippine healthcare system.

The corresponding L1 narrative basis page explains how this implementation guide is grounded in national policy, HCPN service-delivery design, primary care coordination, and future traceability to WHO SMART L2 and L3 work.

## Purpose and Scope

The PH eReferral IG aims to:

1. Enable standardized electronic referral workflows between healthcare facilities within HCPNs
1. Support patient care continuity through interoperable FHIR-based data exchange
1. Implement[UHC Act (RA 11223)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/86448)and[DOH AO 2020-0019](https://drive.google.com/file/d/1Uri9Iov3YPw3rc3AidV6dXjv8y_W7ydr/view)requirements for referral systems
1. Provide clear, testable specifications for HCPN referral system implementers

This guide focuses on referral-specific FHIR resources (e.g., ServiceRequest, Task, Communication) and their relationships with core clinical and administrative resources (Patient, Practitioner, Organization, Encounter).

It does not define general clinical workflows outside the referral context.

## Usage of this Guide

* **Healthcare Facilities**: Implement eReferral profiles to enable standardized patient referrals
* **Health Information Systems**: Use as a baseline for developing interoperable referral capabilities
* **Developers and Vendors**: Build and validate FHIR-conformant referral systems

## Relationship with Other IGs

PH eReferral fits into the Philippine FHIR IG architecture as a **use case layer** implementation guide that builds upon foundational profiles:

| | | |
| :--- | :--- | :--- |
| Core | [PH Core IG](https://github.com/UP-Manila-SILab/ph-core) | **Base profiles**– Foundational rules, common extensions, and national identifiers (Patient, Practitioner, Organization, Encounter, etc.) |
| **Use Case** | **PH eReferral IG** | **Referral-specific workflows and interactions**– HCPN referral messaging built on PH Core |
| Program | Program-specific IGs | Tailored implementations for specific health programs or facilities |

PH Core provides the **parent/base profiles** used by this IG. PH eReferral:

* Uses PH Core as its foundation – inheriting constraints from PH Core profiles (Patient, Practitioner, Organization, Encounter, etc.)
* Defines referral-specific profiles (ServiceRequest, Task, etc.) for interoperability
* Specifies the referral workflow actors and their interactions
* Documents the complete referral lifecycle from creation to fulfillment
* Provides RESTful API guidance for referral operations

This layered approach enables reuse of common PH Core definitions while addressing the specific needs of HCPN referral workflows mandated by the [UHC Act](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/86448).

## Dependencies

This publication includes IP covered under the following statements.

* These codes are excerpted from ASTM Standard, E1762-95(2013) - Standard Guide for Electronic Authentication of Health Care Information, Copyright by ASTM International, 100 Barr Harbor Drive, West Conshohocken, PA 19428. Copies of this standard are available through the ASTM Web Site at www.astm.org.

* [Signature Type Codes](http://hl7.org/fhir/R4/codesystem-signature-type.html): [Provenance/ExampleERefProvenanceSignature](Provenance-ExampleERefProvenanceSignature.md)


* This material contains content from [LOINC](http://loinc.org). LOINC is copyright © 1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the [license](http://loinc.org/license). LOINC® is a registered United States trademark of Regenstrief Institute, Inc.

* LOINC: [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md), [Observation/ExampleERefObservationBP](Observation-ExampleERefObservationBP.md)... Show 15 more, [Observation/ExampleERefObservationChiefComplaint](Observation-ExampleERefObservationChiefComplaint.md), [Observation/ExampleERefObservationECG](Observation-ExampleERefObservationECG.md), [Observation/ExampleERefObservationHeartRate](Observation-ExampleERefObservationHeartRate.md), [Observation/ExampleERefObservationLabGlucose](Observation-ExampleERefObservationLabGlucose.md), [Observation/ExampleERefObservationOxygenSat](Observation-ExampleERefObservationOxygenSat.md), [Observation/ExampleERefObservationRespiratoryRate](Observation-ExampleERefObservationRespiratoryRate.md), [Observation/ExampleERefObservationTemperature](Observation-ExampleERefObservationTemperature.md), [Observation/ExampleERefObservationWeight](Observation-ExampleERefObservationWeight.md), [Observation/observation-blood-pressure-ex](Observation-observation-blood-pressure-ex.md), [Observation/observation-chief-complaint-ex](Observation-observation-chief-complaint-ex.md), [Observation/observation-heart-rate-ex](Observation-observation-heart-rate-ex.md), [Observation/observation-oxygen-saturation-ex](Observation-observation-oxygen-saturation-ex.md), [Observation/observation-respiratory-rate-ex](Observation-observation-respiratory-rate-ex.md), [Observation/observation-temperature-ex](Observation-observation-temperature-ex.md) and [Observation/observation-weight-ex](Observation-observation-weight-ex.md)


* This material contains content that is copyright of SNOMED International. Implementers of these specifications must have the appropriate SNOMED CT Affiliate license - for more information contact [https://www.snomed.org/get-snomed](https://www.snomed.org/get-snomed) or [info@snomed.org](mailto:info@snomed.org).

* [SNOMED Clinical Terms&reg; (SNOMED CT&reg;)](http://hl7.org/fhir/R4/codesystem-snomedct.html): [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md), [Bundle/registration-transaction-ex](Bundle-registration-transaction-ex.md)... Show 34 more, [Condition/ExampleERefConditionChestPain](Condition-ExampleERefConditionChestPain.md), [Condition/ExampleERefConditionHypertensiveEmergency](Condition-ExampleERefConditionHypertensiveEmergency.md), [Condition/condition-pregnancy-ex](Condition-condition-pregnancy-ex.md), [ERefServiceRequest](StructureDefinition-ereferral-service-request.md), [EReferralReason](ValueSet-ereferral-reason.md), [EReferralServiceCategory](ValueSet-ereferral-service-category.md), [Encounter/ExampleERefEncounter](Encounter-ExampleERefEncounter.md), [Encounter/encounter-anc-ex](Encounter-encounter-anc-ex.md), [Encounter/encounter-registration-ex](Encounter-encounter-registration-ex.md), [Immunization/ExampleERefImmunizationRoutine](Immunization-ExampleERefImmunizationRoutine.md), [Medication/ExampleERefMedicationAntibiotic](Medication-ExampleERefMedicationAntibiotic.md), [Medication/ExampleERefMedicationTwinact](Medication-ExampleERefMedicationTwinact.md), [MedicationAdministration/ExampleERefMedicationAdministrationAntibiotic](MedicationAdministration-ExampleERefMedicationAdministrationAntibiotic.md), [MedicationAdministration/ExampleERefMedicationAdministrationChronic](MedicationAdministration-ExampleERefMedicationAdministrationChronic.md), [MedicationAdministration/medicationadministration-ifa-ex](MedicationAdministration-medicationadministration-ifa-ex.md), [Practitioner/ExampleERefPractitioner](Practitioner-ExampleERefPractitioner.md), [PractitionerRole/ExampleERefPractitionerRole](PractitionerRole-ExampleERefPractitionerRole.md), [PractitionerRole/ExampleERefPractitionerRoleMinimal](PractitionerRole-ExampleERefPractitionerRoleMinimal.md), [PractitionerRole/ExampleERefPractitionerRoleRequester](PractitionerRole-ExampleERefPractitionerRoleRequester.md), [PractitionerRole/practitionerrole-abraham-ex](PractitionerRole-practitionerrole-abraham-ex.md), [Procedure/ExampleERefProcedureECG](Procedure-ExampleERefProcedureECG.md), [Procedure/ExampleERefProcedureInitialManagement](Procedure-ExampleERefProcedureInitialManagement.md), [ServiceRequest/ExampleERefServiceRequest](ServiceRequest-ExampleERefServiceRequest.md), [ServiceRequest/ExampleERefServiceRequestMinimal](ServiceRequest-ExampleERefServiceRequestMinimal.md), [ServiceRequest/ExampleERefServiceRequestOnward](ServiceRequest-ExampleERefServiceRequestOnward.md), [ServiceRequest/ExampleERefServiceRequestTask](ServiceRequest-ExampleERefServiceRequestTask.md), [ServiceRequest/servicerequest-lab-orders-ex](ServiceRequest-servicerequest-lab-orders-ex.md), [ServiceRequest/servicerequest-ultrasound-ex](ServiceRequest-servicerequest-ultrasound-ex.md), [Task/ExampleERefTaskAccepted](Task-ExampleERefTaskAccepted.md), [Task/ExampleERefTaskCompleted](Task-ExampleERefTaskCompleted.md), [Task/ExampleERefTaskReceived](Task-ExampleERefTaskReceived.md), [Task/ExampleERefTaskReferredOnward](Task-ExampleERefTaskReferredOnward.md), [Task/ExampleERefTaskRejected](Task-ExampleERefTaskRejected.md) and [Task/ExampleERefTaskRequested](Task-ExampleERefTaskRequested.md)


* This material derives from the HL7 Terminology (THO). THO is copyright ©1989+ Health Level Seven International and is made available under the CC0 designation. For more licensing information see: [https://terminology.hl7.org/license.html](https://terminology.hl7.org/license.html)

* [Condition Category Codes](http://terminology.hl7.org/7.2.0/CodeSystem-condition-category.html): [Condition/ExampleERefConditionChestPain](Condition-ExampleERefConditionChestPain.md) and [Condition/ExampleERefConditionHypertensiveEmergency](Condition-ExampleERefConditionHypertensiveEmergency.md)
* [Condition Clinical Status Codes](http://terminology.hl7.org/7.2.0/CodeSystem-condition-clinical.html): [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md), [Condition/ExampleERefConditionChestPain](Condition-ExampleERefConditionChestPain.md), [Condition/ExampleERefConditionHypertensiveEmergency](Condition-ExampleERefConditionHypertensiveEmergency.md) and [Condition/condition-pregnancy-ex](Condition-condition-pregnancy-ex.md)
* [ConditionVerificationStatus](http://terminology.hl7.org/7.2.0/CodeSystem-condition-ver-status.html): [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md), [Condition/ExampleERefConditionChestPain](Condition-ExampleERefConditionChestPain.md), [Condition/ExampleERefConditionHypertensiveEmergency](Condition-ExampleERefConditionHypertensiveEmergency.md) and [Condition/condition-pregnancy-ex](Condition-condition-pregnancy-ex.md)
* [Immunization Funding Source](http://terminology.hl7.org/7.2.0/CodeSystem-immunization-funding-source.html): [Immunization/ExampleERefImmunizationRoutine](Immunization-ExampleERefImmunizationRoutine.md)
* [Observation Category Codes](http://terminology.hl7.org/7.2.0/CodeSystem-observation-category.html): [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md), [Observation/ExampleERefObservationBP](Observation-ExampleERefObservationBP.md)... Show 15 more, [Observation/ExampleERefObservationChiefComplaint](Observation-ExampleERefObservationChiefComplaint.md), [Observation/ExampleERefObservationECG](Observation-ExampleERefObservationECG.md), [Observation/ExampleERefObservationHeartRate](Observation-ExampleERefObservationHeartRate.md), [Observation/ExampleERefObservationLabGlucose](Observation-ExampleERefObservationLabGlucose.md), [Observation/ExampleERefObservationOxygenSat](Observation-ExampleERefObservationOxygenSat.md), [Observation/ExampleERefObservationRespiratoryRate](Observation-ExampleERefObservationRespiratoryRate.md), [Observation/ExampleERefObservationTemperature](Observation-ExampleERefObservationTemperature.md), [Observation/ExampleERefObservationWeight](Observation-ExampleERefObservationWeight.md), [Observation/observation-blood-pressure-ex](Observation-observation-blood-pressure-ex.md), [Observation/observation-chief-complaint-ex](Observation-observation-chief-complaint-ex.md), [Observation/observation-heart-rate-ex](Observation-observation-heart-rate-ex.md), [Observation/observation-oxygen-saturation-ex](Observation-observation-oxygen-saturation-ex.md), [Observation/observation-respiratory-rate-ex](Observation-observation-respiratory-rate-ex.md), [Observation/observation-temperature-ex](Observation-observation-temperature-ex.md) and [Observation/observation-weight-ex](Observation-observation-weight-ex.md)
* [Organization type](http://terminology.hl7.org/7.2.0/CodeSystem-organization-type.html): [Eastern District Medical Center](Organization-ExampleERefOrganizationOnwardReceiving.md), [Manila General Hospital](Organization-ExampleERefOrganizationReceiving.md) and [Philippine Heart Center](Organization-ExampleERefReceivingHospital.md)
* [Practitioner role](http://terminology.hl7.org/7.2.0/CodeSystem-practitioner-role.html): [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md) and [PractitionerRole/practitionerrole-jane-ex](PractitionerRole-practitionerrole-jane-ex.md)
* [Provenance participant type](http://terminology.hl7.org/7.2.0/CodeSystem-provenance-participant-type.html): [ERefProvenance](StructureDefinition-ereferral-provenance.md), [Provenance/ExampleERefProvenanceSignature](Provenance-ExampleERefProvenanceSignature.md) and [Provenance/ExampleERefProvenanceUpdate](Provenance-ExampleERefProvenanceUpdate.md)
* [identifierType](http://terminology.hl7.org/7.2.0/CodeSystem-v2-0203.html): [Barangay Malusog Health Centre](Organization-organization-sending-facility-ex.md), [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md), [Bundle/registration-transaction-ex](Bundle-registration-transaction-ex.md), [Manila General Hospital - Barangay 143 Health Center](Organization-ExampleERefReferringFacility.md) and [Metro Imaging Centre](Organization-organization-receiving-facility-ex.md)
* [providerRole](http://terminology.hl7.org/7.2.0/CodeSystem-v2-0443.html): [Immunization/ExampleERefImmunizationRoutine](Immunization-ExampleERefImmunizationRoutine.md)
* [ActCode](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ActCode.html): [Bundle/anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md), [Bundle/registration-transaction-ex](Bundle-registration-transaction-ex.md), [Encounter/ExampleERefEncounter](Encounter-ExampleERefEncounter.md), [Encounter/encounter-anc-ex](Encounter-encounter-anc-ex.md) and [Encounter/encounter-registration-ex](Encounter-encounter-registration-ex.md)
* [DataOperation](http://terminology.hl7.org/7.2.0/CodeSystem-v3-DataOperation.html): [Provenance/ExampleERefProvenanceSignature](Provenance-ExampleERefProvenanceSignature.md) and [Provenance/ExampleERefProvenanceUpdate](Provenance-ExampleERefProvenanceUpdate.md)
* [ObservationInterpretation](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ObservationInterpretation.html): [Observation/ExampleERefObservationBP](Observation-ExampleERefObservationBP.md), [Observation/ExampleERefObservationECG](Observation-ExampleERefObservationECG.md)... Show 4 more, [Observation/ExampleERefObservationHeartRate](Observation-ExampleERefObservationHeartRate.md), [Observation/ExampleERefObservationOxygenSat](Observation-ExampleERefObservationOxygenSat.md), [Observation/ExampleERefObservationRespiratoryRate](Observation-ExampleERefObservationRespiratoryRate.md) and [Observation/ExampleERefObservationTemperature](Observation-ExampleERefObservationTemperature.md)
* [ParticipationType](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ParticipationType.html): [Encounter/ExampleERefEncounter](Encounter-ExampleERefEncounter.md)
* [Race](http://terminology.hl7.org/7.2.0/CodeSystem-v3-Race.html): [Patient/ERefPatientExample](Patient-ERefPatientExample.md)
* [Religious Affiliation](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ReligiousAffiliation.html): [Patient/ERefPatientExample](Patient-ERefPatientExample.md)
* [RoleCode](http://terminology.hl7.org/7.2.0/CodeSystem-v3-RoleCode.html): [Bundle/registration-transaction-ex](Bundle-registration-transaction-ex.md), [ERefRelatedPerson](StructureDefinition-ereferral-related-person.md)... Show 6 more, [EReferralRelationshipType](ValueSet-ereferral-relationship-type.md), [Manila General Hospital - Barangay 143 Health Center](Organization-ExampleERefReferringFacility.md), [Patient/ERefPatientExample](Patient-ERefPatientExample.md), [RelatedPerson/ExampleERefRelatedPersonAccompanying](RelatedPerson-ExampleERefRelatedPersonAccompanying.md), [RelatedPerson/ExampleERefRelatedPersonNextOfKin](RelatedPerson-ExampleERefRelatedPersonNextOfKin.md) and [RelatedPerson/relatedperson-companion-ex](RelatedPerson-relatedperson-companion-ex.md)


This is an R4 IG. None of the features it uses are changed in R4B, so it can be used as is with R4B systems. Packages for both [R4 (fhir.ph.ereferral.r4)](../package.r4.tgz) and [R4B (fhir.ph.ereferral.r4b)](../package.r4b.tgz) are available.




| | | |
| :--- | :--- | :--- |
| [Draft PH Core](https://build.fhir.org/ig/jgsuess/ph-core/) | [current](https://simplifier.net/packages/fhir.ph.core/current) |  |
| [FHIR Extensions Pack](http://hl7.org/fhir/extensions/5.3.0) | [5.3.0](https://simplifier.net/packages/hl7.fhir.uv.extensions.r4/5.3.0) | Automatically added as a dependency - all IGs depend on the HL7 Extension Pack |
| [FHIR R4 package : Core](http://hl7.org/fhir/R4) | [4.0.1](https://simplifier.net/packages/hl7.fhir.r4.core/4.0.1) | Imported by HL7 Terminology (THO) (and potentially others) |
| [HL7 Terminology (THO)](http://terminology.hl7.org/7.2.0) | [7.2.0](https://simplifier.net/packages/hl7.terminology.r4/7.2.0) | Automatically added as a dependency - all IGs depend on HL7 Terminology |

*There are no Global profiles defined*

