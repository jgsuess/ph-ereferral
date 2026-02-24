Instance: servicerequest-lab-orders-ex
InstanceOf: ServiceRequest
Usage: #example
Title: "ServiceRequest — Laboratory Orders"
Description: "Routine ANC laboratory tests ordered for Charity: diabetes screen, hepatitis B surface antigen, and HIV — in line with WHO recommended investigations."
* meta.tag = $peref-dd#REF-39 "REF-39"
* status = #active
* intent = #order
* priority = #routine
* category = $sct#108252007 "Laboratory procedure"
* category.text = "Laboratory"
* code = $sct#15220000 "Laboratory test"
* code.text = "Diabetes screen, Hepatitis B surface antigen, HIV test"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* encounter = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* authoredOn = "2026-02-24"
* requester = Reference(urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d)
* reasonReference = Reference(urn:uuid:c3d4e5f6-a7b8-9012-cdef-123456789012)
* note.text = "Ordered during first ANC contact: diabetes screening, hepatitis B, HIV."