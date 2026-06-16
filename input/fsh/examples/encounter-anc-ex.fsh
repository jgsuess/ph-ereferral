Instance: encounter-anc-ex
InstanceOf: Encounter
Usage: #example
Title: "Encounter — First Antenatal Care Contact"
Description: "The counselling session (08:30–10:00) in which nurse Jane confirms Charity's pregnancy, records vital signs and clinical history, and initiates the referral."
* meta.profile = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter"
* meta.tag = $peref-dd#REF-43 "REF-43"
* status = #finished
* class = $v3-ActCode#AMB "ambulatory"
* type = $sct#424619006 "Prenatal visit"
* type.text = "First antenatal care contact"
* reasonCode = $sct#77386006 "Pregnant"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* participant.individual = Reference(urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d)
* serviceProvider = Reference(urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7)
* period.start = "2026-02-24T08:30:00+08:00"
* period.end = "2026-02-24T10:00:00+08:00"