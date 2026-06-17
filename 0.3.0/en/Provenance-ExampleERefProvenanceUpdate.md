# Example eReferral Provenance for Status Update - PH eReferral Implementation Guide v0.3.0

## Example Provenance: Example eReferral Provenance for Status Update

Profile: [EReferral Provenance](StructureDefinition-ereferral-provenance.md)

Provenance for [ServiceRequest Patient referral to specialist](ServiceRequest-ExampleERefServiceRequestMinimal.md)

Summary

| | |
| :--- | :--- |
| Recorded | 2025-03-16 14:22:00+0800 |
| Activity | revise |

**Agents**

* **Type**: Author
  * **who**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRoleMinimal.md)
  * **On Behalf Of**: [Organization Rural Health Unit - Barangay Health Center](Organization-ExampleERefOrganizationMinimal.md)



## Resource Content

```json
{
  "resourceType" : "Provenance",
  "id" : "ExampleERefProvenanceUpdate",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-provenance"]
  },
  "target" : [{
    "reference" : "ServiceRequest/ExampleERefServiceRequestMinimal"
  }],
  "recorded" : "2025-03-16T14:22:00+08:00",
  "activity" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
      "code" : "UPDATE",
      "display" : "revise"
    }]
  },
  "agent" : [{
    "type" : {
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
        "code" : "author",
        "display" : "Author"
      }]
    },
    "who" : {
      "reference" : "PractitionerRole/ExampleERefPractitionerRoleMinimal"
    },
    "onBehalfOf" : {
      "reference" : "Organization/ExampleERefOrganizationMinimal"
    }
  }]
}

```
