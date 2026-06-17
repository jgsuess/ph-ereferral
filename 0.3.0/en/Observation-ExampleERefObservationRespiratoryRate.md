# Example Respiratory Rate Observation - PH eReferral Implementation Guide v0.3.0

## Example Observation: Example Respiratory Rate Observation

Profile: [EReferral Observation](StructureDefinition-ereferral-observation.md)

**status**: Final

**category**: Vital Signs

**code**: Respiratory rate

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**effective**: 2025-03-15 09:15:00+0800

**performer**: [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md)

**value**: 20 breaths/minute (Details: UCUM code/min = '/min')

**interpretation**: Normal



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleERefObservationRespiratoryRate",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-observation"]
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
      "code" : "9279-1",
      "display" : "Respiratory rate"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "effectiveDateTime" : "2025-03-15T09:15:00+08:00",
  "performer" : [{
    "reference" : "Practitioner/ExampleERefPractitioner"
  }],
  "valueQuantity" : {
    "value" : 20,
    "unit" : "breaths/minute",
    "system" : "http://unitsofmeasure.org",
    "code" : "/min"
  },
  "interpretation" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
      "code" : "N",
      "display" : "Normal"
    }]
  }]
}

```
