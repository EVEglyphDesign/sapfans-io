# Power Automate Cloud Flow Resilience and Error Handling

## Purpose
This is a reusable design reference for production-oriented Power Automate cloud flows that need predictable failure handling, safe diagnostic logging, operational notifications, and supportable run history. It is relevant to SAP-adjacent business processes, approvals, master-data workflows, monitoring, and enterprise automation.

## Recommended flow pattern

1. **Trigger** — start the flow from an approved event, such as a SharePoint item being created or modified.
2. **Retrieve and validate** — obtain required data and verify business conditions before executing material actions.
3. **Try scope** — execute the business actions within a Scope.
4. **Catch scope** — configure `Run after` so the Catch Scope runs when the Try Scope has failed, timed out, or been skipped, as appropriate to the design.
5. **Capture diagnostic context** — capture the action name, safe error message, timestamp, run ID or correlation ID, and approved diagnostic context.
6. **Log the event** — write the diagnostic record to an approved controlled destination, such as SharePoint, Dataverse, Application Insights, or an enterprise incident/logging platform.
7. **Notify responsibly** — send a success notification only after successful completion; send a failure notification containing safe operational context and a link or identifier for the authoritative log or run history.
8. **Terminate explicitly** — end the flow with an intentional success or failure status after the appropriate logging and notification actions complete.

## Copilot implementation prompt

> Fix the error handling in my Power Automate cloud flow. Add a proper try-catch pattern using Scopes, configure Run after for failures, capture detailed error information, log the error details, and send a failure notification email containing the action name, error message, and timestamp. Also send a success notification when the flow completes successfully.

Use the prompt as an implementation aid, not as a substitute for solution review, security review, testing, or production change control.

## Governance and security controls

- Do not include credentials, secrets, personally identifiable information, protected health information, confidential payloads, or full raw action inputs/outputs in email or chat notifications.
- Apply least-privilege identities and governed connection references to every flow connection.
- Store detailed diagnostics only in an approved destination with appropriate access controls, retention, and audit requirements.
- Preserve the run ID, timestamps, and accountable support ownership so incidents can be traced and triaged.
- Define alert severity, notification recipients, escalation ownership, and suppression thresholds to prevent alert fatigue.
- Test expected failure paths, retries, timeouts, malformed inputs, downstream dependency failures, and notification failures before production release.

## SAPfans applicability

Use this pattern for Power Automate flows that support SAP-facing processes or related enterprise operations. The pattern is additive: it improves observability and resilience without changing the business authority, approval model, or system-of-record responsibilities of SAP and connected systems.

## Source context

Reference captured from a user-supplied LinkedIn post, **“Fixing Power Automate Error Handling with GitHub Copilot: From Failure-Prone to Resilient Flows,”** by Ravi Potturu, supplied as screenshots in September 2026. The post illustrates the use of Scopes, Run after configuration, detailed error logging, and success/failure notifications. This repository page is an independently structured implementation reference and should be validated against the target Power Platform tenant, licensing, connector controls, and organizational policies before adoption.
