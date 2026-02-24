// =============================================================================
// ANC Contact Transaction Bundle (Process B)
// DD Coverage: REF-1, REF-9..REF-10, REF-12..REF-13, REF-15..REF-16,
//              REF-30..REF-40, REF-42..REF-43
// =============================================================================
// This bundle captures nurse Jane's first antenatal care contact with
// Charity: examination, observations, pregnancy confirmation, IFA
// dispensing, ultrasound referral, and lab orders.

Instance: anc-contact-transaction-ex
InstanceOf: Bundle
Usage: #example
Description: """
  ANC contact transaction bundle — Nurse Jane conducts the first antenatal
  care visit for Charity at Barangay Malusog Health Centre (Process B: Routine ANC).
  DD elements covered: REF-1 (practitioner Jane), REF-9..REF-10 (receiving facility),
  REF-12..REF-13 (referral date/category), REF-15 (reason for referral),
  REF-16 + REF-42 (task/response), REF-30 (chief complaint), REF-31 (clinical history),
  REF-32..REF-37 (vitals), REF-38 (treatment/IFA), REF-39 (lab orders),
  REF-40 (working impression), REF-43 (encounter).
"""
* type = #transaction
* timestamp = "2026-02-24T10:00:00+08:00"

// --- REF-1: Practitioner (Jane) ---
* entry[0].fullUrl = "urn:uuid:4e8f6b0c-5a7d-6c3e-1b0f-9d8a7f6e5d4c"
* entry[=].resource = practitioner-jane-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Practitioner"

// --- REF-1: PractitionerRole (Jane → nurse) ---
* entry[+].fullUrl = "urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d"
* entry[=].resource = practitionerrole-jane-ex
* entry[=].request.method = #POST
* entry[=].request.url = "PractitionerRole"

// --- REF-9, REF-10: Receiving Organization (imaging centre) ---
* entry[+].fullUrl = "urn:uuid:1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed"
* entry[=].resource = organization-receiving-facility-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Organization"

// --- REF-43: Encounter (ANC contact) ---
* entry[+].fullUrl = "urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901"
* entry[=].resource = encounter-anc-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Encounter"

// --- REF-40: Condition (pregnancy — working impression) ---
* entry[+].fullUrl = "urn:uuid:c3d4e5f6-a7b8-9012-cdef-123456789012"
* entry[=].resource = condition-pregnancy-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Condition"

// --- REF-30: Observation (chief complaint) ---
* entry[+].fullUrl = "urn:uuid:d4e5f6a7-b8c9-0123-defa-234567890123"
* entry[=].resource = observation-chief-complaint-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Observation"

// --- REF-32: Observation (blood pressure) ---
* entry[+].fullUrl = "urn:uuid:e5f6a7b8-c9d0-1234-efab-345678901234"
* entry[=].resource = observation-blood-pressure-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Observation"

// --- REF-33: Observation (heart rate) ---
* entry[+].fullUrl = "urn:uuid:f6a7b8c9-d0e1-2345-fabc-456789012345"
* entry[=].resource = observation-heart-rate-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Observation"

// --- REF-34: Observation (respiratory rate) ---
* entry[+].fullUrl = "urn:uuid:a7b8c9d0-e1f2-3456-abcd-567890123456"
* entry[=].resource = observation-respiratory-rate-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Observation"

// --- REF-35: Observation (oxygen saturation) ---
* entry[+].fullUrl = "urn:uuid:b8c9d0e1-f2a3-4567-bcde-678901234567"
* entry[=].resource = observation-oxygen-saturation-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Observation"

// --- REF-36: Observation (temperature) ---
* entry[+].fullUrl = "urn:uuid:c9d0e1f2-a3b4-5678-cdef-789012345678"
* entry[=].resource = observation-temperature-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Observation"

// --- REF-37: Observation (weight) ---
* entry[+].fullUrl = "urn:uuid:d0e1f2a3-b4c5-6789-defa-890123456789"
* entry[=].resource = observation-weight-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Observation"

// --- REF-38: MedicationAdministration (IFA tablets) ---
* entry[+].fullUrl = "urn:uuid:e1f2a3b4-c5d6-7890-efab-901234567890"
* entry[=].resource = medicationadministration-ifa-ex
* entry[=].request.method = #POST
* entry[=].request.url = "MedicationAdministration"

// --- REF-12, REF-13, REF-15, REF-31: ServiceRequest (ultrasound referral) ---
* entry[+].fullUrl = "urn:uuid:f2a3b4c5-d6e7-8901-fabc-012345678901"
* entry[=].resource = servicerequest-ultrasound-ex
* entry[=].request.method = #POST
* entry[=].request.url = "ServiceRequest"

// --- REF-39: ServiceRequest (lab orders) ---
* entry[+].fullUrl = "urn:uuid:a3b4c5d6-e7f8-9012-abcd-123456789012"
* entry[=].resource = servicerequest-lab-orders-ex
* entry[=].request.method = #POST
* entry[=].request.url = "ServiceRequest"

// --- REF-16, REF-42: Task (referral tracking) ---
* entry[+].fullUrl = "urn:uuid:b4c5d6e7-f8a9-0123-bcde-234567890123"
* entry[=].resource = task-referral-ex
* entry[=].request.method = #POST
* entry[=].request.url = "Task"
