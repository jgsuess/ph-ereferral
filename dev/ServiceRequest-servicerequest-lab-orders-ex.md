# ServiceRequest — Laboratory Orders - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ServiceRequest — Laboratory Orders**

## Example ServiceRequest: ServiceRequest — Laboratory Orders

Tag: REF-39 (Details: peref-dd code REF-39)

**status**: Active

**intent**: Order

**category**: Laboratory

**priority**: Routine

**code**: Diabetes screen, Hepatitis B surface antigen, HIV test

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**encounter**: [Encounter: status = finished; class = ambulatory (ActCode#AMB); type = Prenatal initial visit; period = 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800; reasonCode = Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-b2c3d4e5-f6a7-8901-bcde-f12345678901)

**authoredOn**: 2026-02-24

**requester**: [PractitionerRole Nurse](Bundle-anc-contact-transaction-ex.md#urn-uuid-5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d)

**reasonReference**: [Condition Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-c3d4e5f6-a7b8-9012-cdef-123456789012)

**note**: 

> 

Ordered during first ANC contact: diabetes screening, hepatitis B, HIV.




## Resource Content

```json
{
  "resourceType" : "ServiceRequest",
  "id" : "servicerequest-lab-orders-ex",
  "meta" : {
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-39",
      "display" : "REF-39"
    }]
  },
  "status" : "active",
  "intent" : "order",
  "category" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "108252007",
      "display" : "Laboratory procedure"
    }],
    "text" : "Laboratory"
  }],
  "priority" : "routine",
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "15220000",
      "display" : "Laboratory test"
    }],
    "text" : "Diabetes screen, Hepatitis B surface antigen, HIV test"
  },
  "subject" : {
    "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
  },
  "encounter" : {
    "reference" : "urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901"
  },
  "authoredOn" : "2026-02-24",
  "requester" : {
    "reference" : "urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d"
  },
  "reasonReference" : [{
    "reference" : "urn:uuid:c3d4e5f6-a7b8-9012-cdef-123456789012"
  }],
  "note" : [{
    "text" : "Ordered during first ANC contact: diabetes screening, hepatitis B, HIV."
  }]
}

```
