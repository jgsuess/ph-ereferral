# Example eReferral Service Request (Minimal) - PH eReferral Implementation Guide v0.3.1

## Example ServiceRequest: Example eReferral Service Request (Minimal)

Profile: [EReferral ServiceRequest](StructureDefinition-ereferral-service-request.md)

**status**: Active

**intent**: Order

**code**: Patient referral to specialist

**subject**: [Juan Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatientMinimal.md)

**authoredOn**: 2025-03-15 09:30:00+0800

**requester**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRoleMinimal.md)



## Resource Content

```json
{
  "resourceType" : "ServiceRequest",
  "id" : "ExampleERefServiceRequestMinimal",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request"]
  },
  "status" : "active",
  "intent" : "order",
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "103696004",
      "display" : "Patient referral to specialist"
    }]
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatientMinimal"
  },
  "authoredOn" : "2025-03-15T09:30:00+08:00",
  "requester" : {
    "reference" : "PractitionerRole/ExampleERefPractitionerRoleMinimal"
  }
}

```
