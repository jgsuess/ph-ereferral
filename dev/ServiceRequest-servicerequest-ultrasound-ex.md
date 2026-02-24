# ServiceRequest — Obstetric Ultrasound Referral - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ServiceRequest — Obstetric Ultrasound Referral**

## Example ServiceRequest: ServiceRequest — Obstetric Ultrasound Referral

Tags: REF-12 (Details: peref-dd code REF-12), REF-13 (Details: peref-dd code REF-13), REF-15 (Details: peref-dd code REF-15), REF-31 (Details: peref-dd code REF-31)

**status**: Active

**intent**: Order

**category**: Diagnostics

**priority**: Routine

**code**: Obstetric ultrasound to estimate gestational age

**subject**: [Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)](Bundle-registration-transaction-ex.md#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479)

**encounter**: [Encounter: status = finished; class = ambulatory (ActCode#AMB); type = Prenatal initial visit; period = 2026-02-24 08:30:00+0800 --> 2026-02-24 10:00:00+0800; reasonCode = Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-b2c3d4e5-f6a7-8901-bcde-f12345678901)

**authoredOn**: 2026-02-24

**requester**: [PractitionerRole Nurse](Bundle-anc-contact-transaction-ex.md#urn-uuid-5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d)

**performer**: [Organization Metro Imaging Centre](Bundle-anc-contact-transaction-ex.md#urn-uuid-1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed)

**reasonReference**: [Condition Pregnant](Bundle-anc-contact-transaction-ex.md#urn-uuid-c3d4e5f6-a7b8-9012-cdef-123456789012)

**note**: 

> 

First ANC contact. LMP approximately New Year 2026; gestational age estimated 12–15 weeks. Ultrasound needed before 24 weeks to confirm dates and due date.




## Resource Content

```json
{
  "resourceType" : "ServiceRequest",
  "id" : "servicerequest-ultrasound-ex",
  "meta" : {
    "tag" : [{
      "system" : "https://example.com/peref-dd",
      "code" : "REF-12",
      "display" : "REF-12"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-13",
      "display" : "REF-13"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-15",
      "display" : "REF-15"
    },
    {
      "system" : "https://example.com/peref-dd",
      "code" : "REF-31",
      "display" : "REF-31"
    }]
  },
  "status" : "active",
  "intent" : "order",
  "category" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "103693007",
      "display" : "Diagnostic procedure"
    }],
    "text" : "Diagnostics"
  }],
  "priority" : "routine",
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "268445003",
      "display" : "Ultrasound scan - Loss of pregnancy"
    }],
    "text" : "Obstetric ultrasound to estimate gestational age"
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
  "performer" : [{
    "reference" : "urn:uuid:1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed"
  }],
  "reasonReference" : [{
    "reference" : "urn:uuid:c3d4e5f6-a7b8-9012-cdef-123456789012"
  }],
  "note" : [{
    "text" : "First ANC contact. LMP approximately New Year 2026; gestational age estimated 12–15 weeks. Ultrasound needed before 24 weeks to confirm dates and due date."
  }]
}

```
