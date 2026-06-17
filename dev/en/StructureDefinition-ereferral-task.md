# EReferral Task - PH eReferral Implementation Guide v0.1.0

 

Other representations of profile: [CSV](../StructureDefinition-ereferral-task.csv), [Excel](../StructureDefinition-ereferral-task.xlsx), [Schematron](../StructureDefinition-ereferral-task.sch) 

## Resource Profile: EReferral Task 

 
Task profile for Philippine eReferral workflow management. Tracks referral state transitions from request through completion, supporting workflow coordination between sending and receiving facilities. 

**Usages:**

* Examples for this Profile: [Task/ExampleERefTaskAccepted](Task-ExampleERefTaskAccepted.md), [Task/ExampleERefTaskCompleted](Task-ExampleERefTaskCompleted.md), [Task/ExampleERefTaskReceived](Task-ExampleERefTaskReceived.md), [Task/ExampleERefTaskReferredOnward](Task-ExampleERefTaskReferredOnward.md)... Show 2 more, [Task/ExampleERefTaskRejected](Task-ExampleERefTaskRejected.md) and [Task/ExampleERefTaskRequested](Task-ExampleERefTaskRequested.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/fhir.ph.ereferral|current/StructureDefinition/StructureDefinition-ereferral-task.json)

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

#### Terminology Bindings (Differential)

#### Terminology Bindings

#### Constraints

** Summary **

Mandatory: 2 elements
 Must-Support: 8 elements
 Fixed: 1 element

**Structures**

This structure refers to these other structures:

* [EReferral ServiceRequest (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request)](StructureDefinition-ereferral-service-request.md)
* [PH Core Practitioner (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitioner)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-practitioner.html)
* [PH Core PractitionerRole (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitionerrole)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-practitionerrole.html)
* [PH Core Organization (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-organization.html)

 **Key Elements View** 

#### Terminology Bindings

#### Constraints

 **Differential View** 

#### Terminology Bindings (Differential)

 **Snapshot ViewView** 

#### Terminology Bindings

#### Constraints

** Summary **

Mandatory: 2 elements
 Must-Support: 8 elements
 Fixed: 1 element

**Structures**

This structure refers to these other structures:

* [EReferral ServiceRequest (https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request)](StructureDefinition-ereferral-service-request.md)
* [PH Core Practitioner (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitioner)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-practitioner.html)
* [PH Core PractitionerRole (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitionerrole)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-practitionerrole.html)
* [PH Core Organization (https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization)](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-organization.html)



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ereferral-task",
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
      "valueCode" : "SHALL:able-to-populate"
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
      "valueCode" : "SHALL:able-to-populate"
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
  "url" : "https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-task",
  "version" : "0.1.0",
  "name" : "ERefTask",
  "title" : "EReferral Task",
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
  "description" : "Task profile for Philippine eReferral workflow management. Tracks referral state transitions from request through completion, supporting workflow coordination between sending and receiving facilities.",
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
  "type" : "Task",
  "baseDefinition" : "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-task",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Task",
      "path" : "Task"
    },
    {
      "id" : "Task.statusReason",
      "path" : "Task.statusReason",
      "short" : "Reason for current workflow status",
      "definition" : "Reason or instruction associated with the receiving facility response, such as capacity full or other instructions."
    },
    {
      "id" : "Task.businessStatus",
      "path" : "Task.businessStatus",
      "short" : "Receiving-facility response",
      "definition" : "The receiving facility response after referral receipt. Uses local eReferral terms for received, accepted, rejected, or referred onward while Task.status remains the standard FHIR Task lifecycle status.",
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "https://fhir.doh.gov.ph/pheref/ValueSet/ereferral-receiving-response"
      }
    },
    {
      "id" : "Task.intent",
      "path" : "Task.intent",
      "short" : "Fixed to 'order' for referrals",
      "definition" : "The intent is fixed to 'order' as eReferral tasks represent actionable orders for services to be performed by receiving facilities.",
      "fixedCode" : "order",
      "mustSupport" : true
    },
    {
      "id" : "Task.focus",
      "path" : "Task.focus",
      "short" : "Reference to the ServiceRequest being tracked",
      "definition" : "The ServiceRequest that this task is tracking through the eReferral workflow. Required for all eReferral tasks.",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-service-request"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Task.authoredOn",
      "path" : "Task.authoredOn",
      "short" : "When task was created",
      "definition" : "The date and time when the eReferral task was created.",
      "mustSupport" : true
    },
    {
      "id" : "Task.lastModified",
      "path" : "Task.lastModified",
      "short" : "When task was last updated",
      "definition" : "The date and time when the eReferral task was last modified.",
      "mustSupport" : true
    },
    {
      "id" : "Task.requester",
      "path" : "Task.requester",
      "short" : "Requesting practitioner or facility",
      "definition" : "The practitioner or facility that created the referral task. Represents the initiating side of the eReferral workflow.",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitioner",
        "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitionerrole",
        "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Task.owner",
      "path" : "Task.owner",
      "short" : "Assigned care navigator or receiving facility",
      "definition" : "The practitioner, care navigator, or facility responsible for executing the referral task. TDG REF-9: 'Care Navigator' assignment.",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitioner",
        "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitionerrole",
        "https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Task.output",
      "path" : "Task.output",
      "short" : "Receiving response output",
      "definition" : "Structured outputs from the receiving facility response. For referred-onward responses, this may identify that an onward referral request was created; the onward ServiceRequest should use ServiceRequest.replaces to link back to the prior request.",
      "mustSupport" : true
    },
    {
      "id" : "Task.output.value[x]",
      "path" : "Task.output.value[x]",
      "mustSupport" : true
    }]
  }
}

```
