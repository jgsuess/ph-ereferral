# Example ServiceRequest (for Task) - PH eReferral Implementation Guide v0.3.1

## Example ServiceRequest: Example ServiceRequest (for Task)

Profile: [EReferral ServiceRequest](StructureDefinition-ereferral-service-request.md)

**status**: Active

**intent**: Order

**code**: Referral to cardiology service

**subject**: [Juan Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatientTask.md)

**authoredOn**: 2025-03-15 09:30:00+0800

**requester**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRoleRequester.md)

**performer**: [Organization Manila General Hospital](Organization-ExampleERefOrganizationReceiving.md)

**reasonCode**: Chest pain on exertion, suspected unstable angina



## Resource Content

```json
{
  "resourceType" : "ServiceRequest",
  "id" : "ExampleERefServiceRequestTask",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request"]
  },
  "status" : "active",
  "intent" : "order",
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "183519002",
      "display" : "Referral to cardiology service"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatientTask"
  },
  "authoredOn" : "2025-03-15T09:30:00+08:00",
  "requester" : {
    "reference" : "PractitionerRole/ExampleERefPractitionerRoleRequester"
  },
  "performer" : [{
    "reference" : "Organization/ExampleERefOrganizationReceiving"
  }],
  "reasonCode" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "29857009",
      "display" : "Chest pain"
    }],
    "text" : "Chest pain on exertion, suspected unstable angina"
  }]
}

```
