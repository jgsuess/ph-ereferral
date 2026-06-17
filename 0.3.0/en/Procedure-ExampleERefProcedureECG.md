# Example Procedure - Electrocardiogram - PH eReferral Implementation Guide v0.3.0

## Example Procedure: Example Procedure - Electrocardiogram

Profile: [EReferral Procedure](StructureDefinition-ereferral-procedure.md)

**status**: Completed

**category**: Diagnostic procedure

**code**: Electrocardiographic procedure

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**performed**: 2025-03-15 09:15:00+0800

### Performers

| | | |
| :--- | :--- | :--- |
| - | **Function** | **Actor** |
| * | Medical practitioner | [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRole.md) |

**reasonCode**: Chest pain

**reasonReference**: [Condition Chest pain](Condition-ExampleERefConditionChestPain.md)

**note**: 

> 

ECG was performed prior to referral to support clinical assessment of chest pain.




## Resource Content

```json
{
  "resourceType" : "Procedure",
  "id" : "ExampleERefProcedureECG",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-procedure"]
  },
  "status" : "completed",
  "category" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "103693007",
      "display" : "Diagnostic procedure"
    }]
  },
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "29303009",
      "display" : "Electrocardiographic procedure"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "performedDateTime" : "2025-03-15T09:15:00+08:00",
  "performer" : [{
    "function" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "158965000",
        "display" : "Medical practitioner"
      }]
    },
    "actor" : {
      "reference" : "PractitionerRole/ExampleERefPractitionerRole"
    }
  }],
  "reasonCode" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "29857009",
      "display" : "Chest pain"
    }]
  }],
  "reasonReference" : [{
    "reference" : "Condition/ExampleERefConditionChestPain"
  }],
  "note" : [{
    "text" : "ECG was performed prior to referral to support clinical assessment of chest pain."
  }]
}

```
