# PH eReferral PractitionerRole - PH eReferral Implementation Guide v0.1.0

 

Other representations of profile: [CSV](../StructureDefinition-ereferral-practitioner-role.csv), [Excel](../StructureDefinition-ereferral-practitioner-role.xlsx), [Schematron](../StructureDefinition-ereferral-practitioner-role.sch) 

## Resource Profile: PH eReferral PractitionerRole 

 
Profile on PractitionerRole for the Philippines eReferral specification, extending PHCorePractitionerRole. This profile captures the role of the referring practitioner and care navigator within the eReferral workflow, linking practitioners to healthcare facilities. 

**Usages:**

* Examples for this Profile: [PractitionerRole/ExampleERefPractitionerRole](PractitionerRole-ExampleERefPractitionerRole.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/fhir.ph.ereferral|current/StructureDefinition/StructureDefinition-ereferral-practitioner-role.json)

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

Mandatory: 1 element

 **Key Elements View** 

#### Terminology Bindings

#### Constraints

 **Differential View** 

 **Snapshot ViewView** 

#### Terminology Bindings

#### Constraints

** Summary **

Mandatory: 1 element



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ereferral-practitioner-role",
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
      "valueCode" : "SHALL:able-to-populate"
    },
    {
      "url" : "actor",
      "valueCanonical" : "https://fhir.doh.gov.ph/phcore/ActorDefinition/Creator"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/obligation"
  }],
  "url" : "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-practitioner-role",
  "version" : "0.1.0",
  "name" : "ERefPractitionerRole",
  "title" : "PH eReferral PractitionerRole",
  "status" : "draft",
  "date" : "2026-06-16T22:56:55+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Profile on PractitionerRole for the Philippines eReferral specification, extending PHCorePractitionerRole. This profile captures the role of the referring practitioner and care navigator within the eReferral workflow, linking practitioners to healthcare facilities.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "PH",
      "display" : "Philippines"
    }]
  }],
  "purpose" : "This profile defines the constraints for representing practitioner roles in the Philippines eReferral context.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
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
    "identity" : "servd",
    "uri" : "http://www.omg.org/spec/ServD/1.0/",
    "name" : "ServD"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "PractitionerRole",
  "baseDefinition" : "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitionerrole",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "PractitionerRole",
      "path" : "PractitionerRole"
    },
    {
      "id" : "PractitionerRole.code",
      "path" : "PractitionerRole.code",
      "short" : "Role or designation of the practitioner",
      "definition" : "The designation or role of the practitioner (e.g., Midwife, District Nurse, District Medical Officer).",
      "min" : 1
    }]
  }
}

```
