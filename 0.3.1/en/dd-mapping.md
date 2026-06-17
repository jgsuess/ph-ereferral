# Dd Mapping - PH eReferral Implementation Guide v0.3.1

## Dd Mapping

### Data Dictionary to FHIR Mapping

This page provides a detailed, element-by-element mapping between the **PeRef Logical Information Model** (the data dictionary) and the FHIR example resources published in this Implementation Guide.

The content is organised by **clinical information group**. For each group you will find:

1. A**pivot table**showing which example resource covers which data-dictionary element.
1. A**narrative description**explaining how and why each element is represented in FHIR, told through the lens of the ANC scenario (Charity, Abraham, Jane).

**Legend**

| | |
| :--- | :--- |
| ✅ | Fully covered by the example |
| ⚠️ | Partially covered — additional resources needed |
| 🕐 | Deferred to a future release |
| — | Not applicable to this scenario |

> **Note:** This page is generated from `dd-coverage.csv` by the script `utils/generate-dd-mapping-page.py`. Re-run the script after updating the data dictionary to keep this page in sync.

-------

#### Coverage Summary

Out of **46** data-dictionary elements:

| | | |
| :--- | :--- | :--- |
| ✅ Covered | 31 | Fully represented in at least one example |
| ⚠️ Partial | 1 | Modelled as orders; results resource still needed |
| 🕐 Deferred | 4 | Postponed to a future release per CDG consensus |
| — Not covered | 10 | Not applicable to this ANC scenario |

-------

#### Sending Practitioner

| | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REF-1 | Name of Referring Practitioner | ✅ | ✅ | ✅ | ✅ |
| REF-2 | Professional Signature | 🕐 | 🕐 | 🕐 | 🕐 |
| REF-3 | Date & Time of Signature | 🕐 | 🕐 | 🕐 | 🕐 |

-------

#### Sending Facility

| | | |
| :--- | :--- | :--- |
| REF-4 | Initiating Facility Name | ✅ |
| REF-5 | Initiating Facility NHFR Code | ✅ |
| REF-6 | Initiating Facility Address | ✅ |
| REF-7 | Initiating Facility Contact Number | ✅ |

-------

#### Receiving Practitioner

| | | | |
| :--- | :--- | :--- | :--- |
| REF-8 | Receiving Personnel | Communication | — |

-------

#### Receiving Facility

| | | |
| :--- | :--- | :--- |
| REF-9 | Receiving Facility Name | ✅ |
| REF-10 | Receiving Facility NHFR Code | ✅ |

-------

#### Referral Request

| | | | |
| :--- | :--- | :--- | :--- |
| REF-11 | Health Care Provider Network (HCPN) Name | 🕐 | 🕐 |
| REF-12 | Date of Referral | ✅ |   |
| REF-13 | Referral Category | ✅ |   |
| REF-14 | Time Called | — | — |
| REF-15 | Reason for Referral (service type) | ✅ |   |
| REF-16 | Action Point: Received |   | ✅ |
| REF-17 | Action Point: Referred (Forwarded) | — | — |
| REF-18 | Return Referral Slip (Attachment) | 🕐 | 🕐 |
| REF-19 | Call/Email Reference | — | — |

-------

#### Patient Demographics

| | | | |
| :--- | :--- | :--- | :--- |
| REF-20 | Patient Full Name | ✅ |   |
| REF-21 | Sex (Administrative Gender) | ✅ |   |
| REF-22 | Birth Date | ✅ |   |
| REF-23 | Age (computed) | — | — |
| REF-24 | Identity Number (PhilSys) | ✅ |   |
| REF-25 | PhilHealth ID | ✅ |   |
| REF-26 | Patient Address | ✅ |   |
| REF-27 | Contact Number | ✅ |   |
| REF-28 | Accompanied By / Next of Kin |   | ✅ |
| REF-29 | Patient Disability Registration | — | — |

-------

#### Clinical Information

This group covers the clinical observations, treatments and diagnostic information recorded during Charity’s first ANC contact. Because the group contains many elements it is split into three sub-tables.

##### Chief Complaint & Clinical History

| | | | |
| :--- | :--- | :--- | :--- |
| REF-30 | Chief Complaint | ✅ |   |
| REF-31 | Clinical History |   | ✅ |

##### Vital Signs

| | | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| REF-32 | Vital Signs – Blood Pressure | ✅ |   |   |   |   |   |
| REF-33 | Vital Signs – Heart Rate |   | ✅ |   |   |   |   |
| REF-34 | Vital Signs – Respiratory Rate |   |   |   | ✅ |   |   |
| REF-35 | Vital Signs – Oxygen Saturation |   |   | ✅ |   |   |   |
| REF-36 | Vital Signs – Temperature |   |   |   |   | ✅ |   |
| REF-37 | Vital Signs – Weight |   |   |   |   |   | ✅ |

##### Treatment, Orders & Working Impression

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| REF-38 | Treatment Given |   | ✅ |   |
| REF-39 | Laboratory Results (attachments) |   |   | ⚠️ |
| REF-40 | Working Impression (clinical reason) | ✅ |   |   |

-------

#### System, Logistics & Workflow

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| REF-41 | Transport Mode / Ambulance | — | — | — |
| REF-42 | Response |   |   | ✅ |
| REF-43 | Referring Encounter | ✅ | ✅ |   |
| REF-44 | Receiving Encounter | — | — | — |
| REF-45 | Navigator (Receiving/PHU) | — | — | — |
| REF-46 | Navigator (Referring) | — | — | — |

-------

