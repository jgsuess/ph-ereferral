Instance: encounter-registration-ex
InstanceOf: Encounter
Usage: #example
Title: "Encounter — Registration"
Description: "A brief ambulatory encounter (08:00–08:15) in which clerk Abraham collects Charity's demographic information and registers her in the system."
* meta.profile = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter"
* meta.tag = $peref-dd#REF-43 "REF-43"
* status = #finished
* class = $v3-ActCode#AMB "ambulatory"
* type = $sct#185349003 "Encounter for check up"
* type.text = "Registration"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* participant.individual = Reference(urn:uuid:3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a)
* serviceProvider = Reference(urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7)
* period.start = "2026-02-24T08:00:00+08:00"
* period.end = "2026-02-24T08:15:00+08:00"