# Example Chronic Medication Administration - PH eReferral Implementation Guide v0.3.1

## Example MedicationAdministration: Example Chronic Medication Administration

Profile: [EReferral MedicationAdministration](StructureDefinition-ereferral-medication-administration.md)

**status**: Completed

**medication**: [Medication Substance](Medication-ExampleERefMedicationTwinact.md)

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**context**: [Encounter: identifier = https://pgh.gov.ph/fhir/encounter-id#ENC-2025-001234; status = finished; class = ambulatory (ActCode#AMB); type = Consultation; priority = Emergency; period = 2025-03-16 08:00:00+0800 --> 2025-03-16 10:30:00+0800; reasonCode = Chest pain](Encounter-ExampleERefEncounter.md)

**effective**: 2025-03-15 07:00:00+0800

### Performers

| | | |
| :--- | :--- | :--- |
| - | **Function** | **Actor** |
| * | Medical practitioner | [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md) |

**note**: 

> 

Patient's regular morning antihypertensive medication given before referral. Patient has been compliant with daily dosing.


### Dosages

| | | |
| :--- | :--- | :--- |
| - | **Route** | **Dose** |
| * | Oral route | 1 tablet (Details: UCUM code{tablet} = '{tablet}') |



## Resource Content

```json
{
  "resourceType" : "MedicationAdministration",
  "id" : "ExampleERefMedicationAdministrationChronic",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-medication-administration"]
  },
  "status" : "completed",
  "medicationReference" : {
    "reference" : "Medication/ExampleERefMedicationTwinact"
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "context" : {
    "reference" : "Encounter/ExampleERefEncounter"
  },
  "effectiveDateTime" : "2025-03-15T07:00:00+08:00",
  "performer" : [{
    "function" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "158965000",
        "display" : "Medical practitioner"
      }]
    },
    "actor" : {
      "reference" : "Practitioner/ExampleERefPractitioner"
    }
  }],
  "note" : [{
    "text" : "Patient's regular morning antihypertensive medication given before referral. Patient has been compliant with daily dosing."
  }],
  "dosage" : {
    "route" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "26643006",
        "display" : "Oral route"
      }]
    },
    "dose" : {
      "value" : 1,
      "unit" : "tablet",
      "system" : "http://unitsofmeasure.org",
      "code" : "{tablet}"
    }
  }
}

```
