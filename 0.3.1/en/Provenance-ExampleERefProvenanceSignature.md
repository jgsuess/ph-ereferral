# Example eReferral Provenance with Signature - PH eReferral Implementation Guide v0.3.1

## Example Provenance: Example eReferral Provenance with Signature

Profile: [EReferral Provenance](StructureDefinition-ereferral-provenance.md)

Provenance for [ServiceRequest Patient referral to specialist](ServiceRequest-ExampleERefServiceRequestMinimal.md)

Summary

| | |
| :--- | :--- |
| Recorded | 2025-03-15 09:30:00+0800 |
| Activity | create |

**Agents**

* **Type**: Author
  * **who**: [PractitionerRole Medical practitioner](PractitionerRole-ExampleERefPractitionerRoleMinimal.md)
  * **On Behalf Of**: [Organization Rural Health Unit - Barangay Health Center](Organization-ExampleERefOrganizationMinimal.md)



## Resource Content

```json
{
  "resourceType" : "Provenance",
  "id" : "ExampleERefProvenanceSignature",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-provenance"]
  },
  "target" : [{
    "reference" : "ServiceRequest/ExampleERefServiceRequestMinimal"
  }],
  "recorded" : "2025-03-15T09:30:00+08:00",
  "activity" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
      "code" : "CREATE",
      "display" : "create"
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
  }],
  "signature" : [{
    "type" : [{
      "system" : "urn:iso-astm:E1762-95:2013",
      "code" : "1.2.840.10065.1.12.1.5",
      "display" : "Verification Signature"
    }],
    "when" : "2025-03-15T09:30:00+08:00",
    "who" : {
      "reference" : "PractitionerRole/ExampleERefPractitionerRoleMinimal"
    },
    "sigFormat" : "application/signature+xml",
    "data" : "dGVzdHNpZ25hdHVyZWJhc2U2NA=="
  }]
}

```
