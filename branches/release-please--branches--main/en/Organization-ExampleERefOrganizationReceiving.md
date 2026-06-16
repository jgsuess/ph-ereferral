# Example Receiving Facility (for Task) - PH eReferral Implementation Guide v0.1.0

## Example Organization: Example Receiving Facility (for Task)

Profile: [PH Core Organization](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-organization.html)

**identifier**: `http://fhir.nhdr.gov.ph/nhfr/hospcode`/DOH789012

**type**: Healthcare Provider

**name**: Manila General Hospital

**address**: 456 Hospital Drive Manila Metro Manila PH 



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "ExampleERefOrganizationReceiving",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization"]
  },
  "identifier" : [{
    "system" : "http://fhir.nhdr.gov.ph/nhfr/hospcode",
    "value" : "DOH789012"
  }],
  "type" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
      "code" : "prov",
      "display" : "Healthcare Provider"
    }]
  }],
  "name" : "Manila General Hospital",
  "address" : [{
    "line" : ["456 Hospital Drive"],
    "city" : "Manila",
    "state" : "Metro Manila",
    "country" : "PH"
  }]
}

```
