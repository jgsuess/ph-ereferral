# Encounter — Registration - PH eReferral Implementation Guide v0.1.0

## Example Encounter: Encounter — Registration

Profile: `http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter`

Tag: 

**status**: Finished

**class**: [ActCode: AMB](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ActCode.html#v3-ActCode-AMB) (ambulatory)

**type**: Registration

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

### Participants

| | |
| :--- | :--- |
| - | **Individual** |
| * | [PractitionerRole Administrative/managerial worker](Bundle-registration-transaction-ex.md#urn-uuid-3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a) |

**period**: 2026-02-24 08:00:00+0800 --> 2026-02-24 08:15:00+0800

**serviceProvider**: [Organization Barangay Malusog Health Centre](Bundle-registration-transaction-ex.md#urn-uuid-7c9e6679-7425-40de-944b-e07fc1f90ae7)



## Resource Content

```json
{
  "resourceType" : "Encounter",
  "id" : "encounter-registration-ex",
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
      "code" : "185349003",
      "display" : "Encounter for check up"
    }],
    "text" : "Registration"
  }],
  "subject" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "participant" : [{
    "individual" : {
      "reference" : "urn:uuid:3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a"
    }
  }],
  "period" : {
    "start" : "2026-02-24T08:00:00+08:00",
    "end" : "2026-02-24T08:15:00+08:00"
  },
  "serviceProvider" : {
    "reference" : "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7"
  }
}

```
