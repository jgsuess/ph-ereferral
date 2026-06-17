# eReferral Priority - PH eReferral Implementation Guide v0.1.0

## ValueSet: eReferral Priority (Experimental) 

 
Priority levels for eReferral requests. Uses standard FHIR RequestPriority values. 

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
  "id" : "ereferral-priority",
  "url" : "https://fhir.doh.gov.ph/pheref/ValueSet/ereferral-priority",
  "version" : "0.1.0",
  "name" : "EReferralPriority",
  "title" : "eReferral Priority",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-06-17T04:31:39+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Priority levels for eReferral requests. Uses standard FHIR RequestPriority values.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "PH",
      "display" : "Philippines"
    }]
  }],
  "compose" : {
    "include" : [{
      "system" : "http://hl7.org/fhir/request-priority",
      "concept" : [{
        "code" : "routine",
        "display" : "Routine"
      },
      {
        "code" : "urgent",
        "display" : "Urgent"
      },
      {
        "code" : "stat",
        "display" : "STAT"
      }]
    }]
  }
}

```
