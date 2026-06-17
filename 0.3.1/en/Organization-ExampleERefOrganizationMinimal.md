# Example Referring Facility (Minimal) - PH eReferral Implementation Guide v0.3.1

## Example Organization: Example Referring Facility (Minimal)

Profile: [PH Core Organization](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-organization.html)

**identifier**: `http://fhir.nhdr.gov.ph/nhfr/hospcode`/DOH123456

**name**: Rural Health Unit - Barangay Health Center

**address**: 123 Health Center Road Quezon City Metro Manila PH 



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "ExampleERefOrganizationMinimal",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization"]
  },
  "identifier" : [{
    "system" : "http://fhir.nhdr.gov.ph/nhfr/hospcode",
    "value" : "DOH123456"
  }],
  "name" : "Rural Health Unit - Barangay Health Center",
  "address" : [{
    "line" : ["123 Health Center Road"],
    "city" : "Quezon City",
    "state" : "Metro Manila",
    "country" : "PH"
  }]
}

```
