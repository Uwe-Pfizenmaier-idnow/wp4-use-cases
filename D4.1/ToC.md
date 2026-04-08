# D4.1: UC Specifications and Scenarios

## Table of Contents

### 1. Executive Summary (GRNET)

### 2. Introduction (GRNET)

- 2.1 Purpose and Scope of this Deliverable (GRNET)

- 2.2 Relation to the Grant Agreement and WP4 Objectives (GRNET)

- 2.3 Relation to Other Work Packages and Deliverables (GRNET)

  - 2.3.1 WP2 -- Technical Standards and Specifications (GRNET)

    > WP2 provides the technical profiles, testbed, and trust infrastructure that WP4 implementations must comply with. References D2.1 (implementation profiles) and the testbed (D2.2/D2.3) that WP4 will use for conformance and interoperability testing.

  - 2.3.2 WP3 -- Digital Travel Credentials (DTC) (Amadeus, UAegean, IN Groupe)

    > Several WP4 travel use cases involve passengers whose passport data is held as a DTC managed by WP3.

  - 2.3.3 WP6 -- Wallet for Payment and Banking (UAegean, PagoPA)

    > WP4 use cases that include payment steps (hotel booking, taxi, ferry, train tickets, student fares) rely on WP6.

- 2.4 Document Structure (GRNET)

- 2.5 Terminology and Definitions (GRNET)

  > Defines most used key terms used throughout the document (EUDIW, PID, EAA, RP, CI, etc.). Full list in Annex C.

### 3. Methodology

> Describes how the content of this deliverable was produced during the T4.2 stock-taking phase.

- 3.1 Stock-Taking and Analysis Approach (GRNET)

  > Outlines the overall process: how the 11 use cases were collected, and how the analysis was structured (business requirements → legal analysis → functional/non-functional specifications). Presents and explains the standardised template used by all 11 UC leads to document their use cases. Explains why this template was chosen and its goals.

- 3.2 Stakeholder Involvement (All UC leads)

  > Categories of stakeholders consulted/involved and the engagement methods (workshops, bilateral calls, written questionnaires).

- 3.3 Sources and Tools (All UC leads)

  > Key reference documents (ARF, eIDAS Implementing Acts, ICAO standards, IATA specifications, European Student Card Initiative documentation) and any collaborative tools used (e.g., document repositories, shared templates).

### 4. WP4 Scenarios and Use Cases

> Scenario-level and UC-level view. Presents each of the three WP4 scenarios, and the use cases that contribute to them. Detailed per-UC specification sheets are in Annex A.

- 4.1 Overview and Use Case Mapping (GRNET)

  > High-level summary table of all 11 accepted use cases.

- 4.2 UC 1 -- Board the Flight (Amadeus)

- 4.3 UC 2 -- Electronic Travel Authorization / ETA (Amadeus)

- 4.4 UC 3 -- Seamless Digital Traveller Experience / SEDIT-X (UAegean)

  - 4.4.1 Episode 1 -- Smart Airport: Biometric Boarding (UAegean)

  - 4.4.2 Episode 2 -- Urban Mobility in Athens (UAegean)

  - 4.4.3 Episode 3 -- Ferry Transport (UAegean)

  - 4.4.4 Episode 4 -- Hospitality (UAegean)

  - 4.4.5 Episode 5 -- Academic Access (UAegean)

- 4.5 UC 4 -- Streamlined Travel Experience (FastID)

- 4.6 UC 5 -- Stadium Access (FastID)

- 4.7 UC 6 -- European Student Experience / Student Access via EUDI Wallet (iDAKTO / PagoPA)

- 4.8 UC 7 -- Accessing Discounted Train Fares via EUDIW (PagoPA)

- 4.9 UC 8 -- Overnight Hospitality & Cross-Border Train Journey (PagoPA)

- 4.10 UC 9 -- Biometric Profile / Carrier Held Biometrics for Seamless Airport Travel (IN Groupe)

- 4.11 UC 10 -- Streamlined End-to-End Hotel Booking (IDnow)

- 4.12 UC 11 -- France-Canada Student Digital Identity (SIROS Foundation)

### 5. Current Landscape and Baseline Analysis (All UC leads → GRNET)

> Findings of the T4.2 stock-taking activity "Analysis of existing processes, technical implementations supporting online services, identity matching and management." Establishes the baseline against which the EUDIW-enabled use cases are designed: how things work today, what technology is already in place, and where the gaps and pain points may exist.

- 5.1 Current Processes and Existing Implementations (All UC leads)

  > Describes how each sector currently handles the processes that WP4 aims to transform with the EUDIW. For each sector: existing digital infrastructure (APIs, apps, identity systems) that WP4 implementations will need to interoperate.

- 5.2 Identity Matching and Management (All UC leads)

  > How organisations in each sector currently match a person to their booking, ticket, or enrolment? Current approaches and their limitations (transliteration errors, name discrepancies across documents, no interoperable identity layer across providers or borders). Describes how the EUDIW's technologies address these challanges.

- 5.3 Current Constraints, Limitations and Pain Points (All UC leads)

  > Summary of pain points identified from the analysis in 5.1 and 5.2. Also identifies technical and operational constraints that the pilot implementations will need to work within or around.

### 6. Legal and Regulatory Framework (GRNET)

> Legal and regulatory context that constrains or enables the WP4 use cases.

- 6.1 eIDAS 2.0 and Implementing Acts (GRNET)

  > Provisions of the revised eIDAS Regulation and its Implementing Acts that are directly relevant to WP4: mandatory wallet provision, credential issuance/verification obligations, trust framework requirements, and cross-border recognition rules.

- 6.2 Sector-Specific Regulations (Review by UC Leads)

  > Covers regulations beyond eIDAS that apply to specific WP4 scenarios.

  - 6.2.1 Hospitality and Guest Registration (GRNET)

  - 6.2.2 Transport and Passenger Rights (GRNET)

  - 6.2.3 Student Mobility and Academic Recognition (GRNET)

### 7. Technical Foundations (All UC leads → GRNET)

> Describes the technical building blocks that underline WP4 use cases. Individual UC-specific technical details are in Annex A.

- 7.1 EUDIW Architecture and Reference Framework (ARF) Alignment (All UC leads)

  > How WP4 implementations align with the ARF: which ARF components are used (wallet instance, PID provider, attestation provider, relying party), which protocol profiles, baseline version.

  - 7.1.1 "UC Title - UC Lead name" (repeating for all use cases)

- 7.2 Credential Types and Attestations Used in WP4 (All UC leads → GRNET)

  > Overview of all credential types that appear across the 11 use cases, with their data models, issuers, and intended verifiers.

  - 7.2.1 UC 1
      - 7.2.1.1 PID (Personal Identification Data)
      - 7.2.1.2 Electronic Attestations of Attributes (EAA / QEAA)

  - 7.2.2 UC 2
  ...

- 7.3 Issuance, Verification and Revocation Flows (All UC leads)

  - 7.3.1 UC 1
    - 7.3.1.1 Issuance
    - 7.3.1.2 Verification
    - 7.3.1.3 Revocation

- 7.4 Selective Disclosure and User Consent (All UC leads)

  > How WP4 use cases implement selective disclosure.

  - 7.4.1 UC 1
    - 7.4.1.1 Selective Disclosure
    - 7.4.1.2 User Consent

- 7.5 Trust Framework and Trusted Issuer Lists (All UC leads)

  > How WP4 relying parties determine whether a presented credential is trustworthy, covering cross-border cases.

  - 7.5.1 UC 1
    - 7.5.1.1 Trust Framework
    - 7.5.1.2 Trusted Issuer Lists

- 7.6 Standards and Protocols (All UC leads → GRNET)

  > All WP4-related specific technical standards and protocols.

  - 7.6.1 UC 1 Technical standards and protocols

### 8. Description of the Ecosystem: Actors and Roles (All UC leads → GRNET)

> Consolidated view of all actor types that participate in WP4 use cases. Definition of actor types and roles.

- 8.1 Mapping of Actors to Use Cases and Scenarios (All UC leads → GRNET)

  > A summary table mapping each APTITUDE actor to the UCs they participate in, indicating their role (wallet issuer, PID provider, credential issuer, relying party).

### 9. Challenges and Opportunities (All UC leads → GRNET)

> Reflect on what may go wrong, what is uncertain, and what lies ahead.

- 9.1 Identified Risks and Mitigation Measures (All UC leads → GRNET)

  > Lists the risks specific to WP4 use cases (drawn from the Grant Agreement risk register and updated with risks discovered during stock-taking): interoperability gaps between operators (Risk 10), scheduling overlap with other LSPs (Risk 4), instability of technical specifications (Risk 5), regulatory uncertainty in specific Member States, etc. For each risk, describe the agreed mitigation measures.

- 9.2 Future Directions and Open Questions (All UC leads → GRNET)

  > Identifies topics that are relevant to WP4 but are deliberately out of scope for D4.1 or the current project phase: extensions to additional transport modes, integration with other LSPs, long-term credential lifecycle management, and scalability considerations for production deployment. Also lists open technical or legal questions that remain unresolved and need further work in D4.2 or beyond.

### 10. Conclusions and Next Steps (GRNET)

> Summary and forward-looking roadmap.

- 10.1 Summary of Specified Use Cases (GRNET)

  > Recaps the 11 use cases across 3 scenarios: what was specified, the key findings from the stock-taking, and the overall readiness level for the next phases.

- 10.2 Open Issues and Outstanding Decisions (All UC leads → GRNET)

  > Lists concrete open items that need resolution before or during the implementation phase, besides the ones in 9.1.

- 10.3 Roadmap Towards D4.2 (Implementation Manual) (GRNET)

  > Describes the planned activities and timeline for moving from specifications (D4.1) to implementation (D4.2): what needs to happen in T4.3 (implementation support), the key milestones (Milestone 15 at M18), and the expected structure of D4.2.

- 10.4 Roadmap Towards D4.3 (Validation Report) (GRNET)

  > Describes the planned activities for T4.4 (piloting, user testing, UC evaluation) that will feed into D4.3: testing approach, KPI framework, feedback collection, and the expected structure of D4.3 (Milestone 16 at M22).

### Annexes

- Annex A: Detailed Use Case Specification Sheets (Each UC lead)

  > One complete specification sheet per UC (11 total), each following the standardised template from Section 3.4.

- Annex B: List of WP4 Partners and Roles (GRNET)

  > Complete list of all APTITUDE partners involved in WP4, with their country, organisation type, and role(s) in each use case (UC lead, credential issuer, relying party, wallet provider, etc.).

- Annex C: Glossary (GRNET)

  > Full glossary of terms used throughout the document, expanding on the key terms introduced in Section 2.5.

- Annex D: List of Authors (All)

- Annex E: References (All UC leads → GRNET)

  > Grant Agreement, ARF versions, eIDAS Regulation and Implementing Acts, standards, laws, WP2 technical profiles, etc.
