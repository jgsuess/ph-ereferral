# Example Heart Rate Observation - PH eReferral Implementation Guide v0.3.0

## Example Observation: Example Heart Rate Observation

Profile: [EReferral Observation](StructureDefinition-ereferral-observation.md)

**status**: Final

**category**: Vital Signs

**code**: Heart rate

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**effective**: 2025-03-15 09:15:00+0800

**performer**: [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md)

**value**: 88 beats/minute (Details: UCUM code/min = '/min')

**interpretation**: Normal



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleERefObservationHeartRate",
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
      "code" : "8867-4",
      "display" : "Heart rate"
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
    "value" : 88,
    "unit" : "beats/minute",
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
