#!/usr/bin/env python3
"""
Generate / update the DD coverage report from actual JSON example files.

Reads all *-ex.json in input/examples/ and extracts DD element tags
(meta.tag with system = https://example.com/peref-dd), then updates
input/data-dictionary/dd-coverage.csv and prints a summary.

Usage:
    cd <repo-root>
    .venv/bin/python utils/update-dd-coverage.py
"""
import csv
import json
import glob
import os
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EXAMPLES_DIR = REPO_ROOT / "input" / "examples-json-source"
COVERAGE_CSV = REPO_ROOT / "input" / "data-dictionary" / "dd-coverage.csv"
DD_TAG_SYSTEM = "https://example.com/peref-dd"

# All DD elements
ALL_REFS = [f"REF-{i}" for i in range(1, 47)]

# Elements deferred per DD status (Future Release / On-Hold / Excluded from MVP)
DEFERRED = {"REF-2", "REF-3", "REF-11", "REF-18"}

# Elements not applicable to this scenario
NOT_APPLICABLE = {
    "REF-8",   # Receiving personnel — not known at creation
    "REF-14",  # Time called — routine referral, no call
    "REF-17",  # Forwarded — no forwarding in this scenario
    "REF-19",  # Call/email reference — routine referral
    "REF-23",  # Age computed — derived from DOB, not persisted
    "REF-29",  # PWD registration — not applicable
    "REF-41",  # Transport mode — outpatient self-transport
    "REF-44",  # Receiving encounter — not in sending scenario
    "REF-45",  # Navigator receiving — not applicable
    "REF-46",  # Navigator referring — not applicable
}

# Partial coverage notes
PARTIAL = {
    "REF-39": "Lab orders created as ServiceRequest; no DiagnosticReport with results yet",
}

def scan_json_examples():
    """Scan all *-ex.json files and return {ref_id: [list_of_files]}."""
    ref_to_files = {}
    for json_path in sorted(glob.glob(str(EXAMPLES_DIR / "*-ex.json"))):
        with open(json_path) as f:
            resource = json.load(f)
        tags = resource.get("meta", {}).get("tag", [])
        filename = os.path.basename(json_path)
        for tag in tags:
            if tag.get("system") == DD_TAG_SYSTEM:
                ref_id = tag["code"]
                ref_to_files.setdefault(ref_id, []).append(filename)
    return ref_to_files


def determine_bundle(ref_id, files):
    """Determine which bundle(s) an element appears in."""
    bundles = set()
    for f in files:
        if any(x in f for x in ["abraham", "registration", "patient-charity", "relatedperson", "organization-sending"]):
            bundles.add("A")
        if any(x in f for x in ["jane", "anc", "condition", "observation", "medication", "servicerequest", "task", "organization-receiving"]):
            bundles.add("B")
    # Some resources appear in both (e.g., sending org referenced by both bundles)
    if not bundles:
        bundles.add("—")
    return "+".join(sorted(bundles))


def main():
    ref_to_files = scan_json_examples()

    # Read existing CSV to preserve DD metadata columns
    existing = {}
    if COVERAGE_CSV.exists():
        with open(COVERAGE_CSV, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing[row["Element ID"]] = row

    # Build updated rows
    rows = []
    for ref_id in ALL_REFS:
        old = existing.get(ref_id, {})
        files = ref_to_files.get(ref_id, [])

        if ref_id in DEFERRED:
            status = "deferred"
        elif ref_id in NOT_APPLICABLE:
            status = "not-covered"
        elif ref_id in PARTIAL:
            status = "partial"
        elif files:
            status = "covered"
        else:
            status = "not-covered"

        notes = old.get("Notes", "")
        if ref_id in PARTIAL:
            notes = PARTIAL[ref_id]
        elif ref_id in DEFERRED:
            existing_note = old.get("Notes", "")
            if existing_note and not existing_note.startswith("Deferred"):
                notes = f"Deferred — {existing_note}"
            elif not existing_note:
                notes = "Deferred — Future Release / On-Hold per DD"
            # else keep existing note as-is
        elif ref_id in NOT_APPLICABLE and not notes:
            notes = "Not applicable to this ANC scenario"

        rows.append({
            "Element ID": ref_id,
            "Data Element": old.get("Data Element", ""),
            "Clinical Information Group": old.get("Clinical Information Group", ""),
            "FHIR Resource": old.get("FHIR Resource", ""),
            "FHIR Element (R4)": old.get("FHIR Element (R4)", ""),
            "CDG Status": old.get("CDG Status", ""),
            "DD Required": old.get("DD Required", ""),
            "Example File": "; ".join(files) if files else "",
            "Bundle": determine_bundle(ref_id, files) if files else "—",
            "Coverage Status": status,
            "Notes": notes,
        })

    # Write CSV
    fieldnames = ["Element ID", "Data Element", "Clinical Information Group",
                  "FHIR Resource", "FHIR Element (R4)", "CDG Status", "DD Required",
                  "Example File", "Bundle", "Coverage Status", "Notes"]
    with open(COVERAGE_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Print summary
    counts = {"covered": 0, "partial": 0, "deferred": 0, "not-covered": 0}
    for r in rows:
        counts[r["Coverage Status"]] = counts.get(r["Coverage Status"], 0) + 1

    print("=== DD Coverage Report ===")
    print(f"  Total elements:  {len(ALL_REFS)}")
    print(f"  Covered:         {counts['covered']}")
    print(f"  Partial:         {counts['partial']}")
    print(f"  Deferred:        {counts['deferred']}")
    print(f"  Not covered:     {counts['not-covered']}")
    print(f"  Coverage rate:   {(counts['covered'] + counts['partial']) / len(ALL_REFS) * 100:.0f}%")
    print(f"  (excl. deferred + N/A): {(counts['covered'] + counts['partial']) / (len(ALL_REFS) - counts['deferred'] - len(NOT_APPLICABLE)) * 100:.0f}%")
    print(f"\nUpdated: {COVERAGE_CSV}")

    # Detailed listing
    print("\n--- By Status ---")
    for status in ("covered", "partial", "deferred", "not-covered"):
        refs = [r["Element ID"] for r in rows if r["Coverage Status"] == status]
        if refs:
            print(f"\n  {status.upper()} ({len(refs)}):")
            for ref in refs:
                r = next(x for x in rows if x["Element ID"] == ref)
                files_str = r["Example File"] or "(none)"
                print(f"    {ref}: {r['Data Element'] or '?'} → {files_str}")


if __name__ == "__main__":
    main()
