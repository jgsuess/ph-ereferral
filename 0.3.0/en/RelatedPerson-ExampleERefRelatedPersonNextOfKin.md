# Example ERefRelatedPerson - Next of Kin - PH eReferral Implementation Guide v0.3.0

## Example RelatedPerson: Example ERefRelatedPerson - Next of Kin

Roberto Dela Cruz is the patient's father and next of kin. Contact: +639189876543.



## Resource Content

```json
{
  "resourceType" : "RelatedPerson",
  "id" : "ExampleERefRelatedPersonNextOfKin",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-related-person"]
  },
  "active" : true,
  "patient" : {
    "reference" : "Patient/ERefPatientExample"
  },
  "relationship" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "code" : "NOK",
      "display" : "next of kin"
    }]
  },
  {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "code" : "FTH",
      "display" : "father"
    }]
  }],
  "name" : [{
    "use" : "official",
    "family" : "Dela Cruz",
    "given" : ["Roberto"]
  }],
  "telecom" : [{
    "system" : "phone",
    "value" : "+639189876543",
    "use" : "mobile"
  }],
  "gender" : "male",
  "birthDate" : "1958-04-12",
  "address" : [{
    "use" : "home",
    "line" : ["456 Mabini Street"],
    "city" : "Quezon City",
    "state" : "Metro Manila",
    "postalCode" : "1100",
    "country" : "PH"
  }],
  "period" : {
    "start" : "2025-03-15"
  }
}

```
