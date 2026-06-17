# Example ECG Observation - PH eReferral Implementation Guide v0.3.0

## Example Observation: Example ECG Observation

Profile: [EReferral Observation](StructureDefinition-ereferral-observation.md)

**status**: Final

**category**: Procedure

**code**: EKG study

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**effective**: 2025-03-15 09:20:00+0800

**performer**: [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md)

**value**: ST depression in leads V4-V6, T wave inversion in lead III

**interpretation**: Abnormal

**note**: 

> 

Suggestive of ischemic changes, cardiology referral recommended




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleERefObservationECG",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-observation"]
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "procedure",
      "display" : "Procedure"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "http://loinc.org",
      "code" : "11524-6",
      "display" : "EKG study"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "effectiveDateTime" : "2025-03-15T09:20:00+08:00",
  "performer" : [{
    "reference" : "Practitioner/ExampleERefPractitioner"
  }],
  "valueString" : "ST depression in leads V4-V6, T wave inversion in lead III",
  "interpretation" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
      "code" : "A",
      "display" : "Abnormal"
    }]
  }],
  "note" : [{
    "text" : "Suggestive of ischemic changes, cardiology referral recommended"
  }]
}

```
