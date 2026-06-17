# Example Blood Pressure Observation - PH eReferral Implementation Guide v0.3.0

## Example Observation: Example Blood Pressure Observation

Profile: [EReferral Observation](StructureDefinition-ereferral-observation.md)

**status**: Final

**category**: Vital Signs

**code**: Blood pressure panel with all children optional

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**effective**: 2025-03-15 09:15:00+0800

**performer**: [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md)

**interpretation**: High

**note**: 

> 

Patient hypertensive on initial assessment


> **component****code**: Systolic blood pressure**value**: 160 mmHg (Details: UCUM codemm[Hg] = 'mm[Hg]')

> **component****code**: Diastolic blood pressure**value**: 95 mmHg (Details: UCUM codemm[Hg] = 'mm[Hg]')



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleERefObservationBP",
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
      "code" : "85354-9",
      "display" : "Blood pressure panel with all children optional"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "effectiveDateTime" : "2025-03-15T09:15:00+08:00",
  "performer" : [{
    "reference" : "Practitioner/ExampleERefPractitioner"
  }],
  "interpretation" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
      "code" : "H",
      "display" : "High"
    }]
  }],
  "note" : [{
    "text" : "Patient hypertensive on initial assessment"
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
      "value" : 160,
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
      "value" : 95,
      "unit" : "mmHg",
      "system" : "http://unitsofmeasure.org",
      "code" : "mm[Hg]"
    }
  }]
}

```
