# Testing Companion - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* **Testing Companion**

## Testing Companion

### Testing Companion IG

The PH eReferral Testing Companion is a separate FHIR Implementation Guide that **depends on** the main IG. It exists to keep the main IG focused, clean, and fast to render, while providing a rich set of testing, demonstration, and experimentation artefacts alongside it.

-------

#### Why a Separate IG?

A FHIR IG that tries to serve two purposes at once — communicating the standard clearly **and** exercising it thoroughly — ends up doing neither well. Bulk test data inflates page count, slows the IG Publisher, and buries the handful of carefully constructed mainline examples that implementers actually need to understand the model.

The solution is a clean separation:

| | |
| :--- | :--- |
| One clear example per key concept | Hundreds of examples for edge cases, boundary values, and variant scenarios |
| Narrative pages explaining the standard | Scripts and forms for hands-on experimentation |
| Profiles, value sets, and canonical definitions | Bulk test fixtures for matrix testing and load testing |
| A fast, readable rendered site | Containerised tooling that runs locally |

The companion depends on the main IG (declared via `dependsOn` in its `sushi-config.yaml`), so all companion instances and questionnaires are validated against the same profiles and terminology. It is not a fork — it is an extension.

-------

#### Bulk Test Examples

The companion's primary purpose is to hold the test data that would otherwise clutter the main IG. This includes:

* **Scenario variants** — alternative pathways through the referral workflow: referral declined, referral redirected, referral completed with feedback, referral for a non-pregnant patient.
* **Edge cases** — instances with optional elements populated to their boundaries, unusual but valid code combinations, and minimal-conformant instances with only required fields.
* **Negative test cases** — intentionally invalid instances used to verify that validators correctly reject non-conformant data.
* **Volume fixtures** — larger sets of patients, encounters, and referrals used for load testing and matrix test seeding.

Keeping this material in the companion means the main IG remains focused on the handful of examples that matter for understanding the standard — and the companion can grow without any impact on main IG build times or readability.

-------

#### Interactive Demonstration Artefacts

Beyond bulk data, the companion provides artefacts designed for **hands-on exploration** by clinicians, business analysts, and implementers who want to understand the IG's behaviour without reading raw FHIR JSON.

##### Demo Scripts

Executable scripts (shell or Python) that replay end-to-end scenarios against a live FHIR server. A single command can:

1. Load the eReferral test data into a local FHIR server.
1. Submit a referral transaction bundle.
1. Query the resulting`Task`resource for its current status.
1. Simulate a status update from the receiving facility.
1. Print a human-readable summary of the outcome.

Scripts serve two audiences: developers who want to understand the API surface, and project managers who want to see a live walkthrough without writing a line of code.

##### SDC Questionnaires

The most important interactive artefact is a set of **Structured Data Capture (SDC) Questionnaires** — FHIR `Questionnaire` resources built to the [FHIR SDC specification](https://build.fhir.org/ig/HL7/sdc/) that render as familiar data-entry forms and automate the extraction of completed data into conformant FHIR resources.

Each SDC Questionnaire in the companion does three things:

1. **Renders a form** — a clinician or analyst sees a familiar referral form with labelled fields, dropdowns, and date pickers rather than raw FHIR structure. No technical knowledge is required to interact with it.
1. **Pre-populates from existing data** — using SDC population expressions, the form can draw existing `Patient`, `Practitioner`, and `Encounter` data from a connected FHIR server to pre-fill fields, simulating how the form would behave in a real system.
1. **Extracts to FHIR resources** — when the form is submitted, SDC extraction rules (definition-based or `questionnaire-itemExtractionContext`) transform the answers into a `Bundle` of profiled FHIR resources conformant with the main IG. This round-trip — from blank form to valid FHIR bundle — demonstrates that the IG's data model is practically implementable in a form-driven system.

The extraction output is validated against the main IG profiles, making SDC forms a powerful tool for identifying ambiguities: if a clinician's natural way of completing the form cannot be mapped cleanly to a valid FHIR bundle, that is a signal the data model needs refinement.

**SDC forms in the companion are specifically intended to be shared with domain experts** — clinicians, DOH reviewers, and programme managers — as a non-technical way to verify that the IG captures the right information in the right way.

-------

#### Containerised Local Stack

To make experimentation as frictionless as possible, the companion includes a `docker-compose` configuration that spins up a complete local testing environment with a single command.

The stack includes:

| | |
| :--- | :--- |
| **HAPI FHIR Server (R4)** | Hosts the loaded IG packages and test resources; provides the FHIR REST API for all other services |
| **SDC Form Renderer**(e.g. LHC-Forms) | Renders`Questionnaire`resources from the companion as interactive web forms; handles population and extraction |
| **Test Data Seeder** | On startup, loads a curated set of companion examples into the FHIR server — patients, practitioners, organisations — so forms have data to pre-populate from |
| **IG Validator** | Runs`publisher.jar -validate`to validate extracted bundles against the main IG profiles on demand |
| **Demo scripts** | Drives end-to-end scenario replays against the local stack |

Starting the stack requires only Docker and one command:

```
docker-compose up

```

Once running, an implementer can open the SDC form renderer in a browser, complete a referral form, and see the extracted FHIR bundle validated against the IG — all without deploying anything to a shared environment or requiring access to a test server.

This is particularly valuable for:

* **Connectathon preparation** — participants can develop and test locally before the event.
* **Stakeholder demonstrations** — project teams can run a live walkthrough on a laptop.
* **IG authoring feedback loops** — authors can immediately see whether a profile change breaks existing SDC extraction rules.

-------

#### Relationship to Other Testing Approaches

The companion IG and its artefacts occupy a specific position in the overall testing landscape:

| | | |
| :--- | :--- | :--- |
| **Mainline examples** | Main IG | Communicate the standard clearly to implementers |
| **Bulk test examples** | Companion IG | Exercise edge cases; feed matrix and load testing |
| **SDC forms** | Companion IG | Interactive demonstration; domain expert validation |
| **CI matrix testing** | [Interop Testing](interop-testing.md)page | Automated N×N endpoint testing between live implementations |
| **Connectathon** | HL7 process (see[HL7 Lifecycle](hl7-lifecycle.md)) | Formal interoperability evidence for FMM advancement |
| **Formal compliance** | Accredited bodies | Regulatory or contractual certification |

The companion does not replace any of these — it makes the earlier stages cheaper and more effective by giving implementers a working, explorable environment before they commit to building production systems.

-------

#### Status and Roadmap

The Testing Companion IG is planned as a follow-on artefact to the main IG. The current priorities for its development are:

1. **SDC Questionnaire for the referral request**— covering the core REF-11 to REF-19 data elements.
1. **Registration form**— covering the patient demographics elements (REF-20 to REF-29).
1. **Bulk scenario fixtures**— at least five scenario variants covering the most common referral pathways.
1. **`docker-compose` stack**— HAPI FHIR + LHC-Forms renderer + seeder.
1. **Connectathon prep package**— scripts and fixtures specifically structured for use at a FHIR Connectathon event.

For the current state of the main IG artefacts on which the companion will depend, see the [Resource Architecture](resource-architecture.md) and [DD Mapping](dd-mapping.md) pages.

