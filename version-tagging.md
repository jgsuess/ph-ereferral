A solid, automation-friendly way to **synchronize a Git tag with a FHIR IG version** *and* keep a clean **publication history** is to treat “version” as a **first‑class release artifact** and drive it from a **single source of truth**, while separating **CI preview builds** from **milestone publications**.

Below is the pattern I recommend (and that aligns with how the HL7 tooling ecosystem expects IGs to be managed and published), with concrete mechanics you can drop into GitHub Actions/Azure DevOps.

***

## 1) Use a “two-lane” model: **CI lane** vs **Release lane**

### CI lane (every commit / every branch)

Goal: fast feedback, always available, not necessarily immutable.

*   Build on every push (any branch). The standard auto-builder model does exactly this: commit triggers a build and publishes to a predictable branch URL under `build.fhir.org/ig/.../branches/...`. [\[FHIR IG Workflow \| PowerPoint\]](https://csiroau-my.sharepoint.com/personal/sue005_csiro_au/_layouts/15/Doc.aspx?sourcedoc=%7BC7946D3E-913B-48BC-9947-9E509C771681%7D&file=FHIR%20IG%20Workflow.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1), [\[github.com\]](https://github.com/FHIR/auto-ig-builder)
*   Version string for CI builds should be **distinct** from releases (e.g. `1.4.0-cibuild`), which is consistent with the IG guidance on working versions (`-cibuild`, `-preview`, `-draft`, etc.). [\[build.fhir.org\]](https://build.fhir.org/ig/FHIR/ig-guidance/versions.html)

**Key point:** CI builds are *not* your publication history; they’re your “living head”.

### Release lane (only on tags)

Goal: immutable, citable, and appears in “Directory of published versions” / history pages.

*   Only publish when a **release tag** is created (or when a GitHub Release is cut).
*   Each tag corresponds to a semver milestone (e.g. `v1.3.0`, `v1.3.1`), consistent with the IG semver guidance. [\[build.fhir.org\]](https://build.fhir.org/ig/FHIR/ig-guidance/versions.html)
*   After publication, increment to the next dev version and add a suffix (e.g. `1.4.0-draft`) before further changes. This lifecycle is explicitly described in the SMART starter kit’s versioning guidance (draft → active release → bump next draft). [\[smart.who.int\]](https://smart.who.int/ig-starter-kit/versioning.html)

***

## 2) Make Git tags the “release intent”, not the live version generator

There’s active discussion in the IG Publisher community about “passing an external version into the publisher”, but also caution that you **don’t** want the version to bump on *every commit*. [\[github.com\]](https://github.com/HL7/fhir-ig-publisher/issues/1105)

So the robust approach is:

### ✅ On `main` (or `release/*`) you keep:

*   `sushi-config.yaml` / `ImplementationGuide` version set to the **next intended** development version, e.g. `1.4.0-draft` (or `-preview`). [\[smart.who.int\]](https://smart.who.int/ig-starter-kit/versioning.html), [\[build.fhir.org\]](https://build.fhir.org/ig/FHIR/ig-guidance/versions.html)
*   CI builds reflect that version (fine; it’s a working build).

### ✅ On tag `v1.3.0` you publish:

*   Build from the tag commit (detached checkout).
*   Ensure the IG version *in the produced output* is `1.3.0`.
*   Publish that output into your publication webroot under `/1.3.0/` (or similar), and update the history index.

**Important:** you want reproducibility: checking out tag `v1.3.0` and rebuilding should produce the same site/package.

***

## 3) Synchronization pattern (the “single source of truth” rule)

Pick **one** canonical source for the version string during a release build:

### Recommended: **Tag is source of truth for releases**

*   Tag name: `vX.Y.Z`
*   Derived IG version: `X.Y.Z`

Then, in the release pipeline:

1.  Parse `GITHUB_REF_NAME` (or equivalent) → `X.Y.Z`
2.  Fail the build if:
    *   repo files claim a different release version (guardrail)
    *   or IG version still contains `-draft/-cibuild` (unless you intentionally release those)

This gives you an invariant:

> **Release tag = Published IG version = Published package version**

…and prevents “oops we tagged 1.3.0 but the IG says 1.2.9”.

*(Tooling note: IG publisher produces an NPM `package.tgz` as part of the build output.  So version drift matters for downstream consumers.)* [\[confluence.hl7.org\]](https://confluence.hl7.org/spaces/FHIR/pages/35718627/IG+Publisher+Documentation)

***

## 4) Publication history: use the standard history template / layout approach

HL7’s publication ecosystem uses a **history/versions index** pattern (often `history.html`) and a conventional layout for “directory of published versions”. The IG Publisher documentation explicitly covers history management as part of IG management. [\[confluence.hl7.org\]](https://confluence.hl7.org/spaces/FHIR/pages/35718627/IG+Publisher+Documentation)

And the “How to Publish a FHIR IG” guide describes staging multiple releases, typically publishing only key versions plus one “most recent dev/CI build”, and keeping historical versions accessible. [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/)

### What this means in practice

Maintain a **publication repository or publication webroot** that contains:

    / (root)
      /current/        (optional alias to latest release)
      /dev/            (optional alias to CI build)
      /1.3.0/          (immutable release)
      /1.2.1/          (immutable release)
      /package-feed.xml
      /publication-feed.xml
      /history.html

The “How to Publish” setup describes establishing a publication directory with templates/webroot and a `publish-setup.json` describing layout rules, including support for GitHub Pages/cloud hosting. [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/setup.html)

***

## 5) Concrete automation flow (GitHub Actions style)

### A) CI workflow (push / PR)

*   Run SUSHI + IG Publisher
*   Publish to preview site (GitHub Pages branch, or rely on auto-ig-builder for public repos) [\[FHIR IG Workflow \| PowerPoint\]](https://csiroau-my.sharepoint.com/personal/sue005_csiro_au/_layouts/15/Doc.aspx?sourcedoc=%7BC7946D3E-913B-48BC-9947-9E509C771681%7D&file=FHIR%20IG%20Workflow.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1), [\[github.com\]](https://github.com/FHIR/auto-ig-builder)
*   Version stays `*-draft` or `*-cibuild` per your repo config [\[build.fhir.org\]](https://build.fhir.org/ig/FHIR/ig-guidance/versions.html), [\[smart.who.int\]](https://smart.who.int/ig-starter-kit/versioning.html)

### B) Release workflow (on tag `v*`)

1.  Checkout tag
2.  Derive `VERSION=X.Y.Z`
3.  Update version inputs *for the build only* (common techniques):
    *   patch `sushi-config.yaml` and/or IG resource in a temp workspace
    *   or pass parameters if your build tooling supports it (the desire exists, but don’t rely on it being universally available) [\[github.com\]](https://github.com/HL7/fhir-ig-publisher/issues/1105)
4.  Run IG Publisher build
5.  Publish output to `/X.Y.Z/`
6.  Update:
    *   `history.html` / “Directory of published versions”
    *   feeds (`package-feed.xml`, `publication-feed.xml`) if you use them [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/setup.html), [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/)
7.  Commit publication repo changes (or upload artifact set to your web host)

This yields a durable publication history that does **not** depend on GitHub Pages retaining old build artifacts.

***

## 6) Guardrails I strongly recommend (prevents footguns)

1.  **Tag/IG mismatch check** (fail the workflow)
    *   If tag says `v1.3.0` but IG version in source is `1.4.0-draft`, require the workflow to patch for release build, or require that the tagged commit already contains `1.3.0`.
2.  **Immutability by path**
    *   Never overwrite `/1.3.0/` once published.
3.  **One moving pointer**
    *   `/dev/` and/or `/current/` may be overwritten.
4.  **Release notes / change tracking**
    *   Track changes via GitHub issues and/or release notes; this is called out as part of “tracking changes” expectations. [\[smart.who.int\]](https://smart.who.int/ig-starter-kit/versioning.html)

***

## 7) Minimal “best practice” recommendation (if you want one crisp answer)

**Best pattern:**

*   Keep your repo’s working version as `NEXTVERSION-draft` (or `-cibuild`) for day-to-day work and CI. [\[build.fhir.org\]](https://build.fhir.org/ig/FHIR/ig-guidance/versions.html), [\[smart.who.int\]](https://smart.who.int/ig-starter-kit/versioning.html)
*   Cut immutable releases **only** from annotated Git tags `vX.Y.Z`; the tag is the authoritative release version.
*   In the release pipeline, build from the tag and publish to a versioned directory (`/X.Y.Z/`), updating your `history.html` / versions index and feeds using the standard IG publication layout tooling. [\[confluence.hl7.org\]](https://confluence.hl7.org/spaces/FHIR/pages/35718627/IG+Publisher+Documentation), [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/setup.html), [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/)
*   Keep CI preview builds separate (auto-build branch URLs or `/dev/`). [\[github.com\]](https://github.com/FHIR/auto-ig-builder), [\[FHIR IG Workflow \| PowerPoint\]](https://csiroau-my.sharepoint.com/personal/sue005_csiro_au/_layouts/15/Doc.aspx?sourcedoc=%7BC7946D3E-913B-48BC-9947-9E509C771681%7D&file=FHIR%20IG%20Workflow.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1)

That gives you: **reproducible releases**, **clean semver mapping**, and **a maintained publication history**.

***

Perfect — **GitHub Pages from a branch** is actually the *cleanest* way to do this for FHIR IGs if you lean into a **branch‑per‑role** model and keep **tags authoritative**.

Below is a **concrete, opinionated pattern** that works well with IG Publisher, SUSHI, and GitHub Actions, and keeps your **IG version, git tags, and publication history aligned** without hacks.

***

# Recommended Pattern: **`gh-pages` publication branch + tag‑driven releases**

## Branch roles (very explicit)

| Branch        | Purpose                                        | Mutability             |
| ------------- | ---------------------------------------------- | ---------------------- |
| `main`        | Source of truth for *next* version (`*-draft`) | Mutable                |
| `gh-pages`    | Published website only (HTML, history, feeds)  | Mutable but controlled |
| tags `vX.Y.Z` | Release intent & immutability boundary         | Immutable              |

**Key rule**

> The `gh-pages` branch contains *only* rendered IG output — never source.

***

## Version semantics (this is the spine)

You keep **exactly one version string in source**:

*   On `main`
    ```yaml
    version: 1.4.0-draft
    ```
*   On release tag `v1.3.0`  
    → published IG version = **`1.3.0`**

You **do not** permanently rewrite source files for releases.  
The release pipeline **derives the version from the tag**.

This avoids the classic:

> “Oops, forgot to bump the version before tagging”

***

## GitHub Pages layout (what actually gets served)

Your `gh-pages` branch should look like this:

    /
    ├── index.html              # landing page (optional)
    ├── history.html            # generated by IG Publisher
    ├── package-feed.xml
    ├── publication-feed.xml
    ├── dev/                    # CI build from main
    │   └── index.html
    ├── 1.2.1/
    │   └── index.html
    ├── 1.3.0/
    │   └── index.html
    └── current -> 1.3.0/       # optional symlink or redirect

**Only these move:**

*   `/dev/`
*   `/current/`

Everything under `/X.Y.Z/` is immutable.

***

## Workflow 1: CI preview (push to `main`)

### Trigger

```yaml
on:
  push:
    branches: [ main ]
```

### What it does

1.  Checkout `main`
2.  Run SUSHI + IG Publisher
3.  Publish output to `gh-pages:/dev/`
4.  (Optional) update `/current/` **only if no releases exist yet**

### Result

*   Always‑fresh preview
*   URL stable:
        https://<org>.github.io/<repo>/dev/

No tags involved. No history changes.

***

## Workflow 2: Release publish (push tag `v*`)

### Trigger

```yaml
on:
  push:
    tags:
      - "v*"
```

### Release algorithm (this is the important part)

```text
TAG = v1.3.0
VERSION = 1.3.0
```

Steps:

1.  **Checkout the tag**
    ```bash
    git checkout $GITHUB_REF_NAME
    ```

2.  **Derive version from tag**
    ```bash
    VERSION=${GITHUB_REF_NAME#v}
    ```

3.  **Patch version *at build time only***
    *   patch `sushi-config.yaml`
    *   or patch the IG resource
    *   do NOT commit this back

4.  **Build the IG**
    ```bash
    sushi .
    java -jar publisher.jar ...
    ```

5.  **Publish to `gh-pages:/1.3.0/`**
    *   copy rendered output
    *   do **not** overwrite existing versions

6.  **Update history & feeds**
    *   `history.html`
    *   `package-feed.xml`
    *   `publication-feed.xml`

7.  **Update `/current/ → /1.3.0/`**

8.  Commit **only** to `gh-pages`

***

## Guardrails (highly recommended)

### 1. Fail fast on version mistakes

If source version is still `*-draft` **and** you’re not patching it at build time → fail the release job.

This stops:

> “We tagged 1.3.0 but published 1.4.0-draft”

***

### 2. Never rebuild a released directory

In your workflow:

```bash
if [ -d "1.3.0" ]; then
  echo "Release already exists – refusing to overwrite"
  exit 1
fi
```

***

### 3. One moving pointer only

*   `/dev/` moves
*   `/current/` moves
*   `/X.Y.Z/` never moves

This makes auditors, implementers, and downstream tooling happy.

***

## Why this works *especially well* for FHIR IGs

*   ✅ Aligns with HL7’s expectation of **milestone publications vs CI builds**
*   ✅ Preserves reproducibility (tag → exact site)
*   ✅ Works cleanly with **FHIR package publishing**
*   ✅ No reliance on half‑supported “pass version via CLI” features
*   ✅ History pages and feeds stay canonical

This is the same conceptual model HL7 uses internally — just implemented cleanly with GitHub Pages instead of FTP/S3.

***

## Minimal checklist

If you want the TL;DR:

*   ✅ `main` always holds `NEXTVERSION-draft`
*   ✅ Git tag `vX.Y.Z` = *release intent*
*   ✅ Release pipeline derives version from tag
*   ✅ `gh-pages` branch contains **only** rendered output
*   ✅ `/dev/` for CI, `/X.Y.Z/` for releases
*   ✅ Never rewrite history

***

Below is a **drop‑in GitHub Actions setup** that implements the pattern we discussed:

*   **CI preview** on every push to `main` → publishes rendered IG to **`gh-pages:/dev/`**
*   **Release publish** on tag `v*` → publishes rendered IG to **`gh-pages:/X.Y.Z/`**, updates **`history.html`**, and moves **`/current/`** to latest release
*   **Never overwrites** an existing released version directory

This is aligned with HL7 IG build/publish expectations (CI builds vs milestone publications) and the auto‑builder model (commit‑triggered builds). [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/), [\[confluence.hl7.org\]](https://confluence.hl7.org/display/HAFWG/FHIR+IG+History), [\[confluence.hl7.org\]](https://confluence.hl7.org/spaces/FHIR/pages/35718627/IG+Publisher+Documentation)

***

## 1) `.github/workflows/ig-ci-dev.yml` (publish `/dev/`)

> Trigger: push to `main`  
> Output URL: `https://<org>.github.io/<repo>/dev/`

```yaml
name: IG CI (dev)

on:
  push:
    branches: [ "main" ]

permissions:
  contents: write

concurrency:
  group: ig-dev
  cancel-in-progress: true

jobs:
  build-and-publish-dev:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node (for SUSHI)
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install SUSHI
        run: npm install -g fsh-sushi

      - name: Install Java (for IG Publisher)
        uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "17"

      - name: Download IG Publisher
        run: |
          mkdir -p .tools
          curl -L -o .tools/publisher.jar https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar

      - name: Run SUSHI
        run: sushi .

      - name: Run IG Publisher
        run: |
          # expects ig.ini at repo root (standard IG publisher layout)
          java -jar .tools/publisher.jar -ig ig.ini

      - name: Prepare publish directory (dev)
        run: |
          rm -rf .publish
          mkdir -p .publish/dev
          # IG Publisher output is typically under output/ (common in HL7 guidance/tooling)
          rsync -a output/ .publish/dev/

      - name: Publish to gh-pages:/dev/
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_branch: gh-pages
          publish_dir: .publish
          keep_files: true
          commit_message: "ci(dev): publish dev build from ${{ github.sha }}"
```

### Notes

*   This uses `peaceiris/actions-gh-pages` to push into the `gh-pages` branch.
*   `keep_files: true` ensures existing `/X.Y.Z/` releases aren’t deleted.
*   The IG Publisher output path (`output/`) is the conventional build output directory referenced in HL7 tooling docs (the publisher generates a full rendered IG and package artifacts). [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/)

***

## 2) `.github/workflows/ig-release.yml` (publish `/X.Y.Z/` + update `history.html` + move `/current/`)

> Trigger: push tag `v*` (e.g., `v1.3.0`)  
> Publishes to: `/1.3.0/` and updates `/current/`

```yaml
name: IG Release Publish

on:
  push:
    tags:
      - "v*"

permissions:
  contents: write

concurrency:
  group: ig-release
  cancel-in-progress: false

jobs:
  build-and-publish-release:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout (tag)
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Derive version from tag
        id: v
        run: |
          TAG="${GITHUB_REF_NAME}"
          VERSION="${TAG#v}"
          echo "tag=$TAG" >> "$GITHUB_OUTPUT"
          echo "version=$VERSION" >> "$GITHUB_OUTPUT"
          echo "Release version: $VERSION"

      - name: Setup Node (for SUSHI)
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install SUSHI
        run: npm install -g fsh-sushi

      - name: Install Java (for IG Publisher)
        uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "17"

      - name: Download IG Publisher
        run: |
          mkdir -p .tools
          curl -L -o .tools/publisher.jar https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar

      - name: Patch IG version for this build only (sushi-config.yaml)
        run: |
          # This keeps your repo on main at NEXTVERSION-draft while releases are built from tags.
          if [ -f sushi-config.yaml ]; then
            python3 - <<'PY'
import re, pathlib
p = pathlib.Path("sushi-config.yaml")
txt = p.read_text(encoding="utf-8")
v = "${{ steps.v.outputs.version }}"
# Replace a top-level "version:" line (simple, works for common configs)
txt2 = re.sub(r'(?m)^(version:\s*).+$', r'\g<1>'+v, txt)
p.write_text(txt2, encoding="utf-8")
print("Patched sushi-config.yaml version to", v)
PY
          else
            echo "No sushi-config.yaml found; skipping patch."
          fi

      - name: Run SUSHI
        run: sushi .

      - name: Run IG Publisher
        run: |
          java -jar .tools/publisher.jar -ig ig.ini

      - name: Checkout gh-pages branch into workspace
        run: |
          rm -rf .gh-pages
          git clone --depth 1 --branch gh-pages "https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git" .gh-pages

      - name: Refuse to overwrite an existing release
        run: |
          REL="${{ steps.v.outputs.version }}"
          if [ -d ".gh-pages/$REL" ]; then
            echo "Release $REL already exists in gh-pages. Refusing to overwrite."
            exit 1
          fi

      - name: Copy release output into gh-pages:/VERSION/
        run: |
          REL="${{ steps.v.outputs.version }}"
          mkdir -p ".gh-pages/$REL"
          rsync -a output/ ".gh-pages/$REL/"

      - name: Update /current/ pointer (simple redirect)
        run: |
          REL="${{ steps.v.outputs.version }}"
          mkdir -p ".gh-pages/current"
          cat > ".gh-pages/current/index.html" <<EOF
<!doctype html>
<meta http-equiv="refresh" content="0; url=../$REL/">
../$REL/
<title>Redirecting…</title>
Redirecting to ../$REL/$REL</a>
EOF

      - name: Update history.html (basic “versions index”)
        run: |
          # If your IG build already produces history.html, prefer that.
          # Otherwise create/refresh a simple one from directories present.
          python3 - <<'PY'
import os, re, pathlib
root = pathlib.Path(".gh-pages")
versions = []
for p in root.iterdir():
    if p.is_dir() and re.fullmatch(r"\d+\.\d+\.\d+([\-\.].+)?", p.name):
        versions.append(p.name)
versions.sort(key=lambda s: [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', s)], reverse=True)

html = ["<!doctype html><meta charset='utf-8'><title>Publication History</title>",
        "<h1>Publication History</h1>",
        "<ul>"]
for v in versions:
    html.append(f"<li>./{v}/{v}</a></li>")
html.append("</ul>")
(root/"history.html").write_text("\n".join(html), encoding="utf-8")
print("Wrote history.html with", len(versions), "entries")
PY

      - name: Commit and push gh-pages changes
        run: |
          cd .gh-pages
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git commit -m "release: publish ${{ steps.v.outputs.tag }} (IG ${{ steps.v.outputs.version }})" || exit 0
          git push
```

### What this release workflow guarantees

*   Tag `v1.3.0` → publishes `/1.3.0/`
*   **Won’t overwrite** `/1.3.0/` if it already exists
*   `/current/` always points to latest published release
*   `history.html` lists all published versions (basic implementation).  
    (If you prefer the full HL7 history template approach, that’s typically done with `-go-publish` in a separate publication workspace; GitHub Pages can still host the output, but that’s a more involved setup.) [\[github.com\]](https://github.com/FHIR/ig-registry), [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/)

***

## 3) GitHub Pages settings (one-time)

Set in repo settings:

*   **Pages Source**: `Deploy from a branch`
*   **Branch**: `gh-pages`
*   **Folder**: `/ (root)`

Then your URLs become:

*   Dev: `…/dev/`
*   Release: `…/1.3.0/`
*   Latest: `…/current/`
*   History: `…/history.html`

***

## 4) Why the YAML uses this structure (grounding)

*   The IG Publisher produces rendered HTML and package artifacts as standard outputs, and the HL7 docs describe using CI builds for visibility plus milestone publications for stable versions. [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/), [\[build.fhir.org\]](https://build.fhir.org/ig/FHIR/ig-guidance/using-templates.html)
*   The versioning guidance recommends semver and distinguishes working versions (`-draft`, `-preview`, `-cibuild`) from milestone releases. [\[confluence.hl7.org\]](https://confluence.hl7.org/display/HAFWG/FHIR+IG+History), [\[github.com\]](https://github.com/HL7/fhir-ig-publisher/issues/1105)
*   The auto-build model is explicitly “build on every commit”, which we mirror for `/dev/`. [\[confluence.hl7.org\]](https://confluence.hl7.org/spaces/FHIR/pages/35718627/IG+Publisher+Documentation), [\[FHIR IG Workflow \| PowerPoint\]](https://csiroau-my.sharepoint.com/personal/sue005_csiro_au/_layouts/15/Doc.aspx?sourcedoc=%7BC7946D3E-913B-48BC-9947-9E509C771681%7D&file=FHIR%20IG%20Workflow.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1)

***

## Small optional improvements (safe to add later)

*   Add a step that validates `ImplementationGuide.version` inside your generated IG resource matches the release version (extra guardrail).
*   Generate a richer `history.html` (dates, links to GitHub releases).
*   Publish the `.tgz` package artifacts to a package registry if you use one (separate concern from the website). [\[argentixinfo.com\]](https://www.argentixinfo.com/ig/howtopub/), [\[fhir.github.io\]](https://fhir.github.io/auto-ig-builder/builds.html)

***

If you tell me **your repo layout** (where `ig.ini` lives and whether the IG output is `output/` or something else), I can tailor the paths in the YAML exactly—but the above is drop‑in for the common HL7 IG template layout.
