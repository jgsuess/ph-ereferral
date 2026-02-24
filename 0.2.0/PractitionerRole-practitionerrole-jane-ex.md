# PractitionerRole — Nurse Jane - PH eReferral Implementation Guide v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **PractitionerRole — Nurse Jane**

## Example PractitionerRole: PractitionerRole — Nurse Jane

Tag: REF-1 (Details: peref-dd code REF-1)

**practitioner**: [Practitioner Jane Dela Cruz ](Bundle-anc-contact-transaction-ex.md#urn-uuid-4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c)

**organization**: [Organization Barangay Malusog Health Centre](Bundle-registration-transaction-ex.md#urn-uuid-7c9e6679-7425-40de-944b-e07fc1f90ae7)

**code**: Nurse



## Resource Content

```json
{
  "resourceType" : "PractitionerRole",
  "id" : "practitionerrole-jane-ex",
  "meta" : {
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-1",
      "display" : "REF-1"
    }]
  },
  "practitioner" : {
    "reference" : "urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c"
  },
  "organization" : {
    "reference" : "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7"
  },
  "code" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/practitioner-role",
      "code" : "nurse",
      "display" : "Nurse"
    }],
    "text" : "Nurse"
  }]
}

```
