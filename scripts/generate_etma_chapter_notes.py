#!/usr/bin/env python3
"""Generate chapter-level ETMA study notes from curated MCP evidence metadata."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "evaluation-theory-models-applications"
SLUG = BOOK_ID
TITLE = "Evaluation Theory, Models, and Applications"
FULL_TITLE = TITLE
AUTHORS = "Daniel L. Stufflebeam and Chris L. S. Coryn"
CITATION = "stufflebeam_coryn_2014_evaluation_theory_models_applications"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2014"
PUBLISHER = "Jossey-Bass"


PARTS = [
    "Part One: Fundamentals of Evaluation",
    "Part Two: An Evaluation of Evaluation Approaches and Models",
    "Part Three: Explication of Selected Evaluation Approaches",
    "Part Four: Evaluation Tasks, Procedures, and Tools",
    "Part Five: Metaevaluation and Institutionalizing and Mainstreaming Evaluation",
]


CHAPTERS = [
    {
        "number": 1,
        "title": "Overview of the Evaluation Field",
        "part": PARTS[0],
        "pages": "39-79",
        "file": "chapter-01-overview-of-the-evaluation-field.qmd",
        "section_path": "Part One: Fundamentals of Evaluation > Chapter 1: Overview of the Evaluation Field",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch01-chapter-1-overview-of-the-evaluation-field:c0001",
            "chunk:evaluation-theory-models-applications:how-should-evaluations-be-used:c0005",
            "chunk:evaluation-theory-models-applications:what-are-the-main-historical-milestones-in-the-evaluation-field-s-development:c0028",
        ],
        "core": "Evaluation is presented as a systematic value-oriented discipline that society needs for improvement, accountability, and protection from weak or unsafe services.",
        "summary": [
            "The opening chapter separates formal evaluation from everyday judgment. Informal evaluation is unavoidable, but it is often unsystematic and weakly documented. Formal evaluation is treated as a disciplined process for judging merit, worth, probity, safety, effectiveness, efficiency, and related criteria.",
            "The chapter broadens evaluation beyond objectives and outcomes. Programs, policies, services, products, personnel systems, and organizations can all be evaluands. A sound evaluation asks what value criteria matter, whose needs are at stake, what evidence is credible, and how findings should be communicated.",
            "Formative and summative uses organize much of the chapter. Formative evaluation supports development and improvement, while summative evaluation supports overall judgment, accountability, adoption, or discontinuation. The authors stress that the two uses can interact and should not be treated as mutually exclusive.",
            "The historical review positions evaluation as a profession that grew through educational measurement, objectives-based evaluation, federal program accountability, professional standards, and later multidisciplinary expansion. The field's history is used as a warning against narrow method loyalties and as a rationale for standards-based practice.",
        ],
        "concepts": ["formal evaluation", "informal evaluation", "evaluand", "merit and worth", "probity", "formative use", "summative use", "professionalization"],
        "structure": ["definitions and objects of evaluation", "criteria for judging value", "formative and summative uses", "internal and external evaluation", "historical periods in the field"],
        "implications": ["Clarify the evaluand and value criteria before selecting methods.", "Treat formative and summative needs as design choices, not labels added after the fact.", "Use professional standards to check credibility when evaluation findings will affect public decisions."],
    },
    {
        "number": 2,
        "title": "Evaluation Theory",
        "part": PARTS[0],
        "pages": "81-102",
        "file": "chapter-02-evaluation-theory.qmd",
        "section_path": "Part One: Fundamentals of Evaluation > Chapter 2: Evaluation Theory",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch02-chapter-2-evaluation-theory:c0001",
            "chunk:evaluation-theory-models-applications:criteria-for-judging-program-evaluation-theories:c0003",
            "chunk:evaluation-theory-models-applications:program-evaluation-standards-and-theory-development:c0005",
        ],
        "core": "Evaluation approaches should be developed and tested as theories rather than treated only as branded models or practitioner traditions.",
        "summary": [
            "Chapter 2 asks what it would mean for evaluation to have stronger theory. The authors distinguish a theory from an approach or model: a theory should contain conceptual, hypothetical, pragmatic, and ethical principles that explain and guide evaluation practice.",
            "The chapter argues that the evaluation field has generated many useful concepts, standards, approaches, and practical guidelines, but fewer well-tested propositions about what evaluation actions produce useful consequences in particular contexts. This makes humility important when applying any model.",
            "Criteria for judging evaluation theories include their contribution to professionalizing evaluation, supporting research, guiding planning, structuring implementation, and strengthening use. The existing major-section note on theory development belongs here because it captures the authors' argument that standards and metaevaluation should help convert promising approaches into better tested theories.",
            "The chapter frames theory development as both creative and empirical. Evaluators need conceptual imagination, but they also need metaevaluations and research on evaluation to test whether an approach actually improves utility, feasibility, propriety, accuracy, accountability, and use.",
        ],
        "concepts": ["evaluation theory", "evaluation model", "evaluation approach", "theory development", "research on evaluation", "metaevaluation", "program evaluation standards"],
        "structure": ["role of theory in the field", "theory versus model or approach", "components of sound theory", "criteria for judging theories", "standards and theory development"],
        "implications": ["Name the theory or model being used and what it is expected to improve.", "Use standards as a critique of an approach before adopting it.", "Document evaluation assumptions so later metaevaluation can test whether they held."],
    },
    {
        "number": 3,
        "title": "Standards for Program Evaluations",
        "part": PARTS[0],
        "pages": "105-138",
        "file": "chapter-03-standards-for-program-evaluations.qmd",
        "section_path": "Part One: Fundamentals of Evaluation > Chapter 3: Standards for Program Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch03-chapter-3-standards-for-program-evaluations:c0001",
            "chunk:evaluation-theory-models-applications:the-need-for-evaluation-standards:c0002",
            "chunk:evaluation-theory-models-applications:using-evaluation-standards:c0005",
        ],
        "core": "Professional standards are the field's practical infrastructure for making evaluations useful, feasible, proper, accurate, and accountable.",
        "summary": [
            "Chapter 3 treats standards as protection against poor, biased, or incredible evaluation work. Standards help evaluators and clients agree on what an evaluation should meet, provide common language, and create grounds for judging plans, conduct, reports, and organizations.",
            "The chapter compares three major sources of guidance: the Joint Committee's Program Evaluation Standards, the American Evaluation Association's Guiding Principles for Evaluators, and Government Auditing Standards. Each has a different origin and emphasis, but all can inform program evaluation practice.",
            "The Joint Committee standards receive special attention because their categories of utility, feasibility, propriety, accuracy, and evaluation accountability recur throughout the book. The authors use those categories later to classify and rate approaches and to structure metaevaluation.",
            "The practical message is not that evaluators should mechanically cite standards. They should select relevant standards, orient stakeholders to them, apply them throughout the evaluation, and decide whether independent metaevaluation is warranted.",
        ],
        "concepts": ["utility", "feasibility", "propriety", "accuracy", "evaluation accountability", "guiding principles", "government auditing standards"],
        "structure": ["need for standards", "background of standards", "Joint Committee standards", "AEA guiding principles", "Government Auditing Standards", "using standards"],
        "implications": ["Choose standards at the start and explain why they fit the assignment.", "Use standards during design and fieldwork, not only at final review.", "Record where standards are adapted because of context or resource limits."],
    },
    {
        "number": 4,
        "title": "Background for Assessing Evaluation Approaches",
        "part": PARTS[1],
        "pages": "143-150",
        "file": "chapter-04-background-for-assessing-evaluation-approaches.qmd",
        "section_path": "Part Two: An Evaluation of Evaluation Approaches and Models > Chapter 4: Background for Assessing Evaluation Approaches",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch04-chapter-4-background-for-assessing-evaluation-approaches:c0001",
            "chunk:evaluation-theory-models-applications:previous-classifications-of-alternative-evaluation-approaches:c0003",
            "chunk:evaluation-theory-models-applications:caveats:c0003",
        ],
        "core": "Evaluation approaches can be compared by how fully they support defensible judgments of value and by how well they meet professional standards.",
        "summary": [
            "Chapter 4 sets up the taxonomy used in Part Two. The authors classify twenty-three approaches into pseudoevaluations, quasi-evaluations, improvement- and accountability-oriented approaches, social agenda and advocacy approaches, and eclectic approaches.",
            "The chapter's main function is methodological. It explains the categories, reviews earlier classification efforts, and defines a set of descriptors used to characterize each approach. These descriptors cover purpose, questions, methods, pioneers, use conditions, strengths, and weaknesses.",
            "The taxonomy is explicitly evaluative. Approaches are not merely listed; they are judged according to whether they support credible assessment of merit and worth. Pseudoevaluations are rejected because they mislead, while legitimate approaches are still assessed for scope and standard compliance.",
            "The chapter prepares readers to avoid method-first thinking. An approach may be useful for a narrow purpose and still be inadequate as a full evaluation. This distinction matters throughout Chapters 5 through 10.",
        ],
        "concepts": ["approach classification", "pseudoevaluation", "quasi-evaluation", "improvement and accountability", "social agenda and advocacy", "eclectic evaluation"],
        "structure": ["rationale for classification", "previous classifications", "five categories", "nine approach descriptors", "caveats and exercises"],
        "implications": ["Classify the actual evaluation being proposed, not the label attached to it.", "Ask whether the approach can judge value or only answer a narrower question.", "Use the nine descriptors as a scoping checklist for comparing alternatives."],
    },
    {
        "number": 5,
        "title": "Pseudoevaluations",
        "part": PARTS[1],
        "pages": "151-168",
        "file": "chapter-05-pseudoevaluations.qmd",
        "section_path": "Part Two: An Evaluation of Evaluation Approaches and Models > Chapter 5: Pseudoevaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch05-chapter-5-pseudoevaluations:c0001",
            "chunk:evaluation-theory-models-applications:approach-6-customer-feedback-evaluation:c0006",
            "chunk:evaluation-theory-models-applications:approach-6-customer-feedback-evaluation:c0010",
        ],
        "core": "Pseudoevaluations use the appearance of evaluation while failing to provide independent, credible, and value-focused assessment.",
        "summary": [
            "Chapter 5 identifies approaches that the authors judge to be invalid or dangerously incomplete when presented as evaluation. The point is not that every activity described is always useless, but that each can mislead when it substitutes for defensible assessment of merit and worth.",
            "The authors discuss politically controlled studies, public relations studies, accountability theatre, and other forms in which the evaluation process is bent toward a predetermined interest. The harm is practical and ethical: weak evidence can legitimate bad decisions and reduce confidence in evaluation.",
            "A recurring warning is that good intentions do not rescue a flawed evaluation structure. Even approaches meant to empower stakeholders can become pseudoevaluative if they give interested parties control over evidence quality and judgment while presenting the result as independent evaluation.",
            "The chapter is a professional ethics checkpoint. Evaluators need to recognize assignments that would compromise independence, distort reporting, hide findings, or confuse satisfaction feedback with a credible value judgment.",
        ],
        "concepts": ["pseudoevaluation", "political control", "public relations evaluation", "customer feedback", "empowerment risk", "independence", "credible reporting"],
        "structure": ["definition of pseudoevaluation", "types of misleading studies", "political and public relations risks", "customer feedback and empowerment concerns", "professional cautions"],
        "implications": ["Screen assignments for control over questions, evidence, and reporting.", "Do not market satisfaction data as a full evaluation of value.", "Negotiate independence and publication conditions before accepting high-risk work."],
    },
    {
        "number": 6,
        "title": "Quasi-evaluation Studies",
        "part": PARTS[1],
        "pages": "169-208",
        "file": "chapter-06-quasi-evaluation-studies.qmd",
        "section_path": "Part Two: An Evaluation of Evaluation Approaches and Models > Chapter 6: Quasi-evaluation Studies",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch06-chapter-6-quasi-evaluation-studies:c0001",
            "chunk:evaluation-theory-models-applications:quasi-evaluation-approaches-defined:c0001",
            "chunk:evaluation-theory-models-applications:approach-14-meta-analysis:c0011",
        ],
        "core": "Quasi-evaluations can answer focused questions well, but their narrow scope means they should not be mistaken for full judgments of merit and worth.",
        "summary": [
            "Chapter 6 covers approaches that are technically useful but limited by question scope, method scope, or both. Objectives-based studies, success case work, value-added assessment, experiments, cost studies, connoisseurship, theory-based evaluation, and meta-analysis can all serve evaluators.",
            "The authors' caution is that a high-quality answer to a narrow question is not necessarily a complete evaluation. For example, objective attainment does not by itself show whether objectives were worth pursuing, whether needs were met, or whether side effects mattered.",
            "The chapter is not anti-method. It asks evaluators to know these approaches well enough to use them appropriately. Narrow studies may be valuable when clients need focused, timely evidence, but the reporting should make the limits explicit.",
            "The chapter also prepares readers for later chapters on experimental designs and case studies. Some approaches receive fuller treatment in Part Three because they are common and powerful, but their limitations still need to be understood.",
        ],
        "concepts": ["quasi-evaluation", "objectives-based study", "success case method", "value-added assessment", "experimental study", "cost study", "meta-analysis", "narrow-scope evidence"],
        "structure": ["definition and functions", "strengths and weaknesses", "eight quasi-evaluation approaches", "summary and cautions"],
        "implications": ["Match a narrow approach to a narrow question and say so in the report.", "Add value criteria when a client asks for conclusions about merit or worth.", "Use focused studies as components of broader evaluations when stakes require fuller judgment."],
    },
    {
        "number": 7,
        "title": "Improvement- and Accountability-oriented Evaluation Approaches",
        "part": PARTS[1],
        "pages": "209-226",
        "file": "chapter-07-improvement-and-accountability-oriented-evaluation-approaches.qmd",
        "section_path": "Part Two: An Evaluation of Evaluation Approaches and Models > Chapter 7: Improvement- and Accountability-oriented Evaluation Approaches",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:improvement-and-accountability-oriented-evaluation-defined:c0001",
            "chunk:evaluation-theory-models-applications:approach-15-decision-and-accountability-oriented-studies:c0001",
            "chunk:evaluation-theory-models-applications:approach-17-accreditation-and-certification:c0004",
        ],
        "core": "Improvement- and accountability-oriented approaches are closest to the authors' definition of evaluation because they explicitly assess value while serving decisions and public responsibility.",
        "summary": [
            "Chapter 7 describes approaches that seek to determine an evaluand's value rather than only answer a technical subquestion. The chapter covers decision- and accountability-oriented studies, consumer-oriented studies, and accreditation or certification.",
            "Decision- and accountability-oriented studies are represented mainly through CIPP. They combine improvement feedback with retrospective judgment, attend to stakeholders, and use multiple methods to assess context, plans, implementation, outcomes, and value.",
            "Consumer-oriented studies, associated with Scriven, are more directly focused on consumers' needs, alternatives, costs, and comparative value. Accreditation and certification add a standards-based institutional form in which a program or organization is judged against external criteria.",
            "The authors present these approaches as generally stronger than quasi-evaluations because they confront value. Their differences matter: CIPP is more improvement and systems oriented, consumer-oriented evaluation is more independent and comparative, and accreditation is more rule-bound.",
        ],
        "concepts": ["improvement", "accountability", "decision-oriented evaluation", "CIPP", "consumer-oriented evaluation", "accreditation", "certification"],
        "structure": ["definition and functions", "general strengths and weaknesses", "decision- and accountability-oriented studies", "consumer-oriented studies", "accreditation and certification"],
        "implications": ["Select these approaches when the client needs a defensible value judgment.", "Clarify the balance between improvement feedback and accountability reporting.", "Check whether external standards or consumer needs should dominate the value frame."],
    },
    {
        "number": 8,
        "title": "Social Agenda and Advocacy Evaluation Approaches",
        "part": PARTS[1],
        "pages": "227-245",
        "file": "chapter-08-social-agenda-and-advocacy-evaluation-approaches.qmd",
        "section_path": "Part Two: An Evaluation of Evaluation Approaches and Models > Chapter 8: Social Agenda and Advocacy Evaluation Approaches",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:overview-of-social-agenda-and-advocacy-approaches:c0003",
            "chunk:evaluation-theory-models-applications:approach-19-constructivist-evaluation:c0006",
            "chunk:evaluation-theory-models-applications:approach-21-transformative-evaluation:c0006",
        ],
        "core": "Social agenda and advocacy approaches bring democratic and justice commitments into evaluation, but they require strong safeguards against bias, impracticality, and loss of closure.",
        "summary": [
            "Chapter 8 examines approaches that use evaluation to serve equity, democratic participation, and social change. Responsive or stakeholder-centered evaluation, constructivist evaluation, deliberative democratic evaluation, and transformative evaluation all give stakeholders a central role.",
            "The authors recognize the strengths of these approaches: they engage affected groups, surface multiple value perspectives, and challenge evaluations that ignore power and injustice. These strengths make them important correctives to technocratic evaluation.",
            "The chapter also raises concerns. Extensive participation can be expensive and difficult to close; relativist assumptions can make bottom-line judgment harder; advocacy commitments can create bias risks if not checked by evidence, standards, and metaevaluation.",
            "The practical lesson is to separate legitimate value commitments from uncontrolled advocacy. A justice-oriented evaluation still needs explicit standards, defensible evidence, transparent roles, and credible reporting.",
        ],
        "concepts": ["responsive evaluation", "constructivist evaluation", "deliberative democratic evaluation", "transformative evaluation", "social justice", "stakeholder engagement", "bias control"],
        "structure": ["overview of advocacy approaches", "responsive or stakeholder-centered evaluation", "constructivist evaluation", "deliberative democratic evaluation", "transformative evaluation", "shared strengths and weaknesses"],
        "implications": ["Design stakeholder participation with clear roles and limits.", "Protect marginalized perspectives without giving up evidence standards.", "Use independent metaevaluation when advocacy commitments could be questioned."],
    },
    {
        "number": 9,
        "title": "Eclectic Evaluation Approaches",
        "part": PARTS[1],
        "pages": "247-261",
        "file": "chapter-09-eclectic-evaluation-approaches.qmd",
        "section_path": "Part Two: An Evaluation of Evaluation Approaches and Models > Chapter 9: Eclectic Evaluation Approaches",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:approach-22-utilization-focused-evaluation:c0002",
            "chunk:evaluation-theory-models-applications:approach-23-participatory-evaluation:c0014",
            "chunk:evaluation-theory-models-applications:approach-23-participatory-evaluation:c0015",
        ],
        "core": "Eclectic approaches deliberately borrow from multiple evaluation traditions to serve users and contexts, but they must still meet standards for sound evaluation.",
        "summary": [
            "Chapter 9 focuses on utilization-focused evaluation and participatory evaluation as eclectic approaches. They do not fit cleanly into quasi-evaluation, improvement-accountability, or social agenda categories because they select concepts and methods according to user needs.",
            "Utilization-focused evaluation is organized around intended users and intended uses. The evaluator works with primary users to focus questions, select methods, interpret evidence, and support use. The chapter treats this as powerful but dependent on user commitment and evaluator skill.",
            "Participatory evaluation also involves stakeholders, but it is less restricted to a predefined group of intended users. It can build ownership and capacity, while raising questions about independence, representativeness, and control over judgments.",
            "The authors' standard-based frame remains in place. Eclecticism is not permission to improvise without discipline. It is defensible only when the selected combination of methods, roles, and values can be justified against utility, feasibility, propriety, accuracy, and accountability.",
        ],
        "concepts": ["eclectic evaluation", "utilization-focused evaluation", "intended users", "intended use", "participatory evaluation", "stakeholder ownership", "evaluation standards"],
        "structure": ["definition of eclectic approaches", "utilization-focused evaluation", "participatory evaluation", "strengths and limitations", "review prompts"],
        "implications": ["Identify intended users before choosing a utilization-focused design.", "Do not let participation obscure who is accountable for quality.", "Explain why the selected mix of methods and roles fits the evaluation purpose."],
    },
    {
        "number": 10,
        "title": "Best Approaches for Twenty-first-century Evaluations",
        "part": PARTS[1],
        "pages": "265-281",
        "file": "chapter-10-best-approaches-for-twenty-first-century-evaluations.qmd",
        "section_path": "Part Two: An Evaluation of Evaluation Approaches and Models > Chapter 10: Best Approaches for Twenty-first-century Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch10-chapter-10-best-approaches-for-twenty-first-century-evaluations:c0001",
            "chunk:evaluation-theory-models-applications:the-bottom-line:c0002",
            "chunk:evaluation-theory-models-applications:overall-observations:c0003",
        ],
        "core": "Stufflebeam and Coryn use the program evaluation standards to compare selected approaches and argue that model choice should be standards-based rather than fashion-based.",
        "summary": [
            "Chapter 10 functions like a consumer report on selected evaluation approaches. The authors rate nine approaches against utility, feasibility, propriety, accuracy, evaluation accountability, and overall merit using a standards-derived checklist.",
            "The chapter is explicit about selection and judgment. The chosen approaches represent several categories, but they are not the only legitimate approaches. The ratings reflect the authors' methodology, experience, and criteria, so they should be read as a structured expert judgment rather than a universal ranking.",
            "CIPP, utilization-focused, constructivist, responsive or stakeholder-centered, and consumer-oriented approaches are among those the authors rate relatively well overall. Experimental, objectives-based, success case, and case study approaches receive more limited ratings because they often answer narrower questions or have lower utility/accountability ratings.",
            "The practical value of the chapter is its method, not only its rankings. Evaluators can adapt the standards-based rating logic to assess approaches for a particular assignment, making assumptions and tradeoffs visible before committing to a design.",
        ],
        "concepts": ["standards-based comparison", "approach rating", "utility", "feasibility", "propriety", "accuracy", "evaluation accountability", "expert judgment"],
        "structure": ["selection of approaches", "rating methodology", "comparison of approaches", "overall observations", "bottom line and caveats"],
        "implications": ["Treat approach selection as a standards-informed judgment.", "Report conflicts of interest or model loyalties when rating approaches.", "Use the checklist logic locally rather than importing rankings mechanically."],
    },
    {
        "number": 11,
        "title": "Experimental and Quasi-experimental Design Evaluations",
        "part": PARTS[2],
        "pages": "285-324",
        "file": "chapter-11-experimental-and-quasi-experimental-design-evaluations.qmd",
        "section_path": "Part Three: Explication of Selected Evaluation Approaches > Chapter 11: Experimental and Quasi-experimental Design Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:chapter-overview:c0001",
            "chunk:evaluation-theory-models-applications:chapter-overview:c0003",
            "chunk:evaluation-theory-models-applications:contemporary-concepts-associated-with-the-experimental-and-quasi-experimental-de:c0006",
        ],
        "core": "Experimental and quasi-experimental designs are valuable for causal inference when conditions fit, but they are not sufficient by themselves for many evaluation purposes.",
        "summary": [
            "Chapter 11 explains the logic of experimental and quasi-experimental design evaluations. Random assignment is the key feature of the strongest experimental designs, while quasi-experimental designs use other assignment, comparison, and measurement strategies when randomization is not feasible.",
            "The authors present these designs as part of the evaluator's repertoire, not as the universal model of evaluation. They are especially useful for estimating effects, but they can be weak on context, implementation, side effects, values, and ongoing improvement feedback.",
            "The chapter connects older scientific evaluation traditions to contemporary field trials and quasi-experimental design notation. Design elements include assignment, measurement timing, comparison groups, treatments, and validity threats.",
            "A major practical warning is that causal inference requirements can conflict with real program conditions. Evaluators must consider feasibility, ethics, stakeholder acceptance, treatment stability, and whether a narrow effect estimate will answer the evaluation's value questions.",
        ],
        "concepts": ["random assignment", "quasi-experimental design", "comparison group", "validity threat", "causal inference", "field trial", "design notation"],
        "structure": ["chapter overview", "scientific approach", "randomized field trials", "quasi-experimental concepts", "planning and execution guidelines"],
        "implications": ["Use experiments when the assignment process and intervention conditions can support them.", "Supplement effect estimates with context, process, cost, and value evidence.", "Make validity assumptions explicit before reporting causal claims."],
    },
    {
        "number": 12,
        "title": "Case Study Evaluations",
        "part": PARTS[2],
        "pages": "327-342",
        "file": "chapter-12-case-study-evaluations.qmd",
        "section_path": "Part Three: Explication of Selected Evaluation Approaches > Chapter 12: Case Study Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch12-chapter-12-case-study-evaluations:c0001",
            "chunk:evaluation-theory-models-applications:overview-of-the-chapter:c0001",
            "chunk:evaluation-theory-models-applications:particular-case-study-information-collection-methods:c0010",
        ],
        "core": "Case study evaluation provides rich, naturalistic understanding of a case, especially when evaluators need depth, context, and triangulated perspectives.",
        "summary": [
            "Chapter 12 treats case study evaluation as an in-depth, noninterventionist examination of a program, component, situation, or case in its natural setting. It is especially useful when the evaluator needs a holistic account rather than a controlled test.",
            "The chapter contrasts Stake's and Yin's contributions. Stake's approach emphasizes naturalistic, responsive understanding and the case's complexity. Yin's approach is more design-oriented and concerned with systematic case study logic for answering evaluation questions.",
            "Information collection is central. The authors discuss documents, records, observation, interviews, site visits, content analysis, and triangulation. The evaluator follows trails of interest but still needs enough discipline to support credible interpretation.",
            "The chapter also notes limits. Case studies can illuminate value and context, but they may not provide strong generalizability or confident recommendations unless designed carefully and connected to the evaluation's purpose.",
        ],
        "concepts": ["case study", "naturalistic inquiry", "noninterventionist evaluation", "Stake", "Yin", "triangulation", "content analysis", "site visit"],
        "structure": ["overview of the approach", "Stake's case study evaluation", "Yin's case study methodology", "information collection methods", "summary and prompts"],
        "implications": ["Use case studies when context and lived process matter.", "Triangulate sources and methods rather than relying on a single narrative.", "Be precise about what the case can and cannot support beyond its setting."],
    },
    {
        "number": 13,
        "title": "Daniel Stufflebeam's CIPP Model for Evaluation",
        "part": PARTS[2],
        "pages": "345-375",
        "file": "chapter-13-daniel-stufflebeams-cipp-model-for-evaluation.qmd",
        "section_path": "Part Three: Explication of Selected Evaluation Approaches > Chapter 13: Daniel Stufflebeam's CIPP Model for Evaluation: an Improvement- and Accountability-oriented Approach",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch13-chapter-13-daniel-stufflebeam-s-cipp-model-for-evaluation-an-improvement-and-acc:c0001",
            "chunk:evaluation-theory-models-applications:overview-of-the-chapter-2:c0002",
            "chunk:evaluation-theory-models-applications:philosophy-and-code-of-ethics-underlying-the-cipp-model:c0006",
            "chunk:evaluation-theory-models-applications:use-of-the-cipp-model-as-a-systems-strategy-for-improvement:c0009",
        ],
        "core": "The CIPP model links context, input, process, and product evaluation to support both improvement and accountability across a program's life cycle.",
        "summary": [
            "Chapter 13 gives the fullest account of Stufflebeam's CIPP model. The model defines evaluation as delineating, obtaining, reporting, and applying descriptive and judgmental information about an object's value, with attention to quality, worth, probity, equity, cost, efficiency, safety, and significance.",
            "The four CIPP categories organize different decision needs. Context evaluation clarifies setting, needs, problems, assets, and goals. Input evaluation assesses strategies, plans, resources, and alternatives. Process evaluation monitors implementation and costs. Product evaluation identifies intended and unintended outcomes.",
            "The current CIPP seed note belongs here because it captures the chapter's overview: CIPP is designed for formative and summative use, works across sectors, and asks evaluators to attend to stakeholders, values, standards, procedures, and systems.",
            "The standards-and-metaevaluation seed note also partly belongs here. The CIPP chapter grounds the model in professional standards, an objectivist orientation, democratic values, improvement, stakeholder service, and internal or external metaevaluation as part of responsible practice.",
        ],
        "concepts": ["CIPP", "context evaluation", "input evaluation", "process evaluation", "product evaluation", "objectivist evaluation", "systems orientation", "metaevaluation"],
        "structure": ["overview and roots", "applications", "definitions of evaluation", "CIPP categories and procedures", "philosophy and ethics", "systems strategy for improvement"],
        "implications": ["Map questions to context, input, process, and product before selecting methods.", "Use CIPP formatively and summatively rather than reducing it to an outcomes model.", "Build standards and metaevaluation into CIPP designs from the start."],
    },
    {
        "number": 14,
        "title": "Michael Scriven's Consumer-oriented Approach to Evaluation",
        "part": PARTS[2],
        "pages": "377-405",
        "file": "chapter-14-michael-scrivens-consumer-oriented-approach-to-evaluation.qmd",
        "section_path": "Part Three: Explication of Selected Evaluation Approaches > Chapter 14: Michael Scriven's Consumer-oriented Approach to Evaluation",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch14-chapter-14-michael-scriven-s-consumer-oriented-approach-to-evaluation:c0001",
            "chunk:evaluation-theory-models-applications:overview-of-scriven-s-contributions-to-evaluation:c0001",
            "chunk:evaluation-theory-models-applications:formative-and-summative-evaluation:c0002",
            "chunk:evaluation-theory-models-applications:scriven-s-look-to-evaluation-s-future:c0007",
        ],
        "core": "Scriven's consumer-oriented approach asks evaluators to act as independent value judges on behalf of consumers and public welfare.",
        "summary": [
            "Chapter 14 reviews Scriven's extensive contributions to evaluation. The authors emphasize his insistence that evaluation is fundamentally about judging value, not merely documenting objective attainment or producing value-free social science.",
            "Consumer orientation means evaluating programs, services, or products in relation to consumer needs, alternatives, costs, and wider social significance. The evaluator is expected to function as an informed surrogate consumer with strong ethical responsibility.",
            "The chapter covers formative and summative evaluation, goal-free evaluation, scoring, ranking, grading, apportioning, causal reasoning, and the Key Evaluation Checklist. These tools support Scriven's broader effort to make evaluation a disciplined transdiscipline.",
            "Scriven's approach contrasts sharply with responsive or utilization-focused traditions. It places more weight on independent judgment and defensible criteria, while still recognizing that formative evaluation can improve what will later be judged summatively.",
        ],
        "concepts": ["consumer-oriented evaluation", "surrogate consumer", "formative evaluation", "summative evaluation", "goal-free evaluation", "Key Evaluation Checklist", "transdiscipline", "value judgment"],
        "structure": ["Scriven's orientation", "critique of objectives-based evaluation", "formative and summative roles", "goal-free evaluation", "key concepts and tools", "future of evaluation"],
        "implications": ["Ask whose needs and alternatives define consumer value.", "Protect evaluator independence when a summative judgment is required.", "Use goal-free inquiry to search for unintended effects and missed criteria."],
    },
    {
        "number": 15,
        "title": "Robert Stake's Responsive or Stakeholder-centered Evaluation Approach",
        "part": PARTS[2],
        "pages": "409-435",
        "file": "chapter-15-robert-stakes-responsive-or-stakeholder-centered-evaluation-approach.qmd",
        "section_path": "Part Three: Explication of Selected Evaluation Approaches > Chapter 15: Robert Stake's Responsive or Stakeholder-centered Evaluation Approach",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch15-chapter-15-robert-stake-s-responsive-or-stakeholder-centered-evaluation-approach:c0002",
            "chunk:evaluation-theory-models-applications:stake-s-1967-countenance-of-educational-evaluation-article:c0016",
            "chunk:evaluation-theory-models-applications:stake-s-recent-rethinking-of-responsive-evaluation:c0004",
        ],
        "core": "Stake's responsive evaluation centers stakeholder concerns, program transactions, and plural value perspectives rather than fixed objectives alone.",
        "summary": [
            "Chapter 15 traces Stake's development from the countenance model to responsive or stakeholder-centered evaluation. The authors place Stake in the social agenda and advocacy tradition because his work emphasizes pluralism, interaction, local autonomy, and service to stakeholders.",
            "The countenance model focuses attention on antecedents, transactions, and outcomes, and on the difference between description and judgment. Responsive evaluation extends this by letting stakeholder issues and observed program activity shape inquiry as the evaluation unfolds.",
            "Stake's approach rejects the idea that the evaluator can always impose one final authoritative value frame. It values subjective information, stakeholder judgments, and thick descriptions of what a program is doing and how people experience it.",
            "The chapter also positions Stake in debate with Scriven. Where Scriven stresses independent consumer judgment, Stake stresses responsiveness to those involved in the program. The evaluator's professional judgment still matters, but it is exercised through interaction and interpretation.",
        ],
        "concepts": ["responsive evaluation", "stakeholder-centered evaluation", "countenance model", "antecedents", "transactions", "outcomes", "plural values", "subjective information"],
        "structure": ["Stake's evaluation philosophy", "countenance article", "responsive evaluation", "recent rethinking", "example and summary"],
        "implications": ["Begin with stakeholder concerns, but continue to broaden inquiry beyond initial requests.", "Document value differences rather than forcing premature consensus.", "Use responsive designs when program experience and local meaning are central."],
    },
    {
        "number": 16,
        "title": "Michael Patton's Utilization-focused Evaluation",
        "part": PARTS[2],
        "pages": "439-453",
        "file": "chapter-16-michael-pattons-utilization-focused-evaluation.qmd",
        "section_path": "Part Three: Explication of Selected Evaluation Approaches > Chapter 16: Michael Patton's Utilization-focused Evaluation",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch16-chapter-16-michael-patton-s-utilization-focused-evaluation:c0003",
            "chunk:evaluation-theory-models-applications:some-general-aspects-of-patton-s-utilization-focused-evaluation:c0003",
            "chunk:evaluation-theory-models-applications:planning-utilization-focused-evaluations:c0003",
            "chunk:evaluation-theory-models-applications:limitations-of-the-utilization-focused-evaluation-approach:c0005",
        ],
        "core": "Utilization-focused evaluation designs every major evaluation choice around intended users and intended uses.",
        "summary": [
            "Chapter 16 expands the utilization-focused approach introduced in Chapter 9. Patton's central claim is that evaluation should be judged by its actual usefulness to specific primary intended users for specific intended uses.",
            "The evaluator is not a detached judge in this approach. The evaluator facilitates decisions about focus, questions, values, methods, interpretation, and reporting with users who are expected to act on findings. This requires skill in group process, negotiation, values analysis, and standards.",
            "The chapter contrasts utilization-focused evaluation with responsive and constructivist approaches. It shares their attention to stakeholders, but it is more explicit about selecting primary users and building the evaluation around expected use.",
            "Limitations follow from the same strength. If intended users are poorly selected, uncommitted, unrepresentative, or unwilling to engage evidence, the evaluation can lose credibility or relevance. The approach also needs safeguards so use does not override propriety or accuracy.",
        ],
        "concepts": ["utilization-focused evaluation", "primary intended users", "intended use", "facilitation", "values negotiation", "use standards", "stakeholder commitment"],
        "structure": ["general aspects of UFE", "values and judgments", "planning UFE", "premises and methods", "limitations"],
        "implications": ["Identify primary intended users explicitly and test their commitment.", "Tie each major design decision to an intended use.", "Protect standards for evidence and propriety when users strongly shape the agenda."],
    },
    {
        "number": 17,
        "title": "Identifying and Assessing Evaluation Opportunities",
        "part": PARTS[3],
        "pages": "459-468",
        "file": "chapter-17-identifying-and-assessing-evaluation-opportunities.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 17: Identifying and Assessing Evaluation Opportunities",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch17-chapter-17-identifying-and-assessing-evaluation-opportunities:c0001",
            "chunk:evaluation-theory-models-applications:ch17-chapter-17-identifying-and-assessing-evaluation-opportunities:c0002",
        ],
        "core": "Before accepting evaluation work, evaluators should systematically identify, screen, and improve opportunities so that the assignment can be conducted credibly.",
        "summary": [
            "Chapter 17 begins the procedural part of the book. It addresses how evaluators find opportunities such as RFPs, RFQs, internal assignments, sole-source requests, evaluator-initiated opportunities, grants, contracts, and cooperative agreements.",
            "The chapter's central practical question is whether an opportunity is worth pursuing. Evaluators should consider purpose, feasibility, ethical conditions, political climate, access to information, reporting freedom, resources, timeline, and fit with their competence.",
            "Internal evaluators sometimes cannot decline assignments. The authors therefore discuss how to ameliorate weak conditions: negotiate scope, clarify standards, document limitations, protect independence where possible, and communicate risks to clients.",
            "The chapter reframes opportunity assessment as quality assurance. The earliest decision about whether and how to engage an assignment can determine whether later design, evidence collection, and reporting will be credible.",
        ],
        "concepts": ["evaluation opportunity", "RFP", "RFQ", "sole-source request", "grant", "contract", "cooperative agreement", "assignment screening"],
        "structure": ["types of opportunities", "sources of information", "questions for deciding whether to pursue", "negative assignments that cannot be declined", "practical advice"],
        "implications": ["Use a go/no-go screen before investing proposal time.", "Identify conditions that could invalidate the evaluation before accepting.", "For unavoidable assignments, document constraints and negotiate improvements."],
    },
    {
        "number": 18,
        "title": "First Steps in Addressing Evaluation Opportunities",
        "part": PARTS[3],
        "pages": "471-479",
        "file": "chapter-18-first-steps-in-addressing-evaluation-opportunities.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 18: First Steps in Addressing Evaluation Opportunities",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch18-chapter-18-first-steps-in-addressing-evaluation-opportunities:c0001",
            "chunk:evaluation-theory-models-applications:developing-the-evaluation-team:c0002",
            "chunk:evaluation-theory-models-applications:planning-for-a-stakeholder-review-panel:c0003",
        ],
        "core": "Once an opportunity is worth pursuing, evaluators need disciplined start-up work before writing or executing the evaluation design.",
        "summary": [
            "Chapter 18 covers the first operational steps after deciding to pursue an evaluation. These include defining team roles, recruiting staff and collaborators, assigning credit, clarifying the evaluation need, and obtaining institutional support.",
            "The chapter emphasizes timing. Strong proposals and evaluations require early recruitment, early drafting, early review, and enough time to satisfy institutional and human-subjects requirements. These tasks are not administrative afterthoughts.",
            "Stakeholder review panels receive specific attention. A well-composed panel can help clarify questions, improve access, review plans and draft reports, and increase relevance and credibility. A poorly composed panel can narrow perspective or create politics.",
            "The practical message is that start-up work is part of evaluation quality. The design will be weaker if the team, institutional base, standards, permissions, and stakeholder relationships are improvised late.",
        ],
        "concepts": ["evaluation team", "subcontracting", "institutional support", "human subjects review", "proposal appendix", "stakeholder review panel", "start-up activities"],
        "structure": ["team development", "recruitment", "institutional support", "human subjects requirements", "appendix materials", "stakeholder panel planning"],
        "implications": ["Define team roles and credentials before committing to the proposal.", "Secure institutional approvals and support early.", "Use stakeholder panels for review and access, not as a substitute for evaluator responsibility."],
    },
    {
        "number": 19,
        "title": "Designing Evaluations",
        "part": PARTS[3],
        "pages": "481-510",
        "file": "chapter-19-designing-evaluations.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 19: Designing Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch19-chapter-19-designing-evaluations:c0001",
            "chunk:evaluation-theory-models-applications:ch19-chapter-19-designing-evaluations:c0002",
            "chunk:evaluation-theory-models-applications:generic-checklist-for-designing-evaluations:c0003",
            "chunk:evaluation-theory-models-applications:generic-checklist-for-designing-evaluations:c0016",
        ],
        "core": "Evaluation design is an integrated set of decisions about purpose, users, questions, values, evidence, analysis, reporting, administration, and use.",
        "summary": [
            "Chapter 19 defines an evaluation design as the decision architecture required to carry out a study. It includes the evaluand, audiences, questions, values, criteria, information sources, methods, analysis, reporting, schedule, administration, and use support.",
            "The chapter uses CIPP and standards as design resources, but the generic checklist is intended to work across approaches. The design must be detailed enough to guide action while remaining adaptable when formative or responsive evaluations surface new questions.",
            "Information planning is treated as part of design, not a later methods step. Evaluators should identify sources, instruments, sampling procedures, multiple evidence points, data control, analysis assumptions, and synthesis plans before fieldwork begins.",
            "The chapter also connects design to budgeting, contracting, reporting, and use. A design that ignores resources, roles, communication, or file management is incomplete even if its methods section looks technically sound.",
        ],
        "concepts": ["evaluation design", "evaluation question", "value criteria", "information source", "sampling", "synthesis", "administration", "CIPP design"],
        "structure": ["definition and design skills", "CIPP-based example", "standards in design", "generic design checklist", "information organization and administration"],
        "implications": ["Design from intended decisions and value criteria, not from preferred methods.", "Plan analysis and synthesis before collecting information.", "Keep the design revisable when the evaluation is formative or responsive."],
    },
    {
        "number": 20,
        "title": "Budgeting Evaluations",
        "part": PARTS[3],
        "pages": "515-539",
        "file": "chapter-20-budgeting-evaluations.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 20: Budgeting Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch20-chapter-20-budgeting-evaluations:c0001",
            "chunk:evaluation-theory-models-applications:ch20-chapter-20-budgeting-evaluations:c0004",
            "chunk:evaluation-theory-models-applications:generic-checklist-for-developing-evaluation-budgets:c0001",
        ],
        "core": "Evaluation budgets are ethical and design instruments: they translate the promised scope of work into feasible, transparent, and defensible resource commitments.",
        "summary": [
            "Chapter 20 explains why budgeting is inseparable from evaluation design. A budget should estimate the resources needed to deliver the agreed design and should make assumptions about tasks, personnel, travel, support, timing, indirect costs, and sponsor contributions visible.",
            "The chapter distinguishes fixed and responsive conditions. Preordinate evaluations may support detailed up-front budgets, while responsive evaluations often need general budgets and periodic updating as user needs and interim findings develop.",
            "Ethical budgeting matters. Underbudgeting can make a promised design impossible; padding or hiding costs can undermine trust; vague agreements can produce conflict. The authors treat budgeting as part of professional integrity.",
            "The generic budgeting checklist is meant for constructing and reviewing budgets. It asks evaluators to link cost categories to design tasks, identify the needed level of detail, determine cost factors, and revisit the budget as plans become clearer.",
        ],
        "concepts": ["evaluation budget", "line-item budget", "modular budget", "cost factor", "grant", "contract", "cooperative agreement", "ethical budgeting"],
        "structure": ["budget rationale", "ethical principles", "illustrative budgets", "budget dimensions", "generic budgeting checklist"],
        "implications": ["Build the budget from tasks in the evaluation design.", "Make uncertainty explicit in responsive or evolving evaluations.", "Use the budget as a feasibility test before finalizing promises."],
    },
    {
        "number": 21,
        "title": "Contracting Evaluations",
        "part": PARTS[3],
        "pages": "541-554",
        "file": "chapter-21-contracting-evaluations.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 21: Contracting Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch21-chapter-21-contracting-evaluations:c0001",
            "chunk:evaluation-theory-models-applications:negotiating-evaluation-agreements:c0002",
            "chunk:evaluation-theory-models-applications:evaluation-contracting-checklist:c0002",
        ],
        "core": "Evaluation contracts and memoranda of agreement protect evaluation quality by making roles, rights, questions, evidence, reporting, and follow-up explicit in advance.",
        "summary": [
            "Chapter 21 ties contracting to design and budgeting. Once an evaluation design and budget are accepted, evaluator and client still need an enforceable or mutually binding agreement that governs how the evaluation will proceed.",
            "The chapter covers contracts and memoranda of agreement. It stresses that agreements should identify the evaluand, purpose, client, audiences, evaluator authority, standards, questions, information requirements, methods, analysis, reporting, schedule, budget, ownership, and follow-up responsibilities.",
            "Advance agreement is especially important for information access, stakeholder cooperation, report review, dissemination, and dealing with potentially harmful findings. These topics become much harder to negotiate after the evaluation is underway.",
            "The contracting checklist is not reproduced in the notes, but its function is central: it turns expectations into explicit commitments so that evaluation independence, feasibility, propriety, and utility are less vulnerable to later conflict.",
        ],
        "concepts": ["evaluation contract", "memorandum of agreement", "client authority", "evaluator responsibility", "reporting rights", "stakeholder cooperation", "advance agreement"],
        "structure": ["definitions", "core requirements", "rationale for advance agreements", "negotiation process", "contracting checklist"],
        "implications": ["Negotiate reporting and dissemination rights before data collection.", "Specify access, confidentiality, and stakeholder roles in writing.", "Align contract terms with the design and budget rather than treating them separately."],
    },
    {
        "number": 22,
        "title": "Collecting Evaluative Information",
        "part": PARTS[3],
        "pages": "555-579",
        "file": "chapter-22-collecting-evaluative-information.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 22: Collecting Evaluative Information",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch22-chapter-22-collecting-evaluative-information:c0001",
            "chunk:evaluation-theory-models-applications:ch22-chapter-22-collecting-evaluative-information:c0002",
            "chunk:evaluation-theory-models-applications:key-standards-for-information-collection:c0040",
            "chunk:evaluation-theory-models-applications:key-standards-for-information-collection:c0045",
        ],
        "core": "Evaluative conclusions are only as defensible as the scope, quality, reliability, validity, and management of the information collected.",
        "summary": [
            "Chapter 22 gives practical advice on information collection. It begins from standards because the credibility of answers depends on whether information is relevant, sufficient, reliable, valid, and responsibly managed.",
            "The chapter proposes a broad information framework that can cover background, context, structure, operations, costs, outputs, outcomes, side effects, and stakeholder perspectives. The goal is to avoid collecting only what is easy or familiar.",
            "Reliability and validity are treated as practical obligations. Evaluators should train collectors, document procedures, use multiple sources and methods when needed, check data quality, protect records, and report threats to validity.",
            "The chapter also recognizes feasibility. Adequate scope must be balanced against burden, time, and cost. The evaluator's job is to gather enough credible information to answer priority questions and support justified conclusions.",
        ],
        "concepts": ["evaluative information", "information scope", "reliability", "validity", "sampling", "information management", "multiple methods", "data quality"],
        "structure": ["standards for collection", "information collection framework", "sampling", "reliability and validity", "collection techniques", "information management"],
        "implications": ["Plan information collection against each evaluation question and value criterion.", "Use multiple sources when single procedures cannot carry the claim.", "Document threats to validity and the steps taken to reduce them."],
    },
    {
        "number": 23,
        "title": "Analyzing and Synthesizing Information",
        "part": PARTS[3],
        "pages": "593-624",
        "file": "chapter-23-analyzing-and-synthesizing-information.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 23: Analyzing and Synthesizing Information",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch23-chapter-23-analyzing-and-synthesizing-information:c0001",
            "chunk:evaluation-theory-models-applications:ch23-chapter-23-analyzing-and-synthesizing-information:c0002",
            "chunk:evaluation-theory-models-applications:principles-for-analyzing-and-synthesizing-information:c0002",
            "chunk:evaluation-theory-models-applications:analysis-of-qualitative-information:c0007",
        ],
        "core": "Analysis breaks evidence into interpretable findings; synthesis combines those findings with values to reach justified conclusions.",
        "summary": [
            "Chapter 23 moves from information collection to analysis, synthesis, and judgment. The evaluator must answer descriptive, relational, and causal questions, but also combine evidence into bottom-line conclusions about value.",
            "Quantitative analysis includes descriptive statistics, relational analysis, causal analysis, statistical significance, practical significance, confidence intervals, and effect sizes. The chapter emphasizes choosing methods whose assumptions fit the data and evaluation questions.",
            "Qualitative analysis is treated as systematic discovery and interpretation. Evaluators define document sets, mark records, read samples, create grounded categories, code materials, summarize findings, and track evidence so claims can be defended.",
            "Synthesis is the distinctive evaluative step. It combines findings across methods and sources, brings facts together with values, and resolves multiple value perspectives enough to support justified conclusions about merit, worth, significance, and probity.",
        ],
        "concepts": ["analysis", "synthesis", "quantitative analysis", "qualitative analysis", "practical significance", "effect size", "fact-value synthesis", "justified conclusions"],
        "structure": ["rationale for conclusion-oriented evaluation", "quantitative analysis", "qualitative analysis", "synthesis", "justified conclusions"],
        "implications": ["Choose analysis methods before collecting data when assumptions matter.", "Keep an audit trail from findings back to sources.", "Separate statistical significance from practical and evaluative significance."],
    },
    {
        "number": 24,
        "title": "Communicating Evaluation Findings",
        "part": PARTS[3],
        "pages": "625-662",
        "file": "chapter-24-communicating-evaluation-findings.qmd",
        "section_path": "Part Four: Evaluation Tasks, Procedures, and Tools > Chapter 24: Communicating Evaluation Findings",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch24-chapter-24-communicating-evaluation-findings:c0001",
            "chunk:evaluation-theory-models-applications:ch24-chapter-24-communicating-evaluation-findings:c0004",
            "chunk:evaluation-theory-models-applications:providing-interim-evaluative-feedback:c0002",
            "chunk:evaluation-theory-models-applications:providing-follow-up-support-to-enhance-an-evaluation-s-impact:c0017",
        ],
        "core": "Evaluation findings have value only when communicated to intended users in credible, timely, accessible, and follow-up-supported ways.",
        "summary": [
            "Chapter 24 argues that sound design, data collection, and analysis can still fail if findings are not communicated effectively. The evaluator must understand intended users, their information rights, their intended uses, and the formats that will support action.",
            "Communication begins before the final report. Interim feedback can help improve programs, test interpretations, surface errors, and sustain use. The chapter links this especially to approaches such as CIPP, responsive evaluation, and utilization-focused evaluation.",
            "Final reporting should synthesize findings around evaluation questions and value judgments rather than merely list methods or data sources. Reports may need different layers, formats, technical appendices, oral presentations, workshops, or other media.",
            "Follow-up support is part of evaluation impact. Evaluators may need to help users interpret findings, plan responses, communicate with stakeholders, and document actions taken while preserving the boundaries of their role.",
        ],
        "concepts": ["intended users", "interim feedback", "final report", "dissemination", "reporting rights", "follow-up support", "evaluation use"],
        "structure": ["reporting challenges", "conditions for use", "interim feedback", "final report preparation", "delivery and follow-up"],
        "implications": ["Plan report audiences and formats during design and contracting.", "Use interim feedback to support correction without compromising final judgment.", "Organize reports around questions and conclusions, not data-collection silos."],
    },
    {
        "number": 25,
        "title": "Metaevaluation: Evaluating Evaluations",
        "part": PARTS[4],
        "pages": "667-705",
        "file": "chapter-25-metaevaluation-evaluating-evaluations.qmd",
        "section_path": "Part Five: Metaevaluation and Institutionalizing and Mainstreaming Evaluation > Chapter 25: Metaevaluation: Evaluating Evaluations",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch25-chapter-25-metaevaluation-evaluating-evaluations:c0001",
            "chunk:evaluation-theory-models-applications:ch25-chapter-25-metaevaluation-evaluating-evaluations:c0002",
            "chunk:evaluation-theory-models-applications:the-role-of-context-and-resource-constraints:c0006",
            "chunk:evaluation-theory-models-applications:comparative-metaevaluations:c0003",
        ],
        "core": "Metaevaluation is the professional requirement to evaluate evaluations for improvement, accountability, and public trust.",
        "summary": [
            "Chapter 25 defines metaevaluation as evaluating evaluations. Metaevaluators can support evaluators formatively by reviewing plans, procedures, reports, and impacts, and summatively by judging the completed evaluation's utility, feasibility, propriety, accuracy, and accountability.",
            "The standards-and-metaevaluation seed note belongs here because this chapter turns standards into a direct quality-assurance process. Standards-based metaevaluation is treated as analogous to auditing in accounting: a profession should not ask society to trust its products without independent scrutiny.",
            "The chapter presents tasks, arrangements, cases, checklists, and qualifications for metaevaluation. It distinguishes metaevaluation from meta-analysis: the former judges an evaluation's quality, while the latter synthesizes results across studies.",
            "The authors also add judgment about scale and context. Not every small local improvement study needs an independent metaevaluation, but high-stakes, public, controversial, or widely used evaluations require stronger review.",
        ],
        "concepts": ["metaevaluation", "formative metaevaluation", "summative metaevaluation", "standards-based review", "evaluation accountability", "meta-analysis", "comparative metaevaluation"],
        "structure": ["rationale and definition", "standards and caveats", "responsibilities", "tasks and checklists", "cases and comparative metaevaluation", "context and constraints"],
        "implications": ["Decide metaevaluation intensity based on stakes, audience, and risk.", "Use standards to review plans before flaws become final findings.", "Report limitations and quality judgments transparently."],
    },
    {
        "number": 26,
        "title": "Institutionalizing and Mainstreaming Evaluation",
        "part": PARTS[4],
        "pages": "707-725",
        "file": "chapter-26-institutionalizing-and-mainstreaming-evaluation.qmd",
        "section_path": "Part Five: Metaevaluation and Institutionalizing and Mainstreaming Evaluation > Chapter 26: Institutionalizing and Mainstreaming Evaluation",
        "evidence_ids": [
            "chunk:evaluation-theory-models-applications:ch26-chapter-26-institutionalizing-and-mainstreaming-evaluation:c0001",
            "chunk:evaluation-theory-models-applications:overview-of-the-remainder-of-the-chapter:c0001",
            "chunk:evaluation-theory-models-applications:checklist-for-use-in-institutionalizing-and-mainstreaming-evaluation:c0025",
        ],
        "core": "Organizations should move evaluation from occasional projects to a mainstreamed system for planning, accountability, learning, and improvement.",
        "summary": [
            "Chapter 26 closes the book by shifting from individual evaluation studies to organizational evaluation systems. The authors argue that organizations should institutionalize and mainstream evaluation so that it becomes part of routine governance and improvement.",
            "Institutionalizing evaluation means establishing a durable system, roles, standards, policies, resources, and review mechanisms. Mainstreaming evaluation means embedding use of that system across levels and functions rather than leaving evaluation in a specialist corner.",
            "The chapter reviews the book's themes and translates them into organizational principles. Evaluation systems should be grounded in theory, standards, stakeholder engagement, sound methods, metaevaluation, communication, and systematic use.",
            "A central practical tool is a checklist for establishing or strengthening an organizational evaluation system. The notes do not reproduce the checklist, but they treat it as a staged planning aid for design teams, review teams, standards selection, communication, capacity building, and periodic review.",
        ],
        "concepts": ["institutionalizing evaluation", "mainstreaming evaluation", "evaluation system", "design team", "review team", "organizational standards", "capacity building", "periodic review"],
        "structure": ["review of book themes", "definitions and rationale", "early efforts and advances", "principles", "institutionalization checklist", "conclusions"],
        "implications": ["Treat evaluation capacity as an organizational system, not a series of ad hoc studies.", "Assign responsibility for standards, review, communication, and use.", "Periodically evaluate the evaluation system itself and revise it."],
    },
]


def wrap(text: str) -> str:
    return textwrap.dedent(text).strip() + "\n"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(rel: str, payload: dict) -> None:
    write_text(rel, json.dumps(payload, indent=2) + "\n")


def yaml_list(items: list[str]) -> str:
    return "\n".join(f'  - "{item}"' for item in items)


def metadata(extra: list[str]) -> str:
    spans = "".join(f"<span>{item}</span>" for item in [YEAR, "MCP evaluation-texts", f"Status: {SOURCE_STATUS}", *extra])
    return f'<div class="chapter-meta">{spans}</div>'


def chapter_link(chapter: dict) -> str:
    return f"[Chapter {chapter['number']}: {chapter['title']}]({chapter['file']})"


def sentence_join(items: list[str], limit: int = 4) -> str:
    selected = items[:limit]
    if len(selected) == 1:
        return selected[0]
    return ", ".join(selected[:-1]) + f", and {selected[-1]}"


def render_reading_note(chapter: dict) -> str:
    concepts = sentence_join(chapter["concepts"], 4)
    structure = sentence_join(chapter["structure"], 3)
    return (
        f"For close reading, track how the chapter uses {concepts} while moving through "
        f"{structure}. The notes below treat those moves as study scaffolding: they identify "
        "what the chapter asks the evaluator to notice, what judgment problem it helps solve, "
        "and what should be checked against the saved evidence records before relying on the "
        "summary in applied work."
    )


def render_book_connection(chapter: dict) -> str:
    number = chapter["number"]
    if number <= 3:
        return (
            "Within the wider book, this chapter belongs to the foundations that make later model "
            "ratings and procedural guidance intelligible. It supplies vocabulary for judging "
            "approaches, reading standards, and distinguishing evaluation from narrower forms of "
            "measurement, monitoring, research, or administrative review."
        )
    if number <= 10:
        return (
            "Within Part Two, this chapter should be read as part of Stufflebeam and Coryn's "
            "standards-based assessment of evaluation approaches. Its classifications and ratings "
            "are their judgments about how well each approach supports defensible evaluation, not a "
            "neutral consensus ranking of the whole field."
        )
    if number <= 16:
        return (
            "Within Part Three, this chapter turns a named approach into a design option. The issue "
            "for study is not whether the model has a memorable label, but which evaluation tasks "
            "it handles well, what ethical stance it implies, and where it needs supplementation by "
            "standards, mixed methods, or metaevaluation."
        )
    if number <= 24:
        return (
            "Within Part Four, this chapter shifts attention from approach selection to execution. "
            "It is most useful when read as procedural guidance that still depends on earlier "
            "choices about purpose, standards, users, evaluand boundaries, and the kind of value "
            "judgment the evaluation must support."
        )
    return (
        "Within Part Five, this chapter asks how evaluation itself is judged, governed, and made "
        "durable. It connects the book's standards language to organizational routines so that "
        "evaluation quality is not left to isolated projects or individual evaluator preference."
    )


def render_chapter(chapter: dict, prev_chapter: dict | None, next_chapter: dict | None) -> str:
    evidence_ids = chapter["evidence_ids"]
    body = [
        "---",
        f'title: "Chapter {chapter["number"]:02d}: {chapter["title"]}"',
        f'description: "Detailed study notes for Chapter {chapter["number"]} of {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Chapter"',
        f'chapter_number: {chapter["number"]}',
        f'part: "{chapter["part"]}"',
        f'source_pages: "{chapter["pages"]}"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence_ids),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        metadata([chapter["part"], f"Chapter {chapter['number']}", f"Source pages {chapter['pages']}"]),
        "",
        f"This note summarises Chapter {chapter['number']}, \"{chapter['title']},\" from {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. It is a paraphrased study note based on source-linked MCP research-library retrieval records, not a substitute for the chapter.",
        "",
        "Evidence records used in the chapter draft:",
        "",
        *[f"- `{evidence_id}`" for evidence_id in evidence_ids],
        "",
        "These records identify the retrieval trail for review. The note paraphrases the chapter's argument and procedures, and it does not reproduce textbook tables, review questions, checklists, exhibits, or extended passages. When a checklist or table is central, the note describes its function and leaves the source artifact in the evidence record.",
        "",
        "## Core Argument",
        "",
        chapter["core"],
        "",
        "## Study Summary",
        "",
        *sum(([paragraph, ""] for paragraph in chapter["summary"]), []),
        render_reading_note(chapter),
        "",
        render_book_connection(chapter),
        "",
        "## Key Concepts",
        "",
        *[
            f"- {concept}: use this term as a study handle for how the chapter frames evaluation design, judgment, evidence, quality, or use."
            for concept in chapter["concepts"]
        ],
        "",
        "## Chapter Structure",
        "",
        *[f"- {item.capitalize()}." for item in chapter["structure"]],
        "",
        "## Practical Implications",
        "",
        *[f"- {item}" for item in chapter["implications"]],
        "",
        "## Connections",
        "",
        f"- Book overview: [Overview](index.qmd)",
        f"- Reading route: [Chapter Map](chapter-map.qmd)",
        f"- Concepts synthesis: [Core Concepts](concepts.qmd)",
        f"- Practice synthesis: [Practice Implications](practice-implications.qmd)",
    ]
    if prev_chapter:
        body.append(f"- Previous: {chapter_link(prev_chapter)}")
    if next_chapter:
        body.append(f"- Next: {chapter_link(next_chapter)}")
    if chapter["number"] == 2:
        body.append("- Seed note folded in: [Program Evaluation Standards and Theory Development](section-01-evaluation-theory-development.qmd)")
    if chapter["number"] == 13:
        body.append("- Seed note folded in: [CIPP Model Overview](section-02-cipp-overview.qmd)")
        body.append("- Related seed note: [Standards and Metaevaluation](section-03-standards-and-metaevaluation.qmd)")
    if chapter["number"] == 25:
        body.append("- Related seed note: [Standards and Metaevaluation](section-03-standards-and-metaevaluation.qmd)")
    body.extend(
        [
            "",
            "## Study Prompts",
            "",
            f"1. What value problem does Chapter {chapter['number']} help an evaluator diagnose?",
            "2. Which assumptions would need evidence before applying this chapter in a live evaluation?",
            "3. How would this chapter change the way an evaluator scopes questions, methods, reporting, or use?",
            "4. Where could the guidance be misused if treated as a fixed template?",
            "",
            "## References",
            "",
            f"- Stufflebeam, D. L., & Coryn, C. L. S. ({YEAR}). *{FULL_TITLE}*. {PUBLISHER}. Chapter {chapter['number']}, pages {chapter['pages']}.",
            f"- Saved retrieval metadata: `data/research-library/evidence/{SLUG}/chapter-evidence-summary.json`.",
            "",
        ]
    )
    return "\n".join(body)


def render_index() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    lines = [
        "---",
        f'title: "{TITLE}"',
        f'description: "Book overview and chapter study-note index for {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Book"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        '<div class="landing-stack">',
        "",
        "::: {.landing-hero}",
        '<span class="hero-eyebrow">Book notes</span>',
        "",
        f"# {TITLE}",
        "",
        f"Study notes on *{FULL_TITLE}* [@{CITATION}]. These chapter notes are generated from source-linked MCP research-library records and are intended for study, comparison, and later refinement.",
        "",
        '<div class="page-metadata">',
        "  <span>26 chapter notes</span>",
        f"  <span>{YEAR}</span>",
        f"  <span>Source status: {SOURCE_STATUS}</span>",
        "  <span>MCP evaluation-texts</span>",
        "</div>",
        ":::",
        "",
        "::: {.section-grid}",
        "::: {.section-card}",
        '<span class="page-badge badge-synthesis">Synthesis</span>',
        "",
        "### [Core Concepts](concepts.qmd)",
        "",
        "Recurring ideas and distinctions used across these chapter notes.",
        ":::",
        "",
        "::: {.section-card}",
        '<span class="page-badge badge-map">Map</span>',
        "",
        "### [Chapter Map](chapter-map.qmd)",
        "",
        "Full part-by-part reading route for all 26 chapters.",
        ":::",
        "",
        "::: {.section-card}",
        '<span class="page-badge badge-practice">Practice</span>',
        "",
        "### [Practice Implications](practice-implications.qmd)",
        "",
        "Practical evaluation design habits drawn from the full chapter set.",
        ":::",
        ":::",
        "",
        "</div>",
        "",
        "## Source",
        "",
        metadata(["Book overview", "Chapter route"]),
        "",
        f"This index summarises generated study notes for {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. The generated pages use selected MCP research-library retrieval records and compact evidence summaries.",
        "",
        "## Core Argument",
        "",
        "Evaluation approaches should be chosen, adapted, and judged by their contribution to defensible value judgments, practical improvement, accountability, standards compliance, and use.",
        "",
        "## Chapter Notes",
        "",
    ]
    for part in PARTS:
        lines.extend([f"### {part}", ""])
        for chapter in [item for item in CHAPTERS if item["part"] == part]:
            lines.append(f"- {chapter_link(chapter)} - source pages {chapter['pages']}")
        lines.append("")
    lines.extend(
        [
            "## Seed Major-Section Notes",
            "",
            "These earlier generated notes are retained for link stability and as topical extracts.",
            "",
            "- [Program Evaluation Standards and Theory Development](section-01-evaluation-theory-development.qmd) - folded into Chapter 2",
            "- [CIPP Model Overview](section-02-cipp-overview.qmd) - folded into Chapter 13",
            "- [Standards and Metaevaluation](section-03-standards-and-metaevaluation.qmd) - folded into Chapters 13 and 25",
            "",
            "## References",
            "",
        ]
    )
    return "\n".join(lines)


def render_chapter_map() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    lines = [
        "---",
        f'title: "{TITLE} Chapter Map"',
        f'description: "Full reading map for {TITLE} chapter notes."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Map"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        f"This map uses selected MCP research-library sections from *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Reading Route",
        "",
    ]
    for part in PARTS:
        lines.extend([f"### {part}", ""])
        for chapter in [item for item in CHAPTERS if item["part"] == part]:
            lines.append(f"- {chapter_link(chapter)} - pages {chapter['pages']}; `{chapter['section_path']}`")
        lines.append("")
    lines.extend(
        [
            "## How to Use This Map",
            "",
            "- Start with Part One to ground definitions, standards, and theory.",
            "- Use Part Two to compare evaluation approaches and understand the authors' standards-based judgments.",
            "- Use Part Three when choosing among selected models such as CIPP, consumer-oriented, responsive, or utilization-focused evaluation.",
            "- Use Part Four as a procedural guide for scoping, designing, budgeting, contracting, collecting, analyzing, reporting, and follow-up.",
            "- Use Part Five to check evaluation quality and organizational evaluation capacity.",
            "",
            "## Seed Notes",
            "",
            "- [Program Evaluation Standards and Theory Development](section-01-evaluation-theory-development.qmd)",
            "- [CIPP Model Overview](section-02-cipp-overview.qmd)",
            "- [Standards and Metaevaluation](section-03-standards-and-metaevaluation.qmd)",
            "",
            "## References",
            "",
        ]
    )
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    concept_groups = [
        ("Value and Judgment", ["merit and worth", "probity", "value criteria", "justified conclusions", "consumer needs"]),
        ("Standards and Accountability", ["utility", "feasibility", "propriety", "accuracy", "evaluation accountability", "metaevaluation"]),
        ("Approach Families", ["pseudoevaluation", "quasi-evaluation", "improvement and accountability", "social agenda and advocacy", "eclectic evaluation"]),
        ("Selected Models", ["CIPP", "consumer-oriented evaluation", "responsive evaluation", "utilization-focused evaluation", "case study evaluation", "experimental design evaluation"]),
        ("Evaluation Process", ["opportunity assessment", "evaluation design", "budgeting", "contracting", "information collection", "analysis and synthesis", "communication and use"]),
    ]
    lines = [
        "---",
        f'title: "Core Concepts in {TITLE}"',
        f'description: "Synthesis note on recurring concepts in {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Synthesis"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        f"This synthesis draws across the chapter notes for *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Central Logic",
        "",
        "The book treats evaluation as a standards-guided practice for producing defensible judgments of value and helping users improve programs, make decisions, and meet accountability obligations.",
        "",
        "## Concepts",
        "",
    ]
    for heading, concepts in concept_groups:
        lines.extend([f"### {heading}", ""])
        for concept in concepts:
            lines.append(f"- {concept}: a recurring idea used to frame evaluation design, evidence, interpretation, quality, or use.")
        lines.append("")
    lines.extend(["## Links", ""])
    for chapter in CHAPTERS:
        lines.append(f"- {chapter_link(chapter)}")
    lines.extend(["", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    implications = [
        "Start every evaluation by clarifying the evaluand, users, purposes, value criteria, standards, and intended uses.",
        "Choose models by fit to the assignment and standards, not by brand familiarity or method preference.",
        "Distinguish focused studies from full evaluations of merit and worth, especially when using quasi-evaluation approaches.",
        "Build standards into design, budgeting, contracting, information collection, reporting, and metaevaluation.",
        "Use multiple sources and methods when a single procedure cannot support the required judgment.",
        "Treat analysis and synthesis as value work: evidence must be connected to criteria before conclusions are justified.",
        "Plan communication and follow-up early so findings reach intended users in forms they can use.",
        "Use metaevaluation proportionate to stakes, risk, and public reliance on the evaluation.",
        "For organizations, move from ad hoc studies toward mainstreamed evaluation systems with periodic review.",
    ]
    lines = [
        "---",
        f'title: "{TITLE} Practice Implications"',
        f'description: "Practice synthesis for {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Practice"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        f"This practice synthesis draws on the chapter notes from *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Evaluation Practice Implications",
        "",
        *[f"- {item}" for item in implications],
        "",
        "## Applying the Notes",
        "",
        "Use these implications as checks during scoping, proposal decisions, design review, method selection, reporting, follow-up, and metaevaluation. They should be adapted to the evaluation's context, available resources, stakeholder needs, and standards obligations.",
        "",
        "## Links",
        "",
        *[f"- {chapter_link(chapter)}" for chapter in CHAPTERS],
        "",
        "## References",
        "",
    ]
    return "\n".join(lines)


def render_evidence_summary() -> dict:
    return {
        "schema_version": "1.0",
        "generated_at": "2026-06-25",
        "collection_id": COLLECTION_ID,
        "book_id": BOOK_ID,
        "book_title": TITLE,
        "source_status": SOURCE_STATUS,
        "rag_status": RAG_STATUS,
        "source_tool": "mcp__researchlibrary.rag_evidence_pack",
        "copyright_note": "Stores retrieval IDs and source locations only; source text is not duplicated.",
        "records": [
            {
                "section_id": f"chapter-{chapter['number']:02d}",
                "section_title": f"Chapter {chapter['number']}: {chapter['title']}",
                "source_pages": chapter["pages"],
                "section_path": chapter["section_path"],
                "evidence_ids": chapter["evidence_ids"],
                "target_path": f"notes/{SLUG}/{chapter['file']}",
            }
            for chapter in CHAPTERS
        ],
    }


def render_chapter_evidence_summary() -> dict:
    return {
        "schema_version": "1.0",
        "generated_at": "2026-06-25",
        "collection_id": COLLECTION_ID,
        "book_id": BOOK_ID,
        "book_title": TITLE,
        "source_status": SOURCE_STATUS,
        "source_tool": "mcp__researchlibrary.rag_evidence_pack",
        "evidence_pack_defaults": {
            "include_neighbors": True,
            "limit": "8-12",
            "include_media": "only where central tables, checklists, figures, or exhibits are needed",
        },
        "chapters": [
            {
                "chapter_number": chapter["number"],
                "chapter_title": chapter["title"],
                "target_path": f"notes/{SLUG}/{chapter['file']}",
                "section_paths": [chapter["section_path"]],
                "source_pages": chapter["pages"],
                "evidence_ids": chapter["evidence_ids"],
                "media_ids": [],
                "status": "drafted",
            }
            for chapter in CHAPTERS
        ],
    }


def update_manifest() -> None:
    path = ROOT / "data" / "research_library_notes_manifest.json"
    manifest = read_json(path)
    for book in manifest.get("books", []):
        if book.get("book_id") == BOOK_ID:
            book.update(
                {
                    "generation_mode": "generated-chapter-notes",
                    "target_path": f"notes/{SLUG}/index.qmd",
                    "sections": [
                        {
                            "id": f"chapter-{chapter['number']:02d}",
                            "title": f"Chapter {chapter['number']}: {chapter['title']}",
                            "source_pages": chapter["pages"],
                            "section_path": chapter["section_path"],
                            "evidence_ids": chapter["evidence_ids"],
                            "target_path": f"notes/{SLUG}/{chapter['file']}",
                        }
                        for chapter in CHAPTERS
                    ],
                }
            )
            break
    else:
        raise SystemExit(f"{BOOK_ID} not found in manifest")
    write_json("data/research_library_notes_manifest.json", manifest)


def generate() -> None:
    base = f"notes/{SLUG}"
    for idx, chapter in enumerate(CHAPTERS):
        prev_chapter = CHAPTERS[idx - 1] if idx else None
        next_chapter = CHAPTERS[idx + 1] if idx + 1 < len(CHAPTERS) else None
        write_text(f"{base}/{chapter['file']}", render_chapter(chapter, prev_chapter, next_chapter))
    write_text(f"{base}/index.qmd", render_index())
    write_text(f"{base}/chapter-map.qmd", render_chapter_map())
    write_text(f"{base}/concepts.qmd", render_concepts())
    write_text(f"{base}/practice-implications.qmd", render_practice())
    write_json(f"data/research-library/evidence/{SLUG}/evidence-summary.json", render_evidence_summary())
    write_json(f"data/research-library/evidence/{SLUG}/chapter-evidence-summary.json", render_chapter_evidence_summary())
    update_manifest()


if __name__ == "__main__":
    generate()
