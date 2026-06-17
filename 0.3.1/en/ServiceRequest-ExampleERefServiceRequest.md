# Example eReferral Service Request - PH eReferral Implementation Guide v0.3.1

## Example ServiceRequest: Example eReferral Service Request

Profile: [EReferral ServiceRequest](StructureDefinition-ereferral-service-request.md)

**requisition**: `urn:oid:1.2.840.113619.21.1.2`/REF-2025-001234

**status**: Active

**intent**: Order

**category**: Patient referral

**priority**: Urgent

**code**: Referral to cardiology service

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**occurrence**: 2025-03-16 08:00:00+0800

**authoredOn**: 2025-03-15 09:30:00+0800

**requester**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRole.md)

**performer**: [Organization Philippine Heart Center](Organization-ExampleERefReceivingHospital.md)

**reasonCode**: Chest pain on exertion, suspected unstable angina

**reasonReference**: [Condition Chest pain](Condition-ExampleERefConditionChestPain.md)

**supportingInfo**: 

* [Observation Blood pressure panel with all children optional](Observation-ExampleERefObservationBP.md)
* [Observation EKG study](Observation-ExampleERefObservationECG.md)

**note**: 

> 

Patient reports chest pain on exertion for 3 days. ECG shows ST depression. Please evaluate for possible PCI. Patient has no known drug allergies.




## Resource Content

```json
{
  "resourceType" : "ServiceRequest",
  "id" : "ExampleERefServiceRequest",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request"]
  },
  "requisition" : {
    "system" : "urn:oid:1.2.840.113619.21.1.2",
    "value" : "REF-2025-001234"
  },
  "status" : "active",
  "intent" : "order",
  "category" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "3457005",
      "display" : "Patient referral"
    }]
  }],
  "priority" : "urgent",
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "183519002",
      "display" : "Referral to cardiology service"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "occurrenceDateTime" : "2025-03-16T08:00:00+08:00",
  "authoredOn" : "2025-03-15T09:30:00+08:00",
  "requester" : {
    "reference" : "PractitionerRole/ExampleERefPractitionerRole"
  },
  "performer" : [{
    "reference" : "Organization/ExampleERefReceivingHospital"
  }],
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
  "supportingInfo" : [{
    "reference" : "Observation/ExampleERefObservationBP"
  },
  {
    "reference" : "Observation/ExampleERefObservationECG"
  }],
  "note" : [{
    "text" : "Patient reports chest pain on exertion for 3 days. ECG shows ST depression. Please evaluate for possible PCI. Patient has no known drug allergies."
  }]
}

```
