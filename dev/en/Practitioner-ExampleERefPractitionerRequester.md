# Example Referring Practitioner (for Task) - PH eReferral Implementation Guide v0.1.0

## Example Practitioner: Example Referring Practitioner (for Task)

Profile: [PH Core Practitioner](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-practitioner.html)

**identifier**: `urn:oid:2.16.840.1.113883.2.9.4.3.3`/MD-98765

**name**: Maria Santos 

**gender**: Female



## Resource Content

```json
{
  "resourceType" : "Practitioner",
  "id" : "ExampleERefPractitionerRequester",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitioner"]
  },
  "identifier" : [{
    "system" : "urn:oid:2.16.840.1.113883.2.9.4.3.3",
    "value" : "MD-98765"
  }],
  "name" : [{
    "family" : "Santos",
    "given" : ["Maria"],
    "prefix" : ["Dr."]
  }],
  "gender" : "female"
}

```
