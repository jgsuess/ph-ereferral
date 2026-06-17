# Example Condition - Chest Pain - PH eReferral Implementation Guide v0.3.0

## Example Condition: Example Condition - Chest Pain

Profile: [EReferral Condition](StructureDefinition-ereferral-condition.md)

**clinicalStatus**: Active

**verificationStatus**: Provisional

**category**: Encounter Diagnosis

**severity**: Severe

**code**: Chest pain on exertion

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**onset**: 2025-03-12 08:00:00+0800

**recordedDate**: 2025-03-15 09:10:00+0800

**note**: 

> 

Patient reports exertional chest pain for 3 days with abnormal ECG findings.




## Resource Content

```json
{
  "resourceType" : "Condition",
  "id" : "ExampleERefConditionChestPain",
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
      "code" : "provisional",
      "display" : "Provisional"
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
      "code" : "29857009",
      "display" : "Chest pain"
    }],
    "text" : "Chest pain on exertion"
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "onsetDateTime" : "2025-03-12T08:00:00+08:00",
  "recordedDate" : "2025-03-15T09:10:00+08:00",
  "note" : [{
    "text" : "Patient reports exertional chest pain for 3 days with abnormal ECG findings."
  }]
}

```
