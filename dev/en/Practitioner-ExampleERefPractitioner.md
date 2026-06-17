# Example Referring Practitioner - PH eReferral Implementation Guide v0.1.0

## Example Practitioner: Example Referring Practitioner

Profile: [PH Core Practitioner](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-practitioner.html)

**identifier**: `urn:oid:2.16.840.1.113883.2.9.4.3.3`/PRAC-12345

**active**: true

**name**: Dr. Maria Cruz Santos(Official)

**telecom**: [+63 2 8123 4567](tel:+63281234567), [mcsantos@hospital.ph](mailto:mcsantos@hospital.ph)

**gender**: Female

### Qualifications

| | |
| :--- | :--- |
| - | **Code** |
| * | Medical practitioner |



## Resource Content

```json
{
  "resourceType" : "Practitioner",
  "id" : "ExampleERefPractitioner",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-practitioner"]
  },
  "identifier" : [{
    "system" : "urn:oid:2.16.840.1.113883.2.9.4.3.3",
    "value" : "PRAC-12345"
  }],
  "active" : true,
  "name" : [{
    "use" : "official",
    "text" : "Dr. Maria Cruz Santos",
    "family" : "Santos",
    "given" : ["Maria", "Cruz"],
    "prefix" : ["Dr."]
  }],
  "telecom" : [{
    "system" : "phone",
    "value" : "+63 2 8123 4567",
    "use" : "work"
  },
  {
    "system" : "email",
    "value" : "mcsantos@hospital.ph",
    "use" : "work"
  }],
  "gender" : "female",
  "qualification" : [{
    "code" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "158965000",
        "display" : "Medical practitioner"
      }]
    }
  }]
}

```
