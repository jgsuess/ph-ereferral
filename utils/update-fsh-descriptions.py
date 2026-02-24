#!/usr/bin/env python3
"""
update-fsh-descriptions.py — Add narrative Title/Description to all FSH examples
and rewrite DD-heavy bundle descriptions.

Run from repo root:
    python3 utils/update-fsh-descriptions.py
"""
import re, os

EXAMPLES_DIR = "input/fsh/examples"

# Map of filename -> (Title, Description)
META = {
    "patient-charity-ex.fsh": (
        "Patient — Charity Santos",
        "Charity is a 24-year-old woman from Barangay Malusog, Quezon City, visiting the health centre for the first time during her pregnancy. Abraham registers her demographics, national IDs, and contact details."
    ),
    "practitioner-jane-ex.fsh": (
        "Practitioner — Jane Dela Cruz",
        "Jane is the nurse who conducts Charity's first antenatal care counselling session, records vital signs, and creates the ultrasound referral."
    ),
    "practitioner-abraham-ex.fsh": (
        "Practitioner — Abraham Reyes",
        "Abraham is the registration clerk who creates Charity's patient record at the health centre front desk."
    ),
    "practitionerrole-jane-ex.fsh": (
        "PractitionerRole — Nurse Jane",
        "Jane's role as a nurse at Barangay Malusog Health Centre, linked to her practitioner record and the sending facility."
    ),
    "practitionerrole-abraham-ex.fsh": (
        "PractitionerRole — Clerk Abraham",
        "Abraham's role as a registration clerk at Barangay Malusog Health Centre."
    ),
    "organization-sending-facility-ex.fsh": (
        "Organization — Barangay Malusog Health Centre",
        "The government health centre where Charity is registered and receives her first ANC contact. Identified by its NHFR code."
    ),
    "organization-receiving-facility-ex.fsh": (
        "Organization — Metro Imaging Centre",
        "The external imaging centre where Charity is referred for an obstetric ultrasound to confirm gestational age."
    ),
    "encounter-registration-ex.fsh": (
        "Encounter — Registration",
        "A brief ambulatory encounter (08:00\u201308:15) in which clerk Abraham collects Charity's demographic information and registers her in the system."
    ),
    "encounter-anc-ex.fsh": (
        "Encounter — First Antenatal Care Contact",
        "The counselling session (08:30\u201310:00) in which nurse Jane confirms Charity's pregnancy, records vital signs and clinical history, and initiates the referral."
    ),
    "condition-pregnancy-ex.fsh": (
        "Condition — Pregnancy",
        "Charity's confirmed pregnancy, provisionally dated to a last menstrual period around New Year 2026, giving an estimated gestational age of 12\u201315 weeks."
    ),
    "observation-chief-complaint-ex.fsh": (
        "Observation — Chief Complaint",
        "Charity's reason for visiting the health centre: a missed menstrual cycle and nausea, prompting her to seek antenatal care."
    ),
    "observation-blood-pressure-ex.fsh": (
        "Observation — Blood Pressure",
        "Charity's blood pressure measured during the physical exam: systolic 110 mmHg, diastolic 70 mmHg \u2014 within the normal range for pregnancy."
    ),
    "observation-heart-rate-ex.fsh": (
        "Observation — Heart Rate",
        "Charity's resting heart rate of 78 beats per minute, recorded as part of her vital signs during the ANC contact."
    ),
    "observation-respiratory-rate-ex.fsh": (
        "Observation — Respiratory Rate",
        "Charity's respiratory rate of 18 breaths per minute, within the normal adult range."
    ),
    "observation-oxygen-saturation-ex.fsh": (
        "Observation — Oxygen Saturation",
        "Charity's peripheral oxygen saturation at 98 percent, confirming adequate oxygenation."
    ),
    "observation-temperature-ex.fsh": (
        "Observation — Body Temperature",
        "Charity's body temperature of 36.8 degrees Celsius, a normal reading taken during the physical exam."
    ),
    "observation-weight-ex.fsh": (
        "Observation — Body Weight",
        "Charity's weight of 55 kg, recorded as a baseline measurement at her first ANC contact."
    ),
    "medicationadministration-ifa-ex.fsh": (
        "MedicationAdministration — Iron and Folic Acid",
        "Jane dispenses iron and folic acid (IFA) tablets to Charity with instructions to take one tablet daily, following WHO ANC guidelines for nutritional supplementation."
    ),
    "servicerequest-ultrasound-ex.fsh": (
        "ServiceRequest — Obstetric Ultrasound Referral",
        "Jane refers Charity to Metro Imaging Centre for an obstetric ultrasound to confirm gestational age and due date, needed before 24 weeks of pregnancy."
    ),
    "servicerequest-lab-orders-ex.fsh": (
        "ServiceRequest — Laboratory Orders",
        "Routine ANC laboratory tests ordered for Charity: diabetes screen, hepatitis B surface antigen, and HIV \u2014 in line with WHO recommended investigations."
    ),
    "task-referral-ex.fsh": (
        "Task — Referral Tracking",
        "Tracks the status of Charity's ultrasound referral. Currently in 'requested' state, awaiting acceptance by Metro Imaging Centre."
    ),
    "relatedperson-companion-ex.fsh": (
        "RelatedPerson — Maria Santos (Mother)",
        "Charity's mother Maria, registered as her next-of-kin and alternative contact person during the registration process."
    ),
}

def main():
    count = 0

    # Step 1: Add Title + Description to individual examples
    for fname, (title, desc) in META.items():
        path = os.path.join(EXAMPLES_DIR, fname)
        if not os.path.exists(path):
            print(f"SKIP (not found): {fname}")
            continue
        txt = open(path).read()
        if "Title:" in txt:
            print(f"SKIP (already has Title): {fname}")
            continue
        txt = txt.replace(
            "Usage: #example",
            f'Usage: #example\nTitle: "{title}"\nDescription: "{desc}"',
            1
        )
        open(path, 'w').write(txt)
        count += 1
        print(f"  OK: {fname}")

    # Step 2: Replace DD-heavy bundle descriptions with narrative ones
    BUNDLE_DESCS = {
        "registration-transaction-ex.fsh": (
            'Description: """\n'
            "  Clerk Abraham registers Charity at Barangay Malusog Health Centre.\n"
            "  This bundle captures everything recorded at the front desk: Charity's\n"
            "  demographic details, her national identifiers (PhilSys and PhilHealth),\n"
            "  her home address and phone number, and her mother Maria as next-of-kin.\n"
            "  It also records Abraham's practitioner role and the registration encounter.\n"
            '"""'
        ),
        "anc-contact-transaction-ex.fsh": (
            'Description: """\n'
            "  Nurse Jane conducts Charity's first antenatal care visit at\n"
            "  Barangay Malusog Health Centre. This bundle captures the full clinical\n"
            "  encounter: pregnancy confirmation, vital signs, chief complaint,\n"
            "  iron-and-folic-acid dispensing, laboratory orders, and the ultrasound\n"
            "  referral to Metro Imaging Centre \u2014 along with the task that tracks the\n"
            "  referral outcome.\n"
            '"""'
        ),
    }

    for bname, new_desc in BUNDLE_DESCS.items():
        path = os.path.join(EXAMPLES_DIR, bname)
        txt = open(path).read()
        txt = re.sub(r'Description: """.*?"""', new_desc, txt, flags=re.DOTALL)
        open(path, 'w').write(txt)
        count += 1
        print(f"  OK bundle: {bname}")

    print(f"\nDone. Updated {count} files.")

if __name__ == "__main__":
    main()
