# Example ERefRelatedPerson - Accompanying Person - PH eReferral Implementation Guide v0.3.1

## Example RelatedPerson: Example ERefRelatedPerson - Accompanying Person

Maria Dela Cruz is the patient's spouse and emergency contact accompanying the patient during referral. Contact: +639171112222.



## Resource Content

```json
{
  "resourceType" : "RelatedPerson",
  "id" : "ExampleERefRelatedPersonAccompanying",
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
      "code" : "ECON",
      "display" : "emergency contact"
    }]
  },
  {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "code" : "SPS",
      "display" : "spouse"
    }]
  }],
  "name" : [{
    "use" : "official",
    "family" : "Dela Cruz",
    "given" : ["Maria"]
  }],
  "telecom" : [{
    "system" : "phone",
    "value" : "+639171112222",
    "use" : "mobile"
  }],
  "gender" : "female",
  "period" : {
    "start" : "2025-03-15"
  }
}

```
