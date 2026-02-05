# PRD — Bloomberg-Harvard City Leadership Initative (BHCLI) Impact OS (Impact OS + City Capability Graph + Impact Story Studio)

**Doc version:** 1.0 (one-shot build spec for an agentic coding implementation)
**Audience:** Engineering (Codex), Product, Impact/Research, Program Ops, Comms
**Primary outcome:** A single internal platform that (1) unifies evidence and outcomes, (2) models relationships as a capability knowledge graph, and (3) generates evidence-backed stories/reports with citations + confidence—while matching BHCLI’s editorial, topic-driven UI/UX.

---

## 0) Executive summary

BHCLI Impact OS is a **staff-only** web application composed of three tightly integrated modules:

1. **Impact OS (Evidence + Dashboards):**
   Central repository for 10 years of program data, city outcome indicators, and qualitative evidence; role-based dashboards; reproducible analysis “runs”; exportable figures/tables.

2. **City Capability Graph (Knowledge Graph):**
   A queryable graph that connects **Cities ↔ Leaders ↔ Cohorts ↔ Practices/Topics ↔ Initiatives ↔ Evidence ↔ Outcomes ↔ Confounders/Context** to support contribution-style analysis and pattern discovery.

3. **Impact Story Studio (Claim → Evidence → Confidence → Citations → Visuals):**
   A guided, AI-assisted workspace to draft narratives and reports where **every claim is backed by linked evidence objects**, includes caveats and alternative explanations, and exports to DOCX/PDF/Slides-ready outlines.

**Key principle:** AI is **assistive**. The tool never “declares impact” without **linked sources** and an explicit **confidence rationale**.

---

## 1) Problem statement

BHCLI needs to deliver a credible **10-year impact assessment** demonstrating how making city leaders more effective contributes to better city outcomes. Current evidence is typically fragmented across surveys, documents, notes, spreadsheets, and public datasets—making it hard to:

* trace “capability building” → outcomes across cohorts and cities
* standardize the theory of change and measurement
* produce consistent, well-cited stories, dashboards, and funder reporting
* do rigorous analysis quickly and repeatably

---

## 2) Goals, non-goals, and success metrics

### 2.1 Goals (what success looks like)

**G1. Evidence traceability:** 90%+ of final published “key claims” in the 10-year report have:

* linked evidence objects,
* visible citations (source docs + excerpt anchors),
* confidence rating + rationale,
* logged methodology and caveats.

**G2. Repeatable reporting:** Reduce time to produce recurring outputs (annual impact summary / funder updates) by **60%+** via reusable templates and claim/evidence re-use.

**G3. Discovery and analysis:** Enable the impact team to answer queries like:

* “Which cities that participated in the Data & Evidence track show improvements in performance management indicators within 18 months?”
* “What common enabling conditions show up in high-confidence collaboration improvements?”

**G4. BHCLI-style experience:** Topic-driven navigation and card-based editorial layouts that feel like BHCLI’s public-facing content.

### 2.2 Non-goals (v1)

* Automated causal attribution (“BHCLI caused X”) without human review.
* Real-time monitoring for every city KPI.
* Building a full CRM replacement.

### 2.3 Product success metrics (instrumented)

* **Weekly active users** by role (Impact, Program, Comms, Leadership)
* **Claim reuse rate** (claims reused across outputs with updated evidence)
* **Evidence coverage** per ToC node and per cohort (coverage score)
* **AI acceptance rate** (draft outputs accepted after edits)
* **Median time-to-draft**: “City vignette” and “Section draft”
* **Search latency** p50/p95
* **Export count** + export error rate

---

## 3) Users, roles, and permissions

### 3.1 Personas

* **Impact/Research Lead:** defines ToC, approves claims, runs analysis.
* **Impact Analyst:** imports evidence, codes themes, builds dashboards.
* **Program Ops:** manages cohorts, participants, sessions, attendance.
* **Comms/Fundraising:** builds stories and report outputs.
* **Executive/Leadership:** consumes dashboards and curated outputs.
* **External Viewer (optional later):** read-only access to curated exports.

### 3.2 RBAC roles (must-have)

* **Admin**: system config, user provisioning, global policies.
* **Impact Editor**: create/edit evidence, claims, ToC, analyses; approve exports.
* **Program Editor**: cohort/participant/session data; view evidence (limited).
* **Comms Editor**: story studio; can draft claims, but needs approval to publish/export externally.
* **Viewer**: read-only dashboards + approved reports.

### 3.3 Data access controls

* Evidence has **confidentiality levels**: `Public`, `Internal`, `Sensitive`, `Restricted`.
* User role + team determines access; exports enforce policy gates:

  * “External export” requires **Impact Editor approval** and PII scan pass.

---

## 4) Product scope: modules and capabilities

### Module A — Evidence & Impact OS

1. Evidence Library (documents, surveys, notes, metrics, artifacts)
2. ToC Builder + Evidence Mapping
3. Dashboards + Analysis Runs
4. Search (metadata + full-text + semantic)
5. Export (tables, figures, appendices)

### Module B — City Capability Graph

1. Graph schema/ontology + synchronization
2. Query UI (“Graph Explorer”) + saved queries
3. Pattern detection helpers (cohort comparisons, pathway views)

### Module C — Impact Story Studio

1. Claim Cards (claim → evidence → confidence → caveats)
2. Storyboards (multi-claim narrative flows)
3. Section/Report Builder (templated outputs + citations)
4. AI Copilot with strict citation + audit trail

---

## 5) UX/UI: BHCLI-style requirements

**Design intent:** Editorial, calm, and topic-led—organized like an “Explore by Topic” resource library with cards and whitespace.

### 5.1 Visual language (implementation-ready tokens)

Implement a theme system with tokens; defaults approximate BHCLI vibes but are configurable:

* **Typography**

  * Display: `--font-display` (e.g., a clean sans or editorial serif)
  * Body: `--font-body` (readable sans)
  * Scale: H1 44–56px, H2 32–40px, body 16–18px, generous line-height.

* **Layout**

  * 12-col grid, max width 1200–1320px
  * Spacing: 8px baseline; lots of vertical breathing room.

* **Cards**

  * Rounded corners (12–16px)
  * Subtle shadows, bordered states
  * “Editorial card” template: eyebrow label → headline → short deck → metadata chips.

* **Navigation**

  * Top-level: `Explore`, `Graph`, `Story Studio`, `Dashboards`, `Reports`, `Admin`
  * Global topic filter: `Collaboration`, `Data & Evidence`, `Innovation`, `Strategic Leadership & Management` (configurable list)

### 5.2 Key screens (must-have)

1. **Home / Explore**

   * Featured cards: “Latest insights,” “Cities to watch,” “Draft claims needing review”
   * Topic chips + cohort filter + search bar
2. **Evidence Library**

   * Filters: topic, cohort year, city, evidence type, confidentiality, date range, tags
   * Evidence card grid + list view toggle
3. **City Profile**

   * Timeline of “change episodes”
   * Capability signals (surveys/themes) + outcome indicators
   * Linked evidence + key claims
4. **ToC Map**

   * Node graph (editable) + evidence strength meter per node
5. **Graph Explorer**

   * Query builder + results table + graph visualization
6. **Story Studio**

   * Claim builder + storyboard canvas + report section generator
7. **Dashboards**

   * Role-based views + saved “analysis runs”
8. **Reports**

   * Build/export final report; versioned outputs

---

## 6) Data model (relational + graph)

### 6.1 Core entities (relational DB)

**Cities**

* `city_id (uuid)`, name, state/country, population (optional), region, metadata JSON

**Leaders/Participants**

* `person_id`, name, role_title, org (mayor’s office/agency), city_id, start/end in role, contact fields (optional, PII)

**Cohorts / Programs**

* `cohort_id`, name, year, start/end dates
* `program_id`, name, description
* join tables:

  * `cohort_participants(person_id, cohort_id, role_in_program, attendance_score)`
  * `cohort_sessions(session_id, cohort_id, topic_id, date, format, facilitators)`

**Topics / Practices**

* `topic_id`, name, parent_topic_id (for taxonomy), description
* Example taxonomy:

  * Collaboration
  * Data & Evidence
  * Innovation
  * Strategic Leadership & Management

**Evidence Objects** (the spine)

* `evidence_id`, type enum (`doc`, `survey`, `interview`, `note`, `metric_series`, `artifact`, `publication`)
* `title`, `summary`, `city_id (nullable)`, `cohort_id (nullable)`, `topic_ids[]`
* `source_uri` (S3/Blob path), `source_system` (upload/connector)
* `confidentiality`, `consent_status`
* `created_by`, `created_at`, `version`
* `quality_signals JSON` (sample size, method, missingness, etc.)
* `extracted_entities JSON` (AI-extracted)
* `full_text` (for search; or separate table)

**Evidence Excerpts (citation anchors)**

* `excerpt_id`, `evidence_id`, `page_start`, `page_end`, `char_start`, `char_end`
* `quote_text` (redactable), `redaction_status`, `created_by`

**Outcome Indicators**

* `indicator_id`, name, description, unit, directionality (+/-)
* `city_indicator_series(series_id, city_id, indicator_id)`
* `indicator_points(point_id, series_id, date, value, source_evidence_id, method_note)`

**Change Episodes (qualitative timeline)**

* `episode_id`, city_id, date_start/end, title, description
* links: evidence, initiatives, leadership transitions, confounders

**Initiatives/Interventions**

* `initiative_id`, city_id, name, start/end, description, status
* linked topics, linked evidence, linked outcomes

**Theory of Change**

* `toc_id`, name, version, description
* `toc_nodes(node_id, toc_id, node_type enum [input/activity/output/capability/outcome], title, definition)`
* `toc_edges(edge_id, toc_id, from_node_id, to_node_id, rationale)`
* `toc_node_evidence(node_id, evidence_id, support_type enum [supports/contradicts/context], strength_weight)`

**Claims (Story Studio atom)**

* `claim_id`, title, claim_text
* `claim_scope` (city/cohort/global), `city_id nullable`, `cohort_id nullable`, `topic_ids[]`
* `confidence enum [Low/Med/High]`
* `confidence_rationale`
* `alt_explanations` (array)
* `status enum [draft/in_review/approved/published/archived]`
* links:

  * `claim_evidence(claim_id, evidence_id, excerpt_id nullable, role enum [supporting/counter/context])`

**Reports**

* `report_id`, title, type enum [impact_assessment/annual_update/funder_brief/city_vignette]
* `sections(section_id, report_id, order, title, content_md, generated_from_storyboard_id)`
* `report_claims(report_id, claim_id, order)`
* `exports(export_id, report_id, format, status, file_uri, created_at, created_by)`

**Audit logs (required)**

* `audit_id`, actor_id, action, entity_type, entity_id, timestamp, diff_json`

---

### 6.2 Knowledge graph ontology (graph DB)

Use a graph database (recommended) OR implement as adjacency tables + materialized views. Graph DB recommended for agentic querying.

**Node labels**

* `City`, `Person`, `Cohort`, `Topic`, `Practice`, `Initiative`, `Evidence`, `Claim`, `Indicator`, `Episode`, `Outcome`, `ContextEvent`

**Relationships (examples)**

* `(Person)-[:PARTICIPATED_IN {role, attendance}]->(Cohort)`
* `(Cohort)-[:COVERED_TOPIC]->(Topic)`
* `(City)-[:HAS_LEADER]->(Person)`
* `(City)-[:RAN_INITIATIVE]->(Initiative)`
* `(Evidence)-[:ABOUT_CITY]->(City)`
* `(Evidence)-[:SUPPORTS]->(Claim)`
* `(Claim)-[:MAPS_TO]->(ToCNode)`
* `(City)-[:HAS_INDICATOR]->(IndicatorSeries)`
* `(Episode)-[:SUPPORTED_BY]->(Evidence)`
* `(ContextEvent)-[:AFFECTS]->(City)`

**Graph synchronization rule**

* Relational DB is source of truth.
* A “graph sync worker” updates graph nodes/edges on create/update events.

---

## 7) AI Copilot: requirements and guardrails

### 7.1 AI jobs (must-have)

1. **Ingestion extraction**

   * Parse doc → extract metadata suggestions: city/cohort/topic, entities (people/orgs), dates, initiatives mentioned, outcome indicators mentioned
2. **Excerpt suggestion**

   * Identify candidate quotable passages with offsets
3. **Evidence-to-claim suggestion**

   * Propose which evidence supports/contradicts a claim
4. **Claim drafting**

   * Draft claim text + confidence + caveats
5. **Section drafting**

   * Draft report section with citations and claim cards embedded
6. **PII detection + redaction suggestions**

   * Flag personal emails, phone numbers, sensitive attributes (conservative)

### 7.2 Hard constraints (enforced in code)

* **No-citation mode disabled by default**: AI cannot output “findings” without linking evidence IDs.
* AI outputs must return structured JSON with:

  * `output_text`
  * `citations: [{evidence_id, excerpt_id|char_range, relevance}]`
  * `confidence`
  * `limitations`
* Every AI-generated artifact stores:

  * prompt template ID + version
  * model config ID
  * evidence IDs used
  * output hash
  * human edits (diff)

### 7.3 Retrieval strategy (agentic + safe)

* Hybrid retrieval:

  * metadata filters (city, cohort, topic, confidentiality)
  * full-text search
  * vector search (embeddings) on evidence chunks
* Build “evidence packs” (curated sets) for each claim/section to keep context bounded and auditable.

### 7.4 Prompt templates (implementation-ready)

**Template: Claim Draft**

* Inputs: claim goal, scope (city/cohort/global), topic, ToC node, evidence pack
* Output JSON schema:

  * `claim_text`, `confidence`, `confidence_rationale`, `supporting_citations`, `counter_citations`, `alternative_explanations`, `suggested_visuals`

**Template: Section Draft**

* Inputs: section title, report type, storyboard (ordered claims), style guide
* Output JSON schema:

  * `section_md`, `citations`, `figures_needed`, `tables_needed`, `review_notes`

**Style guide input** (BHCLI editorial feel)

* crisp, action-oriented headings
* short paragraphs, strong subheads
* “What changed / How / Evidence / What to watch” framing

---

## 8) Functional requirements (by module) with acceptance criteria

### 8.1 Evidence Library (Impact OS)

**FR-E1 Upload & ingest**

* Upload PDF/DOCX/CSV/XLSX/PNG/JPG + bulk import via CSV manifest.
* Must extract text and store page/offset mapping for citations.

**Acceptance criteria**

* Upload completes with processing status (`queued → processing → ready/failed`).
* Evidence is searchable within 2 minutes for files <50MB.
* Excerpts can be created with stable anchors (page + char offsets).

**FR-E2 Metadata + taxonomy**

* Required fields: title, type, confidentiality, topics, date range, city/cohort (optional)
* Suggested fields auto-populated by AI but editable.

**Acceptance criteria**

* Cannot mark evidence “Approved for external export” unless confidentiality <= Internal and consent_status valid.

**FR-E3 Evidence cards**

* Card shows: title, type icon, topics chips, city/cohort chips, confidentiality badge, “evidence quality” meter.

**Acceptance criteria**

* Card grid and list view both supported; filters persist in URL.

---

### 8.2 ToC Builder + Evidence Mapping

**FR-T1 ToC editing**

* Create ToC versions; nodes and edges; node types (input/activity/output/capability/outcome).

**Acceptance criteria**

* ToC versioning: changes create a new version; prior versions remain viewable and exportable.

**FR-T2 Evidence mapping**

* Attach evidence to ToC nodes with support type and weight.

**Acceptance criteria**

* Node displays coverage score:

  * coverage = (#evidence linked * quality weights * recency factor)
* Clicking coverage reveals evidence list.

---

### 8.3 Dashboards + Analysis Runs

**FR-D1 Dashboard widgets**

* Cohort reach, topic uptake, participant engagement, capability survey shifts, outcome indicator trends.

**Acceptance criteria**

* Widgets can be saved into a dashboard layout per role.

**FR-D2 Analysis runs**

* A “run” is a saved configuration (filters + methods + indicator selections) producing outputs (tables/figures).

**Acceptance criteria**

* Runs are reproducible: re-running yields same outputs given same dataset snapshot.

---

### 8.4 City Capability Graph

**FR-G1 Graph Explorer**

* Query builder supports:

  * city + cohort + topic filters
  * pathway view: (topic participation → initiative → indicators)
  * “find similar cities” by capability signature

**Acceptance criteria**

* Queries can be saved and shared (RBAC enforced).
* Results show both graph visualization + exportable table.

**FR-G2 Graph sync**

* Any update to core entities triggers graph update.

**Acceptance criteria**

* Sync latency p95 < 60 seconds.
* Graph is consistent with relational source (daily reconciliation job).

---

### 8.5 Impact Story Studio

**FR-S1 Claim cards**

* Guided claim creation:

  1. define claim scope
  2. select ToC node + topic
  3. attach evidence + excerpts
  4. write confidence + caveats
  5. request AI draft (optional)

**Acceptance criteria**

* Claim cannot move to “Approved” without:

  * ≥2 evidence objects OR explicit note why only one
  * ≥1 excerpt anchor
  * confidence rationale and at least one alternative explanation field (can be “none identified”)

**FR-S2 Storyboards**

* Storyboard is an ordered set of claims + transitions.

**Acceptance criteria**

* Storyboard supports drag-drop ordering; exports outline with citations.

**FR-S3 Report builder**

* Templates:

  * 10-year impact report
  * funder brief (2–4 pages)
  * city vignette (1–2 pages)
* Exports:

  * DOCX (must-have)
  * PDF (must-have)
  * “Slides outline” (text + figure list) (must-have)

**Acceptance criteria**

* Export includes an auto-generated citations appendix with evidence links and excerpt references.

---

## 9) Search requirements

### 9.1 Search types

* **Metadata search** (filters + exact match)
* **Full-text search** (BM25 / DB FTS)
* **Semantic search** (vector embeddings)
* **Hybrid ranking** with confidentiality gating

### 9.2 Acceptance criteria

* Search respects RBAC: restricted items never appear in results.
* Search p95 latency:

  * metadata-only: <300ms
  * hybrid: <1500ms (typical corpus)

---

## 10) System architecture (implementation blueprint)

### 10.1 Recommended stack (opinionated for one-shot build)

* **Frontend:** Next.js (TypeScript) + Tailwind + shadcn/ui
* **Backend API:** FastAPI (Python) or NestJS (TS) — choose one; below assumes **FastAPI**
* **DB (relational):** Postgres
* **Vector search:** pgvector (in Postgres)
* **Graph DB:** Neo4j (or Postgres + AGE extension if avoiding Neo4j)
* **Queue/Workers:** Redis + Celery/RQ (Python) for ingestion + AI jobs
* **File storage:** S3-compatible (or Azure Blob)
* **Auth:** SSO (SAML/OIDC) + RBAC
* **Observability:** OpenTelemetry + structured logs + audit log table

### 10.2 Services (logical)

1. **API service**
2. **Ingestion worker**
3. **AI worker**
4. **Graph sync worker**
5. **Export worker** (DOCX/PDF generation)

### 10.3 Repository structure (suggested)

```
/apps/web            # Next.js
/apps/api            # FastAPI
/packages/ui         # design system components + tokens
/packages/shared     # types + schemas
/services/worker     # Celery/RQ jobs
/infra               # docker-compose, k8s manifests, terraform optional
```

### 10.4 Environment variables (minimum)

* `DATABASE_URL`
* `REDIS_URL`
* `STORAGE_BUCKET`, `STORAGE_ENDPOINT`, `STORAGE_ACCESS_KEY`, `STORAGE_SECRET_KEY`
* `GRAPH_URL`, `GRAPH_USER`, `GRAPH_PASSWORD`
* `LLM_PROVIDER_API_KEY` (provider-agnostic)
* `SSO_OIDC_ISSUER`, `SSO_CLIENT_ID`, `SSO_CLIENT_SECRET`
* `ENCRYPTION_KEY` (field-level for PII)

---

## 11) API specification (high-level endpoints)

### Auth & users

* `GET /me`
* `GET /users` (admin)
* `POST /users/invite` (admin)
* `GET /roles`, `PUT /users/{id}/roles`

### Core entities

* `GET/POST /cities`, `GET/PUT /cities/{id}`
* `GET/POST /people`, `GET/PUT /people/{id}`
* `GET/POST /cohorts`, `GET/PUT /cohorts/{id}`
* `GET/POST /topics`, `GET/PUT /topics/{id}`

### Evidence

* `POST /evidence/upload` (multipart)
* `GET /evidence` (filters)
* `GET /evidence/{id}`
* `PUT /evidence/{id}`
* `POST /evidence/{id}/excerpts`
* `GET /evidence/{id}/excerpts`
* `POST /evidence/{id}/process` (re-run extraction)
* `POST /evidence/bulk_import` (manifest)

### ToC

* `POST /toc`, `GET /toc/{id}`, `POST /toc/{id}/version`
* `POST /toc/{id}/nodes`, `PUT /toc/nodes/{node_id}`
* `POST /toc/{id}/edges`, `DELETE /toc/edges/{edge_id}`
* `POST /toc/nodes/{node_id}/link_evidence`

### Claims & Storyboards

* `POST /claims`, `GET /claims`, `GET/PUT /claims/{id}`
* `POST /claims/{id}/link_evidence`
* `POST /storyboards`, `GET/PUT /storyboards/{id}`
* `POST /storyboards/{id}/claims/reorder`

### Reports & exports

* `POST /reports`, `GET/PUT /reports/{id}`
* `POST /reports/{id}/generate_section` (AI-assisted)
* `POST /reports/{id}/export` (docx/pdf/outline)
* `GET /exports/{export_id}`

### Dashboards & analysis runs

* `POST /analysis_runs`, `GET /analysis_runs`
* `POST /dashboards`, `GET/PUT /dashboards/{id}`

### Search

* `GET /search` (q + filters + mode=metadata|fulltext|semantic|hybrid)

### Graph

* `GET /graph/query_templates`
* `POST /graph/query` (structured query JSON)
* `GET /graph/saved_queries`, `POST /graph/saved_queries`

### AI operations

* `POST /ai/claim_draft`
* `POST /ai/section_draft`
* `POST /ai/evidence_tag_suggest`
* `POST /ai/pii_scan`
* `GET /ai/jobs/{job_id}`

---

## 12) Data ingestion & processing pipeline

### 12.1 Ingestion steps

1. **Upload** → store raw file
2. **Text extraction** (PDF parsing, docx parsing, OCR only if needed)
3. **Chunking** (page-aware) → store chunks with offsets
4. **Embedding** per chunk (store in pgvector)
5. **AI metadata suggestion**
6. **Entity linking** (match city/person/cohort/topic)
7. **Graph update** (create/update nodes and relations)

### 12.2 Failure handling

* Evidence has `processing_status` and `error_detail`.
* Partial success allowed (e.g., text extracted but AI tagging failed).

### 12.3 Acceptance criteria

* Re-processing evidence keeps prior versions and logs diffs.
* Chunk offsets remain stable per version for citation integrity.

---

## 13) Reporting & export generation

### 13.1 DOCX export (must-have)

* Convert report sections (Markdown) into DOCX with:

  * headings, callout boxes, claim cards
  * embedded figures (images)
  * auto-generated citations appendix

### 13.2 PDF export (must-have)

* Render DOCX to PDF (server-side) or render via HTML→PDF pipeline.

### 13.3 Slides outline export (must-have)

* Outputs: slide titles + bullets + visuals list + citations notes.

### 13.4 Acceptance criteria

* Exports include:

  * report version
  * timestamp
  * evidence list + excerpt anchors
  * confidentiality watermark if not public

---

## 14) Security, privacy, compliance

### 14.1 Controls

* SSO + RBAC
* Confidentiality gating at query layer
* Field-level encryption for PII (contacts)
* Audit logs for:

  * evidence access (for restricted)
  * claim approvals
  * exports
  * AI generation

### 14.2 PII and sensitive content

* “PII scan” required before external export.
* Redaction workflow for excerpts:

  * highlight → redact → store redaction overlay; preserve original only for privileged roles.

---

## 15) Observability & QA

### 15.1 Logging

* Correlation IDs for all API requests.
* AI job logs include: evidence IDs, prompt template ID/version, output hash.

### 15.2 Tests (must-have)

* Unit tests: permissions, ingestion parsing, citation anchoring
* Integration tests: upload → search → claim → export
* Snapshot tests: report template rendering

### 15.3 Quality gates

* No external export if:

  * missing citations
  * restricted evidence included
  * PII scan fails
  * claim not approved

---

## 16) MVP build plan (phased but single coherent product)

### Phase 1 (Core spine)

* Auth/RBAC
* Evidence library + ingestion + search
* City/country/cohort/topic basics
* Excerpts + citation anchors

### Phase 2 (Impact OS)

* ToC builder + evidence mapping
* Dashboards + analysis runs
* City profiles + episodes timeline

### Phase 3 (Graph)

* Graph DB + sync worker
* Graph Explorer + saved queries

### Phase 4 (Story Studio)

* Claim cards + storyboard
* Report builder + exports
* AI drafting with strict citation schema

---

## 17) Seed data & templates (for faster dev/demo)

### 17.1 Seed taxonomy

* Topics: Collaboration, Data & Evidence, Innovation, Strategic Leadership & Management
* Subtopics (examples): cross-silo teams, performance management, experimentation, stakeholder engagement

### 17.2 Report templates (Markdown)

* “10-year impact assessment” skeleton:

  * Executive summary
  * Methodology (contribution logic + limitations)
  * Findings by topic
  * City vignettes
  * Appendix: indicators + evidence registry

### 17.3 Claim card component spec

* Header: claim title + confidence badge
* Body: claim statement
* Evidence strip: 3–6 evidence chips with excerpt hover
* Caveats panel (collapsed)
* Approval status + reviewer

---

## 18) Risks & mitigations

1. **Graph complexity**

   * Mitigation: start with minimal ontology + strict sync; expand labels gradually.
2. **Inconsistent evidence quality**

   * Mitigation: quality signals + confidence scoring + coverage meters; “unknown” states.
3. **AI hallucinations**

   * Mitigation: citation-required schema; block outputs without evidence IDs; human approval gates.
4. **Brand mismatch**

   * Mitigation: shared UI kit + tokens + card-first layouts; topic-led navigation everywhere.

---

## 19) Definition of done (one-shot delivery checklist)

**Platform**

* SSO + RBAC working
* Audit logs present
* Confidentiality enforced in all queries and exports

**Evidence**

* Upload, extract, chunk, search, excerpt anchors working
* AI metadata suggestions available and editable

**ToC**

* ToC editable, versioned, and evidence-mapped
* Coverage meters visible

**Graph**

* Graph sync reliable; Graph Explorer runs saved queries

**Story Studio**

* Claim cards enforce evidence + confidence rules
* Storyboards → Report → DOCX/PDF export with citations appendix

**Quality**

* End-to-end integration test passes: upload → claim → report → export
* Export gate blocks restricted/PII content
