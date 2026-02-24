# PractitionerRole — Clerk Abraham - PH eReferral Implementation Guide v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **PractitionerRole — Clerk Abraham**

## Example PractitionerRole: PractitionerRole — Clerk Abraham

Tag: REF-1 (Details: peref-dd code REF-1)

**practitioner**: [Practitioner Abraham Reyes ](Bundle-registration-transaction-ex.md#urn-uuid-2c6d4f8a-3e5b-4a1c-9f8d-7b6e5d4c3a2b)

**organization**: [Organization Barangay Malusog Health Centre](Bundle-registration-transaction-ex.md#urn-uuid-7c9e6679-7425-40de-944b-e07fc1f90ae7)

**code**: Registration Clerk



## Resource Content

```json
{
  "resourceType" : "PractitionerRole",
  "id" : "practitionerrole-abraham-ex",
  "meta" : {
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-1",
      "display" : "REF-1"
    }]
  },
  "practitioner" : {
    "reference" : "urn:uuid:2c6d4f8a-3e5b-4a1c-9f8d-7b6e5d4c3a2b"
  },
  "organization" : {
    "reference" : "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7"
  },
  "code" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/practitioner-role",
      "code" : "clerk",
      "display" : "Clerk"
    }],
    "text" : "Registration Clerk"
  }]
}

```
