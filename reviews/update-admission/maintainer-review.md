# Draft review request: quality metadata and aggregation influence

Changing only a contribution's quality score changes its aggregation influence in the current proof of concept. I prepared a small reproducible experiment to clarify that behavior and the trust assumptions around it.

The experiment pins commit `3d44c130b78c3b2ce4bd042603873d55ede89faf` and uses unmodified coordinator, policy and merge code with fixed synthetic model states. It covers the core coordinator and the contributed validating coordinator.

With three eligible participants, increasing one score from 1 to 9 raises its quality-weighted share from one third to 9/11. A configured, feasible 0.5 cap holds its share at 0.5. Equal weighting keeps its share at one third above the quality floor. This establishes expected sensitivity, not an exploitable vulnerability or a poisoning result.

Before proposing a policy or implementation change, I would appreciate agreement on:

1. Who should produce and verify the quality score in the intended training workflow?
2. What is the score's valid range, and which evidence should bind it to a particular model update and evaluation?
3. What influence invariant should hold after eligibility filtering, including when too few participants remain to satisfy a configured cap?
4. Which existing coordinator path should host an initial integration test, and who should review the policy assumptions?

This work should complement the existing contribution validator, signed-manifest work (#273) and summary-persistence work (#276). It proposes no parallel implementation of those controls.

The initial contribution could be a short threat model plus a deterministic regression experiment once the intended invariant is agreed. Source observations, candidate requirements, executed tests and unresolved risks are recorded separately. No production-security claim is made.

Draft only. Not posted. Include only these reviewed baseline materials when preparing a public contribution; potentially security-relevant findings require the repository's private reporting route.
