# Example eReferral Patient - PH eReferral Implementation Guide v0.3.0

## Example Patient: Example eReferral Patient

Profile: [PH Core Patient](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-patient.html)

Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)

-------

| | |
| :--- | :--- |
| Contact Detail | * [+63 912 345 6789](tel:+639123456789)
* [juan.delacruz@email.com](mailto:juan.delacruz@email.com)
* 123 Mabini St Quezon City Metro Manila 1100 PH (home)
 |



## Resource Content

```json
{
  "resourceType" : "Patient",
  "id" : "ExampleERefPatient",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-patient"]
  },
  "identifier" : [{
    "system" : "urn:oid:2.16.840.1.113883.2.9.4.3.2",
    "value" : "PH-123456789"
  }],
  "name" : [{
    "family" : "Dela Cruz",
    "given" : ["Juan", "Miguel"]
  }],
  "telecom" : [{
    "system" : "phone",
    "value" : "+63 912 345 6789",
    "use" : "mobile"
  },
  {
    "system" : "email",
    "value" : "juan.delacruz@email.com"
  }],
  "gender" : "male",
  "birthDate" : "1965-07-20",
  "address" : [{
    "use" : "home",
    "line" : ["123 Mabini St"],
    "city" : "Quezon City",
    "state" : "Metro Manila",
    "postalCode" : "1100",
    "country" : "PH"
  }]
}

```
