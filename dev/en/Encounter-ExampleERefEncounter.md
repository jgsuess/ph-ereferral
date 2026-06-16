# Example eReferral Encounter - PH eReferral Implementation Guide v0.1.0

## Example Encounter: Example eReferral Encounter

Profile: [ERefEncounter](StructureDefinition-ereferral-encounter.md)

**identifier**: `https://pgh.gov.ph/fhir/encounter-id`/ENC-2025-001234

**status**: Finished

> **statusHistory****status**: Planned**period**: 2025-03-15 09:30:00+0800 --> 2025-03-16 07:59:00+0800

> **statusHistory****status**: Arrived**period**: 2025-03-16 08:00:00+0800 --> 2025-03-16 08:15:00+0800

> **statusHistory****status**: In Progress**period**: 2025-03-16 08:15:00+0800 --> 2025-03-16 10:30:00+0800

> **statusHistory****status**: Finished**period**: 2025-03-16 10:30:00+0800 --> 2025-03-16 10:30:00+0800

**class**: [ActCode: AMB](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ActCode.html#v3-ActCode-AMB) (ambulatory)

### ClassHistories

| | | |
| :--- | :--- | :--- |
| - | **Class** | **Period** |
| * | [ActCode: AMB](http://terminology.hl7.org/7.2.0/CodeSystem-v3-ActCode.html#v3-ActCode-AMB)(ambulatory) | 2025-03-16 08:00:00+0800 --> 2025-03-16 10:30:00+0800 |

**type**: Consultation

**priority**: Emergency

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**basedOn**: [ServiceRequest Referral to cardiology service](ServiceRequest-ExampleERefServiceRequest.md)

> **participant****type**: consultant**period**: 2025-03-16 08:15:00+0800 --> 2025-03-16 10:30:00+0800**individual**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRole.md)

> **participant****type**: attender**period**: 2025-03-16 08:00:00+0800 --> 2025-03-16 10:30:00+0800**individual**: Mrs. Dela Cruz

**period**: 2025-03-16 08:00:00+0800 --> 2025-03-16 10:30:00+0800

**reasonCode**: Chest pain on exertion, suspected unstable angina

**reasonReference**: [Condition Chest pain](Condition-ExampleERefConditionChestPain.md)

### Diagnoses

| | | |
| :--- | :--- | :--- |
| - | **Condition** | **Use** |
| * | [Condition Chest pain](Condition-ExampleERefConditionChestPain.md) | Final diagnosis (discharge) |

### Locations

| | | | |
| :--- | :--- | :--- | :--- |
| - | **Location** | **Status** | **Period** |
| * | Cardiology Outpatient Clinic | Completed | 2025-03-16 08:00:00+0800 --> 2025-03-16 10:30:00+0800 |



## Resource Content

```json
{
  "resourceType" : "Encounter",
  "id" : "ExampleERefEncounter",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-encounter"]
  },
  "identifier" : [{
    "system" : "https://pgh.gov.ph/fhir/encounter-id",
    "value" : "ENC-2025-001234"
  }],
  "status" : "finished",
  "statusHistory" : [{
    "status" : "planned",
    "period" : {
      "start" : "2025-03-15T09:30:00+08:00",
      "end" : "2025-03-16T07:59:00+08:00"
    }
  },
  {
    "status" : "arrived",
    "period" : {
      "start" : "2025-03-16T08:00:00+08:00",
      "end" : "2025-03-16T08:15:00+08:00"
    }
  },
  {
    "status" : "in-progress",
    "period" : {
      "start" : "2025-03-16T08:15:00+08:00",
      "end" : "2025-03-16T10:30:00+08:00"
    }
  },
  {
    "status" : "finished",
    "period" : {
      "start" : "2025-03-16T10:30:00+08:00",
      "end" : "2025-03-16T10:30:00+08:00"
    }
  }],
  "class" : {
    "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    "code" : "AMB",
    "display" : "ambulatory"
  },
  "classHistory" : [{
    "class" : {
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
      "code" : "AMB",
      "display" : "ambulatory"
    },
    "period" : {
      "start" : "2025-03-16T08:00:00+08:00",
      "end" : "2025-03-16T10:30:00+08:00"
    }
  }],
  "type" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "11429006",
      "display" : "Consultation"
    }]
  }],
  "priority" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "25876001",
      "display" : "Emergency"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "basedOn" : [{
    "reference" : "ServiceRequest/ExampleERefServiceRequest"
  }],
  "participant" : [{
    "type" : [{
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        "code" : "CON",
        "display" : "consultant"
      }]
    }],
    "period" : {
      "start" : "2025-03-16T08:15:00+08:00",
      "end" : "2025-03-16T10:30:00+08:00"
    },
    "individual" : {
      "reference" : "PractitionerRole/ExampleERefPractitionerRole"
    }
  },
  {
    "type" : [{
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        "code" : "ATND",
        "display" : "attender"
      }]
    }],
    "period" : {
      "start" : "2025-03-16T08:00:00+08:00",
      "end" : "2025-03-16T10:30:00+08:00"
    },
    "individual" : {
      "display" : "Mrs. Dela Cruz"
    }
  }],
  "period" : {
    "start" : "2025-03-16T08:00:00+08:00",
    "end" : "2025-03-16T10:30:00+08:00"
  },
  "reasonCode" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "29857009",
      "display" : "Chest pain"
    }],
    "text" : "Chest pain on exertion, suspected unstable angina"
  }],
  "reasonReference" : [{
    "reference" : "Condition/ExampleERefConditionChestPain"
  }],
  "diagnosis" : [{
    "condition" : {
      "reference" : "Condition/ExampleERefConditionChestPain"
    },
    "use" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "89100005",
        "display" : "Final diagnosis (discharge)"
      }]
    }
  }],
  "location" : [{
    "location" : {
      "display" : "Cardiology Outpatient Clinic"
    },
    "status" : "completed",
    "period" : {
      "start" : "2025-03-16T08:00:00+08:00",
      "end" : "2025-03-16T10:30:00+08:00"
    }
  }]
}

```
