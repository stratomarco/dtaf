# Assessment and evidence guide

These conventions can be used with any security checklist or threat model. They do not produce an aggregate security score.

## Independent dimensions

| Dimension | Values | Meaning |
|---|---|---|
| Completion | Completed; Partial; Not assessed; Not applicable | Whether the declared investigation was performed |
| Effectiveness | Effective within tested scope; Ineffective; Inconclusive; Not applicable | Whether the stated expectation is supported within scope |
| Implementation | Planned; Implemented in isolation; Integrated; Unknown; Not applicable | Where the control exists; cite the relevant code or configuration |
| Verification | Record each test type separately | Functional, adversarial, integration and regression tests may coexist; record not run, pass, fail or inconclusive for each |
| Operational evidence | Unavailable; Controlled environment; Operational deployment; Not applicable | Environment, duration, observations and limits |

Evidence dimensions are independent, not a maturity ladder. A unit test may pass without integration, and deployment does not establish adversarial robustness. For each claim, link exact evidence and state what it cannot establish.

Completed requires a recorded scope, work performed, evidence reviewed and a conclusion, including a negative or inconclusive conclusion. Partial identifies unfinished work. Not assessed records why no investigation was performed. A missing control may be found ineffective through a completed investigation.

Not applicable requires a boundary-based reason, reviewer, date and trigger for reconsideration. Missing access, funding, expertise or tests do not make a relevant check inapplicable. Control effectiveness may be not applicable when no control claim is being evaluated (for example an inventory-only record); explain why separately.

Effective within tested scope requires an explicit expectation, supporting observations and limitations. Ineffective identifies a failed expectation. Inconclusive covers insufficient or conflicting evidence. None of these values is a certification.

## Evidence discipline

Assign stable evidence IDs. Capture repository and commit, file/symbol or line range, artifact digest, environment, date, procedure, inputs, expected and observed results, author and reviewer as relevant. Distinguish statements, source inspection, executed tests and operational observations. Use immutable references where possible and controlled storage for sensitive artifacts. Record access restrictions without copying secrets into reports.

Do not infer absence everywhere from absence in one reviewed path. A standalone validator does not demonstrate enforcement in the admission path. A changed output establishes behavior; it establishes a security failure only against an agreed invariant.

Record audit completeness, provenance, integrity protection, retention and access control separately. A log entry alone does not prove a trustworthy audit trail.

## Residual risk and decisions

Record remaining exposure and uncertainty even for completed checks and effective controls. Link threats, controls, evidence and treatment. Separate the person implementing a change from the authority accepting its remaining risk. An assessor identifying a risk does not accept it. Pending approval remains pending; include decision date, expiry or review date and change triggers. If no residual risk is identified, bound that conclusion to the examined scope.

## Migrating historical records

Preserve original statuses and notes as history. A (Assessed) can map to Completed only after checking scope and evidence; infer no effectiveness outcome. RR (Carried as Residual Risk) becomes a linked risk plus an independent completion choice. BC (Beyond Current Capacity) becomes Partial or Not assessed with the specific limitation and follow-up. Neither RR nor BC means ineffective, accepted or not applicable. Revisit old decisions with the authorized reviewer.
