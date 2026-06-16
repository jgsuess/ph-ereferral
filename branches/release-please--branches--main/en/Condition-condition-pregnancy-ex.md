# Condition — Pregnancy - PH eReferral Implementation Guide v0.1.0

## Example Condition: Condition — Pregnancy

Tag: 

**clinicalStatus**: Active

**verificationStatus**: Provisional

**code**: Pregnant

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**encounter**: [Encounter: status = finished; class = ambulatory (ActCode#AMB); type = Prenatal visit; period = 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800; reasonCode = Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-b2c3d4e5-f6a7-8901-bcde-f12345678901)

**onset**: 2026-01-01

**note**: 

> 

LMP approximately around the New Year holiday; gestational age estimated 12–15 weeks.




## Resource Content

```json
{
  "resourceType" : "Condition",
  "id" : "condition-pregnancy-ex",
  "meta" : {
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-40",
      "display" : "REF-40"
    }]
  },
  "clinicalStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-clinical",
      "code" : "active",
      "display" : "Active"
    }]
  },
  "verificationStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-ver-status",
      "code" : "provisional",
      "display" : "Provisional"
    }]
  },
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "77386006",
      "display" : "Pregnant"
    }]
  },
  "subject" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "encounter" : {
    "reference" : "urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901"
  },
  "onsetDateTime" : "2026-01-01",
  "note" : [{
    "text" : "LMP approximately around the New Year holiday; gestational age estimated 12–15 weeks."
  }]
}

```
