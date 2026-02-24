# Copilot Agent Instructions — PeRef (Philippine eReferral FHIR IG)

## Project Overview

This is an **HL7 FHIR Implementation Guide** built with:
- **FHIR Shorthand (FSH)** / SUSHI for resource authoring (`input/fsh/`)
- **IG Publisher** (`publisher.jar`) for HTML generation
- **PlantUML** diagrams in `input/images-source/` rendered during the IG build
- **GitHub Pages** for publication (`/dev/` = CI, `/X.Y.Z/` = releases)

## PlantUML Diagrams — No Graphviz / Use Smetana

The IG Publisher embeds PlantUML, which normally requires an external **Graphviz `dot`**
executable for class diagrams, object diagrams, component diagrams, and other
non-sequence/non-activity diagram types.

**Do NOT install Graphviz in CI.** Instead, every `.plantuml` file that uses a
dot-dependent diagram type MUST include the pragma:

```plantuml
@startuml <name>
!pragma layout smetana
```

This tells PlantUML to use **Smetana**, a pure-Java port of Graphviz bundled
inside the PlantUML jar. It eliminates the external `dot` dependency entirely.

### Which diagram types need the pragma?

| Needs `!pragma layout smetana` | Does NOT need it |
|-------------------------------|-----------------|
| Class diagrams | Sequence diagrams |
| Object diagrams | Activity diagrams |
| Component diagrams | Mind maps |
| State diagrams | Gantt charts |
| Deployment diagrams | Salt (wireframes) |
| Any diagram using `rectangle`, `card`, `package`, `object`, arrows between them | Swimlane activity diagrams |

### Current diagrams

| File | Type | Smetana? |
|------|------|----------|
| `agile-smart-cycle.plantuml` | Activity diagram | ❌ Not needed |
| `dd-fhir-mapping.plantuml` | Rectangle/mapping diagram | ✅ Yes |
| `resource-class-diagram.plantuml` | Object diagram | ✅ Yes |
| `pipeline-dataflow.plantuml` | Rectangle/dataflow diagram | ✅ Yes |
| `scenario-activity.plantuml` | Activity diagram (swimlanes) | ❌ Not needed |

**When adding new PlantUML diagrams**, check if the diagram type requires dot
(see table above) and add `!pragma layout smetana` right after `@startuml` if so.

Reference: <https://docs-as-co.de/news/plantuml-without-graphviz/>

## GitHub Actions Workflows

- `.github/workflows/ig-ci-dev.yml` — builds on push to `main`, publishes to `/dev/`
- `.github/workflows/ig-release.yml` — builds on `v*` tags, publishes to `/<version>/`

Both workflows use: Node (SUSHI) → Java (IG Publisher) → Ruby (Jekyll).
No Graphviz installation step is needed thanks to Smetana (see above).

## Version Management

- `main` always carries the next dev version with `-draft` suffix (e.g. `0.2.0-draft`)
- Releases are cut by tagging `vX.Y.Z`; the release workflow patches `sushi-config.yaml`
- Published release directories are **immutable** — never overwritten

## Key Directories

| Path | Purpose |
|------|---------|
| `input/fsh/` | FSH source (profiles, examples, aliases) |
| `input/pagecontent/` | Markdown narrative pages |
| `input/images-source/` | PlantUML diagram sources (→ SVG at build time) |
| `input/data-dictionary/` | CSV exports from the Excel data dictionary |
| `input/examples-json-source/` | Generated JSON examples (pre-GoFSH) |
| `utils/` | Python/shell pipeline scripts |