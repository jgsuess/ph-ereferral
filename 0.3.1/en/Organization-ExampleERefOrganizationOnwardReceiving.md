# Example Onward Receiving Facility (for Task) - PH eReferral Implementation Guide v0.3.1

## Example Organization: Example Onward Receiving Facility (for Task)

Profile: [PH Core Organization](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-organization.html)

**identifier**: `http://fhir.nhdr.gov.ph/nhfr/hospcode`/DOH345678

**type**: Healthcare Provider

**name**: Eastern District Medical Center

**address**: 789 District Avenue Pasig City Metro Manila PH 



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "ExampleERefOrganizationOnwardReceiving",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization"]
  },
  "identifier" : [{
    "system" : "http://fhir.nhdr.gov.ph/nhfr/hospcode",
    "value" : "DOH345678"
  }],
  "type" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
      "code" : "prov",
      "display" : "Healthcare Provider"
    }]
  }],
  "name" : "Eastern District Medical Center",
  "address" : [{
    "line" : ["789 District Avenue"],
    "city" : "Pasig City",
    "state" : "Metro Manila",
    "country" : "PH"
  }]
}

```
