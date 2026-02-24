Instance: condition-pregnancy-ex
InstanceOf: Condition
Usage: #example
Title: "Condition — Pregnancy"
Description: "Charity's confirmed pregnancy, provisionally dated to a last menstrual period around New Year 2026, giving an estimated gestational age of 12–15 weeks."
* meta.tag = $peref-dd#REF-40 "REF-40"
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#provisional "Provisional"
* code = $sct#77386006 "Pregnant"
* subject = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* encounter = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* onsetDateTime = "2026-01-01"
* note.text = "LMP approximately around the New Year holiday; gestational age estimated 12–15 weeks."