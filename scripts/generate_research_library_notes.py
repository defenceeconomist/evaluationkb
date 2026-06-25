#!/usr/bin/env python3
"""Generate MCP research-library note pages for the Quarto site.

This script writes deterministic site artifacts from a curated MCP evidence
manifest. It does not call MCP itself; update the records below after
refreshing evidence with the research-library tools.
"""

from __future__ import annotations

import json
import inspect
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GENERATED_AT = "2026-06-25"


PLAN = """# MCP Evaluation Text Study Notes

## Summary

- Add study notes for the missing ready books in the MCP `evaluation-texts` collection, keeping the existing Purposeful Program Theory pages as the template and baseline.
- Generate book-level overview, concepts, chapter map, practice implications, and chapter/major-section notes for each added book.
- Use `mcp__researchlibrary` evidence packs as the source of truth; do not depend on local PDFs or the unavailable lower-level MCP chunk fetch endpoint.

## Key Changes

- Add a checked-in manifest at `data/research_library_notes_manifest.json` with `book_id`, slug, title, authors, year, citation key, source status, target paths, and selected section/page ranges.
- Add `notes/<book-slug>/` folders for the missing books, each following the current note structure: Source, Core Argument, Study Summary, Key Concepts, Structure, Practical Implications, Connections, Study Prompts, References.
- Update `references.bib` with citation keys for all added books.
- Refactor `_quarto.yml` sidebar for multi-book navigation: global sidebar lists book-level pages; each book index/chapter map carries detailed chapter links.
- Update `notes/index.qmd`, `index.qmd`, `assets/js/notes_filter.js`, and CSS as needed so note cards can filter by book and note type.

## Extraction Workflow

- Start with `library_list_collections`; select ready books in `evaluation-texts`, excluding `purposeful-program-theory` unless refreshing is explicitly requested.
- Discover candidate chapters/major sections per book using broad `rag_search` queries, then build the manifest from unique `section_id`, `section_path`, and page ranges.
- For each manifest section, call `rag_evidence_pack` with `include_neighbors: true`; use `include_media: true` only when figures/tables are needed for understanding.
- Hydrate important or ambiguous records with `rag_get_record`; scan examples/cases/exhibits with `library_scan_labels`.
- Save compact evidence summaries under `data/research-library/evidence/<book-slug>/` for auditability.
- Write only paraphrased notes, with page ranges and evidence IDs in front matter; avoid long verbatim source passages.

## Interfaces

- QMD front matter adds: `book_id`, `collection_id`, `note_type`, `source_pages`, `citation`, `evidence_ids`, and `source_status`.
- Note cards add `data-book` and keep `data-type`; existing `data-section` can remain for legacy/current pages.
- The link graph pre-render remains `scripts/extract_link_graph.py --include-prefix notes/`; generated pages must use normal relative `.qmd` links.

## Test Plan

- Run manifest QA: no duplicate slugs/paths, all citation keys exist in `references.bib`, all evidence IDs point to saved summaries.
- Run notes QA: every generated page has required sections, source metadata, at least one citation, and no TODO markers.
- Run link graph generation and check internal links resolve.
- Run `quarto render --quiet`.
- Spot-check at least one chapter/major-section note per book against its saved evidence summary for claim support and paraphrase quality.

## Assumptions

- Defaults chosen because no clarification answer was received: add missing books first; generate chapter plus book-synthesis pages; do not create cross-book thematic synthesis pages in v1.
- MCP book records are `rag_status: ready` but `status: needs_review`, so generated pages should remain labelled as source-grounded study notes rather than definitive editions.
- Figures/tables are used as supporting evidence for synthesis, not republished as site assets unless separately approved.
"""


BOOKS: list[dict[str, Any]] = [
    {
        "book_id": "purposeful-program-theory",
        "slug": "purposeful-programme-theory",
        "title": "Purposeful Program Theory",
        "full_title": "Purposeful Program Theory: Effective Use of Theories of Change and Logic Models",
        "authors": ["Sue C. Funnell", "Patricia J. Rogers"],
        "year": "2011",
        "citation": "funnell_rogers_2011_purposeful_program_theory",
        "publisher": "Jossey-Bass",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "existing-hand-authored",
        "card": "Theories of change, theories of action, logic models, assumptions, and causal inference for program theory use.",
        "core": "Program theory makes evaluation more diagnostic by making causal assumptions, implementation conditions, and evidence needs explicit.",
        "concepts": [
            "Program theory",
            "Theory of change",
            "Theory of action",
            "Logic model",
            "Assumptions and context",
            "Causal inference",
        ],
        "practice": [
            "Start evaluation design by asking what must be true for the intervention to work.",
            "Collect evidence along the causal chain, not only at final outcomes.",
            "Use theory to distinguish implementation failure, theory failure, and partial success.",
        ],
        "sections": [],
    },
    {
        "book_id": "practical-program-evaluation",
        "slug": "practical-program-evaluation",
        "title": "Practical Program Evaluation",
        "full_title": "Practical Program Evaluation",
        "authors": ["Huey T. Chen"],
        "year": "2015",
        "citation": "chen_2015_practical_program_evaluation",
        "publisher": "SAGE Publications",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "A practice-oriented guide to matching evaluation types, program stages, logic models, and program theory.",
        "core": "Evaluation design should match a program's stage, stakeholder needs, and theory of how action is expected to produce change.",
        "concepts": [
            "Evaluation design",
            "Program stage",
            "Logic model",
            "Action model/change model schema",
            "Stakeholder use",
            "Constructive and conclusive evaluation",
        ],
        "practice": [
            "Begin by clarifying the program stage and intended evaluation purpose.",
            "Use logic models for tractable program description and program theory when mechanisms and context matter.",
            "Treat stakeholder assumptions as evaluation design evidence, not background noise.",
            "Check whether a familiar logic-model format is hiding system-change or contextual complexity.",
        ],
        "sections": [
            {
                "id": "evaluation-design-components",
                "title": "Evaluation Design and Its Components",
                "source_pages": "39-40",
                "section_path": "Chapter 1: Fundamentals of Program Evaluation > Evaluation Design and Its Components",
                "evidence_ids": ["chunk:practical-program-evaluation:ch01-evaluation-design-and-its-components:c0002"],
                "summary": [
                    "The section treats evaluation design as an explicit agreement about purpose, methodology, program description, and the information needs the evaluation must serve.",
                    "A useful design does more than select methods. It asks whether the program is described coherently enough to support evaluation and whether stakeholders need a logic model, a fuller program theory, or both.",
                    "The practical lesson is proportionality: choose enough structure to make the evaluation credible and useful without forcing every program into the same template.",
                ],
                "concepts": ["Evaluation purpose", "Program description", "Method fit", "Stakeholder agreement"],
                "implications": [
                    "Do not move to methods before the program description is adequate.",
                    "Use design conversations to surface what stakeholders expect the evaluation to decide.",
                    "Escalate from a logic model to program theory when context or causal mechanisms need to be examined.",
                ],
            },
            {
                "id": "logic-models-and-program-theory",
                "title": "Logic Models and the Action Model/Change Model Schema",
                "source_pages": "79",
                "section_path": "Part I: Introduction > Chapter 3: Logic Models and the Action Model/change Model Schema (program Theory)",
                "evidence_ids": ["chunk:practical-program-evaluation:ch03-logic-models-and-the-action-model-change-model-schema-program-theory:c0001"],
                "summary": [
                    "The chapter positions logic models and the action model/change model schema as complementary tools for describing interventions.",
                    "Logic models help simplify a complicated program into components, while the schema gives evaluators a fuller way to address contextual factors and causal mechanisms.",
                    "The distinction matters because many evaluations fail when the representation is too simple for the program's actual operating logic.",
                ],
                "concepts": ["Logic model", "Action model", "Change model", "Contextual factors", "Causal mechanisms"],
                "implications": [
                    "Use logic models for communication and initial structure.",
                    "Use the action model/change model schema when implementation arrangements and causal assumptions require more detail.",
                    "Choose the representation that supports evaluation decisions rather than the one stakeholders already know best.",
                ],
            },
            {
                "id": "logic-model-limits",
                "title": "When Logic Models Do Not Work as Expected",
                "source_pages": "382",
                "section_path": "Chapter 13: What to Do If Your Logic Model Does Not Work as Well as Expected > A Guide to Productively Applying the Logic Model and the Action Model/change Model Schema",
                "evidence_ids": ["chunk:practical-program-evaluation:ch13-a-guide-to-productively-applying-the-logic-model-and-the-action-model-change-mod:c0001"],
                "summary": [
                    "The section warns that logic models can become misleading when programs combine intervention delivery with wider system change.",
                    "The problem is not that logic models are useless, but that they need to be applied with judgment about what the program is trying to change and how stable the causal path is.",
                    "When the model cannot represent system dynamics or multiple layers of action, evaluators should supplement it with richer program theory.",
                ],
                "concepts": ["System change", "Model fit", "Program complexity", "Representation limits"],
                "implications": [
                    "Check whether the model represents both the intervention and the system it seeks to change.",
                    "Look for confusion caused by compressing multiple causal routes into one linear chain.",
                    "Revise the representation before it drives data collection.",
                ],
            },
        ],
    },
    {
        "book_id": "qualitative-research-evaluation-methods",
        "slug": "qualitative-research-evaluation-methods",
        "title": "Qualitative Research & Evaluation Methods",
        "full_title": "Qualitative Research & Evaluation Methods",
        "authors": ["Michael Quinn Patton"],
        "year": "2015",
        "citation": "patton_2015_qualitative_research_evaluation_methods",
        "publisher": "SAGE Publications",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "Qualitative inquiry for evaluation questions where context, meaning, process, and use matter.",
        "core": "Qualitative inquiry is strongest when it is systematic, open to field realities, and connected to practical questions users need answered.",
        "concepts": [
            "Qualitative inquiry",
            "Strategic qualitative principles",
            "Utilization-focused inquiry",
            "Case study",
            "Implementation and process evidence",
            "Theory of change clarification",
        ],
        "practice": [
            "Match qualitative methods to questions about meaning, implementation, variation, and unanticipated effects.",
            "Use observation and interviewing as disciplined ways to learn from context, not as informal anecdotes.",
            "Document qualitative evidence systematically enough that interpretation can be challenged and refined.",
            "Connect qualitative findings to decisions, not only to rich description.",
        ],
        "sections": [
            {
                "id": "strategic-qualitative-principles",
                "title": "Strategic Qualitative Principles in Practice",
                "source_pages": "140-141",
                "section_path": "Part 1 > Chapter 2: Strategic Themes in Qualitative Inquiry > Module 8",
                "evidence_ids": ["chunk:qualitative-research-evaluation-methods:mod08-module-8-integrating-the-12-strategic-qualitative-principles-in-practice-chapter:c0010"],
                "summary": [
                    "The section frames qualitative inquiry as a set of strategic principles that must be adapted to practical field conditions.",
                    "It rejects the idea that qualitative methods only belong in ideal situations; their value often appears when evaluation questions require context-sensitive judgment.",
                    "The evaluator's task is to maintain qualitative discipline while adjusting to real constraints in access, time, and use.",
                ],
                "concepts": ["Strategic principles", "Field adaptation", "Qualitative rigor", "Practical constraints"],
                "implications": [
                    "Define what qualitative evidence is expected to clarify before collecting data.",
                    "Plan for adaptation while protecting documentation and analytic transparency.",
                    "Use qualitative design choices to make trade-offs explicit.",
                ],
            },
            {
                "id": "practical-actionable-qualitative-inquiry",
                "title": "Practical and Actionable Qualitative Inquiry",
                "source_pages": "269-270",
                "section_path": "Part 1 > Chapter 4: Practical and Actionable Qualitative Applications > Module 20",
                "evidence_ids": ["chunk:qualitative-research-evaluation-methods:mod20-module-20-practical-purposes-concrete-questions-and-actionable-answers-illuminat:c0005"],
                "summary": [
                    "This section links qualitative inquiry to practical purposes: better questions, clearer interpretations, and answers that can guide action.",
                    "It emphasizes pragmatic and utilization-focused framing, where the point of inquiry is not only understanding but improvement.",
                    "Qualitative methods are presented as especially useful for questions that need explanation, depth, and sensitivity to local circumstances.",
                ],
                "concepts": ["Actionable answers", "Pragmatic inquiry", "Utilization focus", "Problem-focused evaluation"],
                "implications": [
                    "Phrase qualitative questions so that answers can inform a decision.",
                    "Use fieldwork to understand why performance differs across people, sites, or conditions.",
                    "Report patterns with enough context to support use.",
                ],
            },
            {
                "id": "program-models-and-theories-of-change",
                "title": "Program Models, Theories of Change, and Qualitative Methods",
                "source_pages": "314-316",
                "section_path": "Part 1 > Chapter 4 > Module 23: Evaluating Program Models and Theories of Change",
                "evidence_ids": ["chunk:qualitative-research-evaluation-methods:mod23-module-23-evaluating-program-models-and-theories-of-change-and-evaluation-models:c0024"],
                "summary": [
                    "The section shows how qualitative inquiry can test and refine program models by connecting processes, implementation, and outcomes.",
                    "Qualitative evidence is useful where the formal theory of change is incomplete, contested, or too abstract to explain practice.",
                    "This makes qualitative methods a complement to logic models: they can reveal how the model is experienced and enacted.",
                ],
                "concepts": ["Program model", "Theory of change", "Process study", "Implementation evidence"],
                "implications": [
                    "Use interviews and observations to test whether the stated program model matches implementation.",
                    "Look for mechanisms and unanticipated outcomes that the initial theory missed.",
                    "Treat qualitative findings as evidence for revising the theory of change.",
                ],
            },
        ],
    },
    {
        "book_id": "realistic-evaluation",
        "slug": "realistic-evaluation",
        "title": "Realistic Evaluation",
        "full_title": "Realistic Evaluation",
        "authors": ["Ray Pawson", "Nick Tilley"],
        "year": "1997",
        "citation": "pawson_tilley_1997_realistic_evaluation",
        "publisher": "SAGE Publications",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "A realist approach to explaining what works, for whom, in what circumstances, and why.",
        "core": "Realist evaluation studies programs through context-mechanism-outcome configurations rather than asking only whether a whole program worked.",
        "concepts": [
            "Context-mechanism-outcome configuration",
            "Realist research design",
            "Theory testing",
            "Outcome patterns",
            "Subgroup variation",
            "Teacher-learner cycle",
        ],
        "practice": [
            "Specify conjectured CMO configurations before selecting data collection methods.",
            "Analyze variation across contexts and participants instead of averaging it away too quickly.",
            "Use evaluation findings to refine program theory for future adaptation.",
            "Report findings as conditional explanations, not universal effects.",
        ],
        "sections": [
            {
                "id": "reader-guide-cmo",
                "title": "Reader's Guide to Context, Mechanism, and Outcome",
                "source_pages": "14-15",
                "section_path": "Introduction",
                "evidence_ids": ["chunk:realistic-evaluation:introduction:c0011"],
                "summary": [
                    "The introduction identifies context, mechanism, and outcome as the conceptual backbone of realist evaluation.",
                    "These terms reorient evaluation from a single effect estimate toward explanation of how program resources interact with circumstances.",
                    "The reader is invited to treat evaluation design as a theory-building exercise from the start.",
                ],
                "concepts": ["Context", "Mechanism", "Outcome", "Realist explanation"],
                "implications": [
                    "State the initial CMO proposition before fieldwork.",
                    "Collect data about circumstances and mechanisms, not only outcomes.",
                    "Expect the evaluation design to evolve as the theory becomes sharper.",
                ],
            },
            {
                "id": "scientific-realism-and-cmo",
                "title": "Scientific Realism and CMO Hypotheses",
                "source_pages": "94-95",
                "section_path": "Chapter 3: In with the New: Introducing Scientific Realism",
                "evidence_ids": ["chunk:realistic-evaluation:ch03-chapter-3-in-with-the-new-introducing-scientific-realism:c0051"],
                "summary": [
                    "This section turns realist philosophy into an evaluation task: identify, articulate, test, and refine CMO configurations.",
                    "The emphasis is on hypotheses about how mechanisms operate under social and cultural conditions.",
                    "Realist evidence therefore depends on comparing where the same mechanism appears to work differently.",
                ],
                "concepts": ["Scientific realism", "Hypothesis testing", "Mechanism question", "Context question"],
                "implications": [
                    "Translate broad program theory into testable CMO hypotheses.",
                    "Design comparisons that can expose how context changes mechanism activation.",
                    "Use contrary cases as theory-refining evidence.",
                ],
            },
            {
                "id": "new-rules-cmo-configurations",
                "title": "The New Rules and CMO Configurations",
                "source_pages": "234",
                "section_path": "Chapter 9: The New Rules of Realistic Evaluation",
                "evidence_ids": ["chunk:realistic-evaluation:ch09-chapter-9-the-new-rules-of-realistic-evaluation:c0008"],
                "summary": [
                    "The new-rules section describes CMO configurations as propositions about what works for whom in what circumstances.",
                    "A conjectured configuration is the starting point; a refined configuration is the evaluation finding.",
                    "The cumulative ambition is not exact replication of effects but better focusing of mechanisms across settings.",
                ],
                "concepts": ["CMO proposition", "Theory refinement", "Cumulative learning", "Local adaptation"],
                "implications": [
                    "Write findings as refined explanations rather than as simple success/failure claims.",
                    "Compare evaluations by the mechanisms and contexts they illuminate.",
                    "Use findings to adapt programs to local circumstances.",
                ],
            },
        ],
    },
    {
        "book_id": "impact-evaluation-in-practice",
        "slug": "impact-evaluation-in-practice",
        "title": "Impact Evaluation in Practice",
        "full_title": "Impact Evaluation in Practice",
        "authors": ["Paul J. Gertler", "Sebastian Martinez", "Patrick Premand", "Laura B. Rawlings", "Christel M. J. Vermeersch"],
        "year": "2016",
        "citation": "gertler_martinez_premand_rawlings_vermeersch_2016_impact_evaluation_in_practice",
        "publisher": "World Bank",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "Impact evaluation design around theory of change, counterfactuals, questions, methods, data, and implementation timing.",
        "core": "Impact evaluation estimates causal effects by turning policy questions into testable designs with credible counterfactuals.",
        "concepts": [
            "Impact evaluation",
            "Monitoring versus evaluation",
            "Theory of change",
            "Evaluation question",
            "Counterfactual",
            "Power and sampling",
        ],
        "practice": [
            "Clarify whether the question is descriptive, implementation-focused, or causal.",
            "Build the evaluation around a theory of change before selecting an identification strategy.",
            "Assess whether program rules, timing, and eligibility create feasible comparison options.",
            "Plan data and sample size early enough to protect credibility.",
        ],
        "sections": [
            {
                "id": "what-is-impact-evaluation",
                "title": "What Is Impact Evaluation?",
                "source_pages": "37",
                "section_path": "Part 1: Introduction to Impact Evaluation > Chapter 1: Why Evaluate? > What Is Impact Evaluation?",
                "evidence_ids": ["chunk:impact-evaluation-in-practice:what-is-impact-evaluation:c0001"],
                "summary": [
                    "The section distinguishes monitoring, evaluation, and impact evaluation as related but different evidence functions.",
                    "Monitoring tracks program activity and performance over time; evaluation answers selected questions about design, implementation, and results.",
                    "Impact evaluation focuses on the causal effect of a program or design innovation on outcomes of interest.",
                ],
                "concepts": ["Monitoring", "Evaluation", "Impact evaluation", "Causal effect"],
                "implications": [
                    "Do not ask an impact design to answer every monitoring or implementation question.",
                    "Use monitoring data as context and operational evidence for the impact study.",
                    "State clearly which outcomes the causal claim will cover.",
                ],
            },
            {
                "id": "constructing-theory-of-change",
                "title": "Constructing a Theory of Change",
                "source_pages": "62",
                "section_path": "Part 1: Introduction to Impact Evaluation > Chapter 2: Preparing for an Evaluation > Constructing a Theory of Change",
                "evidence_ids": ["chunk:impact-evaluation-in-practice:constructing-a-theory-of-change:c0001"],
                "summary": [
                    "The section treats theory of change as an early design step for causal evaluation.",
                    "A theory of change maps the causal logic linking program inputs, activities, outputs, behavior change, and outcomes.",
                    "Working through this logic with stakeholders can clarify both the evaluation question and the program design itself.",
                ],
                "concepts": ["Theory of change", "Causal pathway", "Assumptions", "Stakeholder clarification"],
                "implications": [
                    "Use the theory of change to choose outcomes and intermediate indicators.",
                    "Surface assumptions that could invalidate the impact claim.",
                    "Revise the evaluation question if the causal pathway is unclear.",
                ],
            },
            {
                "id": "causal-inference-counterfactuals",
                "title": "Causal Inference and Counterfactuals",
                "source_pages": "77-78",
                "section_path": "Part 2: How to Evaluate > Chapter 3: Causal Inference and Counterfactuals > Causal Inference",
                "evidence_ids": ["chunk:impact-evaluation-in-practice:causal-inference:c0001"],
                "summary": [
                    "The section explains why before-and-after observation alone is not sufficient for causal inference.",
                    "Impact evaluation requires an estimate of what would have happened to participants without the program.",
                    "The central design problem is therefore to construct a credible counterfactual.",
                ],
                "concepts": ["Causal inference", "Counterfactual", "Attribution", "Outcome comparison"],
                "implications": [
                    "Identify the counterfactual strategy before collecting outcome data.",
                    "Avoid interpreting observed change as impact without a comparison logic.",
                    "Explain the assumptions that make the comparison credible.",
                ],
            },
        ],
    },
    {
        "book_id": "handbook-practical-program-evaluation",
        "slug": "handbook-practical-program-evaluation",
        "title": "Handbook of Practical Program Evaluation",
        "full_title": "Handbook of Practical Program Evaluation",
        "authors": ["Kathryn E. Newcomer", "Harry P. Hatry", "Joseph S. Wholey"],
        "year": "2015",
        "citation": "newcomer_hatry_wholey_2015_handbook_practical_program_evaluation",
        "publisher": "Jossey-Bass",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "A broad handbook on evaluation planning, stakeholder engagement, monitoring, study designs, and use.",
        "core": "Practical evaluation should be credible enough for decisions and useful enough to improve public and nonprofit programs.",
        "concepts": [
            "Evaluation planning",
            "Stakeholder engagement",
            "Logic modeling",
            "Evaluability assessment",
            "Performance measurement",
            "Evaluation use",
        ],
        "practice": [
            "Balance rigor, cost, timing, and likely usefulness.",
            "Fit the evaluation design to the program's life cycle and decision context.",
            "Treat performance measurement and evaluation as complementary evidence systems.",
            "Use stakeholder engagement to sharpen, not dilute, evaluation focus.",
        ],
        "sections": [
            {
                "id": "planning-and-design",
                "title": "Evaluation Planning and Design",
                "source_pages": "43-45",
                "section_path": "Part 1: Evaluation Planning and Design",
                "evidence_ids": ["chunk:handbook-practical-program-evaluation:part-1:c0001", "chunk:handbook-practical-program-evaluation:part-1:c0004"],
                "summary": [
                    "The part overview frames planning and design as the work of producing credible, useful evaluation evidence under real constraints.",
                    "It covers stakeholder engagement, logic modeling, evaluability assessment, monitoring, impact designs, case studies, multisite work, and culturally responsive evaluation.",
                    "The recurring design tension is between the precision and generalizability desired and the time and resources available.",
                ],
                "concepts": ["Design trade-offs", "Stakeholder engagement", "Evaluation approach", "Usefulness"],
                "implications": [
                    "Plan evaluation around information needs, not only available methods.",
                    "Make cost, rigor, and timing trade-offs explicit.",
                    "Choose design options that stakeholders can act on.",
                ],
            },
            {
                "id": "planning-useful-evaluations",
                "title": "Planning and Designing Useful Evaluations",
                "source_pages": "49-51",
                "section_path": "Part 1: Evaluation Planning and Design > Chapter 1: Planning and Designing Useful Evaluations",
                "evidence_ids": ["chunk:handbook-practical-program-evaluation:ch01-chapter-1-planning-and-designing-useful-evaluations:c0003"],
                "summary": [
                    "The chapter emphasizes that evaluation should improve programs as well as support accountability.",
                    "A study that produces defensible findings but no improvement leverage may not be worth its cost.",
                    "The evaluator's practical task is to help managers and funders get credible information for decisions they actually face.",
                ],
                "concepts": ["Usefulness", "Accountability", "Program improvement", "Decision support"],
                "implications": [
                    "Ask what decision the evaluation will inform before choosing the design.",
                    "Include improvement questions alongside accountability questions where appropriate.",
                    "Report findings in ways managers can use.",
                ],
            },
            {
                "id": "performance-measurement",
                "title": "Performance Measurement and Program Evaluation",
                "source_pages": "150-151",
                "section_path": "Part 1: Evaluation Planning and Design > Chapter 5: Performance Measurement",
                "evidence_ids": ["chunk:handbook-practical-program-evaluation:ch05-chapter-5-performance-measurement:c0001"],
                "summary": [
                    "The chapter treats performance measurement as both an evaluation tool and a management system.",
                    "Ongoing measures can strengthen decision making, but they need evaluation thinking to avoid becoming mechanical reporting.",
                    "The main issue is how to design and implement systems that focus on results and provide useful feedback.",
                ],
                "concepts": ["Performance measurement", "Monitoring system", "Outcome focus", "Feedback"],
                "implications": [
                    "Design performance measures around decisions and learning needs.",
                    "Use evaluation methods to improve measure validity and interpretation.",
                    "Connect monitoring trends to deeper evaluative questions when needed.",
                ],
            },
        ],
    },
    {
        "book_id": "evaluation-systematic-approach",
        "slug": "evaluation-systematic-approach",
        "title": "Evaluation: A Systematic Approach",
        "full_title": "Evaluation: A Systematic Approach",
        "authors": ["Peter H. Rossi", "Mark W. Lipsey", "Howard E. Freeman"],
        "year": "2004",
        "citation": "rossi_lipsey_freeman_2004_evaluation_systematic_approach",
        "publisher": "SAGE Publications",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "A systematic evaluation framework covering questions, needs, theory, process, impact, efficiency, and use.",
        "core": "Evaluation design should be tailored to the question type, program circumstances, stakeholder relationship, and feasible evidence.",
        "concepts": [
            "Evaluation question",
            "Needs assessment",
            "Program theory assessment",
            "Process evaluation",
            "Impact assessment",
            "Efficiency assessment",
        ],
        "practice": [
            "Classify evaluation questions before selecting methods.",
            "Assess program theory and process before attempting impact claims.",
            "Use stakeholder relationships deliberately: independent, collaborative, or capacity-building.",
            "Prioritize questions that can influence understanding or decisions.",
        ],
        "sections": [
            {
                "id": "tailoring-evaluations",
                "title": "Tailoring Evaluations",
                "source_pages": "38-39",
                "section_path": "Chapter 2: Tailoring Evaluations",
                "evidence_ids": ["chunk:evaluation-systematic-approach:ch02-chapter-2-tailoring-evaluations:c0002"],
                "summary": [
                    "The chapter presents evaluation design as a fit problem rather than a fixed sequence.",
                    "A good plan responds to purposes, stakeholder expectations, program organization, available resources, and question type.",
                    "The major question types include needs, theory, process, impact, and efficiency assessment.",
                ],
                "concepts": ["Tailoring", "Evaluation purpose", "Question type", "Resource constraints"],
                "implications": [
                    "Name the evaluation question type before choosing a method.",
                    "Check whether the program is organized enough for the proposed question.",
                    "Make the evaluator-stakeholder relationship explicit.",
                ],
            },
            {
                "id": "formulating-questions",
                "title": "Identifying Issues and Formulating Questions",
                "source_pages": "89-90",
                "section_path": "Chapter 3: Identifying Issues and Formulating Questions",
                "evidence_ids": ["chunk:evaluation-systematic-approach:ch03-chapter-3-identifying-issues-and-formulating-questions:c0055"],
                "summary": [
                    "The section stresses that evaluation questions organize design, analysis, and eventual use.",
                    "Questions may matter even when immediate instrumental use is not obvious, because evaluation can shape understanding and debate.",
                    "The evaluator must therefore prioritize questions for practical decision value and conceptual influence.",
                ],
                "concepts": ["Question formulation", "Prioritization", "Conceptual use", "Persuasive use"],
                "implications": [
                    "Separate interesting questions from decision-critical questions.",
                    "Keep questions broad enough to support learning but narrow enough to answer.",
                    "Document why lower-priority questions were deferred.",
                ],
            },
            {
                "id": "program-theory-assessment",
                "title": "Expressing and Assessing Program Theory",
                "source_pages": "120-121",
                "section_path": "Chapter 5: Expressing and Assessing Program Theory",
                "evidence_ids": ["chunk:evaluation-systematic-approach:ch05-chapter-5-expressing-and-assessing-program-theory:c0001"],
                "summary": [
                    "The chapter treats program theory as part of the evaluand, not only as an evaluator's planning aid.",
                    "Assessment asks whether the program's logic, objectives, activities, and causal assumptions are explicit and plausible.",
                    "This work helps identify whether later impact evaluation would be meaningful.",
                ],
                "concepts": ["Program theory", "Evaluability", "Logic and plausibility", "Implementation failure"],
                "implications": [
                    "Assess program theory before estimating impact.",
                    "Look for missing links between program activities and expected benefits.",
                    "Use theory assessment to decide whether the program or evaluation design needs revision first.",
                ],
            },
        ],
    },
    {
        "book_id": "essentials-utilization-focused-evaluation",
        "slug": "essentials-utilization-focused-evaluation",
        "title": "Essentials of Utilization-Focused Evaluation",
        "full_title": "Essentials of Utilization-Focused Evaluation",
        "authors": ["Michael Quinn Patton"],
        "year": "2012",
        "citation": "patton_2012_essentials_utilization_focused_evaluation",
        "publisher": "SAGE Publications",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "A compact guide to designing evaluations for primary intended users and actual use.",
        "core": "Utilization-focused evaluation judges design quality by whether intended users can and will use the process and findings.",
        "concepts": [
            "Primary intended users",
            "Primary intended uses",
            "Situation analysis",
            "Process use",
            "Methods negotiation",
            "Findings use",
        ],
        "practice": [
            "Identify real users, not abstract audiences.",
            "Focus questions around intended uses before choosing methods.",
            "Engage users in methods trade-offs so credibility and utility are negotiated together.",
            "Plan interpretation and action, not only reporting.",
        ],
        "sections": [
            {
                "id": "utilization-focused-overview",
                "title": "Utilization-Focused Evaluation Overview",
                "source_pages": "27-28",
                "section_path": "Introduction, Overview, and Context",
                "evidence_ids": ["chunk:essentials-utilization-focused-evaluation:ch-introduction-overview-and-context:c0007"],
                "summary": [
                    "The overview anchors U-FE in a practical sequence from findings to interpretation to action.",
                    "Reports are not the purpose of evaluation; use is the purpose.",
                    "The evaluator facilitates a process in which design decisions are judged by utility and actual use.",
                ],
                "concepts": ["Utility", "Actual use", "Primary intended users", "Action"],
                "implications": [
                    "Name who will use the evaluation and how.",
                    "Make use criteria visible in design decisions.",
                    "Plan beyond the report to interpretation and action.",
                ],
            },
            {
                "id": "seventeen-steps",
                "title": "The 17-Step Utilization-Focused Checklist",
                "source_pages": "36-37",
                "section_path": "Introduction, Overview, and Context",
                "evidence_ids": ["chunk:essentials-utilization-focused-evaluation:ch-introduction-overview-and-context:c0027"],
                "summary": [
                    "The checklist gives a practical sequence for evaluations that are useful and actually used.",
                    "It moves from evaluator readiness and user identification through questions, methods, data, interpretation, reporting, and follow-through.",
                    "The structure makes utilization a design discipline rather than a hope at the end.",
                ],
                "concepts": ["Checklist", "Evaluator readiness", "Priority uses", "Process use"],
                "implications": [
                    "Use the checklist as a design audit across the whole evaluation cycle.",
                    "Return to earlier steps when users, uses, or context change.",
                    "Treat use as a continuing facilitation task.",
                ],
            },
            {
                "id": "methods-for-use",
                "title": "Negotiating Methods for Intended Use",
                "source_pages": "288-289",
                "section_path": "Step 10: Negotiate Appropriate Methods to Generate Credible Findings That Support Intended Use by Intended Users",
                "evidence_ids": ["chunk:essentials-utilization-focused-evaluation:step10-step-10-negotiate-appropriate-methods-to-generate-credible-findings-that-support:c0005"],
                "summary": [
                    "The section frames methods choice as a facilitated negotiation about credibility, utility, and constraints.",
                    "Intended users need to understand methodological debates enough to judge what evidence will be credible for their use.",
                    "The evaluator's role includes surfacing trade-offs before data collection locks them in.",
                ],
                "concepts": ["Methods negotiation", "Credible evidence", "User capacity", "Trade-offs"],
                "implications": [
                    "Discuss methodological controversies before committing to a design.",
                    "Make criteria for credibility explicit with intended users.",
                    "Choose methods that answer priority questions within real constraints.",
                ],
            },
        ],
    },
    {
        "book_id": "magenta-book",
        "slug": "magenta-book",
        "title": "Magenta Book",
        "full_title": "Magenta Book: Central Government guidance on evaluation",
        "authors": ["HM Treasury", "Evaluation Task Force"],
        "year": "2020",
        "citation": "hm_treasury_evaluation_task_force_2020_magenta_book",
        "publisher": "HM Treasury",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "UK central government guidance on evaluation scoping, methods, data, management, dissemination, and capability.",
        "core": "Government evaluation should be scoped around decision needs, appropriate methods, robust data, quality assurance, and clear use of findings.",
        "concepts": [
            "Process evaluation",
            "Impact evaluation",
            "Value for money evaluation",
            "Theory-based methods",
            "Experimental and quasi-experimental methods",
            "Evaluation management",
        ],
        "practice": [
            "Scope evaluation questions before choosing methods.",
            "Use theory-based, experimental, quasi-experimental, qualitative, and economic methods proportionately.",
            "Build quality assurance and flexibility into evaluation management.",
            "Plan dissemination around users and decision timing.",
        ],
        "sections": [
            {
                "id": "executive-summary",
                "title": "Executive Summary and Evaluation Types",
                "source_pages": "3",
                "section_path": "Executive summary",
                "evidence_ids": ["chunk:magenta-book:magenta-book-executive-summary:c0003"],
                "summary": [
                    "The executive summary defines the main evaluation types and the structure of the guidance.",
                    "It distinguishes process, impact, and value for money evaluation while emphasizing that interventions need to be understood across design, delivery, results, and costs.",
                    "The guide is organized around why and when to evaluate, scoping, methods, data, management, findings use, and capability.",
                ],
                "concepts": ["Process evaluation", "Impact evaluation", "Value for money", "Evaluation lifecycle"],
                "implications": [
                    "Choose evaluation type based on the decision problem.",
                    "Combine evaluation types when a single question cannot cover design, delivery, impact, and costs.",
                    "Use the guidance as a lifecycle checklist.",
                ],
            },
            {
                "id": "evaluation-methods",
                "title": "Choosing Evaluation Methods",
                "source_pages": "6",
                "section_path": "3. Evaluation methods",
                "evidence_ids": ["chunk:magenta-book:magenta-book-3-evaluation-methods:c0002"],
                "summary": [
                    "The methods chapter stresses that method choice requires iteration as scope, timing, resources, and questions become clearer.",
                    "Different methods answer different questions and have different resource implications.",
                    "Stakeholder involvement matters because method choice affects what can credibly be answered.",
                ],
                "concepts": ["Method selection", "Theory-based methods", "Experimental methods", "Evidence synthesis"],
                "implications": [
                    "Revisit evaluation questions when methods prove infeasible.",
                    "Communicate any deprioritizing of questions clearly.",
                    "Use stakeholders' context knowledge when judging method assumptions.",
                ],
            },
            {
                "id": "managing-evaluation",
                "title": "Managing an Evaluation",
                "source_pages": "8",
                "section_path": "5. Managing an evaluation",
                "evidence_ids": ["chunk:magenta-book:magenta-book-5-managing-an-evaluation:c0017"],
                "summary": [
                    "The management section highlights the balance between consistency and flexibility.",
                    "Experimental and quasi-experimental designs often need stable delivery and measurement, while complex or innovative interventions may require adaptive evaluation management.",
                    "Quality assurance and early planning help maintain credibility when evaluation requirements change.",
                ],
                "concepts": ["Evaluation management", "Flexibility", "Consistency", "Quality assurance"],
                "implications": [
                    "Build adaptation rules into the evaluation plan.",
                    "Protect comparability when design consistency is required.",
                    "Use quality assurance to manage changes transparently.",
                ],
            },
        ],
    },
    {
        "book_id": "evaluation-theory-models-applications",
        "slug": "evaluation-theory-models-applications",
        "title": "Evaluation Theory, Models, and Applications",
        "full_title": "Evaluation Theory, Models, and Applications",
        "authors": ["Daniel L. Stufflebeam", "Chris L. S. Coryn"],
        "year": "2014",
        "citation": "stufflebeam_coryn_2014_evaluation_theory_models_applications",
        "publisher": "Jossey-Bass",
        "source_status": "needs_review",
        "rag_status": "ready",
        "generation_mode": "generated-major-sections",
        "card": "A survey and assessment of evaluation theory, models, standards, CIPP, metaevaluation, and applications.",
        "core": "Evaluation approaches should be judged against standards for utility, feasibility, propriety, accuracy, accountability, and practical improvement.",
        "concepts": [
            "Evaluation theory",
            "Evaluation models",
            "CIPP",
            "Standards",
            "Metaevaluation",
            "Objectivist evaluation",
        ],
        "practice": [
            "Choose evaluation models by fit to purpose and standards, not by brand familiarity.",
            "Use metaevaluation formatively during the study and summatively at the end.",
            "Distinguish improvement, accountability, social agenda, and eclectic approaches.",
            "Make value criteria explicit before judging merit or worth.",
        ],
        "sections": [
            {
                "id": "evaluation-theory-development",
                "title": "Program Evaluation Standards and Theory Development",
                "source_pages": "101",
                "section_path": "Part One: Fundamentals of Evaluation > Chapter 2: Evaluation Theory > Program Evaluation Standards and Theory Development",
                "evidence_ids": ["chunk:evaluation-theory-models-applications:program-evaluation-standards-and-theory-development:c0005"],
                "summary": [
                    "The section assesses evaluation theory as a field rich in concepts, standards, and approaches but still developing stronger validated theory.",
                    "It argues for converting useful approaches into better-tested theories through research and metaevaluation.",
                    "The practical implication is humility: models should be used critically and improved through evidence.",
                ],
                "concepts": ["Theory development", "Evaluation standards", "Metaevaluation", "Validated theory"],
                "implications": [
                    "Treat models as aids to judgment, not recipes.",
                    "Use standards to critique an evaluation approach before adopting it.",
                    "Document what the evaluation model predicts and how that prediction is checked.",
                ],
            },
            {
                "id": "cipp-overview",
                "title": "CIPP Model Overview",
                "source_pages": "345",
                "section_path": "Part Three > Chapter 13: Daniel Stufflebeam's CIPP Model > Overview of the Chapter",
                "evidence_ids": ["chunk:evaluation-theory-models-applications:overview-of-the-chapter-2:c0002"],
                "summary": [
                    "The CIPP overview introduces context, input, process, and product evaluation as linked ways to support improvement and accountability.",
                    "The model can be used formatively and summatively across sectors.",
                    "Its systems orientation asks evaluators to attend to stakeholders, values, procedures, and use.",
                ],
                "concepts": ["Context evaluation", "Input evaluation", "Process evaluation", "Product evaluation"],
                "implications": [
                    "Use context evaluation to clarify needs and goals.",
                    "Use input evaluation to judge strategies and plans.",
                    "Use process and product evaluation to track implementation and results.",
                ],
            },
            {
                "id": "standards-and-metaevaluation",
                "title": "Standards and Metaevaluation",
                "source_pages": "353",
                "section_path": "Part Three > Chapter 13 > Philosophy and Code of Ethics Underlying the CIPP Model",
                "evidence_ids": ["chunk:evaluation-theory-models-applications:philosophy-and-code-of-ethics-underlying-the-cipp-model:c0006"],
                "summary": [
                    "The section connects CIPP to professional standards and metaevaluation.",
                    "Evaluation quality is judged against utility, feasibility, propriety, accuracy, and accountability.",
                    "Metaevaluation is both formative, guiding correction during the work, and summative, judging final quality.",
                ],
                "concepts": ["Utility", "Feasibility", "Propriety", "Accuracy", "Evaluation accountability"],
                "implications": [
                    "Use standards as checkpoints during the evaluation, not only after completion.",
                    "Report how the evaluation met relevant quality standards.",
                    "Seek independent metaevaluation when stakes justify it.",
                ],
            },
        ],
    },
]


def dedent(value: str) -> str:
    return inspect.cleandoc(value).strip() + "\n"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_text(rel: str, text: str) -> None:
    path = ROOT / rel
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def yaml_list(values: list[str], indent: int = 0) -> str:
    pad = " " * indent
    return "\n".join(f'{pad}- "{value}"' for value in values)


def cite(book: dict[str, Any]) -> str:
    return f"@{book['citation']}"


def author_label(book: dict[str, Any]) -> str:
    authors = book["authors"]
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    return ", ".join(authors[:-1]) + f", and {authors[-1]}"


def front_matter(book: dict[str, Any], title: str, description: str, note_type: str, evidence_ids: list[str], source_pages: str = "") -> str:
    lines = [
        "---",
        f'title: "{title}"',
        f'description: "{description}"',
        f'book_id: "{book["book_id"]}"',
        'collection_id: "evaluation-texts"',
        f'note_type: "{note_type}"',
    ]
    if source_pages:
        lines.append(f'source_pages: "{source_pages}"')
    lines.extend(
        [
            f'citation_key: "{book["citation"]}"',
            "evidence_ids:",
        ]
    )
    if evidence_ids:
        lines.extend(f'  - "{evidence_id}"' for evidence_id in evidence_ids)
    else:
        lines.append("  []")
    lines.extend(
        [
            f'source_status: "{book["source_status"]}"',
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def metadata_html(book: dict[str, Any], extra: list[str] | None = None) -> str:
    items = [book["year"], "MCP evaluation-texts", f"Status: {book['source_status']}"]
    if extra:
        items.extend(extra)
    spans = "".join(f"<span>{item}</span>" for item in items)
    return f'<div class="chapter-meta">{spans}</div>\n'


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def numbered_prompts(book: dict[str, Any], topic: str) -> str:
    prompts = [
        f"What is the main evaluation problem that {topic} helps diagnose?",
        "Which assumptions would need evidence before using this guidance in a live evaluation?",
        "How would this change the way an evaluator scopes questions, methods, or reporting?",
        "Where could the guidance be misused if treated as a fixed template?",
    ]
    return "\n".join(f"{idx}. {prompt}" for idx, prompt in enumerate(prompts, start=1))


def section_file_name(section: dict[str, Any], index: int) -> str:
    return f"section-{index:02d}-{section['id']}.qmd"


def render_section_page(book: dict[str, Any], section: dict[str, Any], index: int) -> str:
    evidence_ids = section["evidence_ids"]
    qmd = front_matter(
        book,
        section["title"],
        f"Study note on {section['title']} in {book['title']}.",
        "Major section",
        evidence_ids,
        section["source_pages"],
    )
    qmd += f"## Source\n\n{metadata_html(book, [f'Source pages {section['source_pages']}', 'Major section'])}"
    qmd += (
        f"This note summarises the MCP research-library section \"{section['title']}\" "
        f"from {author_label(book)}'s *{book['full_title']}* [{cite(book)}]. "
        "It is a paraphrased study note based on source-linked retrieval records, not a substitute for the source text.\n\n"
    )
    qmd += f"## Core Argument\n\n{section['summary'][0]}\n\n"
    qmd += "## Study Summary\n\n" + "\n\n".join(section["summary"]) + "\n\n"
    qmd += "## Key Concepts\n\n" + bullet_list(section["concepts"]) + "\n\n"
    qmd += f"## Source Location\n\n- Section path: {section['section_path']}\n"
    qmd += f"- Evidence records: {', '.join(f'`{item}`' for item in evidence_ids)}\n\n"
    qmd += "## Practical Implications\n\n" + bullet_list(section["implications"]) + "\n\n"
    qmd += "## Connections\n\n"
    qmd += "- Book overview: [Overview](index.qmd)\n"
    qmd += "- Concepts: [Core Concepts](concepts.qmd)\n"
    qmd += "- Map: [Chapter Map](chapter-map.qmd)\n"
    qmd += "- Practice synthesis: [Practice Implications](practice-implications.qmd)\n\n"
    qmd += "## Study Prompts\n\n" + numbered_prompts(book, section["title"]) + "\n\n"
    qmd += "## References\n"
    return qmd


def render_book_index(book: dict[str, Any]) -> str:
    evidence = [eid for section in book["sections"] for eid in section["evidence_ids"][:1]]
    qmd = front_matter(book, book["title"], f"Book overview and study-note index for {book['title']}.", "Book", evidence)
    qmd += dedent(
        f"""
        <div class="landing-stack">

        ::: {{.landing-hero}}
        <span class="hero-eyebrow">Book notes</span>

        # {book['title']}

        Study notes on *{book['full_title']}* [{cite(book)}]. These notes are generated from source-linked MCP research-library records and are intended for study, comparison, and later refinement.

        <div class="page-metadata">
          <span>{len(book['sections'])} major-section notes</span>
          <span>{book['year']}</span>
          <span>Source status: {book['source_status']}</span>
          <span>MCP evaluation-texts</span>
        </div>
        :::

        ::: {{.section-grid}}
        ::: {{.section-card}}
        <span class="page-badge badge-synthesis">Synthesis</span>

        ### [Core Concepts](concepts.qmd)

        Recurring ideas and distinctions used across these notes.
        :::

        ::: {{.section-card}}
        <span class="page-badge badge-map">Map</span>

        ### [Chapter Map](chapter-map.qmd)

        Selected source sections, page ranges, and reading routes.
        :::

        ::: {{.section-card}}
        <span class="page-badge badge-practice">Practice</span>

        ### [Practice Implications](practice-implications.qmd)

        Practical evaluation design habits drawn from the notes.
        :::
        :::

        </div>

        ## Source

        {metadata_html(book, ['Book overview'])}
        This index summarises generated study notes for {author_label(book)}'s *{book['full_title']}* [{cite(book)}]. The generated pages use selected MCP research-library retrieval records and compact evidence summaries.

        ## Core Argument

        {book['core']}

        ## Major-Section Notes
        """
    )
    for idx, section in enumerate(book["sections"], start=1):
        qmd += f"\n- [{section['title']}]({section_file_name(section, idx)}) - source pages {section['source_pages']}"
    qmd += "\n\n## References\n"
    return qmd


def render_concepts(book: dict[str, Any]) -> str:
    evidence = [eid for section in book["sections"] for eid in section["evidence_ids"][:1]]
    qmd = front_matter(book, f"Core Concepts in {book['title']}", f"Synthesis note on recurring concepts in {book['title']}.", "Synthesis", evidence)
    qmd += f"## Source\n\nThis synthesis draws across the generated notes for *{book['full_title']}* [{cite(book)}].\n\n"
    qmd += f"## Central Logic\n\n{book['core']}\n\n"
    qmd += "## Concepts\n\n"
    for concept in book["concepts"]:
        qmd += f"- {concept}: a recurring idea used to frame evaluation design, evidence collection, interpretation, or use in this book.\n"
    qmd += "\n## Links\n\n"
    for idx, section in enumerate(book["sections"], start=1):
        qmd += f"- [{section['title']}]({section_file_name(section, idx)})\n"
    qmd += "\n## References\n"
    return qmd


def render_chapter_map(book: dict[str, Any]) -> str:
    evidence = [eid for section in book["sections"] for eid in section["evidence_ids"][:1]]
    qmd = front_matter(book, f"{book['title']} Chapter Map", f"Reading map for selected {book['title']} notes.", "Map", evidence)
    qmd += f"## Source\n\nThis map uses selected MCP research-library sections from *{book['full_title']}* [{cite(book)}].\n\n"
    qmd += "## Reading Route\n\n"
    for idx, section in enumerate(book["sections"], start=1):
        qmd += f"{idx}. [{section['title']}]({section_file_name(section, idx)}) - pages {section['source_pages']}; `{section['section_path']}`\n"
    qmd += "\n## How to Use This Map\n\n"
    qmd += "- Start with the first section for the book's framing logic.\n"
    qmd += "- Use the middle section to inspect the main design or method implications.\n"
    qmd += "- Use the final section to check limits, quality standards, or implications for use.\n\n"
    qmd += "## References\n"
    return qmd


def render_practice(book: dict[str, Any]) -> str:
    evidence = [eid for section in book["sections"] for eid in section["evidence_ids"][:1]]
    qmd = front_matter(book, f"{book['title']} Practice Implications", f"Practice synthesis for {book['title']}.", "Practice", evidence)
    qmd += f"## Source\n\nThis practice synthesis draws on selected notes from *{book['full_title']}* [{cite(book)}].\n\n"
    qmd += "## Evaluation Practice Implications\n\n" + bullet_list(book["practice"]) + "\n\n"
    qmd += "## Applying the Notes\n\n"
    qmd += "Use these implications as prompts during scoping, design review, method selection, and reporting. They should be adapted to the evaluation's decision context, available evidence, and user needs.\n\n"
    qmd += "## Links\n\n"
    for idx, section in enumerate(book["sections"], start=1):
        qmd += f"- [{section['title']}]({section_file_name(section, idx)})\n"
    qmd += "\n## References\n"
    return qmd


def render_notes_index() -> str:
    qmd = dedent(
        """---
        title: "Notes"
        page-layout: full
        toc: false
        ---

        <div class="landing-stack">

        ::: {.landing-hero}
        <span class="hero-eyebrow">Evaluation notes</span>

        # Notes overview

        This section collects source-grounded study notes from the MCP research library's `evaluation-texts` collection. The notes combine the existing hand-authored Purposeful Program Theory section with generated major-section notes for the other ready evaluation texts.

        <div class="page-metadata">
          <span>10 books</span>
          <span>Evaluation texts</span>
          <span>MCP sourced</span>
          <span><a href="../references.bib" download>Export BibTeX</a></span>
        </div>
        :::

        ```{=html}
        <div class="notes-filter" role="search" aria-label="Filter note tiles">
          <label for="notes-search">Find
            <input id="notes-search" type="search" placeholder="Search notes" autocomplete="off" />
          </label>
          <label for="notes-book-filter">Book
            <select id="notes-book-filter">
              <option value="all">All books</option>
        """
    )
    for book in BOOKS:
        qmd += f'              <option value="{book["slug"]}">{book["title"]}</option>\n'
    qmd += dedent(
        """            </select>
          </label>
          <label for="notes-type-filter">Type
            <select id="notes-type-filter">
              <option value="all">All types</option>
              <option value="Book">Book</option>
              <option value="Synthesis">Synthesis</option>
              <option value="Map">Map</option>
              <option value="Practice">Practice</option>
            </select>
          </label>
        </div>
        <p class="notes-filter-count" id="notes-filter-count" aria-live="polite"></p>
        ```

        ::: {.section-grid}
        """
    )
    for book in BOOKS:
        links = [
            ("Book", book["title"], f"{book['slug']}/index.qmd", book["card"], "badge-book"),
            ("Synthesis", "Core Concepts", f"{book['slug']}/concepts.qmd", "Recurring concepts and distinctions for this source.", "badge-synthesis"),
            ("Map", "Chapter Map", f"{book['slug']}/chapter-map.qmd", "Selected source sections, evidence IDs, and reading route.", "badge-map"),
            ("Practice", "Practice Implications", f"{book['slug']}/practice-implications.qmd" if book["slug"] != "purposeful-programme-theory" else f"{book['slug']}/evaluation-practice-implications.qmd", "Evaluation design habits and practical uses.", "badge-practice"),
        ]
        for note_type, label, href, desc, badge in links:
            if book["slug"] == "purposeful-programme-theory" and label == "Chapter Map":
                href = f"{book['slug']}/chapter-map.qmd"
            card_title = book["title"] if note_type == "Book" else f"{label}: {book['title']}"
            qmd += dedent(
                f"""
                ::: {{.section-card data-note-card="" data-book="{book['slug']}" data-type="{note_type}"}}
                <div class="badge-row"><span class="page-badge {badge}">{note_type}</span><span class="page-badge badge-chapter">{book['year']}</span></div>

                ### [{card_title}]({href})

                {desc}
                :::
                """
            )
    qmd += dedent(
        """
        :::

        ```{=html}
        <script src="../assets/js/notes_filter.js"></script>
        ```

        </div>
        """
    )
    return qmd


def render_home() -> str:
    cards = ""
    for book in BOOKS:
        cards += dedent(
            f"""
            ::: {{.section-card}}
            <span class="page-badge badge-book">Book notes</span>

            ### [{book['title']}](notes/{book['slug']}/index.qmd)

            {book['card']}
            :::
            """
        )
    return (
        '---\n'
        'title: "Evaluation Knowledge Base"\n'
        'page-layout: full\n'
        'toc: false\n'
        '---\n\n'
        '<div class="landing-stack">\n\n'
        '::: {.hero-panel}\n'
        '<span class="hero-eyebrow">Evaluation study notes</span>\n\n'
        '# Evaluation Knowledge Base\n\n'
        'A Quarto knowledge base for source-grounded notes on evaluation books and guidance. '
        'The site now integrates ready `evaluation-texts` records from the MCP research library, '
        'with detailed hand-authored notes for Purposeful Program Theory and generated major-section notes for the wider collection.\n\n'
        '::: {.cta-row}\n'
        '[Open Notes](notes/index.qmd){.cta-button}\n'
        '[Purposeful Program Theory](notes/purposeful-programme-theory/index.qmd){.cta-button .secondary}\n'
        '[Export BibTeX](references.bib){.cta-button .secondary}\n'
        ':::\n'
        ':::\n\n'
        '::: {.section-grid}\n'
        f'{cards}'
        ':::\n\n'
        '</div>\n'
    )


def render_bib() -> str:
    entries = []
    for book in BOOKS:
        if book["book_id"] == "magenta-book":
            entries.append(
                dedent(
                    f"""@techreport{{{book['citation']},
                      author = {{{{{book['authors'][0]}}} and {{{book['authors'][1]}}}}},
                      title = {{{book['full_title']}}},
                      year = {{{book['year']}}},
                      institution = {{{book['publisher']}}}
                    }}"""
                )
            )
        else:
            author_field = " and ".join(book["authors"])
            entries.append(
                dedent(
                    f"""@book{{{book['citation']},
                      author = {{{author_field}}},
                      title = {{{book['full_title']}}},
                      year = {{{book['year']}}},
                      publisher = {{{book['publisher']}}}
                    }}"""
                )
            )
    return "\n".join(entries) + "\n"


def render_manifest() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "generated_at": GENERATED_AT,
        "collection_id": "evaluation-texts",
        "source": {
            "mcp_tool": "mcp__researchlibrary",
            "collection_discovery": "library_list_collections",
            "section_discovery": "rag_search",
            "notes": "Generated notes are paraphrases from selected MCP retrieval records; verbatim source text is not stored.",
        },
        "books": [
            {
                "book_id": book["book_id"],
                "slug": book["slug"],
                "title": book["title"],
                "full_title": book["full_title"],
                "authors": book["authors"],
                "year": book["year"],
                "citation": book["citation"],
                "source_status": book["source_status"],
                "rag_status": book["rag_status"],
                "generation_mode": book["generation_mode"],
                "target_path": f"notes/{book['slug']}/index.qmd",
                "sections": [
                    {
                        "id": section["id"],
                        "title": section["title"],
                        "source_pages": section["source_pages"],
                        "section_path": section["section_path"],
                        "evidence_ids": section["evidence_ids"],
                        "target_path": f"notes/{book['slug']}/{section_file_name(section, idx)}",
                    }
                    for idx, section in enumerate(book["sections"], start=1)
                ],
            }
            for book in BOOKS
        ],
    }


def render_evidence_summary(book: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "generated_at": GENERATED_AT,
        "collection_id": "evaluation-texts",
        "book_id": book["book_id"],
        "book_title": book["title"],
        "source_status": book["source_status"],
        "rag_status": book["rag_status"],
        "source_tool": "mcp__researchlibrary.rag_search",
        "copyright_note": "Stores retrieval IDs and source locations only; source text is not duplicated.",
        "records": [
            {
                "section_id": section["id"],
                "section_title": section["title"],
                "source_pages": section["source_pages"],
                "section_path": section["section_path"],
                "evidence_ids": section["evidence_ids"],
            }
            for section in book["sections"]
        ],
    }


def generate() -> None:
    write_text("docs/mcp_research_library_notes_plan.md", PLAN)
    write_text("references.bib", render_bib())
    write_text("index.qmd", render_home())
    write_text("notes/index.qmd", render_notes_index())
    write_text("data/research_library_notes_manifest.json", json.dumps(render_manifest(), indent=2) + "\n")

    for book in BOOKS:
        write_text(
            f"data/research-library/evidence/{book['slug']}/evidence-summary.json",
            json.dumps(render_evidence_summary(book), indent=2) + "\n",
        )
        if book["generation_mode"] == "existing-hand-authored":
            continue

        base = f"notes/{book['slug']}"
        write_text(f"{base}/index.qmd", render_book_index(book))
        write_text(f"{base}/concepts.qmd", render_concepts(book))
        write_text(f"{base}/chapter-map.qmd", render_chapter_map(book))
        write_text(f"{base}/practice-implications.qmd", render_practice(book))
        for idx, section in enumerate(book["sections"], start=1):
            write_text(f"{base}/{section_file_name(section, idx)}", render_section_page(book, section, idx))


if __name__ == "__main__":
    generate()
