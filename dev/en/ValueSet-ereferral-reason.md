# eReferral Reason - PH eReferral Implementation Guide v0.1.0

## ValueSet: eReferral Reason (Experimental) 

 
Clinical reasons for eReferral requests. Uses SNOMED CT clinical findings and diagnoses. 

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
  "id" : "ereferral-reason",
  "url" : "https://fhir.doh.gov.ph/pheref/ValueSet/ereferral-reason",
  "version" : "0.1.0",
  "name" : "EReferralReason",
  "title" : "eReferral Reason",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-06-17T12:31:02+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Clinical reasons for eReferral requests. Uses SNOMED CT clinical findings and diagnoses.",
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
        "code" : "267036007",
        "display" : "Dyspnea"
      },
      {
        "code" : "29857009",
        "display" : "Chest pain"
      },
      {
        "code" : "414545008",
        "display" : "Suspected lung cancer"
      },
      {
        "code" : "42343007",
        "display" : "Congestive heart failure"
      },
      {
        "code" : "49436004",
        "display" : "Atrial fibrillation"
      },
      {
        "code" : "59621000",
        "display" : "Essential hypertension"
      },
      {
        "code" : "73211009",
        "display" : "Diabetes mellitus"
      },
      {
        "code" : "109006",
        "display" : "Anxiety disorder"
      }]
    }]
  }
}

```
