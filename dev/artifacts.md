# Artifacts Summary - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Example: Example Instances 

These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like.

| | |
| :--- | :--- |
| [Condition — Pregnancy](Condition-condition-pregnancy-ex.md) | Charity's confirmed pregnancy, provisionally dated to a last menstrual period around New Year 2026, giving an estimated gestational age of 12–15 weeks. |
| [Encounter — First Antenatal Care Contact](Encounter-encounter-anc-ex.md) | The counselling session (08:30–10:00) in which nurse Jane confirms Charity's pregnancy, records vital signs and clinical history, and initiates the referral. |
| [Encounter — Registration](Encounter-encounter-registration-ex.md) | A brief ambulatory encounter (08:00–08:15) in which clerk Abraham collects Charity's demographic information and registers her in the system. |
| [MedicationAdministration — Iron and Folic Acid](MedicationAdministration-medicationadministration-ifa-ex.md) | Jane dispenses iron and folic acid (IFA) tablets to Charity with instructions to take one tablet daily, following WHO ANC guidelines for nutritional supplementation. |
| [Observation — Blood Pressure](Observation-observation-blood-pressure-ex.md) | Charity's blood pressure measured during the physical exam: systolic 110 mmHg, diastolic 70 mmHg — within the normal range for pregnancy. |
| [Observation — Body Temperature](Observation-observation-temperature-ex.md) | Charity's body temperature of 36.8 degrees Celsius, a normal reading taken during the physical exam. |
| [Observation — Body Weight](Observation-observation-weight-ex.md) | Charity's weight of 55 kg, recorded as a baseline measurement at her first ANC contact. |
| [Observation — Chief Complaint](Observation-observation-chief-complaint-ex.md) | Charity's reason for visiting the health centre: a missed menstrual cycle and nausea, prompting her to seek antenatal care. |
| [Observation — Heart Rate](Observation-observation-heart-rate-ex.md) | Charity's resting heart rate of 78 beats per minute, recorded as part of her vital signs during the ANC contact. |
| [Observation — Oxygen Saturation](Observation-observation-oxygen-saturation-ex.md) | Charity's peripheral oxygen saturation at 98 percent, confirming adequate oxygenation. |
| [Observation — Respiratory Rate](Observation-observation-respiratory-rate-ex.md) | Charity's respiratory rate of 18 breaths per minute, within the normal adult range. |
| [Organization — Barangay Malusog Health Centre](Organization-organization-sending-facility-ex.md) | The government health centre where Charity is registered and receives her first ANC contact. Identified by its NHFR code. |
| [Organization — Metro Imaging Centre](Organization-organization-receiving-facility-ex.md) | The external imaging centre where Charity is referred for an obstetric ultrasound to confirm gestational age. |
| [Patient — Charity Santos](Patient-patient-charity-ex.md) | Charity is a 24-year-old woman from Barangay Malusog, Quezon City, visiting the health centre for the first time during her pregnancy. Abraham registers her demographics, national IDs, and contact details. |
| [Practitioner — Abraham Reyes](Practitioner-practitioner-abraham-ex.md) | Abraham is the registration clerk who creates Charity's patient record at the health centre front desk. |
| [Practitioner — Jane Dela Cruz](Practitioner-practitioner-jane-ex.md) | Jane is the nurse who conducts Charity's first antenatal care counselling session, records vital signs, and creates the ultrasound referral. |
| [PractitionerRole — Clerk Abraham](PractitionerRole-practitionerrole-abraham-ex.md) | Abraham's role as a registration clerk at Barangay Malusog Health Centre. |
| [PractitionerRole — Nurse Jane](PractitionerRole-practitionerrole-jane-ex.md) | Jane's role as a nurse at Barangay Malusog Health Centre, linked to her practitioner record and the sending facility. |
| [RelatedPerson — Maria Santos (Mother)](RelatedPerson-relatedperson-companion-ex.md) | Charity's mother Maria, registered as her next-of-kin and alternative contact person during the registration process. |
| [ServiceRequest — Laboratory Orders](ServiceRequest-servicerequest-lab-orders-ex.md) | Routine ANC laboratory tests ordered for Charity: diabetes screen, hepatitis B surface antigen, and HIV — in line with WHO recommended investigations. |
| [ServiceRequest — Obstetric Ultrasound Referral](ServiceRequest-servicerequest-ultrasound-ex.md) | Jane refers Charity to Metro Imaging Centre for an obstetric ultrasound to confirm gestational age and due date, needed before 24 weeks of pregnancy. |
| [Task — Referral Tracking](Task-task-referral-ex.md) | Tracks the status of Charity's ultrasound referral. Currently in 'requested' state, awaiting acceptance by Metro Imaging Centre. |
| [anc-contact-transaction-ex](Bundle-anc-contact-transaction-ex.md) | Nurse Jane conducts Charity's first antenatal care visit at Barangay Malusog Health Centre. This bundle captures the full clinical encounter: pregnancy confirmation, vital signs, chief complaint, iron-and-folic-acid dispensing, laboratory orders, and the ultrasound referral to Metro Imaging Centre — along with the task that tracks the referral outcome. |
| [registration-transaction-ex](Bundle-registration-transaction-ex.md) | Clerk Abraham registers Charity at Barangay Malusog Health Centre. This bundle captures everything recorded at the front desk: Charity's demographic details, her national identifiers (PhilSys and PhilHealth), her home address and phone number, and her mother Maria as next-of-kin. It also records Abraham's practitioner role and the registration encounter. |

