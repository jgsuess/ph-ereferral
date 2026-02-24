// =============================================================================
// Registration Transaction Bundle (Process A)
// DD Coverage: REF-1, REF-4..REF-7, REF-20..REF-22, REF-24..REF-28, REF-43
// =============================================================================
// This bundle captures the registration of patient Charity at the
// government health centre by clerk Abraham.

Alias: $dd = https://example.com/peref-dd

Instance: registration-transaction-ex
InstanceOf: Bundle
Usage: #example
Description: """
  Registration transaction bundle — Clerk Abraham registers Charity at
  Barangay Malusog Health Centre (Process A: Registration).
  DD elements covered: REF-1 (practitioner), REF-4..REF-7 (sending facility),
  REF-20..REF-22 (patient name/gender/DOB), REF-24..REF-27 (identifiers/address/phone),
  REF-28 (next of kin), REF-43 (encounter).
"""
* type = #transaction
* timestamp = "2026-02-24T08:15:00+08:00"

// --- REF-20..REF-27: Patient (Charity) ---
* entry[0].fullUrl = "urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479"
* entry[=].resource = patient-charity-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Patient"

// --- REF-28: RelatedPerson (companion / next of kin) ---
* entry[+].fullUrl = "urn:uuid:6ba7b810-9dad-11d1-80b4-00c04fd430c8"
* entry[=].resource = relatedperson-companion-ex
* entry[=].request.method = #POST
* entry[=].request.url = "RelatedPerson"

// --- REF-4..REF-7: Sending Organization (health centre) ---
* entry[+].fullUrl = "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7"
* entry[=].resource = organization-sending-facility-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Organization"

// --- REF-1: Practitioner (Abraham) ---
* entry[+].fullUrl = "urn:uuid:2c6d4f8a-3e5b-4a1c-9f8d-7b6e5d4c3a2b"
* entry[=].resource = practitioner-abraham-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Practitioner"

// --- REF-1: PractitionerRole (Abraham → clerk) ---
* entry[+].fullUrl = "urn:uuid:3d7e5a9b-4f6c-5b2d-0a9e-8c7f6e5d4c3a"
* entry[=].resource = practitionerrole-abraham-ex
* entry[=].request.method = #POST
* entry[=].request.url = "PractitionerRole"

// --- REF-43: Encounter (registration) ---
* entry[+].fullUrl = "urn:uuid:a1b2c3d4-e5f6-7890-abcd-ef1234567890"
* entry[=].resource = encounter-registration-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Encounter"
