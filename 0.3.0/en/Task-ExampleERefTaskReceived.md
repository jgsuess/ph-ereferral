# Example eReferral Task - Received State - PH eReferral Implementation Guide v0.3.0

## Example Task: Example eReferral Task - Received State

Profile: [EReferral Task](StructureDefinition-ereferral-task.md)

**status**: Received

**businessStatus**: Received

**intent**: order

**code**: eReferral for cardiology consultation

**focus**: [ServiceRequest Referral to cardiology service](ServiceRequest-ExampleERefServiceRequestTask.md)

**for**: [Juan Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatientTask.md)

**authoredOn**: 2025-03-15 09:30:00+0800

**lastModified**: 2025-03-15 09:45:00+0800

**requester**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRoleRequester.md)

**owner**: [Organization Manila General Hospital](Organization-ExampleERefOrganizationReceiving.md)

**note**: , 

> 

New referral for patient with chest pain. Awaiting receiving-facility response.


> 

Referral received by Manila General Hospital and queued for clinical review.




## Resource Content

```json
{
  "resourceType" : "Task",
  "id" : "ExampleERefTaskReceived",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-task"]
  },
  "status" : "received",
  "businessStatus" : {
    "coding" : [{
      "system" : "https://fhir.doh.gov.ph/pheref/CodeSystem/ereferral-workflow",
      "code" : "received",
      "display" : "Received"
    }]
  },
  "intent" : "order",
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "3457005",
      "display" : "Patient referral"
    }],
    "text" : "eReferral for cardiology consultation"
  },
  "focus" : {
    "reference" : "ServiceRequest/ExampleERefServiceRequestTask"
  },
  "for" : {
    "reference" : "Patient/ExampleERefPatientTask"
  },
  "authoredOn" : "2025-03-15T09:30:00+08:00",
  "lastModified" : "2025-03-15T09:45:00+08:00",
  "requester" : {
    "reference" : "PractitionerRole/ExampleERefPractitionerRoleRequester"
  },
  "owner" : {
    "reference" : "Organization/ExampleERefOrganizationReceiving"
  },
  "note" : [{
    "text" : "New referral for patient with chest pain. Awaiting receiving-facility response."
  },
  {
    "text" : "Referral received by Manila General Hospital and queued for clinical review."
  }]
}

```
