Instance: medicationadministration-ifa-ex
InstanceOf: MedicationAdministration
Usage: #example
Title: "MedicationAdministration — Iron and Folic Acid"
Description: "Jane dispenses iron and folic acid (IFA) tablets to Charity with instructions to take one tablet daily, following WHO ANC guidelines for nutritional supplementation."
* meta.tag = $peref-dd#REF-38 "REF-38"
* status = #completed
* medicationCodeableConcept = $sct#776023009 "Folic acid and iron only product"
* medicationCodeableConcept.text = "Iron and Folic Acid (IFA) tablets"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* context = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* effectiveDateTime = "2026-02-24"
* performer.actor = Reference(urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c)
* dosage.text = "1 tablet daily"
* dosage.route = $sct#26643006 "Oral route"
* dosage.dose = 1 '{tablet}' "tablet"