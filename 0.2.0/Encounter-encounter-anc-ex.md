# Encounter — First Antenatal Care Contact - PH eReferral Implementation Guide v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Encounter — First Antenatal Care Contact**

## Example Encounter: Encounter — First Antenatal Care Contact

Profile: `http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter`

Tag: 

**status**: Finished

**class**: [ActCode: AMB](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ActCode.html#v3-ActCode-AMB) (ambulatory)

**type**: First antenatal care contact

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

### Participants

| | |
| :--- | :--- |
| - | **Individual** |
| * | [PractitionerRole Nurse](Bundle-anc-contact-transaction-ex.md#urn-uuid-5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d) |

**period**: 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800

**reasonCode**: Pregnant

**serviceProvider**: [Organization Barangay Malusog Health Centre](Bundle-registration-transaction-ex.md#urn-uuid-7c9e6679-7425-40de-944b-e07fc1f90ae7)



## Resource Content

```json
{
  "resourceType" : "Encounter",
  "id" : "encounter-anc-ex",
  "meta" : {
    "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter"],
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-43",
      "display" : "REF-43"
    }]
  },
  "status" : "finished",
  "class" : {
    "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    "code" : "AMB",
    "display" : "ambulatory"
  },
  "type" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "424619006",
      "display" : "Prenatal initial visit"
    }],
    "text" : "First antenatal care contact"
  }],
  "subject" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "participant" : [{
    "individual" : {
      "reference" : "urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d"
    }
  }],
  "period" : {
    "start" : "2026-02-24T08:30:00+08:00",
    "end" : "2026-02-24T10:00:00+08:00"
  },
  "reasonCode" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "77386006",
      "display" : "Pregnant"
    }]
  }],
  "serviceProvider" : {
    "reference" : "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7"
  }
}

```
