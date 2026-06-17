# Example Chief Complaint Observation - PH eReferral Implementation Guide v0.3.0

## Example Observation: Example Chief Complaint Observation

Profile: [EReferral Observation](StructureDefinition-ereferral-observation.md)

**status**: Final

**category**: Survey

**code**: Chief Complaint

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**effective**: 2025-03-15 09:00:00+0800

**performer**: [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md)

**value**: Chest pain for 2 hours, radiating to left arm

**note**: 

> 

Patient reports sudden onset of crushing chest pain while at rest




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleERefObservationChiefComplaint",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-observation"]
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "survey",
      "display" : "Survey"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "http://loinc.org",
      "code" : "10154-3",
      "display" : "Chief complaint Narrative - Reported"
    }],
    "text" : "Chief Complaint"
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "effectiveDateTime" : "2025-03-15T09:00:00+08:00",
  "performer" : [{
    "reference" : "Practitioner/ExampleERefPractitioner"
  }],
  "valueString" : "Chest pain for 2 hours, radiating to left arm",
  "note" : [{
    "text" : "Patient reports sudden onset of crushing chest pain while at rest"
  }]
}

```
