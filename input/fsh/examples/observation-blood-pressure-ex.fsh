Instance: observation-blood-pressure-ex
InstanceOf: Observation
Usage: #example
* meta.profile[0] = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation"
* meta.profile[+] = "http://hl7.org/fhir/StructureDefinition/vitalsigns"
* meta.profile[+] = "http://hl7.org/fhir/StructureDefinition/bp"
* meta.tag = $peref-dd#REF-32 "REF-32"
* status = #final
* category = $observation-category#vital-signs "Vital Signs"
* code = $loinc#85354-9 "Blood pressure panel with all children optional"
* code.text = "Blood pressure systolic & diastolic"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* encounter = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* effectiveDateTime = "2026-02-24T09:00:00+08:00"
* performer = Reference(urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c)
* component[0].code = $loinc#8480-6 "Systolic blood pressure"
* component[=].valueQuantity = 110 'mm[Hg]' "mmHg"
* component[+].code = $loinc#8462-4 "Diastolic blood pressure"
* component[=].valueQuantity = 70 'mm[Hg]' "mmHg"