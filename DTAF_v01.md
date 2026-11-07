# Double Trinity Assessment Framework (DTAF)
**Version:** 0.1 — Draft  
**Status:** v0.1 Draft. All six domains complete. Trust Map Summary present.  
**A note on MITRE ATLAS technique IDs:** ATLAS is a living framework and renames or restructures techniques between releases. This document cites technique IDs without names, and the IDs themselves may change. The IDs were checked against https://atlas.mitre.org on 7 November 2026. Check them again before citing them in an assessment or report.

**Grounded in:** McGraw & Hoglund, *Exploiting Software* (2004); Thompson, "Reflections on Trusting Trust" (1984); BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF; Shaw & Nave, Tri-System Theory (2026); Edmans, *May Contain Lies* (2024).

---

## Purpose

The Double Trinity Assessment Framework is a structured instrument for evaluating the security posture of a deployed ML system against six structural forces — three inherited from software security, three native to machine learning — that make such systems fundamentally difficult to defend.

The Double Trinity is not a vulnerability scanner. It does not run against a model. It requires human judgment, organizational context, and honest characterization of what can and cannot be assessed. It is designed for practitioners who operate the systems they are assessing.

The framework builds on existing work — BIML, MITRE ATLAS, NIST AI RMF, and others — rather than duplicating it. Where those frameworks already cover something well, this instrument references and integrates them. The organizing frame is the Double Trinity. The intellectual honesty is Thompson's.

---

## What This Framework Does Not Do

It does not produce a security certification. A completed assessment is not a clean bill of health.

It does not replace specialist expertise. Several checks in the Bounded Investigation tier require ML security specialists. The framework tells you where that expertise is needed, not how to substitute for it.

It does not eliminate residual risk. For several of the six forces — Opacity and Data Entanglement in particular — some risk cannot be assessed even under full internal access. The framework makes this explicit. Naming residual risk is the honest output, not a failure of the instrument.

It does not assess the model itself in isolation. It assesses the posture of the organization that built, trained, and operates it.

---

## Design Constraints

Every check in this framework satisfies all six of the following:

1. **Traceable.** Each check maps to a specific force, a specific mechanism of failure, and existing work that grounds it.
2. **Incomplete by design.** What cannot be assessed is named explicitly. A completed assessment does not imply complete coverage.
3. **Human layer embedded.** Each domain includes a prompt addressing where the assessor is most at risk of their own judgment failure.
4. **Referential, not duplicative.** Where BIML, ATLAS, or NIST cover something well, we point to it. We do not rebuild it.
5. **Resistant to scoring.** There is no aggregate score. The output is a structured trust map that a practitioner must read and interpret.
6. **Completable in practice.** Every check routes to a defined endpoint. Practitioners can always reach a defensible completion.

---

## The Six Forces

| # | Force | Origin | Core Statement |
|---|---|---|---|
| 1 | Connectivity | Inherited | The attack surface has no perimeter |
| 2 | Extensibility | Inherited | Behavior can be added or changed at runtime |
| 3 | Complexity | Inherited | The system cannot be fully understood by its builders |
| 4 | Opacity | Native to ML | The system cannot be meaningfully inspected |
| 5 | Data Entanglement | Native to ML | The training pipeline is the attack surface |
| 6 | Adaptability | Native to ML | Security properties do not persist across model updates |

---

## How to Use This Framework

**Step 1 — Complete the Assessment Context block below.** Declare the system being assessed, access tier, and foundation model boundary before touching any domain.

**Step 2 — Read the Human Layer prompt** at the start of each domain before beginning checks. Do not skip it.

**Step 3 — Work through each domain** in order: Data Entanglement, Connectivity, Extensibility, Adaptability, Complexity, Opacity. The order moves from most tractable to least. Completing the earlier domains will build context for the harder ones.

**Step 4 — For each check, record a status and evidence notes.** Status has three values only:

| Status | Meaning |
|---|---|
| **A** — Assessed | The check was completed. Evidence is documented. |
| **RR** — Carried as Residual Risk | The check could not be fully completed. The gap is explicitly documented and owned. |
| **BC** — Beyond Current Capacity | The check requires expertise or access not available. Scope or specialist engagement is documented. |

There are no checkboxes. Every check requires written evidence notes. If a check is RR or BC, residual risk notes are required.

**Step 5 — Complete the Domain Residual Risk Register** at the end of each domain.

**Step 6 — Complete the Trust Map Summary** at the end of the full assessment.

---

## Assessment Context

*(Complete before beginning any domain.)*

| Field | Entry |
|---|---|
| System assessed | |
| System description | |
| Assessment date | |
| Assessor(s) | |
| Access tier | Internal |
| Foundation model used | Yes / No |
| Foundation model name and provider | |
| Fine-tuning applied | Yes / No |
| RAG augmentation used | Yes / No |

**Foundation Model Boundary Declaration**

Complete one of the following based on your configuration:

- **Own data, trained from scratch:** All checks in all domains apply. No foundation model blind spot.
- **Fine-tuned on foundation model:** Checks apply to your fine-tuning data and pipeline. Pretraining data is unassessable at internal tier. Carry as explicit residual risk in Data Entanglement. Reference provider model card for what is published.
- **RAG augmentation:** Retrieval corpus checks apply. Pretraining data unassessable as above.
- **API only, no fine-tuning:** Most Data Entanglement checks reduce to provider documentation review. Declare this in the domain and carry the remainder as residual risk.

*Declared boundary:*

---

# Domain 1: Data Entanglement

**Force:** Native to ML — #5  
**Core statement:** The training pipeline is the attack surface.

## Force Summary

In traditional software, data and code are separate. You can reason about a program's logic independently of the data it processes. In ML, this separation does not hold. The training data is the program in a meaningful sense: a model's behavior is a direct function of what it was trained on. A compromise in the training data propagates into the model's behavior, potentially invisibly, and persists through deployment.

This is the Thompson insight applied one level upstream. Thompson showed that a compiler backdoor leaves no trace in source code. A data poisoning attack leaves no trace in model weights that can be read by inspection. The attack lives in the learned behavior, activated under conditions the attacker controls.

## Mechanism of Failure

**Data poisoning** — malicious examples injected into training data alter model behavior under attacker-controlled trigger conditions.

**Unverifiable provenance** — training data at scale cannot be fully audited. Trust in the source becomes the primary control.

**Pipeline integrity** — the transformation process from raw data to training-ready data is an attack surface in its own right.

**Runtime retrieval (RAG-specific)** — retrieval-augmented systems extend the attack surface to inference time.

## Foundation Model Boundary

Pretraining data for the foundation model is not assessable at internal tier. Document what the provider publishes and carry the remainder as explicit residual risk. Do not allow provider documentation to substitute for assessment.

## Human Layer Risk Prompt

*Complete this before beginning any check in this domain.*

The Edmans failure is most acute here. Write down the narrative you have already accepted about this system's training data: "We believe the data is clean because..." Then examine whether each reason rests on evidence gathered or on packaging received.

*Assessment narrative written:* [ ] Yes

*What we believe about this training data and why:*

*(write here)*

*What that belief rests on — evidence vs. packaging:*

*(write here)*

---

## Observable Checks

**DE-O-1 | Data Provenance Documentation**

*What to examine:* Does a written record exist for each training data source documenting origin, collection method, permitted use, and transformations applied?

*Evidence to gather:* Data cards, dataset documentation, pipeline documentation, data sheets.

*Grounded in:* Datasheets for Datasets (Gebru et al., 2021); BIML ML Security Risk Framework.

*Boundary:* Documentation records stated intent. It does not verify whether the data source was compromised before documentation was created.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-O-2 | Data Source Inventory**

*What to examine:* Can you produce a complete inventory of all data sources that contributed to training, including third-party and open datasets?

*Evidence to gather:* Data inventory register, procurement records, pipeline configuration files, dataset version records.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Map 1.6).

*Boundary:* An incomplete inventory is itself a finding, not a reason to mark this assessed.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-O-3 | Third-Party Data Agreements**

*What to examine:* For externally sourced data, do formal agreements document permitted use, quality standards, and provenance claims?

*Evidence to gather:* Data licenses, vendor agreements, terms of service, data use agreements.

*Grounded in:* NIST AI RMF (Govern 1.2); C2PA provenance standards.

*Boundary:* Agreements establish legal provenance. They do not verify data integrity or absence of malicious content.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-O-4 | Training Pipeline Architecture Documentation**

*What to examine:* Is the end-to-end training pipeline documented from data ingestion through all preprocessing stages to training?

*Evidence to gather:* Architecture diagrams, pipeline code repositories, transformation logs, preprocessing scripts.

*Grounded in:* BIML ML Security Risk Framework; SLSA framework adapted to ML pipelines.

*Boundary:* Documentation reflects design intent. Runtime behavior may differ from documented design.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-O-5 | Foundation Model Boundary Documentation** *(if applicable)*

*What to examine:* Is the boundary between your data layer and the foundation model's pretraining data explicitly documented?

*Evidence to gather:* Provider model cards, internal architecture records, fine-tuning configuration documentation.

*Grounded in:* Model Cards for Model Reporting (Mitchell et al., 2019).

*Boundary:* Pretraining data for foundation models is not assessable at internal tier. A = boundary documented, not foundation model data assessed.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Testable Checks

**DE-T-1 | Dataset Artifact Integrity Controls**

*What to examine:* Are cryptographic hashes or equivalent integrity controls applied to dataset artifacts at each pipeline stage?

*Evidence to gather:* Hash records, checksums, pipeline integrity logs, version control records.

*Grounded in:* SLSA framework applied to data artifacts; BIML ML Security Risk Framework.

*Boundary:* Verifies no modification after hashing. Does not verify data was clean when first hashed.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-T-2 | Pipeline Access Controls and Audit Logs**

*What to examine:* Who had write access at each stage? Is access logged, auditable, and reviewed for anomalies?

*Evidence to gather:* IAM records, RBAC documentation, pipeline audit logs, anomaly review records.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Map 2.2).

*Boundary:* Records who had access. Does not record whether authorized access was used maliciously.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-T-3 | Data Quality Controls and Evidence**

*What to examine:* What statistical quality checks were applied? Is there documented evidence they were run, reviewed, and acted upon?

*Evidence to gather:* QA reports, preprocessing logs, anomaly detection outputs, data validation records.

*Grounded in:* CleanLab (dataset quality tooling; Northcutt, Jiang & Chuang, 2021); BIML ML Security Risk Framework.

*Boundary:* Quality checks detect statistical anomalies. Not designed to detect sophisticated poisoning engineered to be statistically indistinguishable.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-T-4 | Poisoning Surface Mapping**

*What to examine:* At what stages could malicious data have been introduced? Map each potential injection point from external source through to training.

*Evidence to gather:* Pipeline architecture review, external data integration points, access records, threat model documentation.

*Grounded in:* MITRE ATLAS AML.T0020; BIML ML Security Risk Framework.

*Boundary:* Threat modeling, not detection. An unmapped injection point is a gap, not a clean finding.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-T-5 | Retrieval Corpus Integrity** *(if RAG is used)*

*What to examine:* What controls govern retrieval corpus ingestion? Has adversarial document injection been tested?

*Evidence to gather:* Corpus access controls, ingestion pipeline documentation, adversarial test records.

*Grounded in:* MITRE ATLAS; Greshake et al. (2023), "Not What You've Signed Up For," *AISec '23*, pp. 79–90.

*Boundary:* Tests anticipated scenarios. Novel injection approaches remain undetected. Continuous concern, not one-time assessment.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Bounded Investigation

**DE-B-1 | Statistical Poisoning Detection**

*What to examine:* Advanced statistical analysis of training data distributions for poisoning anomalies.

*Reference:* Spectral Signatures in Backdoor Attacks (Tran, Li & Madry, NeurIPS 2018); Activation Clustering (Chen et al., AAAI 2019); CleanLab (Northcutt, Jiang & Chuang, 2021).

*Ceiling:* Requires specialist ML security expertise. Scope to highest-risk datasets or engage specialist. If BC, document which datasets are unverified.

**Status:** A / RR / BC

**Scope documented:** *(what was assessed, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

**DE-B-2 | Backdoor Behavioral Testing**

*What to examine:* Systematic probing for trigger-activated behaviors consistent with backdoor injection.

*Reference:* MITRE ATLAS AML.T0020; BadNets (Gu, Dolan-Gavitt & Garg, 2017); Neural Cleanse (Wang et al., IEEE S&P 2019); Sleeper Agents (Hubinger et al., Anthropic, 2024).

*Ceiling:* Requires adversarial expertise and a defined threat model. Scope to highest-risk inputs. If BC, document trigger types not tested.

**Status:** A / RR / BC

**Scope documented:** *(what was tested, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

## Domain Residual Risk Register — Data Entanglement

| Item ID | Description of Gap | Reason Not Fully Assessed | Risk Owner | Review Date |
|---|---|---|---|---|
| | | | | |
| | | | | |

---

# Domain 2: Connectivity

**Force:** Inherited — #1  
**Core statement:** The attack surface has no perimeter.

## Force Summary

In ML, connectivity has become architectural. Models are trained on data scraped from the open web, deployed behind inference APIs, downloaded from public model repositories, and operate within multi-model pipelines where the output of one model becomes the input of another.

## Mechanism of Failure

**Model supply chain compromise** — models from public repositories may be poisoned or backdoored.

**Inference endpoint exposure** — APIs expose the model to adversarial probing and extraction.

**Multi-model pipeline propagation** — upstream compromise propagates through the pipeline.

**Third-party dependency** — external services extend the trust boundary beyond organizational control.

## Foundation Model Boundary

Document what the provider publishes about their security practices. Do not treat major provider status as an assessed security posture.

## Human Layer Risk Prompt

*Complete this before beginning any check in this domain.*

Write down the assumptions you are making about the security of each connectivity dependency: "We assume [model hub / provider / pipeline component] is secure because..." Then examine whether each assumption rests on evidence or on the fact that the dependency has not visibly failed.

*Assessment narrative written:* [ ] Yes

*Connectivity dependencies assumed secure and why:*

*(write here)*

*What each assumption rests on — evidence vs. assumption:*

*(write here)*

---

## Observable Checks

**CN-O-1 | Interface and API Inventory**

*What to examine:* Complete inventory of all external-facing endpoints, APIs, and integration points.

*Evidence to gather:* Network architecture diagrams, API documentation, integration records, infrastructure configuration.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Map 1.5); MITRE ATLAS.

*Boundary:* Inventory records what is known. Review infrastructure configuration directly, not just documentation.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-O-2 | External Model and Service Dependency Documentation**

*What to examine:* All external models, APIs, and services documented, including source, version, and access method.

*Evidence to gather:* Dependency registers, model cards for sourced models, API documentation, service agreements.

*Grounded in:* BIML ML Security Risk Framework; OpenSSF Model Signing Specification; NIST AI RMF (Map 1.6).

*Boundary:* Transitive dependencies are rarely fully catalogued.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-O-3 | Authentication and Authorization Documentation**

*What to examine:* How is access to inference endpoints controlled? Authentication and authorization documented across all interfaces.

*Evidence to gather:* Authentication configuration, authorization policy records, API key management records.

*Grounded in:* NIST AI RMF (Govern 1.2); BIML ML Security Risk Framework.

*Boundary:* Documents intended controls. Implementation correctness requires testable checks.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-O-4 | Model Hub Provenance Documentation**

*What to examine:* For models sourced from public repositories: what was downloaded, from where, when, who approved.

*Evidence to gather:* Sourcing records, repository URLs and commit hashes at download, approval records.

*Grounded in:* OpenSSF Model Signing Specification; MITRE ATLAS AML.T0010.

*Boundary:* Records claimed provenance. Does not verify model behavior under adversarial conditions.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-O-5 | Multi-Model Pipeline Trust Documentation** *(if applicable)*

*What to examine:* Trust boundaries between pipeline components documented; authority per component explicit.

*Evidence to gather:* Pipeline architecture documentation, component trust model, inter-component authentication records.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS.

*Boundary:* Documents intended trust architecture. Enforcement in practice requires testable checks.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Testable Checks

**CN-T-1 | Authentication Controls Verification**

*What to examine:* Do documented authentication and authorization controls function as described? No undocumented access paths exist.

*Evidence to gather:* Access control test results, records of gaps found, remediation records.

*Grounded in:* NIST AI RMF; OWASP API Security Top 10 (2023); BIML.

*Boundary:* Covers access paths identified through architecture review. Novel paths remain unverified.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-T-2 | Model Hub Integrity Verification**

*What to examine:* For models from public repositories: verify cryptographic signatures or hashes against originals at source.

*Evidence to gather:* Signature verification records, hash comparison results, OpenSSF verification outputs.

*Grounded in:* OpenSSF Model Signing Specification; MITRE ATLAS AML.T0010.

*Boundary:* Confirms artifact matches what the signer published. Does not verify signer trustworthiness.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-T-3 | Inference Endpoint Exposure Review**

*What to examine:* What is reachable from outside the intended authorization boundary? Network controls reviewed against documented architecture.

*Evidence to gather:* Network scan results vs. CN-O-1 inventory, firewall review, cloud security group review.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS AML.T0049.

*Boundary:* Covers currently exposed endpoints. Re-run after significant infrastructure changes.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-T-4 | Adversarial Input Entry Point Mapping**

*What to examine:* At which connectivity points can adversarial inputs enter? Map each entry point from external source to model input.

*Evidence to gather:* Input path documentation, validation controls at each entry point, input boundary test results.

*Grounded in:* MITRE ATLAS AML.T0051; OWASP Top 10 for LLMs 2025 (LLM01); BIML.

*Boundary:* Maps identified entry points. Novel input paths not in documented architecture are a gap in the map.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-T-5 | Pipeline Inter-Component Trust Verification** *(if applicable)*

*What to examine:* Are trust boundaries between pipeline components enforced? Can outputs be modified between components without detection?

*Evidence to gather:* Inter-component authentication test results, integrity control verification, anomaly detection coverage.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS.

*Boundary:* Covers in-scope inter-component paths. Document what was and was not tested.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Bounded Investigation

**CN-B-1 | Model Extraction Resistance Testing**

*What to examine:* Can the model be systematically queried to reconstruct its behavior or extract capabilities through the inference API?

*Reference:* MITRE ATLAS AML.T0024; Tramèr, Zhang, Juels, Reiter & Ristenpart (2016), "Stealing Machine Learning Models via Prediction APIs," *USENIX Security 2016*, pp. 601–618.

*Ceiling:* Requires specialist knowledge and significant query budget. Scope to defined extraction vectors. If BC, document what was not tested.

**Status:** A / RR / BC

**Scope documented:** *(what was tested, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

**CN-B-2 | Federated Learning Byzantine Resistance** *(if applicable)*

*What to examine:* Can participating nodes inject malicious gradients that alter the global model without detection?

*Reference:* MITRE ATLAS AML.T0020 (federated learning context); Blanchard, El Mhamdi, Guerraoui & Stainer (2017), "Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent," *NeurIPS 2017*, pp. 118–128.

*Ceiling:* Requires specialist expertise and access to federation architecture. If BC, document unverified nodes.

**Status:** A / RR / BC

**Scope documented:** *(what was tested, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

## Domain Residual Risk Register — Connectivity

| Item ID | Description of Gap | Reason Not Fully Assessed | Risk Owner | Review Date |
|---|---|---|---|---|
| | | | | |
| | | | | |

---

# Domain 3: Extensibility

**Force:** Inherited — #2  
**Core statement:** Behavior can be added or changed at runtime.

## Force Summary

In ML, extensibility means extending behavior, not code. The prompt interface is extensible by design. Agents have tool access. LoRA adapters modify behavior post-deployment. System prompts define behavioral constraints that can be manipulated.

## Mechanism of Failure

**Prompt injection** — malicious inputs manipulate behavior through the extensible prompt interface. Structural property, not misconfiguration.

**Tool and agent scope violation** — agents manipulated into using tools beyond intended scope.

**Adapter and plugin integrity** — externally sourced adapters modify behavior in unauditable ways.

**System prompt override and leakage** — behavioral constraints overridden or leaked through adversarial inputs.

## Foundation Model Boundary

The foundation model's inherent susceptibility to prompt injection is a property of its architecture, partially outside your control. You own the exposure; the model's susceptibility is a shared constraint.

## Human Layer Risk Prompt

*Complete this before beginning any check in this domain.*

Write down what adversarial inputs you have assumed are unlikely to work and why: "We have not tested [X] because..." Examine whether that reasoning is evidence-based or comfort-based. Prompt injection resistance is not binary.

*Assessment narrative written:* [ ] Yes

*What adversarial inputs have been assumed out of scope and why:*

*(write here)*

*What that assumption rests on — evidence vs. comfort:*

*(write here)*

---

## Observable Checks

**EX-O-1 | Extension Point Inventory**

*What to examine:* All ways the system's behavior can be modified at runtime: prompt interfaces, tool access, plugin architecture, adapter layers, retrieval, system prompt configuration.

*Evidence to gather:* System architecture documentation, integration records, tool and plugin registry, adapter sourcing records.

*Grounded in:* BIML ML Security Risk Framework; OWASP Top 10 for LLMs 2025 (LLM01; LLM06).

*Boundary:* Inventory reflects documented extension points. Undocumented ones are a gap in the map.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-O-2 | Agent Tool Inventory and Scope Documentation** *(if applicable)*

*What to examine:* All tools documented, including what each can do, conditions for invocation, and authorization controls.

*Evidence to gather:* Tool registry, function calling documentation, authorization policy per tool, scope decisions.

*Grounded in:* OWASP Top 10 for LLMs 2025 (LLM06); BIML; NIST AI RMF (Map 2.3).

*Boundary:* Documents intended scope. Absence of formal scope decisions is itself a finding.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-O-3 | System Prompt Documentation and Access Control**

*What to examine:* System prompt documented, versioned, access-controlled; change process logged.

*Evidence to gather:* System prompt version history, access control records, change management records.

*Grounded in:* OWASP Top 10 for LLMs 2025 (LLM01; LLM07); BIML.

*Boundary:* Access controls govern authorized modification. Do not prevent adversarial override through the prompt interface.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-O-4 | External Adapter and Plugin Sourcing Documentation** *(if applicable)*

*What to examine:* For externally sourced adapters/plugins: documented record of origin, approval, and integrity verification.

*Evidence to gather:* Adapter sourcing records, approval documentation, integrity verification records.

*Grounded in:* BIML; OpenSSF Model Signing Specification; MITRE ATLAS AML.T0010.

*Boundary:* Documents what was claimed. Does not verify behavior under adversarial conditions.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-O-5 | Extensibility Threat Model**

*What to examine:* Threat model specifically addressing extension points; identifies what an attacker could achieve at each.

*Evidence to gather:* Threat model documentation, attack scenario records, extensibility risk assessments.

*Grounded in:* MITRE ATLAS; BIML; NIST AI RMF (Map 5.1).

*Boundary:* Covers scenarios its authors anticipated. Absence of a threat model is a significant finding.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Testable Checks

**EX-T-1 | Prompt Injection Surface Testing**

*What to examine:* Systematic testing for prompt injection across all identified extension points, including indirect injection via retrieved documents or tool outputs.

*Evidence to gather:* Test plan, test results, records of successful injections, remediation records.

*Grounded in:* OWASP Top 10 for LLMs 2025 (LLM01); MITRE ATLAS AML.T0051; Greshake et al. (2023), *AISec '23*, pp. 79–90.

*Boundary:* Resistance to tested vectors does not imply resistance to untested ones. State untested vectors explicitly in residual risk register.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-T-2 | System Prompt Integrity and Override Testing**

*What to examine:* Can the system prompt be overridden through adversarial inputs? Can its contents be leaked?

*Evidence to gather:* Override attempt results, leakage attempt results, evidence of controls functioning.

*Grounded in:* OWASP Top 10 for LLMs 2025 (LLM01; LLM07); MITRE ATLAS AML.T0051.

*Boundary:* Covers techniques in scope. Novel techniques not tested remain unverified.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-T-3 | Agent Tool Scope Boundary Testing** *(if applicable)*

*What to examine:* Can adversarial inputs cause the agent to invoke tools outside intended scope or chain tool use beyond authorized behavior?

*Evidence to gather:* Tool scope boundary test results, out-of-scope invocation records, authorization control verification.

*Grounded in:* OWASP Top 10 for LLMs 2025 (LLM06); MITRE ATLAS; BIML.

*Boundary:* Covers combinations in the test plan. Multi-step interaction effects may not be covered.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-T-4 | Adapter and Plugin Integrity Verification** *(if applicable)*

*What to examine:* Verify cryptographic signatures for externally sourced adapters. Behavioral tests reveal no unexpected capabilities.

*Evidence to gather:* Signature verification records, behavioral test results for adapted vs. base model, anomaly findings.

*Grounded in:* OpenSSF Model Signing Specification; MITRE ATLAS AML.T0010; BIML.

*Boundary:* Signature verification confirms integrity. Dormant behaviors require Bounded Investigation.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-T-5 | Input Validation and Sanitization at Extension Boundaries**

*What to examine:* Controls at each extension point to validate or sanitize inputs; tested against adversarial inputs.

*Evidence to gather:* Input validation documentation, sanitization control records, adversarial test results.

*Grounded in:* OWASP Top 10 for LLMs 2025 (LLM01); BIML; MITRE ATLAS.

*Boundary:* Reduces the prompt injection surface; does not eliminate it.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Bounded Investigation

**EX-B-1 | Systematic Jailbreak Resistance Assessment**

*What to examine:* Comprehensive adversarial testing using documented jailbreak techniques, multi-turn manipulation, role-play exploitation, and novel patterns beyond standard test suites.

*Reference:* MITRE ATLAS AML.T0051; OWASP Top 10 for LLMs 2025 (LLM01); Perez & Ribeiro (2022), "Ignore Previous Prompt," *arXiv 2211.09527*, NeurIPS ML Safety Workshop 2022.

*Ceiling:* Requires adversarial ML expertise. Scope to highest-risk extension points from EX-O-1 and EX-T-1.

**Status:** A / RR / BC

**Scope documented:** *(what was tested, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

**EX-B-2 | Multi-Turn and Context Manipulation Testing**

*What to examine:* Extended adversarial interaction sequences to gradually shift model behavior across turns.

*Reference:* MITRE ATLAS AML.T0051; published research on multi-turn jailbreaking.

*Ceiling:* Requires specialist expertise. Scope to defined conversation lengths. Document untested interaction patterns.

**Status:** A / RR / BC

**Scope documented:** *(what was tested, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

## Domain Residual Risk Register — Extensibility

| Item ID | Description of Gap | Reason Not Fully Assessed | Risk Owner | Review Date |
|---|---|---|---|---|
| | | | | |
| | | | | |

---

# Domain 4: Adaptability

**Force:** Native to ML — #6  
**Core statement:** Security properties do not persist across model updates.

## Force Summary

ML systems can change through deliberate action (fine-tuning, RLHF) or through environmental drift. Foundation model providers update underlying models. Retrieval corpora accumulate new content. Security properties verified at deployment have an expiry date that is often unknown.

## Mechanism of Failure

**Intentional adaptation** — fine-tuning and RLHF updates introduce new training data and alter verified properties.

**Environmental drift** — input distributions shift and model behavior moves with them.

**Foundation model provider updates** — provider may update without sufficient notice for re-evaluation.

**Configuration and retrieval drift** — system prompts, retrieval corpora, and tool configurations change without triggering re-evaluation.

## Foundation Model Boundary

Document what notification mechanisms the provider offers and your organization's process for responding. Carry the gap as explicit residual risk.

## Human Layer Risk Prompt

*Complete this before beginning any check in this domain.*

Write down the date of your last security evaluation and what it covered. Then write what has changed since: in the model, retrieval corpus, system prompt, foundation model dependency, input distribution. "We evaluated this model" becomes "this model is evaluated" as months pass without repetition.

*Assessment narrative written:* [ ] Yes

*Date of last evaluation and what it covered:*

*(write here)*

*What has changed since that evaluation:*

*(write here)*

*What you are still treating as evaluated that may no longer reflect current system state:*

*(write here)*

---

## Observable Checks

**AD-O-1 | Model Version Control and Change Management**

*What to examine:* Documented process for tracking model versions in production; model updates trigger a defined re-evaluation process.

*Evidence to gather:* Version control records, change management documentation, model registry entries.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Manage 4.2).

*Boundary:* Records deployment changes. Does not verify whether security properties were verified for each version.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-O-2 | Foundation Model Update Notification Process** *(if applicable)*

*What to examine:* Documented process for receiving and acting on provider update notifications; assigned responsibility.

*Evidence to gather:* Notification subscription records, internal communication on recent updates, impact assessment records.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Govern 1.4).

*Boundary:* Records notifications received. Does not verify that review correctly assessed security impact.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-O-3 | Post-Deployment Monitoring Documentation**

*What to examine:* Monitoring in place for post-deployment behavior; scope documented; covers security-relevant behaviors, not only performance metrics.

*Evidence to gather:* Monitoring system documentation, alert configuration, scope definitions, records of alerts acted upon.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Measure 2.7).

*Boundary:* Documents what is being watched. Does not verify monitoring covers the right behaviors or that alerts are acted upon.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-O-4 | Adaptation Governance Process**

*What to examine:* Documented process for approving fine-tuning, RLHF updates, retrieval corpus changes, system prompt changes; security review included.

*Evidence to gather:* Governance process documentation, approval records for recent adaptations, evidence of security review.

*Grounded in:* NIST AI RMF (Govern 1.1; Govern 1.7); BIML.

*Boundary:* Documents intended approval chain. Does not verify consistent adherence in practice.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-O-5 | Evaluation Validity Period Policy**

*What to examine:* Documented policy on how long a security evaluation is valid before re-evaluation is required; triggers defined.

*Evidence to gather:* Policy documentation, record of last evaluation, next scheduled re-evaluation.

*Grounded in:* NIST AI RMF (Manage 4.1); BIML.

*Boundary:* Absence of a validity period policy is itself a finding — evaluations have no defined expiry.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Testable Checks

**AD-T-1 | Monitoring Coverage Verification**

*What to examine:* Does monitoring actually fire on security-relevant behavior changes? Test by introducing controlled behavioral variations.

*Evidence to gather:* Monitoring test results, controlled behavior variation records, alert verification records.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Measure 2.7).

*Boundary:* Verifies coverage for tested variations. Changes outside the test set may not be detected.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-T-2 | Update Detection Verification**

*What to examine:* Can your organization detect when a foundation model dependency has been updated? Verify the mechanism works in practice.

*Evidence to gather:* Detection mechanism test results, records of last detected update, verification against recent provider updates.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Govern 1.4).

*Boundary:* Verified detection means you identified that an update occurred. Does not assess security impact.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-T-3 | Security Behavioral Regression Testing**

*What to examine:* Documented test suite for security-relevant behaviors run after model updates; review coverage and recent results.

*Evidence to gather:* Regression test suite documentation, recent test run results, failure records.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF (Measure 2.5).

*Boundary:* Covers scenarios its authors anticipated. Novel failure modes from adaptation may not be in scope.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-T-4 | Adaptation Governance Adherence Verification**

*What to examine:* For recent adaptations, verify the governance process in AD-O-4 was actually followed. Review approval records against adaptation logs.

*Evidence to gather:* Adaptation logs, approval records, evidence of security review, records of adaptations bypassing the process.

*Grounded in:* NIST AI RMF (Govern 1.7); BIML.

*Boundary:* Covers documented adaptations. Undocumented adaptations are a gap in the log, not a gap in what changed.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-T-5 | Drift Detection Review**

*What to examine:* Are drift detection tools producing outputs that are reviewed and acted upon? Has detected drift been assessed for security relevance?

*Evidence to gather:* Recent drift detection reports, review and action records, security relevance assessments.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Measure 2.6).

*Boundary:* Detects statistical distribution shifts. A model can drift in security-relevant ways while appearing statistically normal.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Bounded Investigation

**AD-B-1 | Longitudinal Behavioral Comparison**

*What to examine:* Systematic comparison of model behavior across versions using a structured test battery to identify security-relevant drift.

*Reference:* BIML ML Security Risk Framework; MITRE ATLAS; published LLM behavioral evaluation research.

*Ceiling:* Requires behavioral test battery and retained baselines from prior versions. If BC, document what version comparison was not performed.

**Status:** A / RR / BC

**Scope documented:** *(what was compared, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

**AD-B-2 | Adaptation Interaction Testing**

*What to examine:* Whether post-deployment adaptations have altered security properties established in the initial evaluation.

*Reference:* BIML ML Security Risk Framework; MITRE ATLAS AML.T0020 (fine-tuning context); Hubinger et al. (2024), Anthropic.

*Ceiling:* Requires original evaluation findings as baseline. Scope to adaptations since last evaluation. If BC, document which adaptations were not tested.

**Status:** A / RR / BC

**Scope documented:** *(what adaptations were tested, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

## Domain Residual Risk Register — Adaptability

| Item ID | Description of Gap | Reason Not Fully Assessed | Risk Owner | Review Date |
|---|---|---|---|---|
| | | | | |
| | | | | |

---

# Domain 5: Complexity

**Force:** Inherited — #3  
**Core statement:** The system cannot be fully understood by its builders.

## Force Summary

In ML, scale produces qualitative changes in capability. Emergent behaviors appear that weren't present in smaller versions of the same architecture. Security properties of the whole are not reducible to properties of the parts.

Note: Complexity and Opacity are distinct forces. Complexity asks what the system does that nobody designed. Opacity asks what can be examined about it. They compound, but require different assessment lenses.

## Mechanism of Failure

**Emergent capabilities** — capabilities not present in smaller versions, including security-relevant ones not anticipated.

**Emergent failure modes** — failures not anticipated from component design, exploitable by adversaries.

**Interaction complexity** — security properties of the whole are not reducible to properties of the parts.

**Evaluation incompleteness as structural condition** — the system is too complex to evaluate comprehensively. This is a structural property, not a failure of effort.

## Foundation Model Boundary

A foundation model's emergent capabilities were not designed by the organization deploying it. Their security implications for your specific deployment context have not been evaluated by anyone for your use case.

## Human Layer Risk Prompt

*Complete this before beginning any check in this domain.*

Write down what you know is not covered by this system's security evaluations. Not what you suspect — what you know. Then write whether that unevaluated space is acknowledged as residual risk or simply not discussed.

*Assessment narrative written:* [ ] Yes

*What is explicitly not covered by this system's security evaluations:*

*(write here)*

*Whether that gap is acknowledged as residual risk or simply not discussed:*

*(write here)*

---

## Observable Checks

**CX-O-1 | System Boundary Documentation**

*What to examine:* Complete boundary of the system: all models, retrieval systems, tools, agents, downstream consumers, and external service dependencies.

*Evidence to gather:* System architecture documentation, dependency maps, integration records, service dependency documentation.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Map 1.1); Anderson, *Security Engineering* (3rd ed., 2020).

*Boundary:* A boundary not updated since initial design is a prior assertion, not a current fact.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-O-2 | Technical Dependency Inventory**

*What to examine:* Complete and current inventory of technical dependencies with known vulnerabilities tracked.

*Evidence to gather:* Dependency inventory, software composition analysis outputs, CVE tracking records, hardware and infrastructure dependency documentation.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Map 1.5).

*Boundary:* Transitive dependencies are rarely fully inventoried.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-O-3 | Emergent Behavior Documentation**

*What to examine:* Known emergent behaviors documented; process for discovering and assessing new ones.

*Evidence to gather:* Emergent behavior documentation, red team findings, deployment incident records, discovery process documentation.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF (Measure 2.5).

*Boundary:* Absence of documented emergent behaviors may mean insufficient discovery, not absence of emergence.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-O-4 | Evaluation Scope and Gap Documentation**

*What to examine:* What is explicitly documented as out of scope in security evaluations, distinct from what was evaluated and found acceptable.

*Evidence to gather:* Evaluation scope documentation, explicit gap documentation, rationale for decisions not to evaluate specific areas.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Measure 1.1).

*Boundary:* Absence of gap documentation is itself a significant finding.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-O-5 | Incident Response Coverage for Unknown Failures**

*What to examine:* Incident response plan explicitly accounts for unanticipated failure modes; process for failures that don't match known patterns.

*Evidence to gather:* Incident response plan, recent incident response records, process documentation for anomalous failures.

*Grounded in:* NIST AI RMF (Manage 4.3); BIML.

*Boundary:* A plan covering known failure modes is not a plan for emergent complexity failures.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Testable Checks

**CX-T-1 | Dependency Vulnerability Review**

*What to examine:* Known vulnerabilities in ML frameworks, libraries, and infrastructure tracked and remediated or accepted with rationale.

*Evidence to gather:* Vulnerability scan results, remediation records, accepted-risk records with rationale.

*Grounded in:* BIML ML Security Risk Framework; CVE databases (PyTorch, TensorFlow, JAX); NIST NVD.

*Boundary:* Covers known, disclosed vulnerabilities in catalogued dependencies only.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-T-2 | Inter-Component Interaction Testing**

*What to examine:* Security properties at boundaries between system components: model and retrieval, model and tools, model outputs and downstream consumers.

*Evidence to gather:* Inter-component test plan and results, property violation records, remediation records.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS; Anderson, *Security Engineering* (3rd ed., 2020).

*Boundary:* Interaction complexity grows combinatorially. Comprehensive coverage is not achievable.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-T-3 | Evaluation Coverage Mapping**

*What to examine:* Map what has been evaluated against the full system surface from CX-O-1. Produce explicit evaluated vs. unevaluated picture.

*Evidence to gather:* Evaluation records, system boundary map, coverage mapping analysis, documented residual risk for unevaluated surface.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Measure 1.1).

*Boundary:* 60% coverage means 40% is unknown, not 40% is clean.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-T-4 | Out-of-Distribution Input Testing**

*What to examine:* Systematic testing of inputs outside the designed distribution. Does the system fail gracefully, safely, or exploitably?

*Evidence to gather:* Out-of-distribution test plan and results, failure mode records, graceful vs. unsafe failure documentation.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF (Measure 2.5).

*Boundary:* Tests OOD scenarios the tester designed. Truly novel inputs outside the tester's model of the unusual are outside coverage.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-T-5 | Known Failure Mode Coverage Verification**

*What to examine:* For each known failure mode in CX-O-3: monitoring covers it; incident response plans address it.

*Evidence to gather:* Known failure mode list, monitoring coverage verification per mode, incident response coverage per mode.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Manage 3.1).

*Boundary:* Covers known failure modes only. Unknown failure modes are outside coverage by definition.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Bounded Investigation

**CX-B-1 | Emergent Capability Assessment**

*What to examine:* Specialist assessment of emergent capabilities relevant to the threat model.

*Reference:* BIML ML Security Risk Framework; MITRE ATLAS; Wei et al. (2022), "Emergent Abilities of Large Language Models," *Transactions on Machine Learning Research*.

*Ceiling:* Requires ML security expertise. Scope to capabilities most relevant to the threat model. If BC, document that emergent capability assessment was not performed.

**Status:** A / RR / BC

**Scope documented:** *(what was assessed, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

**CX-B-2 | Full-System Security Assessment**

*What to examine:* Specialist security assessment of the integrated system as a whole — not individual components but all interactions and emergent properties.

*Reference:* BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF (Measure 2.5).

*Ceiling:* Most resource-intensive check in this domain. Scope to highest-risk portions. If BC, document what was not assessed at integrated level.

**Status:** A / RR / BC

**Scope documented:** *(what was assessed, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

## Domain Residual Risk Register — Complexity

| Item ID | Description of Gap | Reason Not Fully Assessed | Risk Owner | Review Date |
|---|---|---|---|---|
| | | | | |
| | | | | |

---

# Domain 6: Opacity

**Force:** Native to ML — #4  
**Core statement:** The system cannot be meaningfully inspected.

## Force Summary

Ken Thompson ended "Reflections on Trusting Trust" with the observation that trust ultimately rests in people, not systems. Model weights are not readable. There is no source of truth a practitioner can examine. Standard security audit has no equivalent in ML. What exists instead is behavioral testing — categorically different from inspection, with categorically different coverage guarantees.

Note: This domain will carry more BC status items than any other. That is not a design failure. It is the framework being honest about Thompson's problem.

## Mechanism of Failure

**Weight opacity** — model weights are unreadable by anyone, including the organization that trained the model.

**Audit impossibility** — traditional code review has no equivalent. What passes for model audit is behavioral testing of a fraction of possible inputs.

**Backdoor persistence through opacity** — Thompson's insight realized. A backdoor in weights leaves no human-readable trace.

**Safety property unverifiability** — safety properties that hold over tested inputs may not hold over untested ones.

## Foundation Model Boundary

For foundation models, opacity is absolute at the practitioner level. You cannot inspect the weights. Do not treat provider documentation as inspection. It is not.

## Human Layer Risk Prompt

*Complete this before beginning any check in this domain.*

When a system cannot be examined, practitioners accept its outputs rather than scrutinizing them — not out of laziness, but because scrutiny has no purchase. Write down what this system is being trusted to do that cannot be verified by inspection. This should be a long list. Then write what organizational decisions rest on that unexaminable trust.

*Assessment narrative written:* [ ] Yes

*What this system is trusted to do that cannot be verified by inspection:*

*(write here)*

*What decisions rest on that unexaminable trust:*

*(write here)*

---

## Observable Checks

**OP-O-1 | Interpretability Tool Documentation**

*What to examine:* What interpretability tools are applied; what they cover; documented limitations.

*Evidence to gather:* Interpretability tool documentation, coverage scope records, published tool limitations.

*Grounded in:* BIML; Anthropic mechanistic interpretability research; LIME (Ribeiro et al. 2016); SHAP (Lundberg & Lee 2017); TCAV (Kim et al. 2018, ICML).

*Boundary:* Post-hoc explanation tools produce approximations of local behavior, not access to internals. A clean interpretability output means no concerning signals in the scoped analysis, not that the model's internals are clean.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-O-2 | Behavioral Testing Scope and Limit Documentation**

*What to examine:* What behavioral testing has been performed; what is explicitly documented as not tested.

*Evidence to gather:* Behavioral test plan and results, explicit documentation of untested categories, known gaps in coverage.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF (Measure 1.1).

*Boundary:* The ratio of tested to total possible inputs is effectively zero. This is structural, not a gap to close with more testing.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-O-3 | Model Documentation Adequacy**

*What to examine:* Does the model card accurately represent what is and is not known about the model's behavior? Does it acknowledge inspection limitations?

*Evidence to gather:* Model card or equivalent, review of claims against supporting evidence.

*Grounded in:* Mitchell et al. (2019), "Model Cards for Model Reporting"; BIML.

*Boundary:* Model card documents what authors chose to include. Claims are statements by creators, not independently verified.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-O-4 | Unknown Behavior Acknowledgment**

*What to examine:* Explicit documentation acknowledging what is unknown about this model's behavior, distinct from what was tested and found acceptable.

*Evidence to gather:* Unknown behavior documentation, risk acceptance records for opacity-related gaps, records of decisions made on unverifiable trust.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Govern 6.1).

*Boundary:* Absence of documented unknowns is itself a significant finding. For most ML deployments, this documentation does not exist. Creating it is the value of this check.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-O-5 | Foundation Model Opacity Statement** *(if applicable)*

*What to examine:* What has the provider published about the model's internals? What is explicitly unverifiable at the practitioner level?

*Evidence to gather:* Provider model cards, technical reports, published interpretability work on the foundation model.

*Grounded in:* Mitchell et al. (2019); BIML.

*Boundary:* Provider documentation is a statement by an interested party, not an independent audit. A = opacity statement produced and documented, not opacity resolved.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Testable Checks

**OP-T-1 | Behavioral Test Coverage Characterization**

*What to examine:* Explicit characterization of what fraction of the relevant input space has been covered by behavioral testing and what properties that coverage supports.

*Evidence to gather:* Behavioral test results, input space characterization, coverage analysis, statement of what coverage permits the practitioner to claim.

*Grounded in:* BIML ML Security Risk Framework; NIST AI RMF (Measure 1.1; Measure 2.5).

*Boundary:* Coverage characterization tells you the shape of the known space. 15% tested means 85% is unknown, not 85% is safe.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-T-2 | Adversarial Robustness Testing**

*What to examine:* What adversarial inputs have been tested; what categories have not been tested. Document both with equal care.

*Evidence to gather:* Adversarial test plan and results, documentation of adversarial categories not tested, vulnerability records.

*Grounded in:* BIML; MITRE ATLAS; Goodfellow, Shlens & Szegedy (2015), *ICLR 2015*; Carlini & Wagner (2017), *IEEE S&P 2017*.

*Boundary:* The adversarial landscape evolves. Opacity means you cannot determine from inspection why a model is vulnerable to a specific input.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-T-3 | Confidence Calibration Testing**

*What to examine:* Does stated confidence correlate with actual accuracy across a representative sample? Miscalibration inhibits human scrutiny.

*Evidence to gather:* Calibration test results, reliability diagram or equivalent, calibration records across input categories.

*Grounded in:* Guo, Pleiss, Sun & Weinberger (2017), "On Calibration of Modern Neural Networks," *ICML 2017*; BIML.

*Boundary:* Tests calibration on tested inputs. Not a guarantee of calibration on out-of-distribution inputs.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-T-4 | Failure Mode Behavioral Characterization**

*What to examine:* For known failure modes: characterize the behavioral signature before, during, and after failure. Can failure be detected from behavioral observation?

*Evidence to gather:* Behavioral characterization records for known failure modes, monitoring signatures, detection records.

*Grounded in:* BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF (Measure 2.6).

*Boundary:* Covers known failure modes. Unknown failure modes produce unknown behavioral signatures.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-T-5 | Interpretability Tool Output Review** *(if applicable)*

*What to examine:* Review interpretability tool outputs from OP-O-1 for security-relevant findings.

*Evidence to gather:* Interpretability tool output records, security-relevant findings, records of findings acted upon.

*Grounded in:* BIML ML Security Risk Framework; Anthropic mechanistic interpretability research.

*Boundary:* Tool outputs cover scoped analysis only. A clean output means no signals in that scope, not that internals are clean.

**Status:** A / RR / BC

**Evidence notes:** *(write here)*

**Residual risk notes:** *(required if RR or BC)*

---

## Bounded Investigation

**OP-B-1 | Mechanistic Interpretability Assessment**

*What to examine:* Specialist assessment using mechanistic interpretability techniques to characterize specific circuits or representations relevant to the threat model.

*Reference:* Elhage et al. (2021), "A Mathematical Framework for Transformer Circuits," Anthropic; Templeton et al. (2024), "Scaling Monosemanticity," Anthropic; BIML.

*Ceiling:* Current techniques cover specific studied behaviors in specific architectures. Comprehensive internal audit is not achievable. Scope tightly to behaviors of concern from behavioral testing. Note: mechanistic interpretability is rapidly developing.

**Status:** A / RR / BC

**Scope documented:** *(what was examined, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

**OP-B-2 | Structured Red Team Assessment**

*What to examine:* Systematic adversarial testing by a dedicated red team specifically targeting the opacity of the model's decision process.

*Reference:* BIML ML Security Risk Framework; MITRE ATLAS; NIST AI RMF (Measure 2.5); published red-teaming methodology for large language models.

*Ceiling:* Requires dedicated adversarial ML expertise. Scope to highest-risk behavior space as defined by the threat model. If BC, document what adversarial scenarios were not covered.

**Status:** A / RR / BC

**Scope documented:** *(what was assessed, what was not, and why)*

**Residual risk notes:** *(required if RR or BC)*

---

## Domain Residual Risk Register — Opacity

*Note: This register is expected to be the longest in the framework. A long residual risk register in this domain is an honest assessment, not a failed one.*

| Item ID | Description of Gap | Reason Not Fully Assessed | Risk Owner | Review Date |
|---|---|---|---|---|
| | | | | |
| | | | | |

---

# Trust Map Summary

*(Complete after all six domains.)*

## Assessed Posture by Force

| Force | Observable | Testable | Bounded | Overall Posture |
|---|---|---|---|---|
| Data Entanglement | | | | |
| Connectivity | | | | |
| Extensibility | | | | |
| Adaptability | | | | |
| Complexity | | | | |
| Opacity | | | | |

## Cross-Domain Residual Risk Register

*Consolidate all RR and BC items from domain registers here.*

| Item ID | Domain | Description | Reason | Owner | Review Date |
|---|---|---|---|---|---|
| | | | | | |

## Assessment Limitations Statement

*Required. A completed assessment without a limitations statement is a false document.*

*(write here)*

## Foundation Model Blind Spot Statement

*Required if foundation model is used.*

*(write here)*

---

*Double Trinity Assessment Framework v0.1*  
*Built on: BIML ML Security Risk Framework · MITRE ATLAS · NIST AI RMF · Thompson (1984) · McGraw & Hoglund (2004)*

---

# Reference List

## Frameworks and Standards

**BIML ML Security Risk Framework.** Berryville Institute of Machine Learning. https://berryvilleiml.com/

**MITRE ATLAS.** Adversarial Threat Landscape for Artificial-Intelligence Systems. MITRE Corporation. https://atlas.mitre.org/

**NIST AI RMF.** Artificial Intelligence Risk Management Framework. NIST, 2023. https://www.nist.gov/system/files/documents/2023/01/26/NIST-AI-100-1.pdf

**OWASP Top 10 for LLM Applications 2025.** LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. https://owasp.org/www-project-top-10-for-large-language-model-applications/

**OWASP API Security Top 10 2023.** OWASP Foundation. https://owasp.org/API-Security/editions/2023/en/0x11-t10/

**OpenSSF Model Signing Specification.** https://github.com/sigstore/model-transparency

**C2PA.** https://c2pa.org/

**SLSA.** https://slsa.dev/

## Papers

Gebru, T. et al. (2021). Datasheets for datasets. *Communications of the ACM*, 64(12), 86–92.

Mitchell, M. et al. (2019). Model cards for model reporting. *FAT* '19*, 220–229.

Gu, T., Dolan-Gavitt, B., & Garg, S. (2017). BadNets. *arXiv:1708.06733*.

Tran, B., Li, J., & Madry, A. (2018). Spectral signatures in backdoor attacks. *NeurIPS 2018*.

Chen, B. et al. (2019). Detecting backdoor attacks by activation clustering. *AAAI Workshop on AI Safety*.

Northcutt, C. G., Jiang, L., & Chuang, I. L. (2021). Confident learning: Estimating uncertainty in dataset labels. *Journal of Artificial Intelligence Research*, 70, 1373–1411. https://doi.org/10.1613/jair.1.12125

Wang, B. et al. (2019). Neural cleanse. *IEEE S&P 2019*, 707–723.

Hubinger, E. et al. (2024). Sleeper agents. *arXiv:2401.05566*. Anthropic.

Tramèr, F. et al. (2016). Stealing machine learning models via prediction APIs. *USENIX Security 2016*, 601–618.

Blanchard, P. et al. (2017). Machine learning with adversaries: Byzantine tolerant gradient descent. *NeurIPS 2017*, 118–128.

Perez, F., & Ribeiro, I. (2022). Ignore previous prompt. *arXiv:2211.09527*. NeurIPS ML Safety Workshop 2022.

Greshake, K. et al. (2023). Not what you've signed up for. *AISec '23*, 79–90.

Thompson, K. (1984). Reflections on trusting trust. *Communications of the ACM*, 27(8), 761–763.

McGraw, G., & Hoglund, G. (2004). *Exploiting Software: How to Break Code*. Addison-Wesley.

Anderson, R. (2020). *Security Engineering* (3rd ed.). Wiley.

Shaw, S. D., & Nave, G. (2026). Thinking—Fast, Slow, and Artificial: How AI is reshaping human reasoning and the rise of cognitive surrender. SSRN preprint, 11 January 2026. https://doi.org/10.2139/ssrn.6097646

Edmans, A. (2024). *May Contain Lies: How Stories, Statistics, and Studies Exploit Our Biases—And What We Can Do about It*. University of California Press.

Wei, J. et al. (2022). Emergent abilities of large language models. *Transactions on Machine Learning Research*.

Goodfellow, I., Shlens, J., & Szegedy, C. (2015). Explaining and harnessing adversarial examples. *ICLR 2015*.

Carlini, N., & Wagner, D. (2017). Towards evaluating the robustness of neural networks. *IEEE S&P 2017*, 39–57.

Guo, C. et al. (2017). On calibration of modern neural networks. *ICML 2017*, 1321–1330.

Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?". *KDD 2016*, 1135–1144.

Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. *NeurIPS 2017*.

Kim, B. et al. (2018). Interpretability beyond feature attribution: Quantitative testing with concept activation vectors (TCAV). *ICML 2018*, 2673–2682.

Elhage, N. et al. (2021). A mathematical framework for transformer circuits. Anthropic. https://transformer-circuits.pub/2021/framework/index.html

Templeton, A. et al. (2024). Scaling monosemanticity. Anthropic. https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
