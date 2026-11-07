# Residual risk and decision register

No acceptance is implied by assignment, a passing test or completed review. Implementation owners and acceptance authority require maintainer confirmation. Every decision below is Pending as of 8 November 2026.

| ID | Linked threats / controls | Remaining exposure or uncertainty | Evidence | Proposed next treatment | Implementation owner / acceptance authority | Review trigger |
|---|---|---|---|---|---|---|
| R-1 | T-3 / C-3 | The authority and validity of quality metadata in actual orchestration are unknown | E-1/E-3 | Agree score producer, policy invariant and allowed score domain; map actual ingress | Unresolved / unresolved | Before making a security claim or changing weighting |
| R-2 | T-1 / C-1 | Validation exists in a contributed path; deployed integration and resource bounds are unverified | E-1/E-2 | Confirm chosen path and configured limits with its owner | Unresolved / unresolved | Integration or configuration change |
| R-3 | T-2 / C-4 | Identity and artifact binding were not exercised | E-6 | Coordinate with manifest/signature work; obtain protocol and trust-store decisions | Unresolved / unresolved | Manifest format or membership/key lifecycle change |
| R-4 | T-4 / C-5 | Structural validity and a scalar merge experiment do not establish resistance to harmful updates | E-3/E-5 | Define attack scope and evaluate the full protective sequence, including release and rollback | Unresolved / unresolved | Before deployment assurance or poisoning-resistance claims |
| R-5 | T-5 / C-6 | Durability, integrity, retention and access control of decision evidence remain unverified | E-1/E-6 | Coordinate with persistence work and identify evidence requirements | Unresolved / unresolved | Persistence or observability design review |
| R-6 | T-3 / C-2 | The selected cap is effective only within the measured configuration; the appropriate insufficient-participant behavior is a policy decision | E-2/E-3 | Agree whether a round should pause, reject or use another expressly authorized fallback | Unresolved / unresolved | Participant eligibility or quorum policy change |

Target for the next review: before preparing an upstream implementation proposal. No delivery dates or risk owners have been invented on maintainers' behalf.
