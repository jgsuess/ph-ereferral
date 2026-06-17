# Example Twinact Medication - PH eReferral Implementation Guide v0.3.1

## Example Medication: Example Twinact Medication

Profile: [PH Core Medication](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-medication.html)

**code**: Twinact (Telmisartan 80mg + Amlodipine 5mg) - antihypertensive

**status**: Active



## Resource Content

```json
{
  "resourceType" : "Medication",
  "id" : "ExampleERefMedicationTwinact",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-medication"]
  },
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "105590001",
      "display" : "Substance"
    }],
    "text" : "Twinact (Telmisartan 80mg + Amlodipine 5mg) - antihypertensive"
  },
  "status" : "active"
}

```
