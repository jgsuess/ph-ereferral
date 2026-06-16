# EReferral Condition - PH eReferral Implementation Guide v0.1.0

 

Other representations of profile: [CSV](../StructureDefinition-ereferral-condition.csv), [Excel](../StructureDefinition-ereferral-condition.xlsx), [Schematron](../StructureDefinition-ereferral-condition.sch) 

## Resource Profile: EReferral Condition 

 
Condition profile for diagnoses, problems, or clinical conditions relevant to a Philippine eReferral request. 

**Usages:**

* Examples for this Profile: [Condition/ExampleERefConditionChestPain](Condition-ExampleERefConditionChestPain.md) and [Condition/ExampleERefConditionHypertensiveEmergency](Condition-ExampleERefConditionHypertensiveEmergency.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/fhir.ph.ereferral|current/StructureDefinition/StructureDefinition-ereferral-condition.json)

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

Must-Support: 2 elements

 **Key Elements View** 

#### Terminology Bindings

#### Constraints

 **Differential View** 

 **Snapshot ViewView** 

#### Terminology Bindings

#### Constraints

** Summary **

Must-Support: 2 elements



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ereferral-condition",
  "url" : "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-condition",
  "version" : "0.1.0",
  "name" : "ERefCondition",
  "title" : "EReferral Condition",
  "status" : "draft",
  "date" : "2026-06-16T23:15:28+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Condition profile for diagnoses, problems, or clinical conditions relevant to a Philippine eReferral request.",
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
    "identity" : "sct-concept",
    "uri" : "http://snomed.info/conceptdomain",
    "name" : "SNOMED CT Concept Domain Binding"
  },
  {
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
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
    "identity" : "sct-attr",
    "uri" : "http://snomed.org/attributebinding",
    "name" : "SNOMED CT Attribute Binding"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Condition",
  "baseDefinition" : "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-condition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Condition",
      "path" : "Condition"
    },
    {
      "id" : "Condition.clinicalStatus",
      "path" : "Condition.clinicalStatus",
      "short" : "Clinical status of the condition",
      "definition" : "The current clinical status of the diagnosis, problem, or condition relevant to the referral."
    },
    {
      "id" : "Condition.verificationStatus",
      "path" : "Condition.verificationStatus",
      "short" : "Verification status of the condition",
      "definition" : "The certainty or verification state for the diagnosis, problem, or condition, such as provisional or confirmed."
    },
    {
      "id" : "Condition.category",
      "path" : "Condition.category",
      "short" : "Condition category",
      "definition" : "Categorizes the condition as a problem list item, encounter diagnosis, or other category supported by the inherited PH Core binding."
    },
    {
      "id" : "Condition.code",
      "path" : "Condition.code",
      "short" : "Diagnosis, problem, or condition",
      "definition" : "The coded diagnosis, problem, symptom, or clinical condition that is relevant to the eReferral request."
    },
    {
      "id" : "Condition.subject",
      "path" : "Condition.subject",
      "short" : "Patient with the condition",
      "definition" : "The patient who has the diagnosis, problem, or clinical condition relevant to the referral."
    },
    {
      "id" : "Condition.onset[x]",
      "path" : "Condition.onset[x]",
      "short" : "Condition onset",
      "definition" : "The estimated or known date, date/time, age, period, range, or text describing when the condition began.",
      "mustSupport" : true
    },
    {
      "id" : "Condition.recordedDate",
      "path" : "Condition.recordedDate",
      "short" : "Date condition was recorded",
      "definition" : "The date when the condition was first recorded in the referring facility's clinical record.",
      "mustSupport" : true
    },
    {
      "id" : "Condition.note",
      "path" : "Condition.note",
      "short" : "Condition notes",
      "definition" : "Additional clinical notes about the condition that may support referral assessment or triage."
    }]
  }
}

```
