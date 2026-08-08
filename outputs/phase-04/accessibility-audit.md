# Accessibility Audit — Clinic Appointment Demo

> **EVIDENCE-BOUNDED ACCESSIBILITY RISK REVIEW.** This combines manual static inspection, interactive keyboard-oriented DOM checks, and contrast calculation using supplied/implemented colors. It is not a full automated audit, assistive-technology study, formal WCAG conformance evaluation, or legal compliance determination.

## Evidence inspected

- `projects/starter/input/design-system.md`
- `outputs/phase-03/screen-spec.md`
- `outputs/phase-03/interaction-states.md`
- `outputs/phase-03/prototype/index.html`, `styles.css`, and `app.js`
- Interactive local walkthrough of Search → Availability → Details → Review → timeout outcome

## Positive evidence

| Area | Evidence-bounded result |
|---|---|
| Structure | A semantic `main`, one page `h1`, and step `h2` headings are exposed in the accessibility tree. |
| Labels | Implemented form controls have persistent visible labels or checkbox label text. |
| Native operation | Buttons, selects, checkboxes, inputs, and textarea are native HTML controls and therefore provide a keyboard-operable baseline. |
| Focus visibility | CSS supplies a visible `2px solid #2563EB` focus indicator with offset. |
| Non-color meaning | Available/unavailable and outcome states include text, disabled/pressed state, symbols, and headings; color is not the sole visible cue. |
| Consent separation | Privacy and optional marketing are separate native checkboxes; marketing is unchecked by default in the demo. |
| Outcome clarity | The timeout outcome exposes “Outcome unknown” and warns not to assume success. |

## Potential conformance issues and risks

| ID | Severity | Finding | Evidence | Required validation/action |
|---|---|---|---|---|
| A-01 | MEDIUM | Required-field errors are generic and not associated with individual inputs. | `#err` has no `role`, inputs have no `aria-describedby`, and the message does not identify each field. | Add field-level corrective messages and programmatic associations; test announcement behavior. |
| A-02 | MEDIUM | Focus remains on the triggering button after invalid submission instead of moving to the first invalid field. | Interactive DOM check after empty “Review request” activation. | Implement first-invalid focus consistent with ST-04 and verify keyboard/screen-reader behavior. |
| A-03 | MEDIUM | Dynamic step replacement has no deliberate focus placement; the whole `#app` region is `aria-live="polite"`. | `app.js` replaces `innerHTML`; interactive transitions did not expose focus management. | Move focus to an appropriate heading/control and narrow announcements; test with multiple screen readers. |
| A-04 | LOW | DOB, phone, and email use `type="text"` and no autocomplete tokens. | Interactive DOM inspection and input template in `app.js`. | Use appropriate semantic types/input modes/autocomplete after privacy review. |
| A-05 | MEDIUM | Session warning/expiry and cancellation paths cannot be audited because they are absent from the runnable prototype. | ST-14–ST-20 exist only in documentation. | Implement, then audit focus, announcements, timing controls, and recovery. |
| A-06 | LOW | Touch-target sizing and responsive behavior cannot be confirmed against a system rule. | The supplied design system explicitly omits touch-target and breakpoint specifications. | Define measurable criteria and validate at supported viewport/device sizes. |
| A-07 | MEDIUM | English-only delivery is an inclusivity risk with no language-needs evidence or alternative assistance path in the demo. | BRD constraint; Phase 1 risk review. | Validate language/access needs with representative users and define support/translation scope. |

## Contrast checks

Calculated with relative luminance from the actual hexadecimal pairs:

| Pair | Ratio | Evidence-bounded interpretation |
|---|---:|---|
| Primary text `#1F2937` on white | 14.68:1 | Exceeds common WCAG AA/AAA text contrast thresholds in isolation. |
| Error text `#B42318` on white | 6.57:1 | Exceeds the common 4.5:1 normal-text threshold in isolation. |
| Focus color `#2563EB` on white | 5.17:1 | Exceeds the common 3:1 non-text contrast threshold in isolation. |
| White button text on `#175CD3` | 5.99:1 | Exceeds the common 4.5:1 normal-text threshold in isolation. |

These calculations do not cover every rendered state, anti-aliasing, adjacent colors, disabled controls, zoom, high-contrast modes, or user overrides.

## Human and tool validation still required

- Complete keyboard-only traversal, including backward navigation and recovery paths.
- Screen-reader checks for step changes, errors, loading, processing, pending, timeout, stale-slot, cancellation, and expiry states.
- Browser zoom/reflow, narrow viewport, text spacing, high-contrast/forced-colors, reduced-motion, and touch-target checks.
- Assistive-technology and cognitive-accessibility evaluation with representative users.
- A defined WCAG target/version, supported platforms, and testable acceptance criteria.

## Conclusion

The demo contains useful accessibility foundations but has material error and focus-management risks, and several required states are not implemented. The available evidence cannot support a claim of WCAG compliance.

