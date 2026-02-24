#!/usr/bin/env python3
"""
generate-dd-mapping-page.py — Generate input/pagecontent/dd-mapping.md

Reads dd-coverage.csv and PeRef_Logical_Information_Model.csv to produce:
  1. One pivot table per clinical information group (DD elements × example files)
  2. Narrative mapping descriptions for each element

Usage:
    cd <repo-root>
    python3 utils/generate-dd-mapping-page.py
"""
import csv
import pathlib
import textwrap

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
COVERAGE_CSV = REPO_ROOT / "input" / "data-dictionary" / "dd-coverage.csv"
OUTPUT_MD = REPO_ROOT / "input" / "pagecontent" / "dd-mapping.md"

# ── Narrative descriptions per element ──────────────────────────────────────
# Each entry provides a human-friendly explanation of *why* the DD element
# maps to a particular FHIR resource/element, using scenario persona names.
NARRATIVES = {
    "REF-1": (
        "The printed name of the referring health professional is stored in a "
        "**Practitioner** resource and linked to the facility through a "
        "**PractitionerRole**. In our scenario clerk Abraham creates Charity's "
        "record during registration (Bundle\u00a0A), while nurse Jane authors the "
        "referral during the ANC contact (Bundle\u00a0B). Both practitioners appear "
        "with their own Practitioner and PractitionerRole instances."
    ),
    "REF-2": (
        "A digital or scanned professional signature would be captured in a "
        "**Provenance** resource attached to the ServiceRequest. This element "
        "is deferred to a future release because the CDG has not yet decided "
        "whether the MVP requires electronic signatures or whether a typed "
        "name with a system timestamp is sufficient attestation."
    ),
    "REF-3": (
        "The date and time of the professional\u2019s signature is intended for "
        "**Provenance.occurredDateTime**. Like REF\u20112, it is deferred\u00a0\u2014 the "
        "system can auto-stamp submission time as a fallback."
    ),
    "REF-4": (
        "The official name of the referring (sending) facility is recorded in "
        "**Organization.name**. In our scenario this is \u201cBarangay Malusog "
        "Health Centre\u201d, the government clinic where Charity is registered."
    ),
    "REF-5": (
        "The DOH National Health Facility Registry (NHFR) code uniquely "
        "identifies the sending facility. It is stored in "
        "**Organization.identifier** using the PH-Core NHFR identifier slice, "
        "enabling automated routing and facility look-up."
    ),
    "REF-6": (
        "The sending facility\u2019s address is captured in **Organization.address** "
        "using the PH-Core structured address format (with barangay, city, "
        "province). It is optional when the address can be retrieved from the "
        "NHFR directory."
    ),
    "REF-7": (
        "The facility\u2019s contact phone number is stored in "
        "**Organization.telecom** (system\u00a0=\u00a0phone). This supports coordination "
        "between sending and receiving facilities."
    ),
    "REF-8": (
        "The name of the staff member who acknowledges or accepts the referral "
        "at the receiving facility. Mapped to **Communication.recipient**, but "
        "not applicable during referral creation\u00a0\u2014 the receiving person is only "
        "known after acceptance. Not modelled in this ANC scenario."
    ),
    "REF-9": (
        "The name of the intended receiving facility is stored in a separate "
        "**Organization** resource. In our scenario this is \u201cMetro Imaging "
        "Centre\u201d, the external facility where Charity is referred for an "
        "obstetric ultrasound."
    ),
    "REF-10": (
        "The NHFR code of the receiving facility, stored in "
        "**Organization.identifier** (system\u00a0=\u00a0NHFR). This is conditional\u00a0\u2014 "
        "required once the receiving facility is confirmed."
    ),
    "REF-11": (
        "The Health Care Provider Network (HCPN) name is the umbrella "
        "referral network. Mapped to a separate **Organization.name**, but "
        "currently on hold pending a CDG decision on whether it should be "
        "computed or manually entered."
    ),
    "REF-12": (
        "The date the referral was created is captured in "
        "**ServiceRequest.authoredOn**. In our scenario this is "
        "2026-02-24, the date of Charity\u2019s first ANC contact when nurse Jane "
        "initiates the ultrasound referral."
    ),
    "REF-13": (
        "The referral category indicates urgency: emergency or "
        "outpatient/routine. It maps to **ServiceRequest.priority** using "
        "the FHIR `request-priority` value set (emergency\u00a0\u2192\u00a0`stat`, "
        "outpatient\u00a0\u2192\u00a0`routine`). Charity\u2019s referral is routine."
    ),
    "REF-14": (
        "The date and time when the sending facility called the receiving "
        "facility. Mapped to **Communication.sent**. Not applicable in this "
        "scenario\u00a0\u2014 Charity\u2019s referral is routine and does not require a "
        "phone call."
    ),
    "REF-15": (
        "The classification of the requested service (e.g.\u00a0Diagnostics, "
        "Consultation). Stored in **ServiceRequest.category** using SNOMED\u00a0CT "
        "codes. For Charity\u2019s ultrasound referral the category is "
        "\u201cDiagnostic procedure\u201d."
    ),
    "REF-16": (
        "The action point confirming receipt of the referral by the receiving "
        "facility. Modelled through **Task.status** (accepted) combined with "
        "**Task.note** for timestamped annotations. In our example the Task "
        "is currently in `requested` state, awaiting acceptance."
    ),
    "REF-17": (
        "When a referral is redirected to another facility a new **Task** is "
        "created and linked via `Task.basedOn`. Not applicable in this "
        "scenario\u00a0\u2014 Charity\u2019s referral is not forwarded."
    ),
    "REF-18": (
        "A return referral slip or back-referral summary would be attached as "
        "a **DocumentReference**. Excluded from the MVP per CDG consensus."
    ),
    "REF-19": (
        "The communication channel (phone, email, SMS) and reference used for "
        "referral coordination, captured in **Communication.category**, "
        "**medium**, and **note**. Not applicable\u00a0\u2014 Charity\u2019s is a routine "
        "outpatient referral."
    ),
    "REF-20": (
        "Charity\u2019s full legal name is recorded in **Patient.name** using "
        "the HumanName data type (family\u00a0=\u00a0\u201cSantos\u201d, given\u00a0=\u00a0\u201cCharity\u201d). "
        "This is the primary way the patient is identified across all "
        "subsequent resources."
    ),
    "REF-21": (
        "Charity\u2019s administrative gender (`female`) is captured in "
        "**Patient.gender** using the HL7 AdministrativeGender code system."
    ),
    "REF-22": (
        "Charity\u2019s date of birth (2001-08-15) is stored in "
        "**Patient.birthDate**. Age can be computed from this value, avoiding "
        "the need to persist it separately."
    ),
    "REF-23": (
        "Age is a derived value computed from the patient\u2019s birth date. "
        "Following the data dictionary recommendation it is **not persisted** "
        "as a separate resource\u00a0\u2014 systems should calculate it on the fly."
    ),
    "REF-24": (
        "Charity\u2019s Philippine Identification System (PhilSys) national ID is "
        "stored in **Patient.identifier** using the PH-Core PhilSys identifier "
        "slice. This supports patient matching across facilities."
    ),
    "REF-25": (
        "Charity\u2019s PhilHealth membership number is recorded in "
        "**Patient.identifier** using the PH-Core PhilHealth identifier slice, "
        "enabling insurance verification and claims linkage."
    ),
    "REF-26": (
        "Charity\u2019s home address in Barangay Malusog, Quezon City is captured "
        "in **Patient.address** using the PH-Core structured address format "
        "with barangay-level detail."
    ),
    "REF-27": (
        "Charity\u2019s mobile phone number is stored in **Patient.telecom** "
        "(system\u00a0=\u00a0phone, use\u00a0=\u00a0mobile), providing a direct contact channel."
    ),
    "REF-28": (
        "Charity\u2019s mother Maria is recorded as a **RelatedPerson** with "
        "relationship\u00a0=\u00a0\u201cMother\u201d, including her name and mobile number. "
        "This serves as the alternative contact and next-of-kin record."
    ),
    "REF-29": (
        "The patient\u2019s PWD (Person with Disability) registration status would "
        "be stored in a **Patient extension**. Not applicable in this "
        "scenario; the DD has an open question on whether to capture status "
        "only or also the PWD ID."
    ),
    "REF-30": (
        "Charity\u2019s chief complaint\u00a0\u2014 a missed menstrual cycle and nausea\u00a0\u2014 is "
        "captured in an **Observation** coded with LOINC\u00a010154-3 "
        "(\u201cChief complaint\u00a0\u2013 Reported\u201d) and a free-text value string."
    ),
    "REF-31": (
        "Pertinent clinical history is recorded as a narrative note in "
        "**ServiceRequest.note**. For Charity this includes her LMP estimate "
        "and the rationale for the ultrasound referral."
    ),
    "REF-32": (
        "Charity\u2019s blood pressure (110/70\u00a0mmHg) is captured using the FHIR "
        "blood pressure panel profile (**Observation** with LOINC\u00a085354-9), "
        "with separate components for systolic (8480-6) and diastolic (8462-4)."
    ),
    "REF-33": (
        "Charity\u2019s heart rate of 78\u00a0bpm is recorded as an **Observation** "
        "coded with LOINC\u00a08867-4, conforming to the FHIR vital signs profile."
    ),
    "REF-34": (
        "Charity\u2019s respiratory rate of 18\u00a0breaths per minute is stored in an "
        "**Observation** (LOINC\u00a09279-1), part of the standard vital signs set."
    ),
    "REF-35": (
        "Charity\u2019s oxygen saturation of 98\u00a0% is captured in an **Observation** "
        "(LOINC\u00a059408-5), confirming adequate oxygenation."
    ),
    "REF-36": (
        "Charity\u2019s body temperature of 36.8\u00a0\u00b0C is recorded in an "
        "**Observation** (LOINC\u00a08310-5), a normal reading from the physical "
        "exam."
    ),
    "REF-37": (
        "Charity\u2019s body weight of 55\u00a0kg is stored as an **Observation** "
        "(LOINC\u00a029463-7), providing a baseline measurement for her pregnancy."
    ),
    "REF-38": (
        "Nurse Jane dispenses iron and folic acid (IFA) tablets to Charity, "
        "captured in a **MedicationAdministration** resource coded with "
        "SNOMED\u00a0CT\u00a074935002. The dosage instructions (one tablet daily, oral) "
        "follow WHO ANC supplementation guidelines."
    ),
    "REF-39": (
        "Routine ANC laboratory tests (diabetes screen, hepatitis\u00a0B, HIV) "
        "are ordered via a **ServiceRequest**. Coverage is partial because "
        "only the orders exist\u00a0\u2014 a **DiagnosticReport** with results will be "
        "added when the receiving lab returns findings."
    ),
    "REF-40": (
        "Charity\u2019s working clinical impression\u00a0\u2014 pregnancy (SNOMED\u00a0CT "
        "77386006)\u00a0\u2014 is recorded as a **Condition** with provisional "
        "verification status. It is referenced from "
        "`ServiceRequest.reasonReference` to link the diagnosis to the "
        "ultrasound referral."
    ),
    "REF-41": (
        "Transport mode or ambulance details would be captured as a "
        "**Task extension**. Not applicable here\u00a0\u2014 Charity\u2019s is a routine "
        "outpatient referral with self-transport."
    ),
    "REF-42": (
        "The referral response/decision is tracked through "
        "**Task.businessStatus** using the `referral-disposition` code system. "
        "In our example the task is in `requested` status, awaiting acceptance "
        "by Metro Imaging Centre."
    ),
    "REF-43": (
        "Two **Encounter** resources provide the clinical context: a "
        "registration encounter (08:00\u201308:15, clerk Abraham) and an ANC "
        "contact encounter (08:30\u201310:00, nurse Jane). Both use the PH-Core "
        "Encounter profile."
    ),
    "REF-44": (
        "A receiving encounter would be created when Charity arrives at "
        "Metro Imaging Centre. It belongs to the receiving facility\u2019s workflow "
        "and is not part of this sending scenario."
    ),
    "REF-45": (
        "A navigator role at the receiving facility or PHU would be captured "
        "as a **PractitionerRole** with a navigator code. Not applicable in "
        "this scenario."
    ),
    "REF-46": (
        "A navigator role at the referring facility would similarly be a "
        "**PractitionerRole**. Not applicable in this scenario."
    ),
}

# ── Clinical Information Group ordering and friendly labels ─────────────────
GROUP_ORDER = [
    "01 Sending Practitioner (requestor)",
    "02 Sending Facility (requestor)",
    "03 Receiving Practitioner",
    "03 Recieving Practitioner",          # handle typo in source CSV
    "04 Receiving Facility",
    "05 Referral Request",
    "06 Patient Demographics",
    "07 Clinical Information",
]

GROUP_LABELS = {
    "01 Sending Practitioner (requestor)": "Sending Practitioner",
    "02 Sending Facility (requestor)":     "Sending Facility",
    "03 Receiving Practitioner":           "Receiving Practitioner",
    "03 Recieving Practitioner":           "Receiving Practitioner",
    "04 Receiving Facility":               "Receiving Facility",
    "05 Referral Request":                 "Referral Request",
    "06 Patient Demographics":             "Patient Demographics",
    "07 Clinical Information":             "Clinical Information",
}

EXTRA_GROUP_LABEL = "System, Logistics & Workflow"

STATUS_ICON = {
    "covered":     "\u2705",
    "partial":     "\u26a0\ufe0f",
    "deferred":    "\U0001f550",
    "not-covered": "\u2014",
}

# ── Helpers ─────────────────────────────────────────────────────────────────

def short_name(filename):
    """Convert 'patient-charity-ex.json' → 'Patient Charity'."""
    name = filename.replace("-ex.json", "").replace("-ex", "")
    parts = name.split("-")
    return " ".join(p.capitalize() for p in parts)


def load_coverage():
    """Load dd-coverage.csv rows."""
    with open(COVERAGE_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def collect_example_files_for_rows(rows):
    """Return a sorted, deduplicated list of example files used by these rows."""
    files = set()
    for row in rows:
        for f in row.get("Example File", "").split("; "):
            f = f.strip()
            if f:
                files.add(f)
    return sorted(files)


def group_rows(rows):
    """Group rows by clinical information group, preserving order."""
    groups = {}
    for row in rows:
        g = row.get("Clinical Information Group", "").strip()
        matched = False
        for key in GROUP_ORDER:
            if g == key or GROUP_LABELS.get(g) == GROUP_LABELS.get(key):
                label = GROUP_LABELS[key]
                groups.setdefault(label, []).append(row)
                matched = True
                break
        if not matched:
            groups.setdefault(EXTRA_GROUP_LABEL, []).append(row)
    ordered = []
    seen = set()
    for key in GROUP_ORDER:
        label = GROUP_LABELS.get(key, key)
        if label not in seen and label in groups:
            ordered.append((label, groups[label]))
            seen.add(label)
    if EXTRA_GROUP_LABEL in groups:
        ordered.append((EXTRA_GROUP_LABEL, groups[EXTRA_GROUP_LABEL]))
    return ordered


# ── Clinical Information sub-groups ─────────────────────────────────────────
# The Clinical Information group has 11 elements; split into smaller tables.

CLINICAL_SUBGROUPS = [
    (
        "Chief Complaint & Clinical History",
        {"REF-30", "REF-31"},
    ),
    (
        "Vital Signs",
        {"REF-32", "REF-33", "REF-34", "REF-35", "REF-36", "REF-37"},
    ),
    (
        "Treatment, Orders & Working Impression",
        {"REF-38", "REF-39", "REF-40"},
    ),
]


def split_clinical_group(rows):
    """Split the Clinical Information rows into sub-groups."""
    sub = []
    for label, ids in CLINICAL_SUBGROUPS:
        sub_rows = [r for r in rows if r["Element ID"] in ids]
        if sub_rows:
            sub.append((label, sub_rows))
    return sub


# ── Table builders ──────────────────────────────────────────────────────────

def build_pivot_table(rows, all_files=None):
    """Build a Markdown pivot table for a set of DD elements."""
    if all_files is None:
        relevant_files = collect_example_files_for_rows(rows)
    else:
        # Filter to files actually referenced by these rows
        relevant_files = []
        for f in all_files:
            for row in rows:
                example_files = [
                    x.strip()
                    for x in row.get("Example File", "").split("; ")
                    if x.strip()
                ]
                if f in example_files:
                    relevant_files.append(f)
                    break

    # If no files are relevant (all deferred / not-covered), simple table
    if not relevant_files:
        lines = []
        lines.append("| Element | Data Element | FHIR Resource | Status |")
        lines.append("|---------|-------------|---------------|:------:|")
        for row in rows:
            eid = row["Element ID"]
            name = row.get("Data Element", "")
            fres = row.get("FHIR Resource", "")
            icon = STATUS_ICON.get(row.get("Coverage Status", ""), "\u2014")
            lines.append(f"| {eid} | {name} | {fres} | {icon} |")
        return "\n".join(lines)

    # Full pivot table
    lines = []
    header = "| Element | Data Element | "
    header += " | ".join(short_name(f) for f in relevant_files)
    header += " |"
    lines.append(header)

    sep = "|---------|-------------|"
    sep += "|".join(":---:" for _ in relevant_files)
    sep += "|"
    lines.append(sep)

    for row in rows:
        eid = row["Element ID"]
        name = row.get("Data Element", "")
        status = row.get("Coverage Status", "")
        example_files = [
            x.strip()
            for x in row.get("Example File", "").split("; ")
            if x.strip()
        ]

        cells = f"| {eid} | {name} | "
        for f in relevant_files:
            if f in example_files:
                cells += "\u26a0\ufe0f" if status == "partial" else "\u2705"
            elif status == "deferred":
                cells += "\U0001f550"
            elif status == "not-covered":
                cells += "\u2014"
            else:
                cells += " "
            cells += " | "
        lines.append(cells)

    return "\n".join(lines)


def build_narrative_section(rows):
    """Build narrative mapping descriptions for a set of DD elements."""
    lines = []
    for row in rows:
        eid = row["Element ID"]
        name = row.get("Data Element", "")
        fhir_elem = row.get("FHIR Element (R4)", "")
        fhir_res = row.get("FHIR Resource", "")
        status = row.get("Coverage Status", "")

        narrative = NARRATIVES.get(eid, "")
        if not narrative:
            narrative = f"Maps to `{fhir_elem}` on the {fhir_res} resource."

        status_label = {
            "covered":     "Covered",
            "partial":     "Partially covered",
            "deferred":    "Deferred",
            "not-covered": "Not covered in this scenario",
        }.get(status, status)

        lines.append(f"**{eid} \u2014 {name}** *({status_label})*")
        lines.append(f":   {narrative}")
        if fhir_elem:
            lines.append(f":   FHIR path: `{fhir_elem}`")
        lines.append("")
    return "\n".join(lines)


# ── Main generation logic ──────────────────────────────────────────────────

def generate_page():
    rows = load_coverage()
    grouped = group_rows(rows)

    md = []

    # ── Page header ─────────────────────────────────────────────────────────
    md.append(textwrap.dedent("""\
        ### Data Dictionary to FHIR Mapping

        This page provides a detailed, element-by-element mapping between the
        **PeRef Logical Information Model** (the data dictionary) and the FHIR
        example resources published in this Implementation Guide.

        The content is organised by **clinical information group**. For each group
        you will find:

        1. A **pivot table** showing which example resource covers which
           data-dictionary element.
        2. A **narrative description** explaining how and why each element is
           represented in FHIR, told through the lens of the ANC scenario
           (Charity, Abraham, Jane).

        **Legend**

        | Icon | Meaning |
        |:----:|---------|
        | \u2705 | Fully covered by the example |
        | \u26a0\ufe0f | Partially covered \u2014 additional resources needed |
        | \U0001f550 | Deferred to a future release |
        | \u2014 | Not applicable to this scenario |

        > **Note:** This page is generated from `dd-coverage.csv` by the script
        > `utils/generate-dd-mapping-page.py`.  Re-run the script after updating
        > the data dictionary to keep this page in sync.

        ---
    """))

    # ── Coverage summary ────────────────────────────────────────────────────
    counts = {}
    for row in rows:
        s = row.get("Coverage Status", "unknown")
        counts[s] = counts.get(s, 0) + 1

    total = len(rows)
    md.append("#### Coverage Summary\n")
    md.append(f"Out of **{total}** data-dictionary elements:\n")
    md.append("| Status | Count | Meaning |")
    md.append("|--------|------:|---------|")
    md.append(f"| \u2705 Covered | {counts.get('covered', 0)} "
              f"| Fully represented in at least one example |")
    md.append(f"| \u26a0\ufe0f Partial | {counts.get('partial', 0)} "
              f"| Modelled as orders; results resource still needed |")
    md.append(f"| \U0001f550 Deferred | {counts.get('deferred', 0)} "
              f"| Postponed to a future release per CDG consensus |")
    md.append(f"| \u2014 Not covered | {counts.get('not-covered', 0)} "
              f"| Not applicable to this ANC scenario |")
    md.append("")
    md.append("---\n")

    # ── Per-group sections ──────────────────────────────────────────────────
    for group_label, group_rows_list in grouped:
        # Clinical Information is split into sub-groups for readability
        if group_label == "Clinical Information":
            md.append(f"#### {group_label}\n")
            md.append(
                "This group covers the clinical observations, treatments and "
                "diagnostic information recorded during Charity\u2019s first ANC "
                "contact. Because the group contains many elements it is split "
                "into three sub-tables.\n"
            )
            for sub_label, sub_rows in split_clinical_group(group_rows_list):
                md.append(f"##### {sub_label}\n")
                md.append(build_pivot_table(sub_rows))
                md.append("")
                md.append(build_narrative_section(sub_rows))
                md.append("")
            md.append("---\n")
        else:
            md.append(f"#### {group_label}\n")
            md.append(build_pivot_table(group_rows_list))
            md.append("")
            md.append(build_narrative_section(group_rows_list))
            md.append("---\n")

    # Write
    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"Generated: {OUTPUT_MD}")
    print(f"  {len(rows)} DD elements across {len(grouped)} groups")


if __name__ == "__main__":
    generate_page()
