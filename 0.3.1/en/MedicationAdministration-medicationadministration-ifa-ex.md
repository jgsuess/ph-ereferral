# MedicationAdministration — Iron and Folic Acid - PH eReferral Implementation Guide v0.3.1

## Example MedicationAdministration: MedicationAdministration — Iron and Folic Acid

Tag: 

**status**: Completed

**medication**: Iron and Folic Acid (IFA) tablets

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**context**: [Encounter: status = finished; class = ambulatory (ActCode#AMB); type = Prenatal visit; period = 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800; reasonCode = Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-b2c3d4e5-f6a7-8901-bcde-f12345678901)

**effective**: 2026-02-24

### Performers

| | |
| :--- | :--- |
| - | **Actor** |
| * | [Practitioner Jane Dela Cruz ](Bundle-anc-contact-transaction-ex.md#urn-uuid-4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c) |

### Dosages

| | | | |
| :--- | :--- | :--- | :--- |
| - | **Text** | **Route** | **Dose** |
| * | 1 tablet daily | Oral route | 1 tablet (Details: UCUM code{tablet} = '{tablet}') |



## Resource Content

```json
{
  "resourceType" : "MedicationAdministration",
  "id" : "medicationadministration-ifa-ex",
  "meta" : {
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-38",
      "display" : "REF-38"
    }]
  },
  "status" : "completed",
  "medicationCodeableConcept" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "776023009",
      "display" : "Folic acid and iron only product"
    }],
    "text" : "Iron and Folic Acid (IFA) tablets"
  },
  "subject" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "context" : {
    "reference" : "urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901"
  },
  "effectiveDateTime" : "2026-02-24",
  "performer" : [{
    "actor" : {
      "reference" : "urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c"
    }
  }],
  "dosage" : {
    "text" : "1 tablet daily",
    "route" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "26643006",
        "display" : "Oral route"
      }]
    },
    "dose" : {
      "value" : 1,
      "unit" : "tablet",
      "system" : "http://unitsofmeasure.org",
      "code" : "{tablet}"
    }
  }
}

```
