# Example Referring Practitioner Role (for Task) - PH eReferral Implementation Guide v0.1.0

## Example PractitionerRole: Example Referring Practitioner Role (for Task)

Profile: [PH Core PractitionerRole](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-practitionerrole.html)

**active**: true

**practitioner**: [Practitioner Maria Santos ](Practitioner-ExampleERefPractitionerRequester.md)

**organization**: [Organization Rural Health Unit - Barangay Health Center](Organization-ExampleERefOrganizationRequester.md)

**code**: Medical practitioner



## Resource Content

```json
{
  "resourceType" : "PractitionerRole",
  "id" : "ExampleERefPractitionerRoleRequester",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitionerrole"]
  },
  "active" : true,
  "practitioner" : {
    "reference" : "Practitioner/ExampleERefPractitionerRequester"
  },
  "organization" : {
    "reference" : "Organization/ExampleERefOrganizationRequester"
  },
  "code" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "158965000",
      "display" : "Medical practitioner"
    }]
  }]
}

```
