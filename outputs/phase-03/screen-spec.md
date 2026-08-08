# Screen Specification and Information Architecture

> **SYNTHETIC DEMO DATA.** Prototype-ready, not usability-validated or evidence of WCAG compliance.

## Information architecture

Shallow task structure: **Search → Availability → Role & details → Review → Outcome**. Progress uses named steps; appointment facts precede personal data; transaction status is separate from marketing consent. Cancellation is a confirmation-link entry flow. Persistent labels, text-plus-icon status, and visible focus follow the supplied design system. Date-control behavior, breakpoints, typography, contrast, and touch targets remain validation needs.

| Screen | Purpose / entry | Key content and actions | Validation/states | Traceability |
|---|---|---|---|---|
| S01 Search | Choose clinic/service at start | Clinic, service; View availability; Exit | Required fields; loading, empty options, lookup error | F01–F03; R1 |
| S02 Availability | Compare returned slots | Search summary, date, text-labelled slots; select/change/refresh | Loading, results, empty, stale, unavailable | F03–F04; R1/R8/R10 |
| S03 Role & details | Collect BRD fields after slot | Summary, self/caregiver, name, DOB, phone, email, reason | Required R2 fields; errors, warning, expiry | F05–F06; R2/R3/R9/R11 |
| S04 Review & consent | Correct and consent before submit | Appointment/details, privacy, notification statement, unselected marketing choice | Privacy required; ready, invalid, locked processing, exit warning | F07–F08; R5/R7 |
| S05 Request outcome | Explain authoritative result | Text/icon status, supplied details/reference, notification result | Confirmed, pending, rejected, stale, timeout, unavailable, partial notification | F09–F11; R4/R5 |
| S06 Cancellation lookup | Identify booking from link | Reference, DOB | Required; error, unavailable | F12; R6 |
| S07 Cancellation outcome | Confirm intent and show result | Supplied summary, warning, result | Processing, cancelled, rejected, timeout, unavailable | F13–F14; R6 |

Caregiver authority is not invented. Marketing is unselected as a safety-preserving demo assumption pending legal/product decision; this does not amend R7.

