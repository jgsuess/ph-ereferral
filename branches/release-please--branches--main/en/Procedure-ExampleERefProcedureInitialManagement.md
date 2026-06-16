# Example Procedure - Initial Management - PH eReferral Implementation Guide v0.1.0

## Example Procedure: Example Procedure - Initial Management

Profile: [EReferral Procedure](StructureDefinition-ereferral-procedure.md)

**status**: Completed

**category**: Therapeutic procedure

**code**: Initial stabilization and symptom management

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**performed**: 2025-03-15 08:45:00+0800 --> 2025-03-15 09:10:00+0800

### Performers

| | | |
| :--- | :--- | :--- |
| - | **Function** | **Actor** |
| * | Medical practitioner | [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRole.md) |

**reasonCode**: Chest pain

**reasonReference**: [Condition Chest pain](Condition-ExampleERefConditionChestPain.md)

**note**: 

> 

Initial management was provided before referral, including monitoring, symptom control, and preparation for transfer.




## Resource Content

```json
{
  "resourceType" : "Procedure",
  "id" : "ExampleERefProcedureInitialManagement",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-procedure"]
  },
  "status" : "completed",
  "category" : {
    "text" : "Therapeutic procedure"
  },
  "code" : {
    "text" : "Initial stabilization and symptom management"
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "performedPeriod" : {
    "start" : "2025-03-15T08:45:00+08:00",
    "end" : "2025-03-15T09:10:00+08:00"
  },
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
    "text" : "Initial management was provided before referral, including monitoring, symptom control, and preparation for transfer."
  }]
}

```
