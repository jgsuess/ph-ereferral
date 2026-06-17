# EReferral Procedure - PH eReferral Implementation Guide v0.1.0

 

Other representations of profile: [CSV](../StructureDefinition-ereferral-procedure.csv), [Excel](../StructureDefinition-ereferral-procedure.xlsx), [Schematron](../StructureDefinition-ereferral-procedure.sch) 

## Resource Profile: EReferral Procedure 

 
Procedure profile for procedures performed or documented as part of the clinical context of a Philippine eReferral. 

**Usages:**

* Refer to this Profile: [EReferral Procedure](StructureDefinition-ereferral-procedure.md)
* Examples for this Profile: [Procedure/ExampleERefProcedureECG](Procedure-ExampleERefProcedureECG.md) and [Procedure/ExampleERefProcedureInitialManagement](Procedure-ExampleERefProcedureInitialManagement.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/fhir.ph.ereferral|current/StructureDefinition/StructureDefinition-ereferral-procedure.json)

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

Must-Support: 3 elements

**Structures**

This structure refers to these other structures:

* [ERefPatient (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient)](StructureDefinition-ereferral-patient.md)
* [ERefEncounter (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-encounter)](StructureDefinition-ereferral-encounter.md)
* [PH Core Condition (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-condition)](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-condition.html)
* [PH Core Observation (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-observation)](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-observation.html)
* [EReferral Procedure (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-procedure)](StructureDefinition-ereferral-procedure.md)

 **Key Elements View** 

#### Terminology Bindings

#### Constraints

 **Differential View** 

 **Snapshot ViewView** 

#### Terminology Bindings

#### Constraints

** Summary **

Must-Support: 3 elements

**Structures**

This structure refers to these other structures:

* [ERefPatient (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient)](StructureDefinition-ereferral-patient.md)
* [ERefEncounter (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-encounter)](StructureDefinition-ereferral-encounter.md)
* [PH Core Condition (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-condition)](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-condition.html)
* [PH Core Observation (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-observation)](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-observation.html)
* [EReferral Procedure (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-procedure)](StructureDefinition-ereferral-procedure.md)



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ereferral-procedure",
  "url" : "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-procedure",
  "version" : "0.1.0",
  "name" : "ERefProcedure",
  "title" : "EReferral Procedure",
  "status" : "draft",
  "date" : "2026-06-17T04:31:39+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Procedure profile for procedures performed or documented as part of the clinical context of a Philippine eReferral.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "PH",
      "display" : "Philippines"
    }]
  }],
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
  "type" : "Procedure",
  "baseDefinition" : "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-procedure",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Procedure",
      "path" : "Procedure"
    },
    {
      "id" : "Procedure.subject",
      "path" : "Procedure.subject",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient"]
      }]
    },
    {
      "id" : "Procedure.encounter",
      "path" : "Procedure.encounter",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-encounter"]
      }]
    },
    {
      "id" : "Procedure.performer",
      "path" : "Procedure.performer",
      "mustSupport" : true
    },
    {
      "id" : "Procedure.performer.actor",
      "path" : "Procedure.performer.actor",
      "mustSupport" : true
    },
    {
      "id" : "Procedure.reasonReference",
      "path" : "Procedure.reasonReference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-condition",
        "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-observation",
        "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-procedure"]
      }]
    },
    {
      "id" : "Procedure.note",
      "path" : "Procedure.note",
      "mustSupport" : true
    }]
  }
}

```
