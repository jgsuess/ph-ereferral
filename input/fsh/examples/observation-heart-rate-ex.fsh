Instance: observation-heart-rate-ex
InstanceOf: Observation
Usage: #example
* meta.profile[0] = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation"
* meta.profile[+] = "http://hl7.org/fhir/StructureDefinition/vitalsigns"
* meta.tag = $peref-dd#REF-33 "REF-33"
* status = #final
* category = $observation-category#vital-signs "Vital Signs"
* code = $loinc#8867-4 "Heart rate"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* encounter = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* effectiveDateTime = "2026-02-24T09:00:00+08:00"
* performer = Reference(urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c)
* valueQuantity = 78 '/min' "beats/minute"