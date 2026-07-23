# Changelog

All notable changes to the Double Trinity Assessment Framework will be documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

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
