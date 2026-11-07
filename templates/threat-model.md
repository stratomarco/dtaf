# Threat model: <boundary>

Status: Draft / Reviewed | Owner: <name> | Reviewer: <name> | Date: <date>

## Scope and version

System, repository, pinned commit/configuration, environment and deployment assumptions:
In scope:
Out of scope and rationale:
Evidence/access limitations:
Review triggers (architecture, policy, dependency, model or trust changes):

## Architecture and trust

Describe components, assets, data flows, entry points and trust boundaries. Link a diagram and immutable architectural references. Identify the authority for each decision and who controls each input.

| Assumption ID | Assumption | Supporting evidence | Consequence if false | Owner / review trigger |
|---|---|---|---|---|
| A-1 | <text> | <E-ID or unknown> | <text> | <text> |

Include cooperative, compromised legitimate and deliberately malicious actors where relevant. Record attacker capabilities, access, objectives and exclusions.

## Threat scenarios

| ID | Actor / preconditions | Boundary and action | Asset / impact | Assumptions | Existing controls and evidence | Proposed control / owner |
|---|---|---|---|---|---|---|
| T-1 | <text> | <text> | <text> | <A-ID> | <C-ID / E-ID or unknown> | <text> |

## Security expectations and verification

Requirements below are candidate expectations until an authorized project reviewer agrees them. A behavioral observation is not a policy violation without an agreed invariant.

| Expectation ID | Threat / control | Testable invariant | Test inputs and procedure | Expected result / oracle | Evidence and actual result | Limitations |
|---|---|---|---|---|---|---|
| V-1 | <T-ID / C-ID> | <text> | <positive, negative, adversarial, integration cases> | <text> | <E-ID or not run> | <text> |

Assess the full protective sequence: admission, aggregation, evaluation, release gating, monitoring and rollback as applicable. Do not prescribe detection at a particular stage without architectural justification.

## Control assessment

Link one [assessment record](assessment-record.md) per control. Keep completion, effectiveness, implementation, test types and operational evidence separate.

## Residual risk and decisions

Link the [risk register](residual-risk-register.md). Include uncertainties, deferred work, risk acceptance authority and pending decisions.

## Review

Open questions for maintainers:
Related work and coordination:
Review decision, reviewer and date:
Next review date / trigger:
