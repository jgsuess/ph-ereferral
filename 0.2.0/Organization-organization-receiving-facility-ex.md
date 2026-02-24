# Organization — Metro Imaging Centre - PH eReferral Implementation Guide v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Organization — Metro Imaging Centre**

## Example Organization: Organization — Metro Imaging Centre

Profile: [PH Core Organization](https://build.fhir.org/ig/UP-Manila-SILab/ph-core/StructureDefinition-ph-core-organization.html)

Tags: REF-9 (Details: peref-dd code REF-9), REF-10 (Details: peref-dd code REF-10)

**identifier**: Facility ID/DOH000-OO-0-0000456 (use: official, )

**name**: Metro Imaging Centre



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "organization-receiving-facility-ex",
  "meta" : {
    "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization"],
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-9",
      "display" : "REF-9"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-10",
      "display" : "REF-10"
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
    "value" : "DOH000-OO-0-0000456"
  }],
  "name" : "Metro Imaging Centre"
}

```
