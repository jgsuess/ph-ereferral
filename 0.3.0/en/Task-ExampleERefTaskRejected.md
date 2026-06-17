# Example eReferral Task - Rejected State - PH eReferral Implementation Guide v0.3.0

## Example Task: Example eReferral Task - Rejected State

Profile: [EReferral Task](StructureDefinition-ereferral-task.md)

**status**: Rejected

**statusReason**: Receiving facility cannot take the case. No onward receiving facility was identified in this response.

**businessStatus**: Rejected

**intent**: order

**code**: eReferral for cardiology consultation

**focus**: [ServiceRequest Referral to cardiology service](ServiceRequest-ExampleERefServiceRequestTask.md)

**for**: [Juan Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatientTask.md)

**authoredOn**: 2025-03-15 09:30:00+0800

**lastModified**: 2025-03-15 10:05:00+0800

**requester**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRoleRequester.md)

**owner**: [Organization Manila General Hospital](Organization-ExampleERefOrganizationReceiving.md)

**note**: , 

> 

New referral for patient with chest pain. Awaiting receiving-facility response.


> 

Manila General Hospital cannot take the case. Referring facility must determine the next action.




## Resource Content

```json
{
  "resourceType" : "Task",
  "id" : "ExampleERefTaskRejected",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-task"]
  },
  "status" : "rejected",
  "statusReason" : {
    "text" : "Receiving facility cannot take the case. No onward receiving facility was identified in this response."
  },
  "businessStatus" : {
    "coding" : [{
      "system" : "https://fhir.doh.gov.ph/pheref/CodeSystem/ereferral-workflow",
      "code" : "rejected",
      "display" : "Rejected"
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
  "lastModified" : "2025-03-15T10:05:00+08:00",
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
    "text" : "Manila General Hospital cannot take the case. Referring facility must determine the next action."
  }]
}

```
