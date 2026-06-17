# Example Onward eReferral ServiceRequest - PH eReferral Implementation Guide v0.3.0

## Example ServiceRequest: Example Onward eReferral ServiceRequest

Profile: [EReferral ServiceRequest](StructureDefinition-ereferral-service-request.md)

**replaces**: [ServiceRequest Referral to cardiology service](ServiceRequest-ExampleERefServiceRequestTask.md)

**status**: Active

**intent**: Order

**code**: Referral to cardiology service

**subject**: [Juan Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatientTask.md)

**authoredOn**: 2025-03-15 10:15:00+0800

**requester**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRoleRequester.md)

**performer**: [Organization Eastern District Medical Center](Organization-ExampleERefOrganizationOnwardReceiving.md)

**reasonCode**: Chest pain on exertion, suspected unstable angina

**note**: 

> 

Onward referral after Manila General Hospital reported capacity full and recommended Eastern District Medical Center.




## Resource Content

```json
{
  "resourceType" : "ServiceRequest",
  "id" : "ExampleERefServiceRequestOnward",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request"]
  },
  "replaces" : [{
    "reference" : "ServiceRequest/ExampleERefServiceRequestTask"
  }],
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
  "authoredOn" : "2025-03-15T10:15:00+08:00",
  "requester" : {
    "reference" : "PractitionerRole/ExampleERefPractitionerRoleRequester"
  },
  "performer" : [{
    "reference" : "Organization/ExampleERefOrganizationOnwardReceiving"
  }],
  "reasonCode" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "29857009",
      "display" : "Chest pain"
    }],
    "text" : "Chest pain on exertion, suspected unstable angina"
  }],
  "note" : [{
    "text" : "Onward referral after Manila General Hospital reported capacity full and recommended Eastern District Medical Center."
  }]
}

```
