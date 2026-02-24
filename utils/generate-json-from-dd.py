#!/usr/bin/env python3
"""
Generate FHIR R4 JSON example resources for the ANC user-scenario (scenario 3.1)
mapped to the PeRef Data Dictionary (dd-coverage.csv).

Each resource is annotated with the DD element IDs it covers via:
  - meta.tag  (system = "https://example.com/peref-dd", code = "REF-xx")

Output: input/examples/<resource-id>-ex.json

Usage:
    cd <repo-root>
    .venv/bin/python utils/generate-json-from-dd.py
"""
import json, os, uuid, pathlib

OUT_DIR = pathlib.Path(__file__).resolve().parent.parent / "input" / "examples-json-source"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DD_TAG_SYSTEM = "https://example.com/peref-dd"

# Stable UUIDs for cross-referencing within bundles
UUIDS = {
    "patient-charity":               "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "relatedperson-companion":       "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
    "organization-sending":          "7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "organization-receiving":        "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed",
    "practitioner-abraham":          "2c6d4f8a-3e5b-4a1c-9f8d-7b6e5d4c3a2b",
    "practitionerrole-abraham":      "3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a",
    "practitioner-jane":             "4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c",
    "practitionerrole-jane":         "5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d",
    "encounter-registration":        "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "encounter-anc":                 "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "condition-pregnancy":           "c3d4e5f6-a7b8-9012-cdef-123456789012",
    "observation-chief-complaint":   "d4e5f6a7-b8c9-0123-defa-234567890123",
    "observation-blood-pressure":    "e5f6a7b8-c9d0-1234-efab-345678901234",
    "observation-heart-rate":        "f6a7b8c9-d0e1-2345-fabc-456789012345",
    "observation-respiratory-rate":  "a7b8c9d0-e1f2-3456-abcd-567890123456",
    "observation-oxygen-saturation": "b8c9d0e1-f2a3-4567-bcde-678901234567",
    "observation-temperature":       "c9d0e1f2-a3b4-5678-cdef-789012345678",
    "observation-weight":            "d0e1f2a3-b4c5-6789-defa-890123456789",
    "medicationadmin-ifa":           "e1f2a3b4-c5d6-7890-efab-901234567890",
    "servicerequest-ultrasound":     "f2a3b4c5-d6e7-8901-fabc-012345678901",
    "servicerequest-lab":            "a3b4c5d6-e7f8-9012-abcd-123456789012",
    "task-referral":                 "b4c5d6e7-f8a9-0123-bcde-234567890123",
}

def urn(key):
    return f"urn:uuid:{UUIDS[key]}"

def dd_tags(*refs):
    """Build meta.tag array for given DD element IDs."""
    return [{"system": DD_TAG_SYSTEM, "code": r, "display": r} for r in refs]

def text_div(desc):
    return {
        "status": "generated",
        "div": f'<div xmlns="http://www.w3.org/1999/xhtml">{desc}</div>'
    }

def write(filename, resource):
    path = OUT_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(resource, f, indent=2, ensure_ascii=False)
    print(f"  ✓ {filename}")

# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------

def patient_charity():
    """DD: REF-20..REF-27, REF-24, REF-25, REF-26"""
    return {
        "resourceType": "Patient",
        "id": "patient-charity-ex",
        "meta": {
            "profile": ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-patient"],
            "tag": dd_tags("REF-20", "REF-21", "REF-22", "REF-24", "REF-25", "REF-26", "REF-27")
        },
        "text": text_div("Charity is a 24-year-old female patient seeking her first antenatal care contact. [DD: REF-20 to REF-27]"),
        "active": True,
        "name": [
            {
                "use": "official",
                "family": "Santos",
                "given": ["Charity"]
            }
        ],
        "gender": "female",           # REF-21
        "birthDate": "2001-08-15",    # REF-22 (age 24 as of 2026-02-24)
        "identifier": [
            {   # REF-24 PhilSys
                "system": "http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns",
                "value": "1234-5678901-2"
            },
            {   # REF-25 PhilHealth
                "system": "http://doh.gov.ph/fhir/ph-core/NamingSystem/philhealth-id-ns",
                "value": "12-345678901-2"
            }
        ],
        "address": [            # REF-26
            {
                "use": "home",
                "line": ["456 Rizal Street", "Barangay Malusog"],
                "city": "Quezon City",
                "district": "NCR",
                "postalCode": "1100",
                "country": "PH"
            }
        ],
        "telecom": [            # REF-27
            {
                "system": "phone",
                "value": "+63-917-123-4567",
                "use": "mobile"
            }
        ]
    }


def relatedperson_companion():
    """DD: REF-28"""
    return {
        "resourceType": "RelatedPerson",
        "id": "relatedperson-companion-ex",
        "meta": {
            "profile": ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-relatedperson"],
            "tag": dd_tags("REF-28")
        },
        "text": text_div("Maria Santos, mother of Charity, listed as next of kin / accompanying person. [DD: REF-28]"),
        "patient": {"reference": urn("patient-charity")},
        "relationship": [
            {
                "coding": [{
                    "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
                    "code": "MTH",
                    "display": "Mother"
                }]
            }
        ],
        "name": [
            {
                "family": "Santos",
                "given": ["Maria"]
            }
        ],
        "telecom": [
            {
                "system": "phone",
                "value": "+63-917-765-4321",
                "use": "mobile"
            }
        ]
    }


def organization_sending():
    """DD: REF-4, REF-5, REF-6, REF-7"""
    return {
        "resourceType": "Organization",
        "id": "organization-sending-facility-ex",
        "meta": {
            "profile": ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization"],
            "tag": dd_tags("REF-4", "REF-5", "REF-6", "REF-7")
        },
        "text": text_div("Barangay Malusog Health Centre — sending facility. [DD: REF-4 to REF-7]"),
        "name": "Barangay Malusog Health Centre",    # REF-4
        "identifier": [
            {   # REF-5  NHFR code
                "system": "http://doh.gov.ph/fhir/Identifier/doh-nhfr-code",
                "value": "DOH000-OO-0-0000123",
                "type": {
                    "coding": [{
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "FI"
                    }]
                },
                "use": "official"
            }
        ],
        "address": [            # REF-6
            {
                "use": "work",
                "line": ["123 Health Centre Road"],
                "city": "Quezon City",
                "state": "NCR",
                "postalCode": "1100",
                "country": "PH"
            }
        ],
        "telecom": [            # REF-7
            {
                "system": "phone",
                "value": "+63-2-1234-5678",
                "use": "work"
            }
        ]
    }


def organization_receiving():
    """DD: REF-9, REF-10"""
    return {
        "resourceType": "Organization",
        "id": "organization-receiving-facility-ex",
        "meta": {
            "profile": ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization"],
            "tag": dd_tags("REF-9", "REF-10")
        },
        "text": text_div("Metro Imaging Centre — receiving facility for ultrasound referral. [DD: REF-9, REF-10]"),
        "name": "Metro Imaging Centre",       # REF-9
        "identifier": [
            {   # REF-10
                "system": "http://doh.gov.ph/fhir/Identifier/doh-nhfr-code",
                "value": "DOH000-OO-0-0000456",
                "type": {
                    "coding": [{
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "FI"
                    }]
                },
                "use": "official"
            }
        ]
    }


def practitioner_abraham():
    """DD: REF-1 (registration context)"""
    return {
        "resourceType": "Practitioner",
        "id": "practitioner-abraham-ex",
        "meta": {
            "tag": dd_tags("REF-1")
        },
        "text": text_div("Abraham — registration clerk at Barangay Malusog Health Centre. [DD: REF-1]"),
        "name": [{"family": "Reyes", "given": ["Abraham"]}]
    }


def practitionerrole_abraham():
    """DD: REF-1 (role linkage)"""
    return {
        "resourceType": "PractitionerRole",
        "id": "practitionerrole-abraham-ex",
        "meta": {
            "tag": dd_tags("REF-1")
        },
        "text": text_div("Abraham's role as registration clerk at the sending facility. [DD: REF-1]"),
        "practitioner": {"reference": urn("practitioner-abraham")},
        "organization": {"reference": urn("organization-sending")},
        "code": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
                "code": "clerk",
                "display": "Clerk"
            }],
            "text": "Registration Clerk"
        }]
    }


def practitioner_jane():
    """DD: REF-1 (ANC context)"""
    return {
        "resourceType": "Practitioner",
        "id": "practitioner-jane-ex",
        "meta": {
            "tag": dd_tags("REF-1")
        },
        "text": text_div("Jane — nurse at Barangay Malusog Health Centre providing ANC. [DD: REF-1]"),
        "name": [{"family": "Dela Cruz", "given": ["Jane"]}]
    }


def practitionerrole_jane():
    """DD: REF-1"""
    return {
        "resourceType": "PractitionerRole",
        "id": "practitionerrole-jane-ex",
        "meta": {
            "tag": dd_tags("REF-1")
        },
        "text": text_div("Jane's role as nurse at the sending facility. [DD: REF-1]"),
        "practitioner": {"reference": urn("practitioner-jane")},
        "organization": {"reference": urn("organization-sending")},
        "code": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
                "code": "nurse",
                "display": "Nurse"
            }],
            "text": "Nurse"
        }]
    }


def encounter_registration():
    """DD: REF-43"""
    return {
        "resourceType": "Encounter",
        "id": "encounter-registration-ex",
        "meta": {
            "profile": ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter"],
            "tag": dd_tags("REF-43")
        },
        "text": text_div("Registration encounter — clerk Abraham registers Charity at the health centre. [DD: REF-43]"),
        "status": "finished",
        "class": {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "AMB",
            "display": "ambulatory"
        },
        "type": [{
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "185349003",
                "display": "Encounter for check up"
            }],
            "text": "Registration"
        }],
        "subject": {"reference": urn("patient-charity")},
        "participant": [{
            "individual": {"reference": urn("practitionerrole-abraham")}
        }],
        "serviceProvider": {"reference": urn("organization-sending")},
        "period": {
            "start": "2026-02-24T08:00:00+08:00",
            "end": "2026-02-24T08:15:00+08:00"
        }
    }


def encounter_anc():
    """DD: REF-43"""
    return {
        "resourceType": "Encounter",
        "id": "encounter-anc-ex",
        "meta": {
            "profile": ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter"],
            "tag": dd_tags("REF-43")
        },
        "text": text_div("First ANC contact — nurse Jane conducts counselling, examination, and referral for Charity. [DD: REF-43]"),
        "status": "finished",
        "class": {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "AMB",
            "display": "ambulatory"
        },
        "type": [{
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "424619006",
                "display": "Prenatal initial visit"
            }],
            "text": "First antenatal care contact"
        }],
        "reasonCode": [{
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "77386006",
                "display": "Pregnant"
            }]
        }],
        "subject": {"reference": urn("patient-charity")},
        "participant": [{
            "individual": {"reference": urn("practitionerrole-jane")}
        }],
        "serviceProvider": {"reference": urn("organization-sending")},
        "period": {
            "start": "2026-02-24T08:30:00+08:00",
            "end": "2026-02-24T10:00:00+08:00"
        }
    }


def condition_pregnancy():
    """DD: REF-40"""
    return {
        "resourceType": "Condition",
        "id": "condition-pregnancy-ex",
        "meta": {
            "tag": dd_tags("REF-40")
        },
        "text": text_div("Working impression: Charity is pregnant (confirmed by pregnancy test). Estimated 12–15 weeks gestational age. [DD: REF-40]"),
        "clinicalStatus": {
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                "code": "active",
                "display": "Active"
            }]
        },
        "verificationStatus": {
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                "code": "provisional",
                "display": "Provisional"
            }]
        },
        "code": {
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "77386006",
                "display": "Pregnant"
            }]
        },
        "subject": {"reference": urn("patient-charity")},
        "encounter": {"reference": urn("encounter-anc")},
        "onsetDateTime": "2026-01-01",
        "note": [{"text": "LMP approximately around the New Year holiday; gestational age estimated 12–15 weeks."}]
    }


def observation_chief_complaint():
    """DD: REF-30"""
    return {
        "resourceType": "Observation",
        "id": "observation-chief-complaint-ex",
        "meta": {
            "profile": ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation"],
            "tag": dd_tags("REF-30")
        },
        "text": text_div("Chief complaint: missed menstrual cycle and nausea. [DD: REF-30]"),
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "exam",
                "display": "Exam"
            }]
        }],
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": "10154-3",
                "display": "Chief complaint - Reported"
            }]
        },
        "subject": {"reference": urn("patient-charity")},
        "encounter": {"reference": urn("encounter-anc")},
        "effectiveDateTime": "2026-02-24",
        "valueString": "Missed menstrual cycle and nausea"
    }


def observation_bp():
    """DD: REF-32"""
    return {
        "resourceType": "Observation",
        "id": "observation-blood-pressure-ex",
        "meta": {
            "profile": [
                "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation",
                "http://hl7.org/fhir/StructureDefinition/vitalsigns",
                "http://hl7.org/fhir/StructureDefinition/bp"
            ],
            "tag": dd_tags("REF-32")
        },
        "text": text_div("Blood pressure: 110/70 mmHg — within normal range. [DD: REF-32]"),
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "vital-signs",
                "display": "Vital Signs"
            }]
        }],
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": "85354-9",
                "display": "Blood pressure panel with all children optional"
            }],
            "text": "Blood pressure systolic & diastolic"
        },
        "subject": {"reference": urn("patient-charity")},
        "encounter": {"reference": urn("encounter-anc")},
        "effectiveDateTime": "2026-02-24T09:00:00+08:00",
        "performer": [{"reference": urn("practitioner-jane")}],
        "component": [
            {
                "code": {
                    "coding": [{"system": "http://loinc.org", "code": "8480-6", "display": "Systolic blood pressure"}]
                },
                "valueQuantity": {"value": 110, "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
            },
            {
                "code": {
                    "coding": [{"system": "http://loinc.org", "code": "8462-4", "display": "Diastolic blood pressure"}]
                },
                "valueQuantity": {"value": 70, "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
            }
        ]
    }


def _simple_vital(resource_id, dd_ref, loinc_code, loinc_display, value, unit, ucum_code, description):
    """Helper for simple single-value vital sign observations."""
    return {
        "resourceType": "Observation",
        "id": f"{resource_id}-ex",
        "meta": {
            "profile": [
                "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation",
                "http://hl7.org/fhir/StructureDefinition/vitalsigns"
            ],
            "tag": dd_tags(dd_ref)
        },
        "text": text_div(f"{description} [DD: {dd_ref}]"),
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "vital-signs",
                "display": "Vital Signs"
            }]
        }],
        "code": {
            "coding": [{"system": "http://loinc.org", "code": loinc_code, "display": loinc_display}]
        },
        "subject": {"reference": urn("patient-charity")},
        "encounter": {"reference": urn("encounter-anc")},
        "effectiveDateTime": "2026-02-24T09:00:00+08:00",
        "performer": [{"reference": urn("practitioner-jane")}],
        "valueQuantity": {
            "value": value,
            "unit": unit,
            "system": "http://unitsofmeasure.org",
            "code": ucum_code
        }
    }


def observation_heart_rate():
    """DD: REF-33"""
    return _simple_vital("observation-heart-rate", "REF-33",
                         "8867-4", "Heart rate", 78, "beats/minute", "/min",
                         "Heart rate: 78 bpm.")

def observation_respiratory_rate():
    """DD: REF-34"""
    return _simple_vital("observation-respiratory-rate", "REF-34",
                         "9279-1", "Respiratory rate", 18, "breaths/minute", "/min",
                         "Respiratory rate: 18 /min.")

def observation_oxygen_saturation():
    """DD: REF-35"""
    return _simple_vital("observation-oxygen-saturation", "REF-35",
                         "59408-5", "Oxygen saturation in Arterial blood by Pulse oximetry",
                         98, "%", "%",
                         "Oxygen saturation: 98%.")

def observation_temperature():
    """DD: REF-36"""
    return _simple_vital("observation-temperature", "REF-36",
                         "8310-5", "Body temperature", 36.8, "°C", "Cel",
                         "Body temperature: 36.8 °C.")

def observation_weight():
    """DD: REF-37"""
    return _simple_vital("observation-weight", "REF-37",
                         "29463-7", "Body weight", 55, "kg", "kg",
                         "Body weight: 55 kg.")


def medicationadmin_ifa():
    """DD: REF-38"""
    return {
        "resourceType": "MedicationAdministration",
        "id": "medicationadministration-ifa-ex",
        "meta": {
            "tag": dd_tags("REF-38")
        },
        "text": text_div("Iron and folic acid (IFA) tablets dispensed to Charity for daily intake. [DD: REF-38]"),
        "status": "completed",
        "medicationCodeableConcept": {
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "74935002",
                "display": "Product containing iron and folic acid"
            }],
            "text": "Iron and Folic Acid (IFA) tablets"
        },
        "subject": {"reference": urn("patient-charity")},
        "context": {"reference": urn("encounter-anc")},
        "effectiveDateTime": "2026-02-24",
        "performer": [{
            "actor": {"reference": urn("practitioner-jane")}
        }],
        "dosage": {
            "text": "1 tablet daily",
            "route": {
                "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": "26643006",
                    "display": "Oral route"
                }]
            }
        }
    }


def servicerequest_ultrasound():
    """DD: REF-12, REF-13, REF-15, REF-31"""
    return {
        "resourceType": "ServiceRequest",
        "id": "servicerequest-ultrasound-ex",
        "meta": {
            "tag": dd_tags("REF-12", "REF-13", "REF-15", "REF-31")
        },
        "text": text_div("Referral for obstetric ultrasound at imaging centre — to estimate gestational age before 24 weeks. [DD: REF-12, REF-13, REF-15, REF-31]"),
        "status": "active",
        "intent": "order",
        "priority": "routine",          # REF-13 (outpatient)
        "category": [{                  # REF-15
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "103693007",
                "display": "Diagnostic procedure"
            }],
            "text": "Diagnostics"
        }],
        "code": {
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "268445003",
                "display": "Ultrasound scan - Loss of pregnancy"
            }],
            "text": "Obstetric ultrasound to estimate gestational age"
        },
        "subject": {"reference": urn("patient-charity")},
        "encounter": {"reference": urn("encounter-anc")},
        "authoredOn": "2026-02-24",     # REF-12
        "requester": {"reference": urn("practitionerrole-jane")},
        "performer": [{"reference": urn("organization-receiving")}],
        "reasonReference": [{"reference": urn("condition-pregnancy")}],
        "note": [{                      # REF-31
            "text": "First ANC contact. LMP approximately New Year 2026; gestational age estimated 12–15 weeks. Ultrasound needed before 24 weeks to confirm dates and due date."
        }]
    }


def servicerequest_lab():
    """DD: REF-39 (lab orders — partially covers; results not yet available)"""
    return {
        "resourceType": "ServiceRequest",
        "id": "servicerequest-lab-orders-ex",
        "meta": {
            "tag": dd_tags("REF-39")
        },
        "text": text_div("Lab orders: diabetes screen, hepatitis B, HIV test. Results pending. [DD: REF-39 (partial — orders only, no DiagnosticReport)]"),
        "status": "active",
        "intent": "order",
        "priority": "routine",
        "category": [{
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "108252007",
                "display": "Laboratory procedure"
            }],
            "text": "Laboratory"
        }],
        "code": {
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "15220000",
                "display": "Laboratory test"
            }],
            "text": "Diabetes screen, Hepatitis B surface antigen, HIV test"
        },
        "subject": {"reference": urn("patient-charity")},
        "encounter": {"reference": urn("encounter-anc")},
        "authoredOn": "2026-02-24",
        "requester": {"reference": urn("practitionerrole-jane")},
        "reasonReference": [{"reference": urn("condition-pregnancy")}],
        "note": [{"text": "Ordered during first ANC contact: diabetes screening, hepatitis B, HIV."}]
    }


def task_referral():
    """DD: REF-16, REF-42"""
    return {
        "resourceType": "Task",
        "id": "task-referral-ex",
        "meta": {
            "tag": dd_tags("REF-16", "REF-42")
        },
        "text": text_div("Referral task tracking the ultrasound referral lifecycle. Status: requested (awaiting acceptance by imaging centre). [DD: REF-16, REF-42]"),
        "status": "requested",
        "businessStatus": {
            "coding": [{
                "system": "https://example.com/peref/CodeSystem/referral-disposition",
                "code": "requested",
                "display": "Requested"
            }]
        },
        "intent": "order",
        "focus": {"reference": urn("servicerequest-ultrasound")},
        "for": {"reference": urn("patient-charity")},
        "encounter": {"reference": urn("encounter-anc")},
        "authoredOn": "2026-02-24",
        "requester": {"reference": urn("practitionerrole-jane")},
        "owner": {"reference": urn("organization-receiving")}
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Generating FHIR JSON examples for ANC scenario...\n")

    generators = [
        ("patient-charity-ex.json",                   patient_charity),
        ("relatedperson-companion-ex.json",            relatedperson_companion),
        ("organization-sending-facility-ex.json",      organization_sending),
        ("organization-receiving-facility-ex.json",    organization_receiving),
        ("practitioner-abraham-ex.json",               practitioner_abraham),
        ("practitionerrole-abraham-ex.json",           practitionerrole_abraham),
        ("practitioner-jane-ex.json",                  practitioner_jane),
        ("practitionerrole-jane-ex.json",              practitionerrole_jane),
        ("encounter-registration-ex.json",             encounter_registration),
        ("encounter-anc-ex.json",                      encounter_anc),
        ("condition-pregnancy-ex.json",                condition_pregnancy),
        ("observation-chief-complaint-ex.json",        observation_chief_complaint),
        ("observation-blood-pressure-ex.json",         observation_bp),
        ("observation-heart-rate-ex.json",             observation_heart_rate),
        ("observation-respiratory-rate-ex.json",       observation_respiratory_rate),
        ("observation-oxygen-saturation-ex.json",      observation_oxygen_saturation),
        ("observation-temperature-ex.json",            observation_temperature),
        ("observation-weight-ex.json",                 observation_weight),
        ("medicationadministration-ifa-ex.json",       medicationadmin_ifa),
        ("servicerequest-ultrasound-ex.json",          servicerequest_ultrasound),
        ("servicerequest-lab-orders-ex.json",          servicerequest_lab),
        ("task-referral-ex.json",                      task_referral),
    ]

    for filename, gen_fn in generators:
        write(filename, gen_fn())

    print(f"\n✓ {len(generators)} JSON files written to {OUT_DIR}")
    print("\nDD coverage summary:")
    covered = set()
    for _, gen_fn in generators:
        res = gen_fn()
        for tag in res.get("meta", {}).get("tag", []):
            if tag["system"] == DD_TAG_SYSTEM:
                covered.add(tag["code"])
    all_refs = {f"REF-{i}" for i in range(1, 47)}
    deferred = {"REF-2", "REF-3", "REF-11", "REF-18"}
    not_applicable = {"REF-8", "REF-14", "REF-17", "REF-19", "REF-23", "REF-29", "REF-41", "REF-44", "REF-45", "REF-46"}
    not_covered = all_refs - covered - deferred - not_applicable
    print(f"  Covered:        {len(covered)}/46  {sorted(covered)}")
    print(f"  Deferred:       {len(deferred)}/46  {sorted(deferred)}")
    print(f"  Not applicable: {len(not_applicable)}/46  {sorted(not_applicable)}")
    print(f"  Not covered:    {len(not_covered)}/46  {sorted(not_covered)}")

if __name__ == "__main__":
    main()
