# Dependency Management - PH eReferral Implementation Guide v0.1.0

## Dependency Management

### Dependency Management

This page describes how to declare and resolve upstream FHIR IG dependencies using versioned packages and custom FHIR package repositories, rather than volatile dev-channel references.

-------

#### Overview

This IG depends on **fhir.ph.core**. Dependencies are declared in `sushi-config.yaml` and resolved by the IG Publisher and SUSHI at build time using the FHIR package cache (`~/.fhir/packages/`).

-------

#### 1. Declare the upstream IG as a package dependency

In `sushi-config.yaml`, declare upstream IGs by their **FHIR package ID** and **pinned version**:

```
dependencies:
  fhir.ph.core: 0.1.0

```

**Do not use `dev` or `current`** — these refer to volatile CI-build snapshots and must not appear in releases. The release workflow enforces this: it fails the build if any `dev`/`current` version is detected in `sushi-config.yaml`.

Dependency resolution is **package/version based**, not Git-repository based. The upstream IG must be available as a FHIR package, not as a Git reference.

-------

#### 2. How the IG Publisher resolves packages

The publisher resolves packages in this order:

1. **Local FHIR package cache**—`~/.fhir/packages/{package-id}#{version}/`
1. **Default FHIR package servers**—`packages.fhir.org`,`packages2.fhir.org`
1. **Custom servers**— configured in`fhir-settings.json`(see below)

For packages not on the public FHIR registry (such as `fhir.ph.core`, which is distributed via GitHub), the local cache is pre-populated by the build tooling before the publisher runs.

-------

#### 3. Local builds

The `_build.sh` script automatically installs `fhir.ph.core#0.1.0` into the local FHIR cache on first run:

```
./_build.sh build

```

Output on first use:

```
Installing fhir.ph.core#0.1.0 into local FHIR cache...
fhir.ph.core#0.1.0 installed.

```

The package is fetched from the ph-core release at `https://jgsuess.github.io/ph-core/0.1.0/package.tgz` — no authentication required.

-------

#### 4. CI builds

All CI workflows (validate, preview, dev, release) include an "Install fhir.ph.core into FHIR cache" step that runs the same curl-based install before the IG Publisher. The step is idempotent — it skips if the cache entry already exists.

-------

#### 5. Custom FHIR package servers (fhir-settings.json)

For cases where an upstream FHIR IG is hosted on a private or project-specific FHIR package server, configure `~/.fhir/fhir-settings.json` (Linux/macOS) or `C:\Users\<username>\.fhir\fhir-settings.json` (Windows):

```
{
  "servers": [
    {
      "url": "https://packages.example.org",
      "type": "fhir-package"
    },
    {
      "url": "https://packages.simplifier.net",
      "type": "fhir-package"
    }
  ]
}

```

The publisher will query these servers (in addition to the defaults) when resolving packages. Each server must speak the FHIR package protocol — i.e. respond to `GET /{package-id}/{version}` with the package tarball or metadata.

To provide the settings file explicitly rather than relying on the default location:

```
java -jar input-cache/publisher.jar -ig . -fhir-settings ./fhir-settings.json

```

The `-fhir-settings` flag is documented in the [IG Publisher CLI reference](https://confluence.hl7.org/spaces/FHIR/pages/175618322/IG+Publisher+CLI). See also the [fhir-settings.json documentation](https://confluence.hl7.org/spaces/FHIR/pages/161072808/Using+fhir-settings.json) for the full schema including `ignoreDefaultPackageServers`.

**Note on GitHub Packages:** GitHub Packages (npm.pkg.github.com) cannot be used directly as a fhir-settings.json server for `fhir.ph.core` because GitHub Packages requires packages to be scoped (e.g. `@jgsuess/fhir.ph.core`), while the IG Publisher resolves packages by their unscoped FHIR ID (`fhir.ph.core`). The name mismatch means the publisher cannot locate the package there. The local-cache pre-install approach described above is the correct workaround until `fhir.ph.core` is published to a public FHIR package registry.

-------

#### 6. Upgrade path

To consume a new version of `fhir.ph.core`:

1. Update`sushi-config.yaml`:

```
dependencies:
  fhir.ph.core: 0.2.0   # new version

```


1. Update the version constant in`_build.sh`(`ensure_fhir_ph_core`) and in each CI workflow step.
1. Verify the new`package.tgz`is available at`https://jgsuess.github.io/ph-core/0.2.0/package.tgz`.
1. Run`./_build.sh build`locally to validate before committing.

