Instance: servicerequest-ultrasound-ex
InstanceOf: ServiceRequest
Usage: #example
Title: "ServiceRequest — Obstetric Ultrasound Referral"
Description: "Jane refers Charity to Metro Imaging Centre for an obstetric ultrasound to confirm gestational age and due date, needed before 24 weeks of pregnancy."
* meta.tag[0] = $peref-dd#REF-12 "REF-12"
* meta.tag[+] = $peref-dd#REF-13 "REF-13"
* meta.tag[+] = $peref-dd#REF-15 "REF-15"
* meta.tag[+] = $peref-dd#REF-31 "REF-31"
* status = #active
* intent = #order
* priority = #routine
* category = $sct#103693007 "Diagnostic procedure"
* category.text = "Diagnostics"
* code = $sct#268445003 "Ultrasound scan - obstetric"
* code.text = "Obstetric ultrasound to estimate gestational age"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* encounter = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* authoredOn = "2026-02-24"
* requester = Reference(urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d)
* performer = Reference(urn:uuid:1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed)
* reasonReference = Reference(urn:uuid:c3d4e5f6-a7b8-9012-cdef-123456789012)
* note.text = "First ANC contact. LMP approximately New Year 2026; gestational age estimated 12–15 weeks. Ultrasound needed before 24 weeks to confirm dates and due date."