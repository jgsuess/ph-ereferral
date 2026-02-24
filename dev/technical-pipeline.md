# Technical Pipeline - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* **Technical Pipeline**

## Technical Pipeline

### Technical Pipeline

This page describes the end-to-end data flow from source artefacts to a published Implementation Guide. For context on the source artefacts and the WHO SMART framework layers, see the [Approach](approach.md) page.

The diagram below summarises the pipeline.

#### Step-by-step

The table below lists each stage of the pipeline, the script or tool used, and the artefacts it consumes and produces.

| | | | |
| :--- | :--- | :--- | :--- |
| **1. Extract data dictionary** | `utils/extract-data-dictionary.py`(Python + openpyxl) | Excel workbook (`.xlsx`) | CSV files in`input/data-dictionary/` |
| **2. Generate JSON skeletons** | `utils/generate-json-from-dd.py` | CSV + scenario narrative | 22 annotated FHIR R4 JSON files in`input/examples-json-source/` |
| **3. Validate JSON** | `utils/validate-all.sh`→`utils/fhir-validate.py` | JSON files + FHIR server | Validation result summaries |
| **4. Convert to FSH** | `utils/convert-to-fsh.sh`→`gofsh` | Validated JSON files | 22 FSH instance files in`input/fsh/examples/` |
| **5. Author bundles** | Manual (FSH) | Individual FSH instances | `registration-transaction-ex.fsh`,`anc-contact-transaction-ex.fsh` |
| **6. Add narrative descriptions** | `utils/update-fsh-descriptions.py` | FSH instance files | FSH files with`Title:`and`Description:`added |
| **7. Generate DD mapping page** | `utils/generate-dd-mapping-page.py` | `dd-coverage.csv` | `input/pagecontent/dd-mapping.md`(pivot tables + narrative) |
| **8. Compile IG** | `sushi .` | All FSH sources + ph-core dependency | `fsh-generated/resources/*.json`(24 resources) |
| **9. Publish IG** | `_genonce.sh`→ IG Publisher | SUSHI output +`publisher.jar` | `output/`(HTML site) |

#### DD Coverage Tracking

To ensure every data-dictionary element is accounted for, each JSON example resource is annotated with `meta.tag` entries that reference the element IDs it satisfies:

```
"meta": {
  "tag": [
    { "system": "https://example.com/peref-dd", "code": "REF-20", "display": "REF-20" },
    { "system": "https://example.com/peref-dd", "code": "REF-21", "display": "REF-21" }
  ]
}

```

A companion script (`utils/update-dd-coverage.py`) scans all JSON examples and regenerates `input/data-dictionary/dd-coverage.csv`, producing this summary:

| | | |
| :--- | :--- | :--- |
| **Covered** | 31 | Fully represented in at least one example resource |
| **Partial** | 1 | REF-39 (lab results) — orders created but no DiagnosticReport yet |
| **Deferred** | 4 | REF-2, REF-3 (signature — Future Release), REF-11 (HCPN — On-Hold), REF-18 (return slip — Excluded from MVP) |
| **Not applicable** | 10 | Elements not relevant to this ANC scenario (e.g. transport mode, receiving encounter, navigators) |

**100 % of applicable elements are covered.**

For the element-by-element breakdown, see the [DD Mapping](dd-mapping.md) page.

