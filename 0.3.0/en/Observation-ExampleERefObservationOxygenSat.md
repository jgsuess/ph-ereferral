# Example Oxygen Saturation Observation - PH eReferral Implementation Guide v0.3.0

## Example Observation: Example Oxygen Saturation Observation

Profile: [EReferral Observation](StructureDefinition-ereferral-observation.md)

**status**: Final

**category**: Vital Signs

**code**: Oxygen saturation in Arterial blood

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**effective**: 2025-03-15 09:15:00+0800

**performer**: [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md)

**value**: 96 % (Details: UCUM code% = '%')

**interpretation**: Normal

**note**: 

> 

Room air saturation




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleERefObservationOxygenSat",
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
      "code" : "2708-6",
      "display" : "Oxygen saturation in Arterial blood"
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
    "value" : 96,
    "unit" : "%",
    "system" : "http://unitsofmeasure.org",
    "code" : "%"
  },
  "interpretation" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
      "code" : "N",
      "display" : "Normal"
    }]
  }],
  "note" : [{
    "text" : "Room air saturation"
  }]
}

```
