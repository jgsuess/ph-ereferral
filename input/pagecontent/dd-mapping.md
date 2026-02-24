### Data Dictionary to FHIR Mapping

This page provides a detailed, element-by-element mapping between the
**PeRef Logical Information Model** (the data dictionary) and the FHIR
example resources published in this Implementation Guide.

The content is organised by **clinical information group**. For each group
you will find:

1. A **pivot table** showing which example resource covers which
   data-dictionary element.
2. A **narrative description** explaining how and why each element is
   represented in FHIR, told through the lens of the ANC scenario
   (Charity, Abraham, Jane).

**Legend**

| Icon | Meaning |
|:----:|---------|
| ✅ | Fully covered by the example |
| ⚠️ | Partially covered — additional resources needed |
| 🕐 | Deferred to a future release |
| — | Not applicable to this scenario |

> **Note:** This page is generated from `dd-coverage.csv` by the script
> `utils/generate-dd-mapping-page.py`.  Re-run the script after updating
> the data dictionary to keep this page in sync.

---

#### Coverage Summary

Out of **46** data-dictionary elements:

| Status | Count | Meaning |
|--------|------:|---------|
| ✅ Covered | 31 | Fully represented in at least one example |
| ⚠️ Partial | 1 | Modelled as orders; results resource still needed |
| 🕐 Deferred | 4 | Postponed to a future release per CDG consensus |
| — Not covered | 10 | Not applicable to this ANC scenario |

---

#### Sending Practitioner

| Element | Data Element | Practitioner Abraham | Practitioner Jane | Practitionerrole Abraham | Practitionerrole Jane |
|---------|-------------|:---:|:---:|:---:|:---:|
| REF-1 | Name of Referring Practitioner | ✅ | ✅ | ✅ | ✅ | 
| REF-2 | Professional Signature | 🕐 | 🕐 | 🕐 | 🕐 | 
| REF-3 | Date & Time of Signature | 🕐 | 🕐 | 🕐 | 🕐 | 

**REF-1 — Name of Referring Practitioner** *(Covered)*
:   The printed name of the referring health professional is stored in a **Practitioner** resource and linked to the facility through a **PractitionerRole**. In our scenario clerk Abraham creates Charity's record during registration (Bundle A), while nurse Jane authors the referral during the ANC contact (Bundle B). Both practitioners appear with their own Practitioner and PractitionerRole instances.
:   FHIR path: `PractitionerRole.practitioner → Practitioner.name`

**REF-2 — Professional Signature** *(Deferred)*
:   A digital or scanned professional signature would be captured in a **Provenance** resource attached to the ServiceRequest. This element is deferred to a future release because the CDG has not yet decided whether the MVP requires electronic signatures or whether a typed name with a system timestamp is sufficient attestation.
:   FHIR path: `Provenance.signature`

**REF-3 — Date & Time of Signature** *(Deferred)*
:   The date and time of the professional’s signature is intended for **Provenance.occurredDateTime**. Like REF‑2, it is deferred — the system can auto-stamp submission time as a fallback.
:   FHIR path: `Provenance.occurredDateTime`

---

#### Sending Facility

| Element | Data Element | Organization Sending Facility |
|---------|-------------|:---:|
| REF-4 | Initiating Facility Name | ✅ | 
| REF-5 | Initiating Facility NHFR Code | ✅ | 
| REF-6 | Initiating Facility Address | ✅ | 
| REF-7 | Initiating Facility Contact Number | ✅ | 

**REF-4 — Initiating Facility Name** *(Covered)*
:   The official name of the referring (sending) facility is recorded in **Organization.name**. In our scenario this is “Barangay Malusog Health Centre”, the government clinic where Charity is registered.
:   FHIR path: `Organization.name`

**REF-5 — Initiating Facility NHFR Code** *(Covered)*
:   The DOH National Health Facility Registry (NHFR) code uniquely identifies the sending facility. It is stored in **Organization.identifier** using the PH-Core NHFR identifier slice, enabling automated routing and facility look-up.
:   FHIR path: `Organization.identifier(system=NHFR)`

**REF-6 — Initiating Facility Address** *(Covered)*
:   The sending facility’s address is captured in **Organization.address** using the PH-Core structured address format (with barangay, city, province). It is optional when the address can be retrieved from the NHFR directory.
:   FHIR path: `Organization.address`

**REF-7 — Initiating Facility Contact Number** *(Covered)*
:   The facility’s contact phone number is stored in **Organization.telecom** (system = phone). This supports coordination between sending and receiving facilities.
:   FHIR path: `Organization.telecom(system=phone)`

---

#### Receiving Practitioner

| Element | Data Element | FHIR Resource | Status |
|---------|-------------|---------------|:------:|
| REF-8 | Receiving Personnel | Communication | — |

**REF-8 — Receiving Personnel** *(Not covered in this scenario)*
:   The name of the staff member who acknowledges or accepts the referral at the receiving facility. Mapped to **Communication.recipient**, but not applicable during referral creation — the receiving person is only known after acceptance. Not modelled in this ANC scenario.
:   FHIR path: `Communication.recipient`

---

#### Receiving Facility

| Element | Data Element | Organization Receiving Facility |
|---------|-------------|:---:|
| REF-9 | Receiving Facility Name | ✅ | 
| REF-10 | Receiving Facility NHFR Code | ✅ | 

**REF-9 — Receiving Facility Name** *(Covered)*
:   The name of the intended receiving facility is stored in a separate **Organization** resource. In our scenario this is “Metro Imaging Centre”, the external facility where Charity is referred for an obstetric ultrasound.
:   FHIR path: `Organization.name`

**REF-10 — Receiving Facility NHFR Code** *(Covered)*
:   The NHFR code of the receiving facility, stored in **Organization.identifier** (system = NHFR). This is conditional — required once the receiving facility is confirmed.
:   FHIR path: `Organization.identifier(system=NHFR)`

---

#### Referral Request

| Element | Data Element | Servicerequest Ultrasound | Task Referral |
|---------|-------------|:---:|:---:|
| REF-11 | Health Care Provider Network (HCPN) Name | 🕐 | 🕐 | 
| REF-12 | Date of Referral | ✅ |   | 
| REF-13 | Referral Category | ✅ |   | 
| REF-14 | Time Called | — | — | 
| REF-15 | Reason for Referral (service type) | ✅ |   | 
| REF-16 | Action Point: Received |   | ✅ | 
| REF-17 | Action Point: Referred (Forwarded) | — | — | 
| REF-18 | Return Referral Slip (Attachment) | 🕐 | 🕐 | 
| REF-19 | Call/Email Reference | — | — | 

**REF-11 — Health Care Provider Network (HCPN) Name** *(Deferred)*
:   The Health Care Provider Network (HCPN) name is the umbrella referral network. Mapped to a separate **Organization.name**, but currently on hold pending a CDG decision on whether it should be computed or manually entered.
:   FHIR path: `Organization.name`

**REF-12 — Date of Referral** *(Covered)*
:   The date the referral was created is captured in **ServiceRequest.authoredOn**. In our scenario this is 2026-02-24, the date of Charity’s first ANC contact when nurse Jane initiates the ultrasound referral.
:   FHIR path: `ServiceRequest.authoredOn`

**REF-13 — Referral Category** *(Covered)*
:   The referral category indicates urgency: emergency or outpatient/routine. It maps to **ServiceRequest.priority** using the FHIR `request-priority` value set (emergency → `stat`, outpatient → `routine`). Charity’s referral is routine.
:   FHIR path: `ServiceRequest.priority`

**REF-14 — Time Called** *(Not covered in this scenario)*
:   The date and time when the sending facility called the receiving facility. Mapped to **Communication.sent**. Not applicable in this scenario — Charity’s referral is routine and does not require a phone call.
:   FHIR path: `Communication.sent`

**REF-15 — Reason for Referral (service type)** *(Covered)*
:   The classification of the requested service (e.g. Diagnostics, Consultation). Stored in **ServiceRequest.category** using SNOMED CT codes. For Charity’s ultrasound referral the category is “Diagnostic procedure”.
:   FHIR path: `ServiceRequest.category`

**REF-16 — Action Point: Received** *(Covered)*
:   The action point confirming receipt of the referral by the receiving facility. Modelled through **Task.status** (accepted) combined with **Task.note** for timestamped annotations. In our example the Task is currently in `requested` state, awaiting acceptance.
:   FHIR path: `Task.status + Task.note`

**REF-17 — Action Point: Referred (Forwarded)** *(Not covered in this scenario)*
:   When a referral is redirected to another facility a new **Task** is created and linked via `Task.basedOn`. Not applicable in this scenario — Charity’s referral is not forwarded.
:   FHIR path: `Task.basedOn`

**REF-18 — Return Referral Slip (Attachment)** *(Deferred)*
:   A return referral slip or back-referral summary would be attached as a **DocumentReference**. Excluded from the MVP per CDG consensus.
:   FHIR path: `DocumentReference.content.attachment`

**REF-19 — Call/Email Reference** *(Not covered in this scenario)*
:   The communication channel (phone, email, SMS) and reference used for referral coordination, captured in **Communication.category**, **medium**, and **note**. Not applicable — Charity’s is a routine outpatient referral.
:   FHIR path: `Communication.category + medium + note`

---

#### Patient Demographics

| Element | Data Element | Patient Charity | Relatedperson Companion |
|---------|-------------|:---:|:---:|
| REF-20 | Patient Full Name | ✅ |   | 
| REF-21 | Sex (Administrative Gender) | ✅ |   | 
| REF-22 | Birth Date | ✅ |   | 
| REF-23 | Age (computed) | — | — | 
| REF-24 | Identity Number (PhilSys) | ✅ |   | 
| REF-25 | PhilHealth ID | ✅ |   | 
| REF-26 | Patient Address | ✅ |   | 
| REF-27 | Contact Number | ✅ |   | 
| REF-28 | Accompanied By / Next of Kin |   | ✅ | 
| REF-29 | Patient Disability Registration | — | — | 

**REF-20 — Patient Full Name** *(Covered)*
:   Charity’s full legal name is recorded in **Patient.name** using the HumanName data type (family = “Santos”, given = “Charity”). This is the primary way the patient is identified across all subsequent resources.
:   FHIR path: `Patient.name`

**REF-21 — Sex (Administrative Gender)** *(Covered)*
:   Charity’s administrative gender (`female`) is captured in **Patient.gender** using the HL7 AdministrativeGender code system.
:   FHIR path: `Patient.gender`

**REF-22 — Birth Date** *(Covered)*
:   Charity’s date of birth (2001-08-15) is stored in **Patient.birthDate**. Age can be computed from this value, avoiding the need to persist it separately.
:   FHIR path: `Patient.birthDate`

**REF-23 — Age (computed)** *(Not covered in this scenario)*
:   Age is a derived value computed from the patient’s birth date. Following the data dictionary recommendation it is **not persisted** as a separate resource — systems should calculate it on the fly.
:   FHIR path: `Observation.valueQuantity`

**REF-24 — Identity Number (PhilSys)** *(Covered)*
:   Charity’s Philippine Identification System (PhilSys) national ID is stored in **Patient.identifier** using the PH-Core PhilSys identifier slice. This supports patient matching across facilities.
:   FHIR path: `Patient.identifier(system=PhilSys)`

**REF-25 — PhilHealth ID** *(Covered)*
:   Charity’s PhilHealth membership number is recorded in **Patient.identifier** using the PH-Core PhilHealth identifier slice, enabling insurance verification and claims linkage.
:   FHIR path: `Patient.identifier(system=PhilHealth)`

**REF-26 — Patient Address** *(Covered)*
:   Charity’s home address in Barangay Malusog, Quezon City is captured in **Patient.address** using the PH-Core structured address format with barangay-level detail.
:   FHIR path: `Patient.address`

**REF-27 — Contact Number** *(Covered)*
:   Charity’s mobile phone number is stored in **Patient.telecom** (system = phone, use = mobile), providing a direct contact channel.
:   FHIR path: `Patient.telecom(system=phone)`

**REF-28 — Accompanied By / Next of Kin** *(Covered)*
:   Charity’s mother Maria is recorded as a **RelatedPerson** with relationship = “Mother”, including her name and mobile number. This serves as the alternative contact and next-of-kin record.
:   FHIR path: `RelatedPerson.patient + name + telecom + relationship`

**REF-29 — Patient Disability Registration** *(Not covered in this scenario)*
:   The patient’s PWD (Person with Disability) registration status would be stored in a **Patient extension**. Not applicable in this scenario; the DD has an open question on whether to capture status only or also the PWD ID.
:   FHIR path: `Patient.extension(pddRegistration)`

---

#### Clinical Information

This group covers the clinical observations, treatments and diagnostic information recorded during Charity’s first ANC contact. Because the group contains many elements it is split into three sub-tables.

##### Chief Complaint & Clinical History

| Element | Data Element | Observation Chief Complaint | Servicerequest Ultrasound |
|---------|-------------|:---:|:---:|
| REF-30 | Chief Complaint | ✅ |   | 
| REF-31 | Clinical History |   | ✅ | 

**REF-30 — Chief Complaint** *(Covered)*
:   Charity’s chief complaint — a missed menstrual cycle and nausea — is captured in an **Observation** coded with LOINC 10154-3 (“Chief complaint – Reported”) and a free-text value string.
:   FHIR path: `Observation.code + valueString`

**REF-31 — Clinical History** *(Covered)*
:   Pertinent clinical history is recorded as a narrative note in **ServiceRequest.note**. For Charity this includes her LMP estimate and the rationale for the ultrasound referral.
:   FHIR path: `ServiceRequest.note`


##### Vital Signs

| Element | Data Element | Observation Blood Pressure | Observation Heart Rate | Observation Oxygen Saturation | Observation Respiratory Rate | Observation Temperature | Observation Weight |
|---------|-------------|:---:|:---:|:---:|:---:|:---:|:---:|
| REF-32 | Vital Signs – Blood Pressure | ✅ |   |   |   |   |   | 
| REF-33 | Vital Signs – Heart Rate |   | ✅ |   |   |   |   | 
| REF-34 | Vital Signs – Respiratory Rate |   |   |   | ✅ |   |   | 
| REF-35 | Vital Signs – Oxygen Saturation |   |   | ✅ |   |   |   | 
| REF-36 | Vital Signs – Temperature |   |   |   |   | ✅ |   | 
| REF-37 | Vital Signs – Weight |   |   |   |   |   | ✅ | 

**REF-32 — Vital Signs – Blood Pressure** *(Covered)*
:   Charity’s blood pressure (110/70 mmHg) is captured using the FHIR blood pressure panel profile (**Observation** with LOINC 85354-9), with separate components for systolic (8480-6) and diastolic (8462-4).
:   FHIR path: `Observation.code + valueQuantity`

**REF-33 — Vital Signs – Heart Rate** *(Covered)*
:   Charity’s heart rate of 78 bpm is recorded as an **Observation** coded with LOINC 8867-4, conforming to the FHIR vital signs profile.
:   FHIR path: `Observation.code + valueQuantity`

**REF-34 — Vital Signs – Respiratory Rate** *(Covered)*
:   Charity’s respiratory rate of 18 breaths per minute is stored in an **Observation** (LOINC 9279-1), part of the standard vital signs set.
:   FHIR path: `Observation.code + valueQuantity`

**REF-35 — Vital Signs – Oxygen Saturation** *(Covered)*
:   Charity’s oxygen saturation of 98 % is captured in an **Observation** (LOINC 59408-5), confirming adequate oxygenation.
:   FHIR path: `Observation.code + valueQuantity`

**REF-36 — Vital Signs – Temperature** *(Covered)*
:   Charity’s body temperature of 36.8 °C is recorded in an **Observation** (LOINC 8310-5), a normal reading from the physical exam.
:   FHIR path: `Observation.code + valueQuantity`

**REF-37 — Vital Signs – Weight** *(Covered)*
:   Charity’s body weight of 55 kg is stored as an **Observation** (LOINC 29463-7), providing a baseline measurement for her pregnancy.
:   FHIR path: `Observation.code + valueQuantity`


##### Treatment, Orders & Working Impression

| Element | Data Element | Condition Pregnancy | Medicationadministration Ifa | Servicerequest Lab Orders |
|---------|-------------|:---:|:---:|:---:|
| REF-38 | Treatment Given |   | ✅ |   | 
| REF-39 | Laboratory Results (attachments) |   |   | ⚠️ | 
| REF-40 | Working Impression (clinical reason) | ✅ |   |   | 

**REF-38 — Treatment Given** *(Covered)*
:   Nurse Jane dispenses iron and folic acid (IFA) tablets to Charity, captured in a **MedicationAdministration** resource coded with SNOMED CT 74935002. The dosage instructions (one tablet daily, oral) follow WHO ANC supplementation guidelines.
:   FHIR path: `MedicationAdministration / Procedure.code`

**REF-39 — Laboratory Results (attachments)** *(Partially covered)*
:   Routine ANC laboratory tests (diabetes screen, hepatitis B, HIV) are ordered via a **ServiceRequest**. Coverage is partial because only the orders exist — a **DiagnosticReport** with results will be added when the receiving lab returns findings.
:   FHIR path: `DiagnosticReport + result + presentedForm`

**REF-40 — Working Impression (clinical reason)** *(Covered)*
:   Charity’s working clinical impression — pregnancy (SNOMED CT 77386006) — is recorded as a **Condition** with provisional verification status. It is referenced from `ServiceRequest.reasonReference` to link the diagnosis to the ultrasound referral.
:   FHIR path: `Condition.code`


---

#### System, Logistics & Workflow

| Element | Data Element | Encounter Anc | Encounter Registration | Task Referral |
|---------|-------------|:---:|:---:|:---:|
| REF-41 | Transport Mode / Ambulance | — | — | — | 
| REF-42 | Response |   |   | ✅ | 
| REF-43 | Referring Encounter | ✅ | ✅ |   | 
| REF-44 | Receiving Encounter | — | — | — | 
| REF-45 | Navigator (Receiving/PHU) | — | — | — | 
| REF-46 | Navigator (Referring) | — | — | — | 

**REF-41 — Transport Mode / Ambulance** *(Not covered in this scenario)*
:   Transport mode or ambulance details would be captured as a **Task extension**. Not applicable here — Charity’s is a routine outpatient referral with self-transport.
:   FHIR path: `Task.extension(transportMode)`

**REF-42 — Response** *(Covered)*
:   The referral response/decision is tracked through **Task.businessStatus** using the `referral-disposition` code system. In our example the task is in `requested` status, awaiting acceptance by Metro Imaging Centre.
:   FHIR path: `Task.businessStatus`

**REF-43 — Referring Encounter** *(Covered)*
:   Two **Encounter** resources provide the clinical context: a registration encounter (08:00–08:15, clerk Abraham) and an ANC contact encounter (08:30–10:00, nurse Jane). Both use the PH-Core Encounter profile.
:   FHIR path: `Encounter.class, period, serviceType`

**REF-44 — Receiving Encounter** *(Not covered in this scenario)*
:   A receiving encounter would be created when Charity arrives at Metro Imaging Centre. It belongs to the receiving facility’s workflow and is not part of this sending scenario.
:   FHIR path: `Encounter.class, period`

**REF-45 — Navigator (Receiving/PHU)** *(Not covered in this scenario)*
:   A navigator role at the receiving facility or PHU would be captured as a **PractitionerRole** with a navigator code. Not applicable in this scenario.
:   FHIR path: `PractitionerRole.code (navigator)`

**REF-46 — Navigator (Referring)** *(Not covered in this scenario)*
:   A navigator role at the referring facility would similarly be a **PractitionerRole**. Not applicable in this scenario.
:   FHIR path: `PractitionerRole.code (navigator)`

---
