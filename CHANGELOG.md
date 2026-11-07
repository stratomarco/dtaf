# Changelog

All notable changes to the Double Trinity Assessment Framework will be documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Applied evidence-based review
- Add a pinned-source admission-path review, focused threat model, evidence and residual-risk records, and a draft maintainer review request.
- Add reproducible metadata-influence measurements through unmodified upstream coordinator and merge code, source digests, 26 recorded CPU cases and dependency versions.
- Record 111 passing targeted upstream tests and eight passing experiment tests. The full upstream pre-PR check and deployment security were not assessed.


### Security assessment improvements
- Separate completion, control effectiveness, implementation, verification and operational evidence across all 72 checks.
- Add justified not-applicable decisions and independent residual-risk decisions, with migration guidance for A/RR/BC records.
- Add framework-neutral templates, evidence and risk registers, contribution review checklist and fictional update-admission example. No project-specific findings or executed security tests are claimed.
- Bound the core opacity and update-persistence statements; retain the v0.1 filename while this revision is unreleased.
- Refresh README navigation to existing work products; Word instrument remains planned.


### Fixed
- The 0.1.0 entry listed `instrument/DTAF_v01_instrument.docx` as added. The file is not in the repository. It is planned.
- Withdrew two claims from the 0.1.0 entry: "verified citations" and "MITRE ATLAS technique IDs verified at time of writing". Only the reference entries added below were checked against publisher or official pages. The older reference entries have not been systematically re-verified. The ATLAS IDs were checked on atlas.mitre.org on 7 November 2026.
- Removed superseded ATLAS technique names from three checks (DE-T-4, CN-O-4, CN-B-1). ATLAS renames techniques between releases, so those checks now cite the ID only.
- Added four sources that the text cited but the reference list lacked: Shaw and Nave (2026), Edmans (2024), OWASP API Security Top 10 (2023), and Northcutt, Jiang and Chuang (2021) for CleanLab.
- Removed "Reference list complete" from the status line of `DTAF_v01.md`. Some checks cite sources only generically (for example "published research on multi-turn jailbreaking") and have no reference entry.

### Changed
- CN-T-4 (Adversarial Input Entry Point Mapping) now cites AML.T0051 (LLM Prompt Injection) instead of AML.T0049, because the check is about prompt inputs.
- README status changed from private to public draft, and the README no longer describes the reference list as complete.

## [0.1.0] — 2026-07-23

### Added
- Initial framework release
- All six domains complete: Data Entanglement, Connectivity, Extensibility, Adaptability, Complexity, Opacity
- 72 checks across three tiers (Observable, Testable, Bounded Investigation)
- Human layer risk prompt in every domain
- Domain residual risk registers
- Trust Map Summary
- Assessment context block with foundation model boundary declaration
- Complete reference list with verified citations
- Word practitioner instrument (DTAF_v01_instrument.docx)

### Design decisions
- Internal access tier only in v0.1; procurement and third-party tiers planned for v0.2
- Foundation model blind spots named explicitly within each domain rather than isolated
- Status system: Assessed / Carried as Residual Risk / Beyond Current Capacity
- No aggregate score by design; output is a structured trust map
- Framework references BIML, MITRE ATLAS, and NIST AI RMF rather than duplicating them
- MITRE ATLAS technique IDs verified at time of writing; consult atlas.mitre.org before formal use
- OWASP LLM Top 10 references use 2025 version numbering throughout

### Known limitations
- Built from first principles rather than observational data; empirical grounding to come from practitioner use
- Procurement and third-party audit tiers not yet designed
- Word instrument requires manual entry; no automated tooling in v0.1

---

## Versioning

This framework uses [Semantic Versioning](https://semver.org/).

- **MAJOR** version — structural changes to the six forces or the assessment tiers
- **MINOR** version — new tiers, new domains, or significant additions to existing checks
- **PATCH** version — corrections, reference updates, and minor check refinements
