# Threat model: contribution receipt through shared-base integration

Status: Candidate. Version and source boundaries: [review](README.md). Assessment date: 8 November 2026. Technical observations were prepared through automated source review and local execution; human architectural review and policy approval remain pending. Control implementation owners and risk acceptance authorities are unresolved.

## Assets, actors and boundaries

Assets: shared-base integrity, availability, authorized participant influence and decision evidence. Trust boundaries lie between participant-controlled output and coordinator policy, between validation and merge, and between integration and any downstream release decision.

Actors include cooperative participants, compromised authorized participants and deliberately malicious participants. The experiment models control of one supplied score with fixed tensors. It does not demonstrate network access, identity forgery, multiple identities or the ability to bypass an external scoring service.

| Assumption | Evidence | Consequence if false |
|---|---|---|
| A-1: actual orchestration uses one of the reviewed paths | Not established beyond local execution | Findings must be remapped to the deployed path |
| A-2: a participant can affect the score supplied to policy | Constructor-to-contribution path observed; deployment authority unknown | An independent trusted evaluator may remove the assumed attacker capability |
| A-3: score magnitude is intended to influence quality weighting | Policy implementation and comments | Behavior may match intent; source alone cannot select the trust requirement |
| A-4: release checks may operate after aggregation | Separate evaluation component exists; enforcement unverified | Claims about released model integrity require additional evidence |

## Scenarios, controls and candidate expectations

| ID | Actor action / possible impact | Existing evidence | Candidate expectation and verification |
|---|---|---|---|
| T-1 | Submit structurally incompatible tensors; disrupt aggregation | Contributed validator and tests; core integration differs | V-1: on the agreed entry path, reject incompatible contributions before unsafe merge; test shape, dtype, coverage, finite values and configured bounds |
| T-2 | Misrepresent sender or reuse a submission; obtain unauthorized influence | Signature work already tracked in #273; identity enforcement not assessed here | V-2: bind authorized identity, round, artifact and declared metadata as the protocol requires; test tampering and replay after format agreement |
| T-3 | Alter quality metadata; change eligibility or influence without changing model state | Measured through both coordinators, E-3 | V-3: owners define score authority, valid range and allowed influence; execute score sweeps against the agreed invariant |
| T-4 | Submit well-shaped harmful updates; degrade a released model | Structural checks do not establish poisoning resistance; evaluation component inspected | V-4: agree an adversary and scoped evaluation/release/rollback sequence; test it end to end and document missed attack classes |
| T-5 | Lose or misattribute decision evidence; prevent reliable reconstruction | Optional coordinator keeps validation summaries in memory; #276 tracks persistence | V-5: reconstruct identity, artifact, policy, validation, influence and decision, with separately tested provenance, integrity, retention and access control |

T-1's experimental check executes one non-finite-tensor case; broad coverage is supported by the targeted existing test suite, not a new resource-exhaustion assessment. No deployed vulnerability is asserted by this model.

## Independent assessment dimensions

| Control / claim | Completion | Effectiveness | Implementation evidence | Verification | Operational evidence |
|---|---|---|---|---|---|
| C-1: optional structural validation on the measured path | Completed for this local fixture and targeted tests | Effective within those tested cases; core path assessed separately | Source and executed integration | Functional, negative-input and integration tests, E-2/E-3 | Controlled local CPU environment only |
| C-2: feasible 0.5 cap with three eligible positive finite scores | Completed for the recorded sweep | Effective within measured cases; no general or deployment guarantee | Policy and coordinator | Scalar oracle, integration and existing policy tests | Controlled local CPU environment only |
| C-3: quality metadata is trustworthy | Not assessed for actual orchestration | Inconclusive | Local metadata path observed; evaluator authority unknown | Sensitivity measured, truthfulness not established | Unavailable |
| C-4: authenticated, replay-resistant ingress | Not assessed | Inconclusive | Related work identified | Not executed | Unavailable |
| C-5: release and rollback protect against poisoning | Partial source review | Inconclusive | Evaluation component inspected; enforcement not evidenced | Not executed end to end | Unavailable |
| C-6: decision evidence is durable and trustworthy | Partial source review | Inconclusive | In-memory contributed summaries inspected | Persistence/integrity/access controls not tested | Unavailable |

No scenario is marked not applicable merely because access is missing. A future exclusion requires an architectural rationale, reviewer and reconsideration trigger. All remaining exposure and pending decisions are linked in the [risk register](residual-risk.md).
