# eReferral Service Category - PH eReferral Implementation Guide v0.1.0

## ValueSet: eReferral Service Category (Experimental) 

 
Categories of services that can be requested through eReferral 

 **References** 

* [EReferral ServiceRequest](StructureDefinition-ereferral-service-request.md)

### Logical Definition (CLD)

 

### Expansion

-------

 [Description of the above table(s)](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#terminology). 



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "ereferral-service-category",
  "url" : "https://fhir.doh.gov.ph/pheref/ValueSet/ereferral-service-category",
  "version" : "0.1.0",
  "name" : "EReferralServiceCategory",
  "title" : "eReferral Service Category",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-06-17T00:28:17+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Categories of services that can be requested through eReferral",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "PH",
      "display" : "Philippines"
    }]
  }],
  "compose" : {
    "include" : [{
      "system" : "http://snomed.info/sct",
      "concept" : [{
        "code" : "108252007",
        "display" : "Laboratory procedure"
      },
      {
        "code" : "363679005",
        "display" : "Imaging"
      },
      {
        "code" : "409063005",
        "display" : "Counselling"
      },
      {
        "code" : "409073007",
        "display" : "Education"
      },
      {
        "code" : "387713003",
        "display" : "Surgical procedure"
      }]
    }]
  }
}

```
