# Observation — Oxygen Saturation - PH eReferral Implementation Guide v0.1.0

## Example Observation: Observation — Oxygen Saturation

Profiles: `http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation`, [Vital Signs Profile](http://hl7.org/fhir/R4/vitalsigns.html)

Tag: 

**status**: Final

**category**: Vital Signs

**code**: Oxygen saturation in Arterial blood

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**encounter**: [Encounter: status = finished; class = ambulatory (ActCode#AMB); type = Prenatal visit; period = 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800; reasonCode = Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-b2c3d4e5-f6a7-8901-bcde-f12345678901)

**effective**: 2026-02-24 09:00:00+0800

**performer**: [Practitioner Jane Dela Cruz ](Bundle-anc-contact-transaction-ex.md#urn-uuid-4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c)

**value**: 98 % (Details: UCUM code% = '%')



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "observation-oxygen-saturation-ex",
  "meta" : {
    "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation",
    "http://hl7.org/fhir/StructureDefinition/vitalsigns"],
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-35",
      "display" : "REF-35"
    }]
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "vital-signs",
      "display" : "Vital Signs"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "http://loinc.org",
      "code" : "2708-6",
      "display" : "Oxygen saturation in Arterial blood"
    },
    {
      "system" : "http://loinc.org",
      "code" : "59408-5",
      "display" : "Oxygen saturation in Arterial blood by Pulse oximetry"
    }]
  },
  "subject" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "encounter" : {
    "reference" : "urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901"
  },
  "effectiveDateTime" : "2026-02-24T09:00:00+08:00",
  "performer" : [{
    "reference" : "urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c"
  }],
  "valueQuantity" : {
    "value" : 98,
    "unit" : "%",
    "system" : "http://unitsofmeasure.org",
    "code" : "%"
  }
}

```
