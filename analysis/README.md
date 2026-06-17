# PH eReferral v0.1 — Specification Holes and Counter-Intuitive Sequences

This directory documents gaps, ambiguities, and modeling issues found in the
PH eReferral v0.1 specification. It is intended as input to the Clinical Design
Group and the IG authoring team, not as normative content.

## Contents

| File | What it covers |
|------|---------------|
| [spec-holes.md](spec-holes.md) | Full catalogue of 18 specification holes across 5 categories, with analysis, consequences, and worked examples. |
| [diagrams/](diagrams/) | PlantUML source files for the diagrams embedded in `spec-holes.md`. |
| [fsh/AbsurdSequences.fsh](fsh/AbsurdSequences.fsh) | FHIR Shorthand instances that are **profile-conformant** but represent counter-intuitive or clinically dangerous states. Each compiles cleanly with `sushi` if placed in `input/fsh/examples/`. |
| [testscripts/](testscripts/) | Narrative TestScript scenarios — sequences of FHIR operations that exercise each hole. Designed to complement the `upstream/80-workflow-state-machine` test infrastructure. |

## Relationship to the upstream state-machine branch

The `upstream/80-workflow-state-machine` branch adds `tests/state-model/referral-workflow-state-machine.yaml` and a `fhir-frog`-driven test infrastructure. That work defines the **intended** state machine and generates conformant TestScripts for the happy path and main rejection/onward paths.

This analysis directory takes the opposite approach: it describes sequences that **the state machine forbids but the FHIR profiles permit**. The gap between the two is where implementers will disagree, servers will diverge, and data quality will erode in production.

## Summary of holes

| Category | Holes | Core problem |
|----------|-------|--------------|
| A — State machine transition gaps | A-01 to A-05 | No forward-only or sequential-order invariants; states exist in the model that are never reachable |
| B — Dual-resource incoherence | B-01 to B-03 | ServiceRequest and Task can move to contradictory states independently |
| C — Semantic contradictions | C-01 to C-04 | Fields within a single Task can carry mutually exclusive values |
| D — Cardinality / optionality gaps | D-01 to D-03 | Required-feeling fields are optional; nothing prevents duplicates |
| E — Lifecycle gaps | E-01 to E-03 | No back-referral model; terminal states are semantically ambiguous |

## How to reproduce

To verify that the FSH examples are profile-conformant:

```bash
# copy analysis/fsh/AbsurdSequences.fsh into input/fsh/examples/
cp analysis/fsh/AbsurdSequences.fsh input/fsh/examples/
sushi .
# Expect: 0 Errors  (the absurdity is in the semantics, not the syntax)
```

The file uses aliases already defined in `input/fsh/aliases.fsh` and references
supporting instances from `input/fsh/examples/ERefTaskExamples.fsh` where possible.
