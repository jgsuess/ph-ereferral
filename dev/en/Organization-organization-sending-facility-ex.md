# Organization — Barangay Malusog Health Centre - PH eReferral Implementation Guide v0.1.0

## Example Organization: Organization — Barangay Malusog Health Centre

Profile: `http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization`

Tags: , , , 

**identifier**: Facility ID/DOH000-OO-0-0000123 (use: official, )

**name**: Barangay Malusog Health Centre

**telecom**: [+63-2-1234-5678](tel:+63-2-1234-5678)

**address**: 123 Health Centre Road Quezon City NCR 1100 PH (work)



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "organization-sending-facility-ex",
  "meta" : {
    "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization"],
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-4",
      "display" : "REF-4"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-5",
      "display" : "REF-5"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-6",
      "display" : "REF-6"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-7",
      "display" : "REF-7"
    }]
  },
  "identifier" : [{
    "use" : "official",
    "type" : {
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
        "code" : "FI"
      }]
    },
    "system" : "http://doh.gov.ph/fhir/Identifier/doh-nhfr-code",
    "value" : "DOH000-OO-0-0000123"
  }],
  "name" : "Barangay Malusog Health Centre",
  "telecom" : [{
    "system" : "phone",
    "value" : "+63-2-1234-5678",
    "use" : "work"
  }],
  "address" : [{
    "use" : "work",
    "line" : ["123 Health Centre Road"],
    "city" : "Quezon City",
    "state" : "NCR",
    "postalCode" : "1100",
    "country" : "PH"
  }]
}

```
