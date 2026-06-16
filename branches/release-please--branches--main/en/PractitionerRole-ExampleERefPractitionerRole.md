# Example Referring Practitioner Role - PH eReferral Implementation Guide v0.1.0

## Example PractitionerRole: Example Referring Practitioner Role

Profile: [PH eReferral PractitionerRole](StructureDefinition-ereferral-practitioner-role.md)

**identifier**: `urn:oid:2.16.840.1.113883.2.9.4.3.3`/MD-98765

**active**: true

**practitioner**: [Practitioner Dr. Maria Cruz Santos(official)](Practitioner-ExampleERefPractitioner.md)

**organization**: [Organization Manila General Hospital - Barangay 143 Health Center](Organization-ExampleERefReferringFacility.md)

**code**: Medical practitioner

**specialty**: Internal medicine

**telecom**: [+63 2 8123 4567](tel:+63281234567)



## Resource Content

```json
{
  "resourceType" : "PractitionerRole",
  "id" : "ExampleERefPractitionerRole",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/pheref/StructureDefinition/ereferral-practitioner-role"]
  },
  "identifier" : [{
    "system" : "urn:oid:2.16.840.1.113883.2.9.4.3.3",
    "value" : "MD-98765"
  }],
  "active" : true,
  "practitioner" : {
    "reference" : "Practitioner/ExampleERefPractitioner"
  },
  "organization" : {
    "reference" : "Organization/ExampleERefReferringFacility"
  },
  "code" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "158965000",
      "display" : "Medical practitioner"
    }]
  }],
  "specialty" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "419192003",
      "display" : "Internal medicine"
    }]
  }],
  "telecom" : [{
    "system" : "phone",
    "value" : "+63 2 8123 4567",
    "use" : "work"
  }]
}

```
