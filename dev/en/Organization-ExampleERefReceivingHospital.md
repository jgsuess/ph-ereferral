# Example Receiving Hospital - PH eReferral Implementation Guide v0.1.0

## Example Organization: Example Receiving Hospital

Profile: [PH Core Organization](file:///home/runner/work/ph-core/ph-core/output/StructureDefinition-ph-core-organization.html)

**identifier**: `urn:oid:2.16.840.1.113883.2.9.4.1.1`/HOSP-QC-001

**active**: true

**type**: Healthcare Provider

**name**: Philippine Heart Center

**address**: East Avenue Quezon City Metro Manila 1100 PH 



## Resource Content

```json
{
  "resourceType" : "Organization",
  "id" : "ExampleERefReceivingHospital",
  "meta" : {
    "profile" : ["https://fhir.doh.gov.ph/phcore/StructureDefinition/ph-core-organization"]
  },
  "identifier" : [{
    "system" : "urn:oid:2.16.840.1.113883.2.9.4.1.1",
    "value" : "HOSP-QC-001"
  }],
  "active" : true,
  "type" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
      "code" : "prov",
      "display" : "Healthcare Provider"
    }]
  }],
  "name" : "Philippine Heart Center",
  "address" : [{
    "line" : ["East Avenue"],
    "city" : "Quezon City",
    "state" : "Metro Manila",
    "postalCode" : "1100",
    "country" : "PH"
  }]
}

```
