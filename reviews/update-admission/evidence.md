# Evidence register

All source references resolve to the pinned commit in the [review](README.md). The [source manifest](../../experiments/aggregation-influence/sources.json) records Git blob IDs and SHA-256 hashes. Results are observations from one CPU environment, not independent certification.

| ID | Claim supported | Evidence | Limitations |
|---|---|---|---|
| E-1 | Actual path from supplied score to policy, merge and next base | Immutable source references S1-S5 in the review | Static review cannot establish which path any deployment uses |
| E-2 | Existing policy, merge, coordinator, validator and fingerprint tests pass in the recorded environment | 111 passed; command and machine-readable test summary in [validation record](../../experiments/aggregation-influence/validation.json) | Five selected files, not the complete repository suite or `make before-pr` |
| E-3 | Metadata-only sweeps affect quality-weighted aggregation and remain capped when the chosen cap is feasible | [26 recorded cases](../../experiments/aggregation-influence/results.json); unchanged fixture hashes within sweeps; independent scalar calculation | Fixed synthetic tensors, one round per case, no trained-model or deployed attack claim |
| E-4 | Measurement is repeatable and checks source integrity | Eight [experiment tests](../../experiments/aggregation-influence/test_experiment.py), repeated identical result object, modified-source rejection | Repeated in one environment; no cross-platform equality claim |
| E-5 | Evaluation/release decision logic exists separately | S6 in the review | Not executed or connected to publication in this assessment |
| E-6 | Related identity and persistence work has defined scope | Issues [#273](https://github.com/The-AI-Alliance/tapestry/issues/273) and [#276](https://github.com/The-AI-Alliance/tapestry/issues/276), observed open during preparation | Issue status is time-dependent; these are coordination references, not proof that controls are deployed |

Prepared by: automated source review and local execution in this working session. Human reviewer: pending. Review date: 8 November 2026, Europe/Oslo. Execution environment and dependency versions are in the results and lock file. Reproduction fetches the partial source snapshot without changing upstream files.
