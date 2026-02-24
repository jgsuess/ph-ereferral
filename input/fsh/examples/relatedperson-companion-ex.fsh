Instance: relatedperson-companion-ex
InstanceOf: RelatedPerson
Usage: #example
Title: "RelatedPerson — Maria Santos (Mother)"
Description: "Charity's mother Maria, registered as her next-of-kin and alternative contact person during the registration process."
* meta.profile = "http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-relatedperson"
* meta.tag = $peref-dd#REF-28 "REF-28"
* patient = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* relationship = $v3-RoleCode#MTH "Mother"
* name.family = "Santos"
* name.given = "Maria"
* telecom.system = #phone
* telecom.value = "+63-917-765-4321"
* telecom.use = #mobile