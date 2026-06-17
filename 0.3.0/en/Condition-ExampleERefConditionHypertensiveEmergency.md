# Example Condition - Hypertensive Emergency - PH eReferral Implementation Guide v0.3.0

## Example Condition: Example Condition - Hypertensive Emergency

Profile: [EReferral Condition](StructureDefinition-ereferral-condition.md)

**clinicalStatus**: Active

**verificationStatus**: Confirmed

**category**: Encounter Diagnosis

**severity**: Severe

**code**: Hypertensive emergency with suspected acute end-organ damage

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**onset**: 2025-03-15 07:45:00+0800

**recordedDate**: 2025-03-15 08:05:00+0800

**note**: 

> 

Blood pressure remained above 180/120 mmHg with severe headache and visual symptoms. Referred for emergency evaluation and management.




## Resource Content

```json
{
  "resourceType" : "Condition",
  "id" : "ExampleERefConditionHypertensiveEmergency",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-condition"]
  },
  "clinicalStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-clinical",
      "code" : "active"
    }]
  },
  "verificationStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-ver-status",
      "code" : "confirmed",
      "display" : "Confirmed"
    }]
  },
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-category",
      "code" : "encounter-diagnosis",
      "display" : "Encounter Diagnosis"
    }]
  }],
  "severity" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "24484000",
      "display" : "Severe"
    }]
  },
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "132721000119104",
      "display" : "Hypertensive emergency"
    }],
    "text" : "Hypertensive emergency with suspected acute end-organ damage"
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "onsetDateTime" : "2025-03-15T07:45:00+08:00",
  "recordedDate" : "2025-03-15T08:05:00+08:00",
  "note" : [{
    "text" : "Blood pressure remained above 180/120 mmHg with severe headache and visual symptoms. Referred for emergency evaluation and management."
  }]
}

```
