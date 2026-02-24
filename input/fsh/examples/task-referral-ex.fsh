Instance: task-referral-ex
InstanceOf: Task
Usage: #example
Title: "Task — Referral Tracking"
Description: "Tracks the status of Charity's ultrasound referral. Currently in 'requested' state, awaiting acceptance by Metro Imaging Centre."
* meta.tag[0] = $peref-dd#REF-16 "REF-16"
* meta.tag[+] = $peref-dd#REF-42 "REF-42"
* status = #requested
* businessStatus = $referral-disposition#requested "Requested"
* intent = #order
* focus = Reference(urn:uuid:f2a3b4c5-d6e7-8901-fabc-012345678901)
* for = Reference(urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479)
* encounter = Reference(urn:uuid:b2c3d4e5-f6a7-8901-bcde-f12345678901)
* authoredOn = "2026-02-24"
* requester = Reference(urn:uuid:5f9a7c1d-6b8e-7d4f-2c1a-0e9b8a7f6e5d)
* owner = Reference(urn:uuid:1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed)