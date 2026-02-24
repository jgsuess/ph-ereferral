# Patient — Charity Santos - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Patient — Charity Santos**

## Example Patient: Patient — Charity Santos

Profile: [PH Core Patient](https://build.fhir.org/ig/UP-Manila-SILab/ph-core/StructureDefinition-ph-core-patient.html)

Tags: REF-20 (Details: peref-dd code REF-20), REF-21 (Details: peref-dd code REF-21), REF-22 (Details: peref-dd code REF-22), REF-24 (Details: peref-dd code REF-24), REF-25 (Details: peref-dd code REF-25), REF-26 (Details: peref-dd code REF-26), REF-27 (Details: peref-dd code REF-27)

Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)

-------

| | |
| :--- | :--- |
| Active: | true |
| Other Id: | `http://doh.gov.ph/fhir/ph-core/NamingSystem/philhealth-id-ns`/12-345678901-2 |
| Contact Detail | * [+63-917-123-4567](tel:+63-917-123-4567)
* 456 Rizal Street Barangay Malusog Quezon City 1100 PH (home)
 |



## Resource Content

```json
{
  "resourceType" : "Patient",
  "id" : "patient-charity-ex",
  "meta" : {
    "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-patient"],
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-20",
      "display" : "REF-20"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-21",
      "display" : "REF-21"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-22",
      "display" : "REF-22"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-24",
      "display" : "REF-24"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-25",
      "display" : "REF-25"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-26",
      "display" : "REF-26"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-27",
      "display" : "REF-27"
    }]
  },
  "identifier" : [{
    "system" : "http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns",
    "value" : "1234-5678901-2"
  },
  {
    "system" : "http://doh.gov.ph/fhir/ph-core/NamingSystem/philhealth-id-ns",
    "value" : "12-345678901-2"
  }],
  "active" : true,
  "name" : [{
    "use" : "official",
    "family" : "Santos",
    "given" : ["Charity"]
  }],
  "telecom" : [{
    "system" : "phone",
    "value" : "+63-917-123-4567",
    "use" : "mobile"
  }],
  "gender" : "female",
  "birthDate" : "2001-08-15",
  "address" : [{
    "use" : "home",
    "line" : ["456 Rizal Street", "Barangay Malusog"],
    "city" : "Quezon City",
    "district" : "NCR",
    "postalCode" : "1100",
    "country" : "PH"
  }]
}

```
