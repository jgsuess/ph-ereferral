Instance: organization-sending-facility-ex
InstanceOf: Organization
Usage: #example
* meta.profile = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization"
* meta.tag[0] = $peref-dd#REF-4 "REF-4"
* meta.tag[+] = $peref-dd#REF-5 "REF-5"
* meta.tag[+] = $peref-dd#REF-6 "REF-6"
* meta.tag[+] = $peref-dd#REF-7 "REF-7"
* name = "Barangay Malusog Health Centre"
* identifier.system = "http://doh.gov.ph/fhir/Identifier/doh-nhfr-code"
* identifier.value = "DOH000-OO-0-0000123"
* identifier.type = $v2-0203#FI
* identifier.use = #official
* address.use = #work
* address.line = "123 Health Centre Road"
* address.city = "Quezon City"
* address.state = "NCR"
* address.postalCode = "1100"
* address.country = "PH"
* telecom.system = #phone
* telecom.value = "+63-2-1234-5678"
* telecom.use = #work