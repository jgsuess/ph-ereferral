# Example Antibiotic Administration - PH eReferral Implementation Guide v0.3.1

## Example MedicationAdministration: Example Antibiotic Administration

Profile: [EReferral MedicationAdministration](StructureDefinition-ereferral-medication-administration.md)

**status**: Completed

**medication**: [Medication Substance](Medication-ExampleERefMedicationAntibiotic.md)

**subject**: [Juan Miguel Dela Cruz Male, DoB: 1965-07-20 ( urn:oid:2.16.840.1.113883.2.9.4.3.2#PH-123456789)](Patient-ExampleERefPatient.md)

**effective**: 2025-03-15 08:00:00+0800 --> 2025-03-15 08:30:00+0800

### Performers

| | | |
| :--- | :--- | :--- |
| - | **Function** | **Actor** |
| * | Medical practitioner | [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md) |

**note**: 

> 

Administered as part of pre-referral treatment for suspected sepsis. Patient to continue oral antibiotics at receiving facility.


### Dosages

| | | | |
| :--- | :--- | :--- | :--- |
| - | **Site** | **Route** | **Dose** |
| * | Structure of median cubital vein | Intravenous route | 750 mg (Details: UCUM codemg = 'mg') |



## Resource Content

```json
{
  "resourceType" : "MedicationAdministration",
  "id" : "ExampleERefMedicationAdministrationAntibiotic",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-medication-administration"]
  },
  "status" : "completed",
  "medicationReference" : {
    "reference" : "Medication/ExampleERefMedicationAntibiotic"
  },
  "subject" : {
    "reference" : "Patient/ExampleERefPatient"
  },
  "effectivePeriod" : {
    "start" : "2025-03-15T08:00:00+08:00",
    "end" : "2025-03-15T08:30:00+08:00"
  },
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
    "text" : "Administered as part of pre-referral treatment for suspected sepsis. Patient to continue oral antibiotics at receiving facility."
  }],
  "dosage" : {
    "site" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "49852007",
        "display" : "Structure of median cubital vein"
      }]
    },
    "route" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "47625008",
        "display" : "Intravenous route"
      }]
    },
    "dose" : {
      "value" : 750,
      "unit" : "mg",
      "system" : "http://unitsofmeasure.org",
      "code" : "mg"
    }
  }
}

```
