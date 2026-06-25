# Detailed Study Notes Plan: Evaluation Theory, Models, and Applications

## Purpose

Expand the current generated major-section notes for Daniel L. Stufflebeam and Chris L. S. Coryn's *Evaluation Theory, Models, and Applications* into source-grounded detailed study notes for all 26 chapters.

The current site has three representative section notes under `notes/evaluation-theory-models-applications/`. This plan keeps those pages as seeds and adds a full chapter sequence that matches the existing Quarto study-notes pattern used elsewhere in the repository.

## Source Rules

- Use the MCP `evaluation-texts` research-library record for `evaluation-theory-models-applications` as the source of truth.
- Retrieve evidence with `rag_evidence_pack` before drafting each chapter note.
- Use `include_neighbors: true` for chapter evidence packs so summaries are grounded in surrounding context.
- Use `include_media: true` only where the chapter depends on a table, checklist, figure, matrix, or exhibit.
- Store compact evidence metadata only, not source text, under `data/research-library/evidence/evaluation-theory-models-applications/`.
- Keep all notes paraphrased. Do not reproduce long source passages or textbook tables.
- Retain `source_status: "needs_review"` in front matter until chapter notes have been manually checked against evidence.

## Deliverables

1. Add 26 chapter-level QMD files under `notes/evaluation-theory-models-applications/`.
2. Update `notes/evaluation-theory-models-applications/index.qmd` to show 26 chapter notes, the three current seed notes, and book-level synthesis pages.
3. Replace or expand `notes/evaluation-theory-models-applications/chapter-map.qmd` with a part-by-part reading route.
4. Refresh `concepts.qmd` and `practice-implications.qmd` after the chapter notes exist.
5. Add a chapter evidence summary file, such as `data/research-library/evidence/evaluation-theory-models-applications/chapter-evidence-summary.json`.
6. Update `data/research_library_notes_manifest.json` or the generation script metadata so chapter pages are tracked.
7. Run QA and render checks before treating the pages as publishable.

## Chapter Note Template

Each chapter page should use this structure:

```yaml
---
title: "Chapter NN: Chapter Title"
description: "Detailed study notes for Chapter NN of Evaluation Theory, Models, and Applications."
book_id: "evaluation-theory-models-applications"
collection_id: "evaluation-texts"
note_type: "Chapter"
chapter_number: NN
part: "Part Name"
citation_key: "stufflebeam_coryn_2014_evaluation_theory_models_applications"
evidence_ids:
  - "chunk:..."
source_status: "needs_review"
---
```

Recommended body sections:

- `## Source`
- `## Core Argument`
- `## Study Summary`
- `## Key Concepts`
- `## Chapter Structure`
- `## Practical Implications`
- `## Connections`
- `## Study Prompts`
- `## References`

Keep chapter notes compact enough for study: aim for 700-1,100 words per chapter, unless the chapter is dense with checklists or model comparisons. The goal is a usable study guide, not a substitute for the source.

## Chapter Build Matrix

| Part | Chapter | Target file | Evidence query focus | Study-note focus |
|---|---:|---|---|---|
| Part One: Fundamentals of Evaluation | 1. Overview of the Evaluation Field | `chapter-01-overview-of-the-evaluation-field.qmd` | `Chapter 1 Overview of the Evaluation Field formal informal evaluation merit worth probity history` | Definitions of evaluation, evaluands, value criteria, formal vs informal evaluation, formative/summative use, historical development. |
| Part One: Fundamentals of Evaluation | 2. Evaluation Theory | `chapter-02-evaluation-theory.qmd` | `Chapter 2 Evaluation Theory theory model approach standards theory development metaevaluation` | What counts as evaluation theory, how models differ from theory, criteria for theory development, role of standards and metaevaluation. |
| Part One: Fundamentals of Evaluation | 3. Standards for Program Evaluations | `chapter-03-standards-for-program-evaluations.qmd` | `Chapter 3 Standards for Program Evaluations Joint Committee AEA Guiding Principles Government Auditing Standards` | Utility, feasibility, propriety, accuracy, accountability, standards selection, standards as quality infrastructure. |
| Part Two: An Evaluation of Evaluation Approaches and Models | 4. Background for Assessing Evaluation Approaches | `chapter-04-background-for-assessing-evaluation-approaches.qmd` | `Chapter 4 Background for Assessing Evaluation Approaches classification twenty-three approaches descriptors` | Five approach categories, nine descriptors for analyzing approaches, reasons for judging approaches against standards. |
| Part Two: An Evaluation of Evaluation Approaches and Models | 5. Pseudoevaluations | `chapter-05-pseudoevaluations.qmd` | `Chapter 5 Pseudoevaluations politically controlled public relations evaluation empowerment customer feedback` | What makes a study a pseudoevaluation, risks of misuse, how evaluators should recognize and avoid corrupt or misleading work. |
| Part Two: An Evaluation of Evaluation Approaches and Models | 6. Quasi-evaluation Studies | `chapter-06-quasi-evaluation-studies.qmd` | `Chapter 6 Quasi-evaluation Studies objectives-based success case value-added experimental cost connoisseurship theory-based meta-analysis` | Narrow-scope approaches, their value and limits, why technical rigor does not automatically equal a full evaluation of merit and worth. |
| Part Two: An Evaluation of Evaluation Approaches and Models | 7. Improvement- and Accountability-oriented Evaluation Approaches | `chapter-07-improvement-and-accountability-oriented-evaluation-approaches.qmd` | `Chapter 7 Improvement and Accountability-oriented Evaluation Approaches decision accountability CIPP consumer-oriented accreditation certification` | Approaches that directly assess value, compare CIPP, consumer-oriented evaluation, and accreditation/certification. |
| Part Two: An Evaluation of Evaluation Approaches and Models | 8. Social Agenda and Advocacy Evaluation Approaches | `chapter-08-social-agenda-and-advocacy-evaluation-approaches.qmd` | `Chapter 8 Social Agenda and Advocacy Evaluation Approaches responsive constructivist deliberative democratic transformative` | Democratic participation, social justice, stakeholder engagement, relativist/objectivist tensions, risks to feasibility and bias control. |
| Part Two: An Evaluation of Evaluation Approaches and Models | 9. Eclectic Evaluation Approaches | `chapter-09-eclectic-evaluation-approaches.qmd` | `Chapter 9 Eclectic Evaluation Approaches utilization-focused participatory evaluation Patton Cousins` | Selective borrowing from evaluation approaches, utilization, participation, stakeholder roles, and limits of eclecticism. |
| Part Two: An Evaluation of Evaluation Approaches and Models | 10. Best Approaches for Twenty-first-century Evaluations | `chapter-10-best-approaches-for-twenty-first-century-evaluations.qmd` | `Chapter 10 Best Approaches for Twenty-first-century Evaluations ratings standards CIPP utilization-focused constructivist consumer report` | Comparative standards-based assessment of selected approaches; what the ratings imply for choosing an evaluation model. |
| Part Three: Explication of Selected Evaluation Approaches | 11. Experimental and Quasi-experimental Design Evaluations | `chapter-11-experimental-and-quasi-experimental-design-evaluations.qmd` | `Chapter 11 Experimental and Quasi-experimental Design Evaluations randomization causal inference validity designs` | Experimental logic, conditions for use, strengths, validity threats, and why experiments are useful but limited as evaluation approaches. |
| Part Three: Explication of Selected Evaluation Approaches | 12. Case Study Evaluations | `chapter-12-case-study-evaluations.qmd` | `Chapter 12 Case Study Evaluations Stake Yin naturalistic noninterventionist case study methods` | Case study as in-depth naturalistic inquiry, Stake and Yin variants, sampling, triangulation, and report use. |
| Part Three: Explication of Selected Evaluation Approaches | 13. Daniel Stufflebeam's CIPP Model for Evaluation | `chapter-13-daniel-stufflebeams-cipp-model-for-evaluation.qmd` | `Chapter 13 Daniel Stufflebeam CIPP Model context input process product improvement accountability` | CIPP roots, context/input/process/product categories, formative and summative use, systems orientation, values, standards, and metaevaluation. |
| Part Three: Explication of Selected Evaluation Approaches | 14. Michael Scriven's Consumer-oriented Approach to Evaluation | `chapter-14-michael-scrivens-consumer-oriented-approach-to-evaluation.qmd` | `Chapter 14 Michael Scriven Consumer-oriented Approach formative summative goal-free Key Evaluation Checklist` | Scriven's objectivist and consumer-oriented stance, goal-free evaluation, formative/summative roles, valuing, causal claims, and checklists. |
| Part Three: Explication of Selected Evaluation Approaches | 15. Robert Stake's Responsive or Stakeholder-centered Evaluation Approach | `chapter-15-robert-stakes-responsive-or-stakeholder-centered-evaluation-approach.qmd` | `Chapter 15 Robert Stake Responsive Stakeholder-centered Evaluation countenance antecedents transactions outcomes` | Stake's countenance and responsive evaluation, stakeholder perspectives, subjectivity, plural values, and responsive design. |
| Part Three: Explication of Selected Evaluation Approaches | 16. Michael Patton's Utilization-focused Evaluation | `chapter-16-michael-pattons-utilization-focused-evaluation.qmd` | `Chapter 16 Michael Patton Utilization-focused Evaluation intended users intended use premises planning` | Intended users, intended use, evaluator facilitation, values negotiation, use-focused design, strengths and limitations. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 17. Identifying and Assessing Evaluation Opportunities | `chapter-17-identifying-and-assessing-evaluation-opportunities.qmd` | `Chapter 17 Identifying and Assessing Evaluation Opportunities RFP RFQ internal assignment sole source evaluator-initiated` | Finding, screening, and judging opportunities; when to pursue, decline, or repair a problematic assignment. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 18. First Steps in Addressing Evaluation Opportunities | `chapter-18-first-steps-in-addressing-evaluation-opportunities.qmd` | `Chapter 18 First Steps in Addressing Evaluation Opportunities evaluation team institutional support human subjects stakeholder review panel` | Start-up work: team roles, collaborators, IRB/human subjects, institutional support, proposal appendices, stakeholder panels. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 19. Designing Evaluations | `chapter-19-designing-evaluations.qmd` | `Chapter 19 Designing Evaluations design CIPP checklist questions values information reporting administration` | Evaluation design as an integrated decision set; focusing, information planning, analysis, reporting, use, and administration. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 20. Budgeting Evaluations | `chapter-20-budgeting-evaluations.qmd` | `Chapter 20 Budgeting Evaluations ethical budgeting line item modular budget cost factors` | Design-budget fit, ethical budgeting, line-item/task/year budgets, responsive vs fixed budgeting, cost realism. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 21. Contracting Evaluations | `chapter-21-contracting-evaluations.qmd` | `Chapter 21 Contracting Evaluations contract memorandum agreement negotiation client evaluator responsibilities` | Contracts and memoranda of agreement, advance agreements, responsibilities, reporting rights, safeguards, and enforceability. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 22. Collecting Evaluative Information | `chapter-22-collecting-evaluative-information.qmd` | `Chapter 22 Collecting Evaluative Information standards reliability validity sampling information collection techniques` | Information quality, standards for data collection, sampling, reliability, validity, information management, and mixed collection methods. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 23. Analyzing and Synthesizing Information | `chapter-23-analyzing-and-synthesizing-information.qmd` | `Chapter 23 Analyzing and Synthesizing Information quantitative qualitative synthesis justified conclusions effect sizes` | Quantitative and qualitative analysis, synthesis across evidence, practical significance, fact-value and value-value synthesis, justified conclusions. |
| Part Four: Evaluation Tasks, Procedures, and Tools | 24. Communicating Evaluation Findings | `chapter-24-communicating-evaluation-findings.qmd` | `Chapter 24 Communicating Evaluation Findings interim feedback final report dissemination follow-up use` | Intended users, communication planning, interim feedback, final reports, follow-up support, and conditions for use. |
| Part Five: Metaevaluation and Institutionalizing and Mainstreaming Evaluation | 25. Metaevaluation: Evaluating Evaluations | `chapter-25-metaevaluation-evaluating-evaluations.qmd` | `Chapter 25 Metaevaluation Evaluating Evaluations standards tasks checklists comparative metaevaluation` | Rationale and definition of metaevaluation, standards-based judging, formative/summative metaevaluation, tasks, cases, and qualifications. |
| Part Five: Metaevaluation and Institutionalizing and Mainstreaming Evaluation | 26. Institutionalizing and Mainstreaming Evaluation | `chapter-26-institutionalizing-and-mainstreaming-evaluation.qmd` | `Chapter 26 Institutionalizing and Mainstreaming Evaluation organizational evaluation system checklist principles` | Organizational evaluation systems, institutionalization vs mainstreaming, design/review teams, standards, communication, periodic review. |

## Evidence Collection Plan

For each chapter:

1. Run a chapter-specific `rag_evidence_pack` query using the query focus from the build matrix.
2. Request `include_neighbors: true`.
3. Set `limit` to 8-12, then inspect whether the result covers the chapter opening, core sections, summary/review material, and relevant exhibits.
4. If the chapter contains a central checklist/table/figure, rerun or supplement with `include_media: true`.
5. Save a compact entry in `chapter-evidence-summary.json` with:
   - chapter number
   - chapter title
   - target QMD file
   - section paths used
   - source page span where available
   - evidence IDs
   - any media IDs used
   - note status: `planned`, `drafted`, `checked`

The chapter-opening records should be preferred as anchors where available. Examples already verified in the MCP index include:

- `chunk:evaluation-theory-models-applications:ch01-chapter-1-overview-of-the-evaluation-field:c0001`
- `chunk:evaluation-theory-models-applications:ch02-chapter-2-evaluation-theory:c0001`
- `chunk:evaluation-theory-models-applications:ch03-chapter-3-standards-for-program-evaluations:c0001`
- `chunk:evaluation-theory-models-applications:ch13-chapter-13-daniel-stufflebeam-s-cipp-model-for-evaluation-an-improvement-and-acc:c0001`
- `chunk:evaluation-theory-models-applications:ch19-chapter-19-designing-evaluations:c0001`
- `chunk:evaluation-theory-models-applications:ch25-chapter-25-metaevaluation-evaluating-evaluations:c0001`
- `chunk:evaluation-theory-models-applications:ch26-chapter-26-institutionalizing-and-mainstreaming-evaluation:c0001`

## Existing Pages to Reuse

Keep these current pages available, but demote them from the main reading route once chapter pages exist:

- `section-01-evaluation-theory-development.qmd`: fold its content into Chapter 2.
- `section-02-cipp-overview.qmd`: fold its content into Chapter 13.
- `section-03-standards-and-metaevaluation.qmd`: split relevant content between Chapter 13 and Chapter 25 as appropriate.

The three pages can remain as short topical extracts or redirects in the chapter map. Do not delete them unless a later cleanup explicitly decides to remove generated major-section notes.

## Navigation Plan

Update `chapter-map.qmd` into five part sections:

1. Fundamentals of Evaluation: Chapters 1-3.
2. Evaluation of Evaluation Approaches and Models: Chapters 4-10.
3. Explication of Selected Evaluation Approaches: Chapters 11-16.
4. Evaluation Tasks, Procedures, and Tools: Chapters 17-24.
5. Metaevaluation and Institutionalizing/Mainstreaming Evaluation: Chapters 25-26.

Update the book index to show:

- a compact book overview
- links to concepts, chapter map, and practice implications
- a part-by-part chapter list
- a short note explaining that source records are `needs_review`

Do not add all 26 chapter files to the global `_quarto.yml` sidebar unless the site design is changed to support nested book navigation. The book index and chapter map should carry the detailed chapter route.

## Writing Standards

Each chapter note should:

- State the chapter's central claim in one or two sentences.
- Explain the chapter structure without mirroring the source table of contents in detail.
- Capture definitions and distinctions in the writer's own words.
- Include practical implications framed as evaluator habits or design checks.
- Link to related local notes, especially CIPP, standards, metaevaluation, program theory, utilization-focused evaluation, and qualitative/quantitative methods.
- Include study prompts that ask readers to apply or critique the chapter, not just recall terms.

Avoid:

- copying review questions wholesale
- reproducing checklists or tables
- making unsupported cross-chapter claims without evidence
- treating the authors' ratings of approaches as neutral facts without noting they are the authors' judgments

## Implementation Sequence

1. Create `chapter-evidence-summary.json` with 26 planned entries.
2. Draft Chapters 1-3 and update the chapter map for Part One.
3. Draft Chapters 4-10 and check approach taxonomy consistency.
4. Draft Chapters 11-16 and cross-link model-specific chapters to the earlier approach-classification chapters.
5. Draft Chapters 17-24 and cross-link procedural chapters to design, evidence, analysis, reporting, and use concepts.
6. Draft Chapters 25-26 and refresh book-level concepts and practice implications.
7. Update the book index and chapter map.
8. Run QA and render.

## QA Plan

Run these checks after drafting:

```bash
python3 scripts/qa_research_library_notes.py
python3 scripts/extract_link_graph.py --include-prefix notes/
quarto render --quiet
```

Manual checks:

- Every chapter page has at least one evidence ID and the book citation key.
- Every chapter page uses the standard body sections.
- No page contains `TODO`, ungrounded claims, or copied textbook tables.
- Chapter map links resolve.
- Existing section pages still render and have a clear relationship to the new chapter route.
- Spot-check at least one chapter from each part against its saved evidence summary.

## Completion Criteria

The expansion is complete when all 26 chapter files exist, the book index and chapter map expose the full reading route, evidence summaries trace each chapter to MCP records, QA passes, and the Quarto site renders without broken links.
