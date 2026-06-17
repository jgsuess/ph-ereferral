# EReferral Provenance - PH eReferral Implementation Guide v0.1.0

 

Other representations of profile: [CSV](../StructureDefinition-ereferral-provenance.csv), [Excel](../StructureDefinition-ereferral-provenance.xlsx), [Schematron](../StructureDefinition-ereferral-provenance.sch) 

## Resource Profile: EReferral Provenance 

 
Profile for tracking audit trail of eReferral actions including signatures and timestamps in the Philippine eReferral context. 

**Usages:**

* Examples for this Profile: [Provenance/ExampleERefProvenanceSignature](Provenance-ExampleERefProvenanceSignature.md) and [Provenance/ExampleERefProvenanceUpdate](Provenance-ExampleERefProvenanceUpdate.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/fhir.ph.ereferral|current/StructureDefinition/StructureDefinition-ereferral-provenance.json)

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

Mandatory: 0 element(1 nested mandatory element)
 Must-Support: 1 element

**Structures**

This structure refers to these other structures:

* [EReferral ServiceRequest (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request)](StructureDefinition-ereferral-service-request.md)

 **Key Elements View** 

#### Terminology Bindings

#### Constraints

 **Differential View** 

 **Snapshot ViewView** 

#### Terminology Bindings

#### Constraints

** Summary **

Mandatory: 0 element(1 nested mandatory element)
 Must-Support: 1 element

**Structures**

This structure refers to these other structures:

* [EReferral ServiceRequest (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request)](StructureDefinition-ereferral-service-request.md)



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ereferral-provenance",
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
  }],
  "url" : "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-provenance",
  "version" : "0.1.0",
  "name" : "ERefProvenance",
  "title" : "EReferral Provenance",
  "status" : "draft",
  "date" : "2026-06-17T00:00:17+00:00",
  "publisher" : "SILab CoP IG Accelerator (eReferral)",
  "contact" : [{
    "name" : "SILab CoP IG Accelerator (eReferral)",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/UP-Manila-SILab"
    }]
  }],
  "description" : "Profile for tracking audit trail of eReferral actions including signatures and timestamps in the Philippine eReferral context.",
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
    "identity" : "w3c.prov",
    "uri" : "http://www.w3.org/ns/prov",
    "name" : "W3C PROV"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "fhirauditevent",
    "uri" : "http://hl7.org/fhir/auditevent",
    "name" : "FHIR AuditEvent Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Provenance",
  "baseDefinition" : "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-provenance",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Provenance",
      "path" : "Provenance"
    },
    {
      "id" : "Provenance.target",
      "path" : "Provenance.target",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request"]
      }]
    },
    {
      "id" : "Provenance.signature",
      "path" : "Provenance.signature",
      "mustSupport" : true
    },
    {
      "id" : "Provenance.signature.data",
      "path" : "Provenance.signature.data",
      "min" : 1
    }]
  }
}

```
