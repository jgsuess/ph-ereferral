# ERefEncounter - PH eReferral Implementation Guide v0.1.0

 

Other representations of profile: [CSV](../StructureDefinition-ereferral-encounter.csv), [Excel](../StructureDefinition-ereferral-encounter.xlsx), [Schematron](../StructureDefinition-ereferral-encounter.sch) 

## Resource Profile: ERefEncounter ( Experimental ) 

 
Encounter profile for the Philippine eReferral system. Extends PHCoreEncounter to capture the clinical encounter context associated with a referral, including encounter status, classification, participants, and clinical information relevant to the referral workflow. 

**Usages:**

* Refer to this Profile: [EReferral Procedure](StructureDefinition-ereferral-procedure.md)
* Examples for this Profile: [Encounter/ExampleERefEncounter](Encounter-ExampleERefEncounter.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/fhir.ph.ereferral|current/StructureDefinition/StructureDefinition-ereferral-encounter.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

*  [Key Elements Table](#tabs-key) 
*  [Differential Table](#tabs-diff) 
*  [Snapshot Table](#tabs-snap) 
*  [Obligations](#tabs-obligations) 
*  [Statistics/References](#tabs-summ) 
*  [All](#tabs-all) 

#### Terminology Bindings

#### Constraints

#### Terminology Bindings

#### Constraints

** Summary **

**Structures**

This structure refers to these other structures:

* [ERefPatient (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient)](StructureDefinition-ereferral-patient.md)
* [EReferral ServiceRequest (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request)](StructureDefinition-ereferral-service-request.md)
* [PH Core Condition (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-condition)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-condition.html)
* [PH Core Observation (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-observation)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-observation.html)
* [PH Core Procedure (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-procedure)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-procedure.html)

 **Key Elements View** 

#### Terminology Bindings

#### Constraints

 **Differential View** 

 **Snapshot ViewView** 

#### Terminology Bindings

#### Constraints

** Summary **

**Structures**

This structure refers to these other structures:

* [ERefPatient (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient)](StructureDefinition-ereferral-patient.md)
* [EReferral ServiceRequest (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request)](StructureDefinition-ereferral-service-request.md)
* [PH Core Condition (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-condition)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-condition.html)
* [PH Core Observation (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-observation)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-observation.html)
* [PH Core Procedure (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-procedure)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-procedure.html)



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ereferral-encounter",
  "url" : "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-encounter",
  "version" : "0.1.0",
  "name" : "ERefEncounter",
  "title" : "ERefEncounter",
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
  "description" : "Encounter profile for the Philippine eReferral system. Extends PHCoreEncounter to capture the clinical encounter context associated with a referral, including encounter status, classification, participants, and clinical information relevant to the referral workflow.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "PH",
      "display" : "Philippines"
    }]
  }],
  "purpose" : "To standardize encounter information within the Philippine eReferral system, ensuring clinical context is consistently captured and linked to referral requests.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Encounter",
  "baseDefinition" : "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-encounter",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Encounter",
      "path" : "Encounter"
    },
    {
      "id" : "Encounter.subject",
      "path" : "Encounter.subject",
      "short" : "The referral patient present at the encounter.",
      "definition" : "The referral patient who is the subject of this encounter.",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient"]
      }]
    },
    {
      "id" : "Encounter.basedOn",
      "path" : "Encounter.basedOn",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request"]
      }]
    },
    {
      "id" : "Encounter.reasonReference",
      "path" : "Encounter.reasonReference",
      "definition" : "Reason the encounter takes place, expressed as a reference to a Condition, Observation, or Procedure.",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-condition",
        "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-observation",
        "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-procedure"]
      }]
    }]
  }
}

```
