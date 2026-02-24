Instance: practitionerrole-jane-ex
InstanceOf: PractitionerRole
Usage: #example
Title: "PractitionerRole — Nurse Jane"
Description: "Jane's role as a nurse at Barangay Malusog Health Centre, linked to her practitioner record and the sending facility."
* meta.tag = $peref-dd#REF-1 "REF-1"
* practitioner = Reference(urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c)
* organization = Reference(urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7)
* code = $practitioner-role#nurse "Nurse"
* code.text = "Nurse"