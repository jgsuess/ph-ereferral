Instance: observation-chief-complaint-ex
InstanceOf: Observation
Usage: #example
* meta.profile = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation"
* meta.tag = $peref-dd#REF-30 "REF-30"
* status = #final
* category = $observation-category#exam "Exam"
* code = $loinc#10154-3 "Chief complaint - Reported"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* encounter = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* effectiveDateTime = "2026-02-24"
* valueString = "Missed menstrual cycle and nausea"