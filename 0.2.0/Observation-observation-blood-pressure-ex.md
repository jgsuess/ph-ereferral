# Observation — Blood Pressure - PH eReferral Implementation Guide v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Observation — Blood Pressure**

## Example Observation: Observation — Blood Pressure

Profiles: [PH Core Observation](https://build.fhir.org/ig/UP-Manila-SILab/ph-core/StructureDefinition-ph-core-observation.html), [Vital Signs Profile](http://hl7.org/fhir/R4/vitalsigns.html), [Observation Blood Pressure Profile](http://hl7.org/fhir/R4/bp.html)

Tag: REF-32 (Details: peref-dd code REF-32)

**status**: Final

**category**: Vital Signs

**code**: Blood pressure systolic & diastolic

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**encounter**: [Encounter: status = finished; class = ambulatory (ActCode#AMB); type = Prenatal initial visit; period = 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800; reasonCode = Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-b2c3d4e5-f6a7-8901-bcde-f12345678901)

**effective**: 2026-02-24 09:00:00+0800

**performer**: [Practitioner Jane Dela Cruz ](Bundle-anc-contact-transaction-ex.md#urn-uuid-4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c)

> **component****code**: Systolic blood pressure**value**: 110 mmHg (Details: UCUM codemm[Hg] = 'mm[Hg]')

> **component****code**: Diastolic blood pressure**value**: 70 mmHg (Details: UCUM codemm[Hg] = 'mm[Hg]')



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "observation-blood-pressure-ex",
  "meta" : {
    "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation",
    "http://hl7.org/fhir/StructureDefinition/vitalsigns",
    "http://hl7.org/fhir/StructureDefinition/bp"],
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-32",
      "display" : "REF-32"
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
      "code" : "85354-9",
      "display" : "Blood pressure panel with all children optional"
    }],
    "text" : "Blood pressure systolic & diastolic"
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
  "component" : [{
    "code" : {
      "coding" : [{
        "system" : "http://loinc.org",
        "code" : "8480-6",
        "display" : "Systolic blood pressure"
      }]
    },
    "valueQuantity" : {
      "value" : 110,
      "unit" : "mmHg",
      "system" : "http://unitsofmeasure.org",
      "code" : "mm[Hg]"
    }
  },
  {
    "code" : {
      "coding" : [{
        "system" : "http://loinc.org",
        "code" : "8462-4",
        "display" : "Diastolic blood pressure"
      }]
    },
    "valueQuantity" : {
      "value" : 70,
      "unit" : "mmHg",
      "system" : "http://unitsofmeasure.org",
      "code" : "mm[Hg]"
    }
  }]
}

```
