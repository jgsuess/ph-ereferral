# Example Referring Practitioner (Minimal) - PH eReferral Implementation Guide v0.1.0

## Example Practitioner: Example Referring Practitioner (Minimal)

Profile: [PH Core Practitioner](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-practitioner.html)

**identifier**: `urn:oid:2.16.840.1.113883.2.9.4.3.3`/MD-98765

**name**: Maria Santos 

**gender**: Female



## Resource Content

```json
{
  "resourceType" : "Practitioner",
  "id" : "ExampleERefPractitionerMinimal",
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
