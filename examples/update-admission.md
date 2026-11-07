# Worked example: update admission

Fictional design exercise. No real repository or deployed system was assessed. No tests were executed. All requirements are candidates for owner review.

## Scope and assumptions

Consider a coordinator receiving model updates and participant-supplied quality metadata, then validating, weighting and aggregating them before release. The boundary spans receipt through release and rollback. Training internals and infrastructure compromise are outside this exercise, not declared safe.

Assets: model integrity, authorized participation, availability and decision evidence.
A-1: enrolled participants can be compromised or malicious.
A-2: quality metadata is untrusted until policy establishes its authority.
A-3: release may be gated after aggregation; pre-merge detection is not assumed mandatory.
All assumptions require owner confirmation.

## Candidate scenarios and expectations

| Threat | Scenario | Candidate expectation / verification |
|---|---|---|
| T-1 | Malformed or oversized update exhausts resources or breaks aggregation | V-1: validate allowed shape, type, finite values and configured size limits on the exercised admission path; submit valid, malformed and oversized inputs and observe bounded rejection before unsafe processing |
| T-2 | Forged or replayed submission gains authorized influence | V-2: bind identity, authorization, artifact and round; test unauthorized identities, changed artifacts and replayed envelopes against the agreed replay policy |
| T-3 | Participant metadata grants influence beyond policy | V-3: owners first define a bounded-influence invariant; vary quality metadata with a fixed update and seed, record resulting weights and check that invariant |
| T-4 | Valid-shaped malicious update degrades the released model | V-4: define scoped adversarial evaluations, release thresholds and rollback expectations across admission, aggregation and release; report attack coverage and false negatives |
| T-5 | Admission decisions cannot be reconstructed reliably | V-5: reconstruct identity, artifact digest, policy version, validation, assigned influence and decision; separately test event completeness, provenance, integrity, retention and access controls |

T-3 observation alone would establish weight sensitivity, not exploitability. T-4 evaluation cannot establish the absence of poisoning.

## Example control record

C-1: integrated update validator supporting T-1 / V-1.
Completion: Not assessed. Effectiveness: Inconclusive.
Implementation: Unknown. Functional, adversarial and integration tests: Not run.
Operational evidence: Unavailable.
Evidence register: empty; no implementation or execution claim is made.
Needed evidence: pinned admission-path source, validator integration, reproducible positive/negative/resource-limit cases and actual results.

## Residual risk and next work

R-1 links T-1 through T-5: behavior and enforcement remain unknown because this is design-only. Treatment: identify actual architecture and existing controls, obtain owner agreement on V-1 through V-5, then execute scoped tests. Implementation owner and acceptance authority: unresolved. Decision: Pending. Review before implementation or any deployment claim.

A future completed inspection could find C-1 ineffective; completion would remain Completed while effectiveness becomes Ineffective. A passing standalone validator test would establish neither integration nor operational effectiveness.

For an applicability example, a service with no participant-supplied quality metadata might exclude T-3 after an architecture reviewer confirms that boundary. Record the reviewer, date and a trigger to revisit the exclusion when metadata is introduced.
