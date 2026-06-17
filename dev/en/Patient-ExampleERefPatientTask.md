# Example eReferral Patient (for Task) - PH eReferral Implementation Guide v0.1.0

## Example Patient: Example eReferral Patient (for Task)

Profile: [PH Core Patient](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-patient.html)

Juan Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)

-------



## Resource Content

```json
{
  "resourceType" : "Patient",
  "id" : "ExampleERefPatientTask",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-patient"]
  },
  "identifier" : [{
    "system" : "urn:oid:2.16.840.1.113883.2.9.4.3.2",
    "value" : "PH-123456789"
  }],
  "name" : [{
    "family" : "Dela Cruz",
    "given" : ["Juan"]
  }],
  "gender" : "male",
  "birthDate" : "1965-07-20"
}

```
