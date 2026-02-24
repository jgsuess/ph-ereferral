# Task — Referral Tracking - PH eReferral Implementation Guide v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Task — Referral Tracking**

## Example Task: Task — Referral Tracking

Tags: REF-16 (Details: peref-dd code REF-16), REF-42 (Details: peref-dd code REF-42)

**status**: Requested

**businessStatus**: Requested

**intent**: order

**focus**: [ServiceRequest Ultrasound scan - Loss of pregnancy](Bundle-anc-contact-transaction-ex.md#urn-uuid-f2a3b4c5-d6e7-8901-fabc-012345678901)

**for**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**encounter**: [Encounter: status = finished; class = ambulatory (ActCode#AMB); type = Prenatal initial visit; period = 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800; reasonCode = Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-b2c3d4e5-f6a7-8901-bcde-f12345678901)

**authoredOn**: 2026-02-24

**requester**: [PractitionerRole Nurse](Bundle-anc-contact-transaction-ex.md#urn-uuid-5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d)

**owner**: [Organization Metro Imaging Centre](Bundle-anc-contact-transaction-ex.md#urn-uuid-1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed)



## Resource Content

```json
{
  "resourceType" : "Task",
  "id" : "task-referral-ex",
  "meta" : {
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-16",
      "display" : "REF-16"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-42",
      "display" : "REF-42"
    }]
  },
  "status" : "requested",
  "businessStatus" : {
    "coding" : [{
      "system" : "https://example.com/peref/CodeSystem/referral-disposition",
      "code" : "requested",
      "display" : "Requested"
    }]
  },
  "intent" : "order",
  "focus" : {
    "reference" : "urn:uuid:f2a3b4c5-d6e7-8901-fabc-012345678901"
  },
  "for" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "encounter" : {
    "reference" : "urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901"
  },
  "authoredOn" : "2026-02-24",
  "requester" : {
    "reference" : "urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d"
  },
  "owner" : {
    "reference" : "urn:uuid:1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed"
  }
}

```
