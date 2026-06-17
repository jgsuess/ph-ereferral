# EReferral Observation - PH eReferral Implementation Guide v0.1.0

 

Other representations of profile: [CSV](../StructureDefinition-ereferral-observation.csv), [Excel](../StructureDefinition-ereferral-observation.xlsx), [Schematron](../StructureDefinition-ereferral-observation.sch) 

## Resource Profile: EReferral Observation 

 
Profile for clinical observations in the Philippine eReferral context. Supports vital signs, laboratory results, and clinical measurements included in referral clinical summaries. Referenced via ServiceRequest.supportingInfo and ServiceRequest.reasonReference. 

**Usages:**

* Examples for this Profile: [Observation/ExampleERefObservationBP](Observation-ExampleERefObservationBP.md), [Observation/ExampleERefObservationChiefComplaint](Observation-ExampleERefObservationChiefComplaint.md), [Observation/ExampleERefObservationECG](Observation-ExampleERefObservationECG.md), [Observation/ExampleERefObservationHeartRate](Observation-ExampleERefObservationHeartRate.md)... Show 5 more, [Observation/ExampleERefObservationLabGlucose](Observation-ExampleERefObservationLabGlucose.md), [Observation/ExampleERefObservationOxygenSat](Observation-ExampleERefObservationOxygenSat.md), [Observation/ExampleERefObservationRespiratoryRate](Observation-ExampleERefObservationRespiratoryRate.md), [Observation/ExampleERefObservationTemperature](Observation-ExampleERefObservationTemperature.md) and [Observation/ExampleERefObservationWeight](Observation-ExampleERefObservationWeight.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/fhir.ph.ereferral|current/StructureDefinition/StructureDefinition-ereferral-observation.json)

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

Must-Support: 1 element

**Structures**

This structure refers to these other structures:

* [ERefPatient (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient)](StructureDefinition-ereferral-patient.md)

 **Key Elements View** 

#### Terminology Bindings

#### Constraints

 **Differential View** 

 **Snapshot ViewView** 

#### Terminology Bindings

#### Constraints

** Summary **

Must-Support: 1 element

**Structures**

This structure refers to these other structures:

* [ERefPatient (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient)](StructureDefinition-ereferral-patient.md)



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ereferral-observation",
  "extension" : [{
    "extension" : [{
      "url" : "code",
      "valueCode" : "SHALL:handle"
    },
    {
      "url" : "actor",
      "valueCanonical" : "https://fhir.doh.gov.ph/phcore/ActorDefinition/Server"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/obligation"
  },
  {
    "extension" : [{
      "url" : "code",
      "valueCode" : "SHALL:handle"
    },
    {
      "url" : "actor",
      "valueCanonical" : "https://fhir.doh.gov.ph/phcore/ActorDefinition/Consumer"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/obligation"
  },
  {
    "extension" : [{
      "url" : "code",
      "valueCode" : "MAY:able-to-populate"
    },
    {
      "url" : "actor",
      "valueCanonical" : "https://fhir.doh.gov.ph/phcore/ActorDefinition/Creator"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/obligation"
  },
  {
    "extension" : [{
      "url" : "code",
      "valueCode" : "SHALL:handle"
    },
    {
      "url" : "actor",
      "valueCanonical" : "https://fhir.doh.gov.ph/phcore/ActorDefinition/Server"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/obligation"
  },
  {
    "extension" : [{
      "url" : "code",
      "valueCode" : "SHALL:handle"
    },
    {
      "url" : "actor",
      "valueCanonical" : "https://fhir.doh.gov.ph/phcore/ActorDefinition/Consumer"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/obligation"
  },
  {
    "extension" : [{
      "url" : "code",
      "valueCode" : "MAY:able-to-populate"
    },
    {
      "url" : "actor",
      "valueCanonical" : "https://fhir.doh.gov.ph/phcore/ActorDefinition/Creator"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/obligation"
  }],
  "url" : "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-observation",
  "version" : "0.1.0",
  "name" : "ERefObservation",
  "title" : "EReferral Observation",
  "status" : "draft",
  "date" : "2026-06-17T10:39:22+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Profile for clinical observations in the Philippine eReferral context. \nSupports vital signs, laboratory results, and clinical measurements included in \nreferral clinical summaries. Referenced via ServiceRequest.supportingInfo and \nServiceRequest.reasonReference.",
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
  "type" : "Observation",
  "baseDefinition" : "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-observation",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Observation",
      "path" : "Observation"
    },
    {
      "id" : "Observation.subject",
      "path" : "Observation.subject",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-patient"]
      }],
      "mustSupport" : true
    }]
  }
}

```
