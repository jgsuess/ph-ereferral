# ERefImmunization Example - Routine Immunization (MMR) - PH eReferral Implementation Guide v0.3.1

## Example Immunization: ERefImmunization Example - Routine Immunization (MMR)

Routine MMR (Measles-Mumps-Rubella) vaccination administered to Juan Dela Cruz on 15 March 2025 at Quezon City Health Center No. 1. Vaccine lot: LOT-2025-MMR-0045 (expires 2026-12-31), manufactured by Serum Institute of India. Dose 1 of 2 administered subcutaneously (0.5 mL) in the left thigh by Nurse Maria Santos, RN. Funded under the national Expanded Program on Immunization (EPI).



## Resource Content

```json
{
  "resourceType" : "Immunization",
  "id" : "ExampleERefImmunizationRoutine",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-immunization"]
  },
  "identifier" : [{
    "system" : "http://example.ph/immunization-records",
    "value" : "IMM-2025-00123"
  }],
  "status" : "completed",
  "vaccineCode" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "871831003",
      "display" : "MMR (measles and mumps and rubella) vaccine"
    }]
  },
  "patient" : {
    "reference" : "Patient/ERefPatientExample"
  },
  "occurrenceDateTime" : "2025-03-15",
  "recorded" : "2025-03-15T09:30:00+08:00",
  "primarySource" : true,
  "location" : {
    "display" : "Quezon City Health Center No. 1"
  },
  "manufacturer" : {
    "display" : "Serum Institute of India"
  },
  "lotNumber" : "LOT-2025-MMR-0045",
  "expirationDate" : "2026-12-31",
  "site" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "61396006",
      "display" : "Structure of left thigh"
    }]
  },
  "route" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "34206005",
      "display" : "Subcutaneous route"
    }]
  },
  "doseQuantity" : {
    "value" : 0.5,
    "unit" : "mL",
    "system" : "http://unitsofmeasure.org",
    "code" : "mL"
  },
  "performer" : [{
    "function" : {
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/v2-0443",
        "code" : "AP",
        "display" : "Administering Provider"
      }]
    },
    "actor" : {
      "display" : "Nurse Maria Santos, RN"
    }
  }],
  "reasonCode" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "33879002",
      "display" : "Administration of vaccine to produce active immunity (procedure)"
    }]
  }],
  "isSubpotent" : false,
  "programEligibility" : [{
    "text" : "Eligible - DOH Expanded Program on Immunization (EPI)"
  }],
  "fundingSource" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/immunization-funding-source",
      "code" : "public",
      "display" : "Public"
    }]
  },
  "protocolApplied" : [{
    "series" : "MMR 2-Dose Series",
    "targetDisease" : [{
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "14189004",
        "display" : "Measles (disorder)"
      }]
    },
    {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "36989005",
        "display" : "Mumps (disorder)"
      }]
    },
    {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "36653000",
        "display" : "Rubella (disorder)"
      }]
    }],
    "doseNumberPositiveInt" : 1,
    "seriesDosesPositiveInt" : 2
  }]
}

```
