# Example Referring Practitioner Role (Minimal) - PH eReferral Implementation Guide v0.3.1

## Example PractitionerRole: Example Referring Practitioner Role (Minimal)

Profile: [PH Core PractitionerRole](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-practitionerrole.html)

**active**: true

**practitioner**: [Practitioner Maria Santos ](Practitioner-ExampleERefPractitionerMinimal.md)

**organization**: [Organization Rural Health Unit - Barangay Health Center](Organization-ExampleERefOrganizationMinimal.md)

**code**: Medical practitioner



## Resource Content

```json
{
  "resourceType" : "PractitionerRole",
  "id" : "ExampleERefPractitionerRoleMinimal",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitionerrole"]
  },
  "active" : true,
  "practitioner" : {
    "reference" : "Practitioner/ExampleERefPractitionerMinimal"
  },
  "organization" : {
    "reference" : "Organization/ExampleERefOrganizationMinimal"
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
