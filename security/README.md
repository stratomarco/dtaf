# Reusable security assessment materials

Use these materials to document one system boundary and make claims that reviewers can trace to evidence. They require no particular assessment framework, domain taxonomy or scoring method.

1. Copy the [threat model template](../templates/threat-model.md) and pin the assessed system version.
2. Record each control in an [assessment record](../templates/assessment-record.md).
3. Link observations through the [evidence register](../templates/evidence-register.md).
4. Track remaining exposure and decisions in the [residual risk register](../templates/residual-risk-register.md).
5. Use the [review checklist](../docs/contribution-review.md) before submission.

The [guide](../docs/assessment-evidence-guide.md) defines the independent dimensions. The [fictional example](../examples/update-admission.md) illustrates candidate requirements and unresolved evidence, not a verified finding.

For a project contribution, use its architecture, vocabulary and documentation conventions. Confirm scope and existing work with maintainers. Submit a small reviewable change, cite actual implementation and test results, and keep assumptions and proposed requirements visibly separate from observations. The repository license applies; preserve applicable attribution when adapting material.

## Applied review and executable evidence

The [update-admission review](../reviews/update-admission/README.md) applies these materials to pinned public source. The [aggregation influence experiment](../experiments/aggregation-influence/README.md) records 26 CPU cases through unmodified coordinators, with 111 targeted upstream tests and eight experiment tests passing. Its conclusions are limited to the recorded paths and fixtures.
