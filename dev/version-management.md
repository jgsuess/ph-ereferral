# Version Management - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* **Version Management**

## Version Management

### Version Management & Publication

This page describes how the IG is versioned, published, and released. For the broader project methodology, see the [Approach](approach.md) page.

-------

#### Publication Model

The IG follows a **two-lane publication model** aligned with HL7 IG publishing guidance:

| | | | |
| :--- | :--- | :--- | :--- |
| **CI (dev)** | Push to`main` | `…/dev/` | Yes — always-fresh preview |
| **Release** | Git tag`vX.Y.Z` | `…/X.Y.Z/` | No — immutable once published |

**Key rules:**

1. The`main`branch always carries the**next**development version with a`-draft`suffix (e.g.`0.2.0-draft`).
1. Release versions are derived from**Git tags**— tagging`v0.1.0`produces IG version`0.1.0`.
1. The release workflow patches`sushi-config.yaml`at build time only; the source on`main`is never modified by the pipeline.
1. Published version directories (`/X.Y.Z/`) are**never overwritten**— the workflow refuses to proceed if the directory already exists.
1. `/current/`redirects to the latest release;`/dev/`always reflects the latest CI build from`main`.
1. A`history.html`page and`package-list.json`feed are maintained automatically on the`gh-pages`branch.

The workflows are defined in:

* `.github/workflows/ig-ci-dev.yml` — CI lane (push to `main`)
* `.github/workflows/ig-release.yml` — Release lane (tag `v*`)

#### Publication URLs

The table below lists the key URLs for accessing published content.

| | |
| :--- | :--- |
| `https://jgsuess.github.io/ph-ereferral/dev/` | Development build (latest CI from`main`) |
| `https://jgsuess.github.io/ph-ereferral/X.Y.Z/` | Immutable release |
| `https://jgsuess.github.io/ph-ereferral/current/` | Redirect to latest release |
| `https://jgsuess.github.io/ph-ereferral/history.html` | Publication history |

#### How to Cut a Release

Follow these steps to publish a new tagged release:

1. Ensure all changes are merged to`main`.
1. Create an annotated tag:`git tag -a v0.1.0 -m "First draft release"`
1. Push the tag:`git push origin v0.1.0`
1. The`ig-release.yml`workflow runs automatically: builds the IG with version`0.1.0`, publishes to`/0.1.0/`, updates`history.html`,`package-list.json`, and`/current/`.
1. After the release, bump the version on`main`to the next draft (e.g.`0.2.0-draft`).

-------

#### Limitations and Future Work

The following items are known gaps or deferred scope. Each is tied back to a specific data-dictionary element where applicable.

1. **Signature / Provenance**(REF-2, REF-3) — deferred to a future release per CDG consensus.
1. **HCPN**(REF-11) — on hold pending CDG decision on whether it should be computed or manually entered.
1. **Return referral slip**(REF-18) — excluded from MVP; requires DocumentReference modelling.
1. **Lab results**(REF-39) — currently modelled as ServiceRequest (orders); DiagnosticReport will be added when results are available.
1. **Receiving encounter**(REF-44) — belongs to the receiving facility's workflow, not the sending scenario.
1. **Pregnancy-specific elements**— the DD notes a placeholder row for gravidity, parity, fundal height, and immunisation history; these should be added as structured Observations in a future iteration.

