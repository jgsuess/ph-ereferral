# Example Referring Facility - PH eReferral Implementation Guide v0.1.0

## Example Organization: Example Referring Facility

Profile: [PH Core Organization](https://build.fhir.org/ig/jgsuess/ph-core/StructureDefinition-ph-core-organization.html)

**identifier**: Facility ID/DOH000000000001234

**active**: true

**type**: Hospital

**name**: Manila General Hospital - Barangay 143 Health Center

**telecom**: [+63 2 8123 4567](tel:+63281234567), [contact@manilagenhosp.ph](mailto:contact@manilagenhosp.ph)

**address**: 123 Rizal Avenue, Barangay 143, Manila, Philippines(work)



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "ExampleERefReferringFacility",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization"]
  },
  "identifier" : [{
    "type" : {
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
        "code" : "FI",
        "display" : "Facility ID"
      }]
    },
    "system" : "https://nhfr.doh.gov.ph/facility",
    "value" : "DOH000000000001234"
  }],
  "active" : true,
  "type" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "code" : "HOSP",
      "display" : "Hospital"
    }]
  }],
  "name" : "Manila General Hospital - Barangay 143 Health Center",
  "telecom" : [{
    "system" : "phone",
    "value" : "+63 2 8123 4567",
    "use" : "work"
  },
  {
    "system" : "email",
    "value" : "contact@manilagenhosp.ph",
    "use" : "work"
  }],
  "address" : [{
    "use" : "work",
    "type" : "both",
    "text" : "123 Rizal Avenue, Barangay 143, Manila, Philippines",
    "line" : ["123 Rizal Avenue"],
    "city" : "Manila",
    "district" : "Barangay 143",
    "state" : "Metro Manila",
    "postalCode" : "1000",
    "country" : "PH"
  }]
}

```
