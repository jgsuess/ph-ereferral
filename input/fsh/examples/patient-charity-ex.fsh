Instance: patient-charity-ex
InstanceOf: Patient
Usage: #example
Title: "Patient — Charity Santos"
Description: "Charity is a 24-year-old woman from Barangay Malusog, Quezon City, visiting the health centre for the first time during her pregnancy. Abraham registers her demographics, national IDs, and contact details."
* meta.profile = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-patient"
* meta.tag[0] = $peref-dd#REF-20 "REF-20"
* meta.tag[+] = $peref-dd#REF-21 "REF-21"
* meta.tag[+] = $peref-dd#REF-22 "REF-22"
* meta.tag[+] = $peref-dd#REF-24 "REF-24"
* meta.tag[+] = $peref-dd#REF-25 "REF-25"
* meta.tag[+] = $peref-dd#REF-26 "REF-26"
* meta.tag[+] = $peref-dd#REF-27 "REF-27"
* active = true
* name.use = #official
* name.family = "Santos"
* name.given = "Charity"
* gender = #female
* birthDate = "2001-08-15"
* identifier[0].system = "http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns"
* identifier[=].value = "1234-5678901-2"
* identifier[+].system = "http://doh.gov.ph/fhir/ph-core/NamingSystem/philhealth-id-ns"
* identifier[=].value = "12-345678901-2"
* address.use = #home
* address.line[0] = "456 Rizal Street"
* address.line[+] = "Barangay Malusog"
* address.city = "Quezon City"
* address.district = "NCR"
* address.postalCode = "1100"
* address.country = "PH"
* telecom.system = #phone
* telecom.value = "+63-917-123-4567"
* telecom.use = #mobile