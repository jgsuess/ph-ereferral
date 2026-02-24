# registration-transaction-ex - PH eReferral Implementation Guide v0.3.0-draft

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **registration-transaction-ex**

## Example Bundle: registration-transaction-ex



## Resource Content

```json
{
  "resourceType" : "Bundle",
  "id" : "registration-transaction-ex",
  "type" : "transaction",
  "timestamp" : "2026-02-24T08:15:00+08:00",
  "entry" : [{
    "fullUrl" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "resource" : {
      "resourceType" : "Patient",
      "id" : "patient-charity-ex",
      "meta" : {
        "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-patient"],
        "tag" : [{
          "system" : "https://example.com/peref-dd",
          "code" : "REF-20",
          "display" : "REF-20"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-21",
          "display" : "REF-21"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-22",
          "display" : "REF-22"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-24",
          "display" : "REF-24"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-25",
          "display" : "REF-25"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-26",
          "display" : "REF-26"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-27",
          "display" : "REF-27"
        }]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Patient_patient-charity-ex\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Patient patient-charity-ex</b></p><a name=\"patient-charity-ex\"> </a><a name=\"hcpatient-charity-ex\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profile: <a href=\"https://build.fhir.org/ig/UP-Manila-SILab/ph-core/StructureDefinition-ph-core-patient.html\">PH Core Patient</a></p><p style=\"margin-bottom: 0px\">Tags: REF-20 (Details: peref-dd code REF-20), REF-21 (Details: peref-dd code REF-21), REF-22 (Details: peref-dd code REF-22), REF-24 (Details: peref-dd code REF-24), REF-25 (Details: peref-dd code REF-25), REF-26 (Details: peref-dd code REF-26), REF-27 (Details: peref-dd code REF-27)</p></div><p style=\"border: 1px #661aff solid; background-color: #e6e6ff; padding: 10px;\">Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)</p><hr/><table class=\"grid\"><tr><td style=\"background-color: #f3f5da\" title=\"Record is active\">Active:</td><td colspan=\"3\">true</td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Other Id (see the one above)\">Other Id:</td><td colspan=\"3\"><code>http://doh.gov.ph/fhir/ph-core/NamingSystem/philhealth-id-ns</code>/12-345678901-2</td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Ways to contact the Patient\">Contact Detail</td><td colspan=\"3\"><ul><li><a href=\"tel:+63-917-123-4567\">+63-917-123-4567</a></li><li>456 Rizal Street Barangay Malusog Quezon City 1100 PH (home)</li></ul></td></tr></table></div>"
      },
      "identifier" : [{
        "system" : "http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns",
        "value" : "1234-5678901-2"
      },
      {
        "system" : "http://doh.gov.ph/fhir/ph-core/NamingSystem/philhealth-id-ns",
        "value" : "12-345678901-2"
      }],
      "active" : true,
      "name" : [{
        "use" : "official",
        "family" : "Santos",
        "given" : ["Charity"]
      }],
      "telecom" : [{
        "system" : "phone",
        "value" : "+63-917-123-4567",
        "use" : "mobile"
      }],
      "gender" : "female",
      "birthDate" : "2001-08-15",
      "address" : [{
        "use" : "home",
        "line" : ["456 Rizal Street", "Barangay Malusog"],
        "city" : "Quezon City",
        "district" : "NCR",
        "postalCode" : "1100",
        "country" : "PH"
      }]
    },
    "request" : {
      "method" : "POST",
      "url" : "Patient"
    }
  },
  {
    "fullUrl" : "urn:uuid:6ba7b810-9dad-11d1-80b4-00c04fd430c8",
    "resource" : {
      "resourceType" : "RelatedPerson",
      "id" : "relatedperson-companion-ex",
      "meta" : {
        "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-relatedperson"],
        "tag" : [{
          "system" : "https://example.com/peref-dd",
          "code" : "REF-28",
          "display" : "REF-28"
        }]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"RelatedPerson_relatedperson-companion-ex\"> </a><p class=\"res-header-id\"><b>Generated Narrative: RelatedPerson relatedperson-companion-ex</b></p><a name=\"relatedperson-companion-ex\"> </a><a name=\"hcrelatedperson-companion-ex\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profile: <a href=\"https://build.fhir.org/ig/UP-Manila-SILab/ph-core/StructureDefinition-ph-core-relatedperson.html\">PH Core RelatedPerson</a></p><p style=\"margin-bottom: 0px\">Tag: REF-28 (Details: peref-dd code REF-28)</p></div><p><b>patient</b>: <a href=\"Bundle-registration-transaction-ex.html#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479\">Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)</a></p><p><b>relationship</b>: <span title=\"Codes:{http://terminology.hl7.org/CodeSystem/v3-RoleCode MTH}\">Mother</span></p><p><b>name</b>: Maria Santos </p><p><b>telecom</b>: <a href=\"tel:+63-917-765-4321\">+63-917-765-4321</a></p></div>"
      },
      "patient" : {
        "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
      },
      "relationship" : [{
        "coding" : [{
          "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
          "code" : "MTH",
          "display" : "Mother"
        }]
      }],
      "name" : [{
        "family" : "Santos",
        "given" : ["Maria"]
      }],
      "telecom" : [{
        "system" : "phone",
        "value" : "+63-917-765-4321",
        "use" : "mobile"
      }]
    },
    "request" : {
      "method" : "POST",
      "url" : "RelatedPerson"
    }
  },
  {
    "fullUrl" : "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "resource" : {
      "resourceType" : "Organization",
      "id" : "organization-sending-facility-ex",
      "meta" : {
        "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization"],
        "tag" : [{
          "system" : "https://example.com/peref-dd",
          "code" : "REF-4",
          "display" : "REF-4"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-5",
          "display" : "REF-5"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-6",
          "display" : "REF-6"
        },
        {
          "system" : "https://example.com/peref-dd",
          "code" : "REF-7",
          "display" : "REF-7"
        }]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Organization_organization-sending-facility-ex\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Organization organization-sending-facility-ex</b></p><a name=\"organization-sending-facility-ex\"> </a><a name=\"hcorganization-sending-facility-ex\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profile: <a href=\"https://build.fhir.org/ig/UP-Manila-SILab/ph-core/StructureDefinition-ph-core-organization.html\">PH Core Organization</a></p><p style=\"margin-bottom: 0px\">Tags: REF-4 (Details: peref-dd code REF-4), REF-5 (Details: peref-dd code REF-5), REF-6 (Details: peref-dd code REF-6), REF-7 (Details: peref-dd code REF-7)</p></div><p><b>identifier</b>: Facility ID/DOH000-OO-0-0000123 (use: official, )</p><p><b>name</b>: Barangay Malusog Health Centre</p><p><b>telecom</b>: <a href=\"tel:+63-2-1234-5678\">+63-2-1234-5678</a></p><p><b>address</b>: 123 Health Centre Road Quezon City NCR 1100 PH (work)</p></div>"
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
        "value" : "DOH000-OO-0-0000123"
      }],
      "name" : "Barangay Malusog Health Centre",
      "telecom" : [{
        "system" : "phone",
        "value" : "+63-2-1234-5678",
        "use" : "work"
      }],
      "address" : [{
        "use" : "work",
        "line" : ["123 Health Centre Road"],
        "city" : "Quezon City",
        "state" : "NCR",
        "postalCode" : "1100",
        "country" : "PH"
      }]
    },
    "request" : {
      "method" : "POST",
      "url" : "Organization"
    }
  },
  {
    "fullUrl" : "urn:uuid:2c6d4f8a-3e5b-4a1c-9f8d-7b6e5d4c3a2b",
    "resource" : {
      "resourceType" : "Practitioner",
      "id" : "practitioner-abraham-ex",
      "meta" : {
        "tag" : [{
          "system" : "https://example.com/peref-dd",
          "code" : "REF-1",
          "display" : "REF-1"
        }]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Practitioner_practitioner-abraham-ex\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Practitioner practitioner-abraham-ex</b></p><a name=\"practitioner-abraham-ex\"> </a><a name=\"hcpractitioner-abraham-ex\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Tag: REF-1 (Details: peref-dd code REF-1)</p></div><p><b>name</b>: Abraham Reyes </p></div>"
      },
      "name" : [{
        "family" : "Reyes",
        "given" : ["Abraham"]
      }]
    },
    "request" : {
      "method" : "POST",
      "url" : "Practitioner"
    }
  },
  {
    "fullUrl" : "urn:uuid:3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a",
    "resource" : {
      "resourceType" : "PractitionerRole",
      "id" : "practitionerrole-abraham-ex",
      "meta" : {
        "tag" : [{
          "system" : "https://example.com/peref-dd",
          "code" : "REF-1",
          "display" : "REF-1"
        }]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"PractitionerRole_practitionerrole-abraham-ex\"> </a><p class=\"res-header-id\"><b>Generated Narrative: PractitionerRole practitionerrole-abraham-ex</b></p><a name=\"practitionerrole-abraham-ex\"> </a><a name=\"hcpractitionerrole-abraham-ex\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Tag: REF-1 (Details: peref-dd code REF-1)</p></div><p><b>practitioner</b>: <a href=\"Bundle-registration-transaction-ex.html#urn-uuid-2c6d4f8a-3e5b-4a1c-9f8d-7b6e5d4c3a2b\">Practitioner Abraham Reyes </a></p><p><b>organization</b>: <a href=\"Bundle-registration-transaction-ex.html#urn-uuid-7c9e6679-7425-40de-944b-e07fc1f90ae7\">Organization Barangay Malusog Health Centre</a></p><p><b>code</b>: <span title=\"Codes:{http://terminology.hl7.org/CodeSystem/practitioner-role clerk}\">Registration Clerk</span></p></div>"
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
    },
    "request" : {
      "method" : "POST",
      "url" : "PractitionerRole"
    }
  },
  {
    "fullUrl" : "urn:uuid:a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "resource" : {
      "resourceType" : "Encounter",
      "id" : "encounter-registration-ex",
      "meta" : {
        "profile" : ["http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter"],
        "tag" : [{
          "system" : "https://example.com/peref-dd",
          "code" : "REF-43",
          "display" : "REF-43"
        }]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Encounter_encounter-registration-ex\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Encounter encounter-registration-ex</b></p><a name=\"encounter-registration-ex\"> </a><a name=\"hcencounter-registration-ex\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profile: <a href=\"https://build.fhir.org/ig/UP-Manila-SILab/ph-core/StructureDefinition-ph-core-encounter.html\">PH Core Encounter</a></p><p style=\"margin-bottom: 0px\">Tag: REF-43 (Details: peref-dd code REF-43)</p></div><p><b>status</b>: Finished</p><p><b>class</b>: <a href=\"http://terminology.hl7.org/7.0.1/CodeSystem-v3-ActCode.html#v3-ActCode-AMB\">ActCode: AMB</a> (ambulatory)</p><p><b>type</b>: <span title=\"Codes:{http://snomed.info/sct 185349003}\">Registration</span></p><p><b>subject</b>: <a href=\"Bundle-registration-transaction-ex.html#urn-uuid-f47ac10b-58cc-4372-a567-0e02b2c3d479\">Charity Santos (official) Female, DoB: 2001-08-15 ( http://doh.gov.ph/fhir/ph-core/NamingSystem/philsys-id-ns#1234-5678901-2)</a></p><h3>Participants</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>Individual</b></td></tr><tr><td style=\"display: none\">*</td><td><a href=\"Bundle-registration-transaction-ex.html#urn-uuid-3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a\">PractitionerRole Clerk</a></td></tr></table><p><b>period</b>: 2026-02-24 08:00:00+0800 --&gt; 2026-02-24 08:15:00+0800</p><p><b>serviceProvider</b>: <a href=\"Bundle-registration-transaction-ex.html#urn-uuid-7c9e6679-7425-40de-944b-e07fc1f90ae7\">Organization Barangay Malusog Health Centre</a></p></div>"
      },
      "status" : "finished",
      "class" : {
        "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "code" : "AMB",
        "display" : "ambulatory"
      },
      "type" : [{
        "coding" : [{
          "system" : "http://snomed.info/sct",
          "code" : "185349003",
          "display" : "Encounter for check up"
        }],
        "text" : "Registration"
      }],
      "subject" : {
        "reference" : "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
      },
      "participant" : [{
        "individual" : {
          "reference" : "urn:uuid:3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a"
        }
      }],
      "period" : {
        "start" : "2026-02-24T08:00:00+08:00",
        "end" : "2026-02-24T08:15:00+08:00"
      },
      "serviceProvider" : {
        "reference" : "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7"
      }
    },
    "request" : {
      "method" : "POST",
      "url" : "Encounter"
    }
  }]
}

```
