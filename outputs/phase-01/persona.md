# Evidence-Limited Personas — Community Clinic Appointment Booking

> **SYNTHETIC DEMO DATA.** These personas synthesize fictional demonstration sources. They are not validated representations of real clinic users and must be validated with real research.

## Persona 1 — Time-Constrained Self-Booker

- **User type:** Person arranging their own routine appointment during limited available time.
- **Summary:** Prioritizes quickly finding a suitable slot, retaining progress, and receiving an unambiguous outcome.
- **Goals:** See useful availability early; complete booking efficiently; recover from stale slots, slow responses, and timeouts.
- **Supported pain signals:** Opening clinics individually to find early availability; unclear session behavior; repeating steps after a slot disappears; unclear errors.
- **Motivations:** Finish an administrative task without calling during reception hours.
- **Evidence:** `synthetic-interview-notes.md` → P1, P4, P5 and repeated patterns; `synthetic-survey-summary.md` → 42/60 prefer availability before personal data; `synthetic-support-tickets.md` → T-102, T-105; `synthetic-analytics-summary.md` → form and confirmation funnel.
- **Synthesis:** P1, P4, and P5 support a shared speed/recovery pattern.
- **Assumptions:** This pattern's prevalence and applicability to real clinic populations are unknown.
- **Confidence:** MEDIUM — consistent across several synthetic sources, but not empirical research.
- **Contradictions:** Confirmation-channel preference varies; P1 prefers SMS while P4 prefers email and does not want SMS.
- **Validation needs:** Real task timing, acceptable timeout, recovery expectations, channel choice, and reasons for abandonment.

## Persona 2 — Caregiver Coordinator

- **User type:** Person arranging an appointment on behalf of someone else.
- **Summary:** Needs clear distinctions between patient and caregiver details, authority, consent, and notification recipients.
- **Goals:** Enter the correct person's information; understand privacy responsibilities; ensure the right people receive the outcome.
- **Supported pain signals:** Uncertainty about whose contact information belongs in the form and who should receive confirmation.
- **Motivations:** Coordinate care without exposing information or losing track of the appointment.
- **Evidence:** `synthetic-interview-notes.md` → P2; `synthetic-support-tickets.md` → T-104; `synthetic-survey-summary.md` → 31/60 report booking for another person; BRD R11 supplies business scope but is not user evidence.
- **Synthesis:** Three synthetic source types support caregiver ambiguity as a distinct task context.
- **Assumptions:** Relationship types, legal authority, consent needs, and preferred notification model are unknown.
- **Confidence:** MEDIUM — triangulated synthetic evidence, not real participant research.
- **Contradictions:** P2 wants confirmation to both people, while privacy boundaries and patient consent remain unresolved.
- **Validation needs:** Caregiver categories, authority/consent, field ownership, notification recipients, and privacy expectations.

## Persona 3 — Access-and-Clarity-Dependent Booker

- **User type:** Person who depends on keyboard-operable controls and redundant, explicit status communication.
- **Summary:** Needs availability, errors, progress, and outcomes conveyed without color-only meaning and with predictable keyboard interaction.
- **Goals:** Identify available slots; navigate and correct the form; understand status and next action.
- **Supported pain signals:** Color-only availability is not inferable; status clarity is needed when slots change.
- **Motivations:** Complete the same booking task without relying on a pointer or color perception.
- **Evidence:** `synthetic-interview-notes.md` → P3 and P5; `design-system.md` → non-color status, focus, labels, corrective errors (design constraint, not user evidence).
- **Synthesis:** P3 supports keyboard/color concerns; P5 supports redundant status needs.
- **Assumptions:** Assistive technologies, impairment types, devices, and actual accessibility barriers are not established.
- **Confidence:** LOW — limited synthetic qualitative evidence and no real accessibility evaluation.
- **Contradictions:** The BRD's green/grey requirement conflicts with the design-system rule against color-only status.
- **Validation needs:** Representative keyboard and assistive-technology research; focus order; announcements; contrast; date-picker behavior.

## Excluded unsupported attributes

No ages, genders, diagnoses, income levels, technical proficiency, quotations beyond supplied synthetic notes, or population prevalence have been invented. Requirements Challenge risks were not used as persona facts.

