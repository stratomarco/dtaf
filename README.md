# Double Trinity Assessment Framework (DTAF)

**Version:** 0.1 — Draft  
**Status:** Private — pending public release alongside the Double Trinity article series

---

## What This Is

The Double Trinity Assessment Framework is a structured instrument for evaluating the security posture of a deployed ML system against six structural forces — three inherited from software security, three native to machine learning.

It is not a vulnerability scanner. It does not run against a model. It requires human judgment, organizational context, and honest characterization of what can and cannot be assessed. It is designed for practitioners who operate the systems they are assessing.

The output is a **trust map**: a structured characterization of posture, evidence reviewed, controls in place and what they actually cover, and explicit residual risk. There is no score. A completed assessment is not a clean bill of health.

---

## The Six Forces

| # | Force | Origin | Core Statement |
|---|---|---|---|
| 1 | Connectivity | Inherited from software security | The attack surface has no perimeter |
| 2 | Extensibility | Inherited from software security | Behavior can be added or changed at runtime |
| 3 | Complexity | Inherited from software security | The system cannot be fully understood by its builders |
| 4 | Opacity | Native to ML | The system cannot be meaningfully inspected |
| 5 | Data Entanglement | Native to ML | The training pipeline is the attack surface |
| 6 | Adaptability | Native to ML | Security properties do not persist across model updates |

The first three are inherited from McGraw and Hoglund's Trinity of Trouble (*Exploiting Software*, 2004). The second three are native to machine learning. Together they form the Double Trinity — two generations of structural risk, compounding each other.

---

## Intellectual Lineage

The DTAF is grounded in:

- Ken Thompson, "Reflections on Trusting Trust" (1984) — the foundational insight that trust ultimately lives in people, not systems
- Gary McGraw and Greg Hoglund, *Exploiting Software* (2004) — structural forces in software security
- BIML ML Security Risk Framework — architectural ML risks, the closest existing work to what the DTAF addresses
- MITRE ATLAS — adversarial threat catalog for AI systems
- NIST AI RMF — governance vocabulary and risk management structure
- Shaw and Nave, "Thinking — Fast, Slow, and Artificial" (Wharton, 2026) — empirical grounding for the human layer prompts
- Alex Edmans, *May Contain Lies* (2024) — narrative and evidence bias in evaluation

The framework builds on these rather than duplicating them. Where they cover something well, the DTAF references and integrates.

---

## What This Framework Does Not Do

- Does not produce a security certification
- Does not replace specialist expertise — the Bounded Investigation tier names where specialists are needed
- Does not eliminate residual risk — for Opacity and Data Entanglement in particular, some risk cannot be assessed even under full internal access
- Does not assess the model in isolation — it assesses the posture of the organization that built, trained, and operates it

---

## Structure

Each of the six domains contains three tiers of checks:

- **Observable** — completable in hours using documentation access and process interviews
- **Testable** — requires deliberate effort and standard security competency, completable in days
- **Bounded Investigation** — requires specialist knowledge; depth is explicitly capped; routes to documented scope or explicit residual risk

Each check has three possible statuses:

| Status | Meaning |
|---|---|
| **A** — Assessed | Check completed. Evidence documented. |
| **RR** — Carried as Residual Risk | Gap explicitly documented and owned. Residual risk notes required. |
| **BC** — Beyond Current Capacity | Expertise or access not available. Scope or specialist engagement documented. |

There are no checkboxes. Every check requires written evidence notes.

---

## Files

- `DTAF_v01.md` — canonical framework with all six domains, all 72 checks, and the complete reference list
- `instrument/DTAF_v01_instrument.docx` — Word practitioner instrument for working through and recording assessments *(coming soon)*

---

## Design Constraints

Every check satisfies all six of the following:

1. **Traceable** — maps to a specific force, mechanism of failure, and existing grounding work
2. **Incomplete by design** — what cannot be assessed is named explicitly
3. **Human layer embedded** — each domain includes a prompt for where the assessor is most at risk of judgment failure
4. **Referential, not duplicative** — points to BIML, ATLAS, and NIST where they cover things well
5. **Resistant to scoring** — output is a trust map, not a dashboard
6. **Completable in practice** — every check routes to a defined endpoint

---

## Roadmap

- v0.1 (current) — all six domains, internal access tier, first principles grounding
- v0.2 — empirical refinement from practitioner use; procurement assessment tier
- v1.0 — community-validated, multi-tier, with aggregated residual risk patterns

---

## Background

The DTAF was developed alongside the Double Trinity article series on Medium by Marco Constantino. The series traces the intellectual path from Ken Thompson's "Reflections on Trusting Trust" through McGraw's Trinity of Trouble to the six structural forces of ML security.

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0).  
You are free to use, share, and adapt this framework with attribution.
