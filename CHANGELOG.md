# Changelog

## [0.4.0](https://github.com/jgsuess/ph-ereferral/compare/v0.3.1...v0.4.0) (2026-07-07)


### Features

* **deps:** bump to fhir.ph.core 0.1.1 and fhir.ph.ereferral 0.3.1 ([1c9a1fc](https://github.com/jgsuess/ph-ereferral/commit/1c9a1fc59c9d3be47363eeae6a024b523a9117b4))


### Bug Fixes

* **ci:** pre-install custom fhir.ph.* packages before IG Publisher ([c61f097](https://github.com/jgsuess/ph-ereferral/commit/c61f09712c48759315ac00ee951d3008a405e201))
* **ci:** pull --rebase before gh-pages push to avoid race with ig-ci-dev ([9b9cfde](https://github.com/jgsuess/ph-ereferral/commit/9b9cfde86ad2173ec296eea52b9f435e2625aa85))
* **ci:** remove --strip-components=1 from FHIR package pre-install ([ea79678](https://github.com/jgsuess/ph-ereferral/commit/ea7967890ea6402a6b0404a343cb12fd1547268b))
* **examples:** update medicationadministration-ifa-ex to current SNOMED code ([90dd927](https://github.com/jgsuess/ph-ereferral/commit/90dd9272a2c9e85b730e85a034e1876ed83aa85c))
* **scripts:** bump upload_examples.sh defaults to ph-core 0.1.1 / ph-ereferral 0.3.1 ([3513327](https://github.com/jgsuess/ph-ereferral/commit/35133277135022561f6acde95988f4eef8732745))

## [0.3.1](https://github.com/jgsuess/ph-ereferral/compare/v0.3.0...v0.3.1) (2026-06-17)


### Bug Fixes

* **deps:** pin fhir.ph.core to 0.1.1 ([6602fe5](https://github.com/jgsuess/ph-ereferral/commit/6602fe56879436a43a77e456cbd9a03fe5d09f22))
* **examples:** correct profile URLs, resolve urn:uuid refs, fix constraints ([570aeba](https://github.com/jgsuess/ph-ereferral/commit/570aebaf929924281e8e95805e2d83729c1ccaac))
* **examples:** use SNOMED code for RelatedPerson.relationship (v3-RoleCode not available without hl7.terminology package) ([abff377](https://github.com/jgsuess/ph-ereferral/commit/abff377d80c9a825db9b557c3374e512b6496025))

## [0.3.0](https://github.com/jgsuess/ph-ereferral/compare/v0.2.0...v0.3.0) (2026-06-17)


### Features

* Add AGENTS.md for Vibe Engineering workflow documentation ([9167384](https://github.com/jgsuess/ph-ereferral/commit/91673844f02612a29997b1f8efac493501b271a4))
* add ERefEncounter profile to standardize encounter information in the Philippine eReferral system ([#68](https://github.com/jgsuess/ph-ereferral/issues/68)) ([2f8c561](https://github.com/jgsuess/ph-ereferral/commit/2f8c5613a7c741dee55aaa22e28c6eada83671c5))
* Add ERefPatient Profile with PWD Disability Extension ([#24](https://github.com/jgsuess/ph-ereferral/issues/24)) ([466ded3](https://github.com/jgsuess/ph-ereferral/commit/466ded39e7de699d29bf443565da33248d77edc0))
* Add ERefPractitionerRole Profile with examples (closes [#28](https://github.com/jgsuess/ph-ereferral/issues/28)) ([#29](https://github.com/jgsuess/ph-ereferral/issues/29)) ([14208fd](https://github.com/jgsuess/ph-ereferral/commit/14208fdcda4ce510bd57455d337d94f1562f62db))
* Add References page with inline PDF previews and Data Dictionary table ([#17](https://github.com/jgsuess/ph-ereferral/issues/17)) ([#129](https://github.com/jgsuess/ph-ereferral/issues/129)) ([75eaca2](https://github.com/jgsuess/ph-ereferral/commit/75eaca20c88614c92c0e31dcc44ba6583c77cc13))
* **ci:** implement SUSHI and IG Publisher validation pipeline ([#54](https://github.com/jgsuess/ph-ereferral/issues/54)) ([9b7f869](https://github.com/jgsuess/ph-ereferral/commit/9b7f86950fe77584767df79b134aa1266220f3c7))
* **profile:** add ERefMedicationAdministration profile with GPS-valid examples ([#55](https://github.com/jgsuess/ph-ereferral/issues/55)) ([f8747b6](https://github.com/jgsuess/ph-ereferral/commit/f8747b6efb87dbd9119177ac584042f8073e34d8))
* **profile:** add ERefObservation profile with TDG-mapped examples ([#82](https://github.com/jgsuess/ph-ereferral/issues/82)) ([8901323](https://github.com/jgsuess/ph-ereferral/commit/89013236fcd25e6ff7bf951208fdf26c40e49d18))
* **profile:** add ERefProvenance profile with GPS-valid examples ([#61](https://github.com/jgsuess/ph-ereferral/issues/61)) ([9a739d0](https://github.com/jgsuess/ph-ereferral/commit/9a739d02a65124c6d4c171ea10652d6548a6ab27)), closes [#31](https://github.com/jgsuess/ph-ereferral/issues/31)
* **profile:** add ERefTask profile with GPS-valid examples ([#32](https://github.com/jgsuess/ph-ereferral/issues/32)) ([#63](https://github.com/jgsuess/ph-ereferral/issues/63)) ([ea4d832](https://github.com/jgsuess/ph-ereferral/commit/ea4d8321be1804b86f03d045475a417f7e392a8c))
* update referral workflow documentation to use generic terminology ([7642467](https://github.com/jgsuess/ph-ereferral/commit/7642467475d13e4202da46c6849cbeba1f425a5f))


### Bug Fixes

* add smetana layout pragma to all PlantUML diagrams ([b81e370](https://github.com/jgsuess/ph-ereferral/commit/b81e3708aaf79da9463d94944c74a355f8243114))
* **config:** correct canonical URL from urn:// to https:// ([#102](https://github.com/jgsuess/ph-ereferral/issues/102)) ([f3e8b60](https://github.com/jgsuess/ph-ereferral/commit/f3e8b60a09972a335a78f344a9a648ef9746606b)), closes [#64](https://github.com/jgsuess/ph-ereferral/issues/64) [#74](https://github.com/jgsuess/ph-ereferral/issues/74)
* consistent swimlane naming to eliminate duplicate columns ([67922b4](https://github.com/jgsuess/ph-ereferral/commit/67922b46ab4f7768b8a7096bb8a4381712dabcf2))
* **examples:** correct terminology errors found in local build validation ([be026af](https://github.com/jgsuess/ph-ereferral/commit/be026af8dfd53c5aae479ca53878891080267d02))
* **examples:** use GPS-compatible SNOMED CT codes and correct terminology bindings ([#101](https://github.com/jgsuess/ph-ereferral/issues/101)) ([8192613](https://github.com/jgsuess/ph-ereferral/commit/8192613705eb09c11b09e4e2bdc776b6ec7ebcba)), closes [#58](https://github.com/jgsuess/ph-ereferral/issues/58)
* **profile:** remove disabilityRegistration extension from ERefPatient ([#108](https://github.com/jgsuess/ph-ereferral/issues/108)) ([#115](https://github.com/jgsuess/ph-ereferral/issues/115)) ([ebebbdd](https://github.com/jgsuess/ph-ereferral/commit/ebebbdd46f04deaff5846b7e030d94a3b706832c))
* **profile:** update parent of ERefServiceRequest to PHCoreServiceRequest ([#104](https://github.com/jgsuess/ph-ereferral/issues/104)) ([5575755](https://github.com/jgsuess/ph-ereferral/commit/5575755ce8f7f072a40a7c508d1f02a802ece571))
* resolve identifier URI conflicts in erefpatient-example.fsh (closes [#51](https://github.com/jgsuess/ph-ereferral/issues/51)) ([#52](https://github.com/jgsuess/ph-ereferral/issues/52)) ([8e83052](https://github.com/jgsuess/ph-ereferral/commit/8e830520256b21fa9454232a6f928f15eaa5fb5b))
* use Smetana layout for PlantUML diagrams (no Graphviz needed) ([de66763](https://github.com/jgsuess/ph-ereferral/commit/de667638bf412be58446388d4636b9d047e380d8))

## [0.2.0](https://github.com/jgsuess/ph-ereferral/compare/v0.1.0...v0.2.0) (2026-06-16)


### Features

* Add AGENTS.md for Vibe Engineering workflow documentation ([9167384](https://github.com/jgsuess/ph-ereferral/commit/91673844f02612a29997b1f8efac493501b271a4))
* add ERefEncounter profile to standardize encounter information in the Philippine eReferral system ([#68](https://github.com/jgsuess/ph-ereferral/issues/68)) ([2f8c561](https://github.com/jgsuess/ph-ereferral/commit/2f8c5613a7c741dee55aaa22e28c6eada83671c5))
* Add ERefPatient Profile with PWD Disability Extension ([#24](https://github.com/jgsuess/ph-ereferral/issues/24)) ([466ded3](https://github.com/jgsuess/ph-ereferral/commit/466ded39e7de699d29bf443565da33248d77edc0))
* Add ERefPractitionerRole Profile with examples (closes [#28](https://github.com/jgsuess/ph-ereferral/issues/28)) ([#29](https://github.com/jgsuess/ph-ereferral/issues/29)) ([14208fd](https://github.com/jgsuess/ph-ereferral/commit/14208fdcda4ce510bd57455d337d94f1562f62db))
* Add References page with inline PDF previews and Data Dictionary table ([#17](https://github.com/jgsuess/ph-ereferral/issues/17)) ([#129](https://github.com/jgsuess/ph-ereferral/issues/129)) ([75eaca2](https://github.com/jgsuess/ph-ereferral/commit/75eaca20c88614c92c0e31dcc44ba6583c77cc13))
* **ci:** implement SUSHI and IG Publisher validation pipeline ([#54](https://github.com/jgsuess/ph-ereferral/issues/54)) ([9b7f869](https://github.com/jgsuess/ph-ereferral/commit/9b7f86950fe77584767df79b134aa1266220f3c7))
* **profile:** add ERefMedicationAdministration profile with GPS-valid examples ([#55](https://github.com/jgsuess/ph-ereferral/issues/55)) ([f8747b6](https://github.com/jgsuess/ph-ereferral/commit/f8747b6efb87dbd9119177ac584042f8073e34d8))
* **profile:** add ERefObservation profile with TDG-mapped examples ([#82](https://github.com/jgsuess/ph-ereferral/issues/82)) ([8901323](https://github.com/jgsuess/ph-ereferral/commit/89013236fcd25e6ff7bf951208fdf26c40e49d18))
* **profile:** add ERefProvenance profile with GPS-valid examples ([#61](https://github.com/jgsuess/ph-ereferral/issues/61)) ([9a739d0](https://github.com/jgsuess/ph-ereferral/commit/9a739d02a65124c6d4c171ea10652d6548a6ab27)), closes [#31](https://github.com/jgsuess/ph-ereferral/issues/31)
* **profile:** add ERefTask profile with GPS-valid examples ([#32](https://github.com/jgsuess/ph-ereferral/issues/32)) ([#63](https://github.com/jgsuess/ph-ereferral/issues/63)) ([ea4d832](https://github.com/jgsuess/ph-ereferral/commit/ea4d8321be1804b86f03d045475a417f7e392a8c))
* update referral workflow documentation to use generic terminology ([7642467](https://github.com/jgsuess/ph-ereferral/commit/7642467475d13e4202da46c6849cbeba1f425a5f))


### Bug Fixes

* add smetana layout pragma to all PlantUML diagrams ([b81e370](https://github.com/jgsuess/ph-ereferral/commit/b81e3708aaf79da9463d94944c74a355f8243114))
* **config:** correct canonical URL from urn:// to https:// ([#102](https://github.com/jgsuess/ph-ereferral/issues/102)) ([f3e8b60](https://github.com/jgsuess/ph-ereferral/commit/f3e8b60a09972a335a78f344a9a648ef9746606b)), closes [#64](https://github.com/jgsuess/ph-ereferral/issues/64) [#74](https://github.com/jgsuess/ph-ereferral/issues/74)
* consistent swimlane naming to eliminate duplicate columns ([67922b4](https://github.com/jgsuess/ph-ereferral/commit/67922b46ab4f7768b8a7096bb8a4381712dabcf2))
* **examples:** correct terminology errors found in local build validation ([be026af](https://github.com/jgsuess/ph-ereferral/commit/be026af8dfd53c5aae479ca53878891080267d02))
* **examples:** use GPS-compatible SNOMED CT codes and correct terminology bindings ([#101](https://github.com/jgsuess/ph-ereferral/issues/101)) ([8192613](https://github.com/jgsuess/ph-ereferral/commit/8192613705eb09c11b09e4e2bdc776b6ec7ebcba)), closes [#58](https://github.com/jgsuess/ph-ereferral/issues/58)
* install Ruby and Jekyll in CI/release workflows ([ba4da6d](https://github.com/jgsuess/ph-ereferral/commit/ba4da6d6158412e55379a9739cdd66b27fe73d8d))
* **profile:** remove disabilityRegistration extension from ERefPatient ([#108](https://github.com/jgsuess/ph-ereferral/issues/108)) ([#115](https://github.com/jgsuess/ph-ereferral/issues/115)) ([ebebbdd](https://github.com/jgsuess/ph-ereferral/commit/ebebbdd46f04deaff5846b7e030d94a3b706832c))
* **profile:** update parent of ERefServiceRequest to PHCoreServiceRequest ([#104](https://github.com/jgsuess/ph-ereferral/issues/104)) ([5575755](https://github.com/jgsuess/ph-ereferral/commit/5575755ce8f7f072a40a7c508d1f02a802ece571))
* resolve identifier URI conflicts in erefpatient-example.fsh (closes [#51](https://github.com/jgsuess/ph-ereferral/issues/51)) ([#52](https://github.com/jgsuess/ph-ereferral/issues/52)) ([8e83052](https://github.com/jgsuess/ph-ereferral/commit/8e830520256b21fa9454232a6f928f15eaa5fb5b))
* use {% include X.svg %} for plantuml diagrams (IG Publisher convention) ([434ae32](https://github.com/jgsuess/ph-ereferral/commit/434ae326ffd3f8dbd73e4d1a9ba57f93f351d213))
* use Smetana layout for PlantUML diagrams (no Graphviz needed) ([de66763](https://github.com/jgsuess/ph-ereferral/commit/de667638bf412be58446388d4636b9d047e380d8))
