# Example Referring Facility (for Task) - PH eReferral Implementation Guide v0.3.0

## Example Organization: Example Referring Facility (for Task)

Profile: [PH Core Organization](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-organization.html)

**identifier**: `http://fhir.nhdr.gov.ph/nhfr/hospcode`/DOH123456

**name**: Rural Health Unit - Barangay Health Center

**address**: 123 Health Center Road Quezon City Metro Manila PH 



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "ExampleERefOrganizationRequester",
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
