# RelatedPerson — Maria Santos (Mother) - PH eReferral Implementation Guide v0.3.1

## Example RelatedPerson: RelatedPerson — Maria Santos (Mother)

Profile: `http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-relatedperson`

Tag: 

**patient**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**relationship**: Mother

**name**: Maria Santos 

**telecom**: [+63-917-765-4321](tel:+63-917-765-4321)



## Resource Content

```json
{
  "resourceType" : "RelatedPerson",
  "id" : "relatedperson-companion-ex",
  "meta" : {
    "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-relatedperson"],
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-28",
      "display" : "REF-28"
    }]
  },
  "patient" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "relationship" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "code" : "MTH",
      "display" : "Mother"
    }]
  }],
  "name" : [{
    "family" : "Santos",
    "given" : ["Maria"]
  }],
  "telecom" : [{
    "system" : "phone",
    "value" : "+63-917-765-4321",
    "use" : "mobile"
  }]
}

```
