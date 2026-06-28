#!/usr/bin/env python3
"""Generate step-level Patton utilization-focused evaluation study notes."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "essentials-utilization-focused-evaluation"
SLUG = BOOK_ID
TITLE = "Essentials of Utilization-Focused Evaluation"
FULL_TITLE = TITLE
AUTHORS = "Michael Quinn Patton"
CITATION = "patton_2012_essentials_utilization_focused_evaluation"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2012"
PUBLISHER = "SAGE Publications"
GENERATED_AT = "2026-06-28"


LEGACY_EXTRACTS = [
    ("Utilization-Focused Evaluation Overview", "section-01-utilization-focused-overview.qmd"),
    ("The 17-Step Utilization-Focused Checklist", "section-02-seventeen-steps.qmd"),
    ("Negotiating Methods for Intended Use", "section-03-methods-for-use.qmd"),
]


CONCEPT_GLOSSES = {
    "adaptive use": "Ongoing adjustment of evaluation questions, methods, communication, or follow-up as users, evidence, and context change.",
    "analysis": "Organizing and reducing data so primary intended users can see patterns, evidence, and implications.",
    "attribution": "Reasoned inquiry into whether observed outcomes can credibly be connected to the program or intervention.",
    "credibility": "The degree to which intended users judge evaluation evidence, methods, and interpretation as trustworthy enough for their uses.",
    "decision-oriented use": "Instrumental use focused on a specific forthcoming choice, action, or allocation decision.",
    "developmental evaluation": "Evaluation use oriented to learning and adaptation in complex, emergent, or innovative settings.",
    "dissemination": "Communication of major findings beyond primary intended users to expand influence without confusing spread with actual use.",
    "evaluation facilitation": "The evaluator role of helping intended users clarify, negotiate, interpret, and act throughout the evaluation.",
    "evaluation questions": "Priority questions that focus inquiry on what intended users need to know and can act on.",
    "evaluative thinking": "A disciplined habit of asking evidence-informed questions, making criteria explicit, and learning from results.",
    "findings use": "Use of evaluation results, interpretations, judgments, or recommendations after data have been gathered.",
    "follow-up": "Post-report support that keeps findings in front of users, adapts communication, and helps facilitate actual use.",
    "implementation": "The program operations, delivery, participation, and context that must be understood before judging outcomes.",
    "intended use": "The specific way evaluation process or findings are expected to inform decisions, learning, action, or influence.",
    "methods negotiation": "Joint selection and adaptation of methods so rigor, feasibility, credibility, and intended use fit together.",
    "metaevaluation": "Evaluation of an evaluation, with emphasis here on whether utility, use, and professional standards were achieved.",
    "personal factor": "The importance of specific people who care about, understand, and are positioned to use evaluation.",
    "primary intended users": "Named people expected to use the evaluation and participate in major focus, design, interpretation, and use decisions.",
    "process use": "Learning, capacity building, shared understanding, or behavior change that occurs through participation in the evaluation process.",
    "program readiness": "The organizational willingness, capacity, incentives, and context needed to support useful evaluation.",
    "reporting": "Purposeful presentation of findings in formats, timing, and venues designed to facilitate use.",
    "simulation": "A rehearsal of likely findings, interpretations, and decisions before data collection to test utility and design fit.",
    "situation analysis": "Joint inquiry into context, politics, stakeholders, risks, and forces that may support or constrain evaluation use.",
    "theory of change": "The intervention model or causal logic being evaluated and used to connect implementation, outcomes, and attribution.",
    "utilization-focused evaluation": "An evaluation approach judged by intended use by intended users, with methods and facilitation fitted to that use.",
}


SECTIONS = [
    {
        "id": "introduction",
        "kind": "Introduction",
        "number": 0,
        "title": "Introduction, Overview, and Context",
        "pages": "27-37",
        "file": "introduction-overview-and-context.qmd",
        "section_path": "Introduction, Overview, and Context",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:ch-introduction-overview-and-context:c0007",
            "chunk:essentials-utilization-focused-evaluation:ch-introduction-overview-and-context:c0026",
            "chunk:essentials-utilization-focused-evaluation:ch-introduction-overview-and-context:c0027",
        ],
        "media_ids": [],
        "core": "The book frames utilization-focused evaluation as a checklist of essentials that must be managed as an adaptive, nonlinear practice centered on intended use by intended users.",
        "summary": [
            "The introduction positions utilization-focused evaluation as a practical approach rather than a preferred method. The central test is whether an evaluation is designed and facilitated so specific users can use the process and findings.",
            "Patton presents the book as a 17-step checklist because evaluators need a manageable sequence for planning and carrying out the work. At the same time, he warns that real evaluations are not mechanical sequences; readiness, users, uses, politics, methods, interpretation, and follow-up interact throughout.",
            "The introductory section therefore establishes two reading lenses. The checklist helps proposal writing, planning, management, and quality review. The complex dynamic systems lens keeps the evaluator alert to feedback loops, adaptations, and changing conditions.",
            "For study purposes, this introduction should be read as the control logic for the rest of the book: every later step asks what will make this evaluation more likely to be useful and actually used.",
        ],
        "concepts": ["utilization-focused evaluation", "intended use", "primary intended users", "adaptive use", "evaluation facilitation"],
        "structure": ["U-FE premise", "17-step checklist", "intended use by intended users", "complex dynamic systems interludes", "practice exercises"],
        "implications": ["Treat use as a design criterion from the beginning.", "Use the checklist for planning while expecting iteration and feedback.", "Name users and uses before making methods or reporting decisions."],
        "group": "Foundations",
    },
    {
        "id": "step-01",
        "kind": "Step",
        "number": 1,
        "title": "Assess and Build Program and Organizational Readiness for Utilization-Focused Evaluation",
        "pages": "39-59",
        "file": "step-01-assess-and-build-program-and-organizational-readiness.qmd",
        "section_path": "Step 1: Assess and Build Program and Organizational Readiness for Utilization-Focused Evaluation",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step01-step-1-assess-and-build-program-and-organizational-readiness-for-utilization-foc:c0011",
            "chunk:essentials-utilization-focused-evaluation:step01-step-1-assess-and-build-program-and-organizational-readiness-for-utilization-foc:c0045",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0001",
        ],
        "media_ids": [],
        "core": "A useful evaluation starts by testing and strengthening whether the organization is ready to engage in evaluation for real use.",
        "summary": [
            "Step 1 treats readiness as an evaluable condition. Before promising utility, the evaluator has to understand how the organization has used data and evaluation in the past, what anxieties or resistance are present, and what incentives support or weaken use.",
            "The step is also developmental. Readiness is not only a gatekeeping judgment; it can be built by helping people articulate a positive vision of useful evaluation, surface barriers, and connect the work to standards, values, and real decisions.",
            "The chapter makes organizational context part of evaluation design. If the setting lacks time, legitimacy, trust, or commitment to use, methods alone will not make findings influential.",
            "The step links directly to later situation analysis and metaevaluation because readiness affects who can participate, what uses are credible, what evidence will be trusted, and how follow-up will be supported.",
        ],
        "concepts": ["program readiness", "utilization-focused evaluation", "evaluative thinking", "intended use", "evaluation facilitation"],
        "structure": ["baseline assessment of evaluation use", "evaluation associations and history", "positive vision for use", "incentives and barriers", "standards and readiness building"],
        "implications": ["Diagnose organizational evaluation history before scoping the study.", "Use readiness conversations to build capacity, not only screen feasibility.", "Record barriers to use as design constraints."],
        "group": "Foundations",
    },
    {
        "id": "step-02",
        "kind": "Step",
        "number": 2,
        "title": "Assess and Enhance Evaluator Readiness and Competence to Undertake a Utilization-Focused Evaluation",
        "pages": "60-83",
        "file": "step-02-assess-and-enhance-evaluator-readiness.qmd",
        "section_path": "Step 2: Assess and Enhance Evaluator Readiness and Competence to Undertake a Utilization-Focused Evaluation",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step02-step-2-assess-and-enhance-evaluator-readiness-and-competence-to-undertake-a-util:c0013",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0003",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-and-2-complex-dynamic-systems-interconnections-assessing-the-m:c0001",
        ],
        "media_ids": [],
        "core": "The evaluator must be ready to facilitate use, negotiate methods pragmatically, and work with people as well as evidence.",
        "summary": [
            "Step 2 turns the readiness question back on the evaluator. Utilization-focused evaluation requires technical competence, but also facilitation skill, humility, political judgment, and willingness to adapt methods to use.",
            "The chapter emphasizes utilization-focused pragmatism. The evaluator should know enough methods to choose appropriately, but should not let a favorite method define the evaluation before users and uses are clear.",
            "Evaluator readiness includes role clarity. A U-FE evaluator facilitates decisions with users without becoming the unilateral decision maker about purposes, methods, interpretation, or recommendations.",
            "The interlude after Steps 1 and 2 reinforces that organizational readiness and evaluator readiness interact. A technically strong evaluator may still fail if the setting is not ready, and a ready setting still needs an evaluator able to facilitate use.",
        ],
        "concepts": ["evaluation facilitation", "methods negotiation", "credibility", "adaptive use", "utilization-focused evaluation"],
        "structure": ["evaluator stance", "technical competence", "facilitation competence", "role negotiation", "readiness interconnections"],
        "implications": ["Assess evaluator fit before accepting a U-FE assignment.", "Make methodological preferences explicit so they do not dominate use decisions.", "Develop facilitation capacity alongside technical capacity."],
        "group": "Foundations",
    },
    {
        "id": "step-03",
        "kind": "Step",
        "number": 3,
        "title": "Identify, Organize, and Engage Primary Intended Users: The Personal Factor",
        "pages": "84-109",
        "file": "step-03-identify-organize-and-engage-primary-intended-users.qmd",
        "section_path": "Step 3: Identify, Organize, and Engage Primary Intended Users: The Personal Factor",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step03-step-3-identify-organize-and-engage-primary-intended-users-the-personal-factor:c0009",
            "chunk:essentials-utilization-focused-evaluation:step03-step-3-identify-organize-and-engage-primary-intended-users-the-personal-factor:c0034",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-2-and-3-complex-dynamic-systems-interconnections-assessing-the:c0001",
        ],
        "media_ids": [],
        "core": "Use depends on specific people, so the evaluator must identify and engage primary intended users who can influence decisions and stay involved.",
        "summary": [
            "Step 3 introduces the personal factor as a central explanation for evaluation use. Evaluations are more likely to matter when named users care about the work, understand it, and are positioned to act on it.",
            "The chapter distinguishes broad stakeholders from primary intended users. Many people may have an interest in the program, but U-FE requires a manageable group that will participate in focus, design, interpretation, and use decisions.",
            "Engagement is not tokenistic. Intended users must be organized, supported, and kept involved through turnover, politics, and competing agendas so that later decisions remain connected to actual use.",
            "The interlude shows how Steps 1, 2, and 3 can reorder in practice. Sometimes identifying users comes first, then evaluator selection and readiness building follow, illustrating the adaptive sequence of real U-FE work.",
        ],
        "concepts": ["primary intended users", "personal factor", "intended use", "evaluation facilitation", "adaptive use"],
        "structure": ["stakeholder distinction", "primary user selection", "engagement strategy", "turnover and continuity", "readiness interconnections"],
        "implications": ["Name primary intended users, not only stakeholder categories.", "Keep the core user group manageable enough for real involvement.", "Plan for turnover and political dynamics from the start."],
        "group": "User and Use Focus",
    },
    {
        "id": "step-04",
        "kind": "Step",
        "number": 4,
        "title": "Situation Analysis Conducted Jointly With Primary Intended Users",
        "pages": "110-135",
        "file": "step-04-situation-analysis-with-primary-intended-users.qmd",
        "section_path": "Step 4: Situation Analysis Conducted Jointly With Primary Intended Users",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step04-step-4-situation-analysis-conducted-jointly-with-primary-intended-users:c0008",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-4-complex-dynamic-systems-interconnections-assessing-t:c0001",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0008",
        ],
        "media_ids": [],
        "core": "Situation analysis makes context, politics, risks, resources, and forces affecting use explicit before the evaluation design hardens.",
        "summary": [
            "Step 4 moves from people to context. Primary intended users and the evaluator jointly analyze the situation in which the evaluation will occur, including political stakes, organizational constraints, available resources, and forces supporting or constraining use.",
            "Tools such as force-field analysis help users move beyond vague awareness of context. The point is to turn context into design intelligence: what must be reinforced, negotiated, protected, or avoided for use to be plausible.",
            "The chapter keeps situation analysis connected to readiness and engagement. A useful evaluation requires alignment among organizational conditions, evaluator role, intended users, and expected uses.",
            "The interlude after Step 4 treats the first four steps as an interacting cluster. Readiness, evaluator capacity, user engagement, and situation analysis should be revisited as conditions change.",
        ],
        "concepts": ["situation analysis", "primary intended users", "program readiness", "adaptive use", "intended use"],
        "structure": ["context scan", "political analysis", "force-field analysis", "risk and resources", "alignment among early steps"],
        "implications": ["Conduct situation analysis with users, not as a private evaluator exercise.", "Translate contextual risks into design and facilitation choices.", "Revisit early readiness judgments as new political information emerges."],
        "group": "User and Use Focus",
    },
    {
        "id": "step-05",
        "kind": "Step",
        "number": 5,
        "title": "Identify and Prioritize Primary Intended Uses by Determining Priority Purposes",
        "pages": "136-162",
        "file": "step-05-identify-and-prioritize-primary-intended-uses.qmd",
        "section_path": "Step 5: Identify and Prioritize Primary Intended Uses by Determining Priority Purposes",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step05-step-5-identify-and-prioritize-primary-intended-uses-by-determining-priority-pur:c0004",
            "chunk:essentials-utilization-focused-evaluation:step05-step-5-identify-and-prioritize-primary-intended-uses-by-determining-priority-pur:c0035",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-5-complex-dynamic-systems-interconnections-focusing-on:c0001",
        ],
        "media_ids": [],
        "core": "The evaluation must prioritize intended uses and purposes so design choices do not drift into trying to serve everything at once.",
        "summary": [
            "Step 5 asks what the evaluation is for. Patton distinguishes alternative purposes such as summative judgment, formative improvement, accountability, monitoring, knowledge generation, and developmental evaluation.",
            "The chapter treats these purposes as menu choices rather than automatic add-ons. Users may want several things, but the evaluator has to help them prioritize because each purpose implies different questions, stakes, timing, evidence, and communication needs.",
            "Identifying intended uses is tightly connected to identifying intended users. Use is not an abstract virtue; it is a claim that specific people will do something with process or findings.",
            "The interlude after Step 5 shows that intended uses integrate the preceding steps. Readiness, evaluator competence, user engagement, and situation analysis all shape which uses are realistic and worth prioritizing.",
        ],
        "concepts": ["intended use", "decision-oriented use", "developmental evaluation", "primary intended users", "adaptive use"],
        "structure": ["purpose distinctions", "use prioritization", "user stakes", "decision timing", "early-step integration"],
        "implications": ["Make trade-offs among possible uses explicit.", "Link each intended use to named users and foreseeable action.", "Avoid designing a vague all-purpose evaluation."],
        "group": "User and Use Focus",
    },
    {
        "id": "step-06",
        "kind": "Step",
        "number": 6,
        "title": "Consider and Build in Process Uses if and as Appropriate",
        "pages": "163-190",
        "file": "step-06-consider-and-build-in-process-uses.qmd",
        "section_path": "Step 6: Consider and Build in Process Uses if and as Appropriate",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step06-step-6-consider-and-build-in-process-uses-if-and-as-appropriate:c0041",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0012",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-6-complex-dynamic-systems-interconnections-integrating:c0001",
        ],
        "media_ids": [],
        "core": "The evaluation process itself can create learning, capacity, shared understanding, and changed behavior before findings are produced.",
        "summary": [
            "Step 6 broadens use beyond final findings. Participating in evaluation can help users develop evaluative thinking, clarify assumptions, strengthen collaboration, or build capacity to use evidence.",
            "Patton treats process use as intentional design work, not an incidental benefit. The evaluator should discuss process-use options with users, prioritize them, and design participation in ways that make the intended learning plausible.",
            "The chapter also warns against dabbling. Process uses can compete with findings uses and with each other, so priorities must be explicit and manageable.",
            "The interlude after Step 6 links findings uses and process uses as mutually interacting. What users learn through the process can reshape questions and methods, while intended findings uses should discipline how process participation is designed.",
        ],
        "concepts": ["process use", "findings use", "evaluative thinking", "primary intended users", "adaptive use"],
        "structure": ["process-use options", "capacity building", "learning and ownership", "priority setting", "findings-use integration"],
        "implications": ["Design participation around intended learning, not generic involvement.", "Prioritize process uses just as explicitly as findings uses.", "Track whether process participation is strengthening or distracting from use."],
        "group": "User and Use Focus",
    },
    {
        "id": "step-07",
        "kind": "Step",
        "number": 7,
        "title": "Focus Priority Evaluation Questions",
        "pages": "192-212",
        "file": "step-07-focus-priority-evaluation-questions.qmd",
        "section_path": "Step 7: Focus Priority Evaluation Questions",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step07-step-7-focus-priority-evaluation-questions:c0001",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0012",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-7-complex-dynamic-systems-interconnections-questioning:c0001",
        ],
        "media_ids": [],
        "core": "Evaluation questions focus attention on what users most need to know, can answer credibly, and can use.",
        "summary": [
            "Step 7 makes focusing a central act of utilization-focused practice. Because no evaluation can examine everything, users and evaluator must select questions that are important, answerable, and actionable.",
            "The chapter frames question development as inquiry culture. Useful questions help users learn and decide rather than confirm predetermined beliefs or satisfy evaluator curiosity.",
            "Focusing is also political and practical. The evaluator listens carefully to intended users while preventing the evaluator's own interests, stakeholder pressure, or diffuse curiosity from controlling the agenda.",
            "The interlude after Step 7 shows questioning and focusing as processes that run through every step. Readiness, uses, process use, methods, and interpretation all depend on disciplined question focus.",
        ],
        "concepts": ["evaluation questions", "intended use", "primary intended users", "evaluative thinking", "adaptive use"],
        "structure": ["question generation", "screening criteria", "user priorities", "actionability", "questioning across steps"],
        "implications": ["Use intended use as the test of whether a question belongs in scope.", "Distinguish important questions from merely interesting ones.", "Keep question focus alive as context and users change."],
        "group": "Design Focus",
    },
    {
        "id": "step-08",
        "kind": "Step",
        "number": 8,
        "title": "Check That Fundamental Areas for Evaluation Inquiry Are Being Adequately Addressed: Implementation, Outcomes, and Attribution Questions",
        "pages": "213-251",
        "file": "step-08-check-fundamental-evaluation-inquiry-areas.qmd",
        "section_path": "Step 8: Check That Fundamental Areas for Evaluation Inquiry Are Being Adequately Addressed: Implementation, Outcomes, and Attribution Questions",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step08-step-8-check-that-fundamental-areas-for-evaluation-inquiry-are-being-adequately-:c0048",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-8-complex-dynamic-systems-interconnections-attending-t:c0002",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0014",
        ],
        "media_ids": [],
        "core": "Focused questions should still be checked against implementation, outcomes, and attribution so the evaluation does not omit fundamental inquiry areas.",
        "summary": [
            "Step 8 adds a fundamental-inquiry check to the priority questions from Step 7. Even when users define their own priorities, the evaluator should help them ask whether implementation, outcomes, and attribution have been addressed adequately.",
            "The chapter is not a demand that every evaluation cover everything. It is a quality check that prevents a use-driven evaluation from ignoring basic questions that affect interpretation and action.",
            "Patton links useful outcomes work to specificity: intended outcomes, indicators, data collection, standards, and use need to be connected so findings can guide decisions.",
            "The interlude after Step 8 explains that Steps 7 and 8 could reasonably appear in either order. In practice, evaluators move between user priorities and fundamental inquiry domains until the focus is both relevant and defensible.",
        ],
        "concepts": ["implementation", "attribution", "evaluation questions", "intended use", "credibility"],
        "structure": ["implementation questions", "outcome questions", "attribution questions", "outcomes framework", "interconnection with focusing"],
        "implications": ["Check priority questions against implementation, outcomes, and attribution.", "Do not let user relevance erase basic evaluative adequacy.", "Specify outcomes and standards in ways users can interpret."],
        "group": "Design Focus",
    },
    {
        "id": "step-09",
        "kind": "Step",
        "number": 9,
        "title": "Determine What Intervention Model or Theory of Change Is Being Evaluated",
        "pages": "252-282",
        "file": "step-09-determine-intervention-model-or-theory-of-change.qmd",
        "section_path": "Step 9: Determine What Intervention Model or Theory of Change Is Being Evaluated",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step09-step-9-determine-what-intervention-model-or-theory-of-change-is-being-evaluated:c0004",
            "chunk:essentials-utilization-focused-evaluation:step09-step-9-determine-what-intervention-model-or-theory-of-change-is-being-evaluated:c0018",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-9-complex-dynamic-systems-interconnections-considering:c0001",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0015",
        ],
        "media_ids": [],
        "core": "A utilization-focused evaluation needs a usable account of the intervention model or theory of change so evidence can be interpreted for action.",
        "summary": [
            "Step 9 asks what model, logic, or theory is actually being evaluated. Without a clear intervention model, users may collect data without knowing how implementation, mechanisms, outcomes, and decisions fit together.",
            "The U-FE stance keeps theory work practical. The theory of change is not an abstract diagram for its own sake; it should help intended users clarify what they think will happen and what evidence would affect their actions.",
            "This step connects earlier question focus to later methods negotiation. Methods can only be credible for use if they fit the intervention model and the claims users hope to make.",
            "The final dynamic-systems graphic shows Step 9 interacting with methods debates, fundamental inquiry checks, data gathering, and reporting. Theory of change is therefore a continuing reference point, not a one-time artifact.",
        ],
        "concepts": ["theory of change", "implementation", "attribution", "credibility", "intended use"],
        "structure": ["intervention model", "causal assumptions", "user theory", "evidence implications", "links to methods"],
        "implications": ["Clarify what model or theory is being tested before choosing methods.", "Use theory work to sharpen users' decisions and claims.", "Revisit theory when methods, findings, or context change."],
        "group": "Design Focus",
    },
    {
        "id": "step-10",
        "kind": "Step",
        "number": 10,
        "title": "Negotiate Appropriate Methods to Generate Credible Findings That Support Intended Use by Intended Users",
        "pages": "283-306",
        "file": "step-10-negotiate-methods-for-credible-use.qmd",
        "section_path": "Step 10: Negotiate Appropriate Methods to Generate Credible Findings That Support Intended Use by Intended Users",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step10-step-10-negotiate-appropriate-methods-to-generate-credible-findings-that-support:c0005",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-10-complex-dynamic-systems-interconnections-attending-:c0001",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0017",
        ],
        "media_ids": [],
        "core": "Method choice is negotiated around intended use, credibility to users, feasibility, quality standards, and field realities.",
        "summary": [
            "Step 10 is the methods chapter, but its distinctive move is negotiation. Methods are selected to generate findings that intended users will judge credible enough for intended uses.",
            "The chapter rejects both method-first rigidity and careless pragmatism. Evaluators must negotiate trade-offs between methodological ideals and what can be implemented under real constraints while making quality criteria explicit.",
            "Methods decisions also include attention to threats to data quality, measurement choices, and adaptation as conditions change during fieldwork.",
            "The interlude after Step 10 emphasizes that methods and design decisions arise throughout the U-FE process. Methods are not isolated after questions; they interact with readiness, users, uses, theory, politics, and reporting.",
        ],
        "concepts": ["methods negotiation", "credibility", "intended use", "primary intended users", "adaptive use"],
        "structure": ["method fit", "credibility criteria", "trade-off negotiation", "data quality threats", "design adaptation"],
        "implications": ["Negotiate methods with intended users around use and credibility.", "Document trade-offs between ideals and constraints.", "Keep methods adaptable without abandoning quality criteria."],
        "group": "Methods and Data",
    },
    {
        "id": "step-11",
        "kind": "Step",
        "number": 11,
        "title": "Make Sure Intended Users Understand Potential Methods Controversies and Their Implications",
        "pages": "307-330",
        "file": "step-11-explain-methods-controversies-and-implications.qmd",
        "section_path": "Step 11: Make Sure Intended Users Understand Potential Methods Controversies and Their Implications",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step11-step-11-make-sure-intended-users-understand-potential-methods-controversies-and-:c0001",
            "chunk:essentials-utilization-focused-evaluation:step11-step-11-make-sure-intended-users-understand-potential-methods-controversies-and-:c0002",
            "chunk:essentials-utilization-focused-evaluation:interlude-steps-1-through-11-complex-dynamic-systems-interconnections-making-met:c0001",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0018",
        ],
        "media_ids": [],
        "core": "Users need enough methodological understanding to grasp controversies, trade-offs, and implications for use.",
        "summary": [
            "Step 11 extends methods negotiation into methods education. Intended users do not need to become technical specialists, but they do need to understand controversies that could affect credibility and use.",
            "The evaluator's facilitation task is to make design implications visible. Disputes about qualitative and quantitative evidence, attribution, sampling, measurement, or standards can change what findings can support.",
            "This step protects later use. If users do not understand major methods limitations and debates before findings arrive, they may overclaim, dismiss credible evidence, or be surprised by predictable constraints.",
            "Within the whole U-FE system, Step 11 sits beside Step 10 because methods must both fit use and be intelligible to those expected to use the evaluation.",
        ],
        "concepts": ["methods negotiation", "credibility", "evaluation facilitation", "primary intended users", "intended use"],
        "structure": ["methods education", "controversy identification", "implications for claims", "user comprehension", "credibility protection"],
        "implications": ["Explain methods trade-offs before findings are politically charged.", "Check that users understand what the design can and cannot claim.", "Treat methodological transparency as a use strategy."],
        "group": "Methods and Data",
    },
    {
        "id": "step-12",
        "kind": "Step",
        "number": 12,
        "title": "Simulate Use of Findings: Evaluation's Equivalent of a Dress Rehearsal",
        "pages": "331-348",
        "file": "step-12-simulate-use-of-findings.qmd",
        "section_path": "Step 12: Simulate Use of Findings: Evaluation's Equivalent of a Dress Rehearsal",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step12-step-12-simulate-use-of-findings-evaluation-s-equivalent-of-a-dress-rehearsal:c0001",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0019",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0020",
        ],
        "media_ids": [],
        "core": "Simulating findings before data collection tests whether the design will produce information users can understand, own, and act on.",
        "summary": [
            "Step 12 asks users to rehearse the future use of findings. By simulating possible results, interpretations, and decisions, users and evaluator can test whether the evaluation design is worth doing as planned.",
            "The step is a final design check before data collection. It can reveal missing measures, unclear standards, implausible decisions, or weak ownership of the design.",
            "Simulation also disciplines expectations. Users confront likely costs, uncertainties, and decision implications before evidence arrives, making later interpretation less reactive.",
            "In the overall U-FE sequence, simulation connects methods negotiation to data gathering. It asks whether the chosen design can actually support intended use at the point of decision.",
        ],
        "concepts": ["simulation", "intended use", "primary intended users", "credibility", "adaptive use"],
        "structure": ["finding scenarios", "interpretation rehearsal", "decision rehearsal", "design revision", "go/no-go judgment"],
        "implications": ["Run a findings-use simulation before data collection.", "Revise measures or design when simulated findings would not support action.", "Use simulation to test whether the evaluation is worth its expected cost."],
        "group": "Methods and Data",
    },
    {
        "id": "step-13",
        "kind": "Step",
        "number": 13,
        "title": "Gather Data With Ongoing Attention to Use",
        "pages": "349-360",
        "file": "step-13-gather-data-with-ongoing-attention-to-use.qmd",
        "section_path": "Step 13: Gather Data With Ongoing Attention to Use",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step13-step-13-gather-data-with-ongoing-attention-to-use:c0001",
            "chunk:essentials-utilization-focused-evaluation:step13-step-13-gather-data-with-ongoing-attention-to-use:c0012",
            "chunk:essentials-utilization-focused-evaluation:step13-step-13-gather-data-with-ongoing-attention-to-use:c0023",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0020",
        ],
        "media_ids": [],
        "core": "Data collection should keep users informed and preserve the relationship between fieldwork decisions and intended use.",
        "summary": [
            "Step 13 treats data gathering as part of utilization-focused facilitation, not a technical pause in stakeholder engagement. Primary intended users should remain appropriately informed as data collection unfolds.",
            "The chapter emphasizes managing fieldwork with use in mind. Changes in access, measures, sample, schedule, or context should be interpreted for their implications for credibility and utility.",
            "Ongoing attention to use does not mean users control every technical detail. It means the evaluator communicates consequential changes and keeps design decisions connected to the uses already negotiated.",
            "This step prepares for Step 14 because data that are collected without attention to users' questions, comprehension, and ownership will be harder to organize for interpretation and action.",
        ],
        "concepts": ["intended use", "credibility", "primary intended users", "adaptive use", "evaluation facilitation"],
        "structure": ["data collection management", "user communication", "fieldwork adaptation", "credibility monitoring", "handoff to interpretation"],
        "implications": ["Keep users informed about consequential data collection developments.", "Track how fieldwork adaptations affect intended use.", "Prepare interpretation while data are being gathered, not only afterward."],
        "group": "Methods and Data",
    },
    {
        "id": "step-14",
        "kind": "Step",
        "number": 14,
        "title": "Organize and Present the Data for Interpretation and Use by Primary Intended Users: Analysis, Interpretation, Judgment, and Recommendations",
        "pages": "361-387",
        "file": "step-14-organize-and-present-data-for-interpretation-and-use.qmd",
        "section_path": "Step 14: Organize and Present the Data for Interpretation and Use by Primary Intended Users: Analysis, Interpretation, Judgment, and Recommendations",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step14-step-14-organize-and-present-the-data-for-interpretation-and-use-by-primary-inte:c0003",
            "chunk:essentials-utilization-focused-evaluation:step14-step-14-organize-and-present-the-data-for-interpretation-and-use-by-primary-inte:c0045",
            "chunk:essentials-utilization-focused-evaluation:step14-step-14-organize-and-present-the-data-for-interpretation-and-use-by-primary-inte:c0052",
        ],
        "media_ids": [],
        "core": "Data must be organized so users can move from what the evidence says to interpretation, judgment, and warranted action.",
        "summary": [
            "Step 14 is about sense-making for use. Patton distinguishes analysis, interpretation, judgment, and recommendations so users do not confuse data display with evaluative conclusion or action.",
            "The chapter emphasizes presenting data in ways that reduce overload and support interpretation. Users need organized evidence that helps them ask what happened, what it means, whether it is good enough, and what should be done.",
            "Recommendations, when appropriate, should be grounded in findings and developed with attention to feasibility, control, cost, and likely follow-up.",
            "The practical challenge is facilitation. The evaluator adds value by getting users to deliberate about the right things, distinguish claims, and make explicit the values that undergird judgments.",
        ],
        "concepts": ["analysis", "primary intended users", "intended use", "credibility", "evaluation facilitation"],
        "structure": ["data organization", "interpretation", "evaluative judgment", "recommendations", "user deliberation"],
        "implications": ["Design data displays around user interpretation, not analyst convenience.", "Separate findings, interpretations, judgments, and recommendations.", "Facilitate user deliberation about values and action implications."],
        "group": "Interpretation and Use",
    },
    {
        "id": "step-15",
        "kind": "Step",
        "number": 15,
        "title": "Prepare an Evaluation Report to Facilitate Use and Disseminate Significant Findings to Expand Influence",
        "pages": "388-400",
        "file": "step-15-prepare-report-to-facilitate-use-and-disseminate-findings.qmd",
        "section_path": "Step 15: Prepare an Evaluation Report to Facilitate Use and Disseminate Significant Findings to Expand Influence",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step15-step-15-prepare-an-evaluation-report-to-facilitate-use-and-disseminate-significa:c0009",
            "chunk:essentials-utilization-focused-evaluation:utilization-focused-evaluation-checklist-17-steps-to-evaluations-that-are-useful:c0025",
            "chunk:essentials-utilization-focused-evaluation:interlude-interconnections-among-steps-14-16-u-fe-as-a-complex-dynamic-system-fa:c0001",
        ],
        "media_ids": [],
        "core": "Reporting should be intentionally designed to answer users' questions, communicate clearly, support use, and distinguish dissemination from actual use.",
        "summary": [
            "Step 15 treats the report as a use instrument, not merely a deliverable. Reporting choices should be negotiated around audience, timing, format, visuals, and the decisions or learning the report is meant to support.",
            "Patton's reporting principles keep users at the center: be purposeful, answer priority questions, communicate succinctly, prepare users for difficult findings, and distinguish dissemination from actual use.",
            "The chapter broadens reporting beyond a formal written document. Oral briefings, tailored products, visual displays, and audience-specific formats may be needed when different users have different uses.",
            "The interlude linking Steps 14-16 shows that reporting can trigger feedback to analysis and interpretation, while follow-up can require adapting reporting for new audiences or uses.",
        ],
        "concepts": ["reporting", "dissemination", "intended use", "primary intended users", "adaptive use"],
        "structure": ["report purpose", "audience and format", "visual communication", "negative findings", "dissemination versus use"],
        "implications": ["Plan reporting formats around users and decisions.", "Do not equate dissemination with use.", "Leave time to adapt reports after user feedback."],
        "group": "Interpretation and Use",
    },
    {
        "id": "step-16",
        "kind": "Step",
        "number": 16,
        "title": "Follow Up With Primary Intended Users to Facilitate and Enhance Use",
        "pages": "401-410",
        "file": "step-16-follow-up-to-facilitate-and-enhance-use.qmd",
        "section_path": "Step 16: Follow Up With Primary Intended Users to Facilitate and Enhance Use",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step16-step-16-follow-up-with-primary-intended-users-to-facilitate-and-enhance-use:c0004",
            "chunk:essentials-utilization-focused-evaluation:step16-step-16-follow-up-with-primary-intended-users-to-facilitate-and-enhance-use:c0011",
            "chunk:essentials-utilization-focused-evaluation:interlude-interconnections-among-steps-14-16-u-fe-as-a-complex-dynamic-system-fa:c0001",
        ],
        "media_ids": [],
        "core": "Use often requires active follow-up after reporting, including planning, support, adaptation, and attention to emergent opportunities or resistance.",
        "summary": [
            "Step 16 makes follow-up a core part of utilization-focused evaluation. The evaluator's responsibility does not necessarily end when the report is delivered, because intended use often requires continued facilitation.",
            "Follow-up can include helping users interpret findings, adapt messages for new audiences, keep findings visible, respond to resistance, guard against misuse, and pursue emergent opportunities.",
            "The chapter also makes follow-up a resource issue. If actual use matters, time and budget for post-report support should be negotiated rather than treated as an optional courtesy.",
            "The interlude among Steps 14-16 shows feedback loops: follow-up may send users back to the report, additional analysis, revised displays, or new dissemination strategies.",
        ],
        "concepts": ["follow-up", "intended use", "reporting", "adaptive use", "evaluation facilitation"],
        "structure": ["follow-up plan", "budget and time", "user support", "resistance and misuse", "feedback to reporting"],
        "implications": ["Budget for follow-up before the evaluation closes.", "Keep findings in front of people positioned to use them.", "Treat follow-up as facilitation of use, not after-sales service."],
        "group": "Interpretation and Use",
    },
    {
        "id": "step-17",
        "kind": "Step",
        "number": 17,
        "title": "Metaevaluation of Use: Be Accountable, Learn, and Improve",
        "pages": "411-420",
        "file": "step-17-metaevaluation-of-use.qmd",
        "section_path": "Step 17: Metaevaluation of Use: Be Accountable, Learn, and Improve",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:step17-step-17-metaevaluation-of-use-be-accountable-learn-and-improve:c0006",
            "chunk:essentials-utilization-focused-evaluation:step17-step-17-metaevaluation-of-use-be-accountable-learn-and-improve:c0010",
            "chunk:essentials-utilization-focused-evaluation:step17-step-17-metaevaluation-of-use-be-accountable-learn-and-improve:c0013",
        ],
        "media_ids": [],
        "core": "A utilization-focused evaluation should be judged by professional standards and by whether intended use actually occurred.",
        "summary": [
            "Step 17 closes the sequence by evaluating the evaluation. Patton emphasizes that metaevaluation is a professional obligation and that U-FE places special emphasis on utility and actual use.",
            "The chapter distinguishes potential utility from actual use. A report can be usable and still not be used; assessing use requires looking beyond the product to whether intended users acted, learned, decided, or changed in intended ways.",
            "Professional standards provide criteria, but U-FE adds a sharper accountability question: did this evaluation serve intended users and intended uses responsibly?",
            "The step also supports learning and improvement. Metaevaluation should help evaluators and users understand what supported use, what constrained it, and how future evaluations should be designed differently.",
        ],
        "concepts": ["metaevaluation", "intended use", "follow-up", "credibility", "utilization-focused evaluation"],
        "structure": ["utility standards", "actual use criteria", "accountability", "learning uses", "professional standards"],
        "implications": ["Evaluate actual use, not only report quality.", "Use metaevaluation findings to improve future evaluation facilitation.", "Include follow-up support as a criterion for utility."],
        "group": "Interpretation and Use",
    },
    {
        "id": "summary-and-conclusion",
        "kind": "Conclusion",
        "number": 18,
        "title": "Summary and Conclusion",
        "pages": "426-449",
        "file": "summary-and-conclusion.qmd",
        "section_path": "Summary and Conclusion; Utilization-Focused Evaluation Checklist; U-FE Complex Dynamic and Adaptive Systems Graphic",
        "evidence_ids": [
            "chunk:essentials-utilization-focused-evaluation:summary-and-conclusion:c0001",
            "chunk:essentials-utilization-focused-evaluation:summary-and-conclusion:c0002",
            "chunk:essentials-utilization-focused-evaluation:u-fe-complex-dynamic-and-adaptive-systems-graphic-interactions-among-all-17-step:c0001",
        ],
        "media_ids": [],
        "core": "The conclusion holds together the two faces of U-FE: a practical 17-step checklist and a complex dynamic system of interacting relationships, feedback loops, and adaptations.",
        "summary": [
            "The concluding material recapitulates U-FE as both checklist and complex system. The checklist provides a practical summary of tasks and facilitation challenges for planning, managing, and reviewing the work.",
            "The complex dynamic systems graphic corrects the checklist's linear distortion. Real utilization-focused evaluation unfolds through interactions among readiness, users, uses, questions, methods, data, reporting, follow-up, and metaevaluation.",
            "Patton's Janus framing means that neither representation is sufficient by itself. The checklist can feel manageable but overly sequential; the dynamic graphic can feel realistic but overwhelming.",
            "For practice, the conclusion asks evaluators to use whichever representation helps in the moment while remembering that actual use depends on the whole interacting system.",
        ],
        "concepts": ["utilization-focused evaluation", "adaptive use", "intended use", "primary intended users", "metaevaluation"],
        "structure": ["complete checklist", "primary tasks", "facilitation challenges", "dynamic systems graphic", "controlled folly and use"],
        "implications": ["Use the checklist to manage work without treating it as mechanical.", "Use the dynamic-systems view to notice feedback loops and adaptations.", "Review each step for both tasks and facilitation challenges."],
        "group": "Synthesis",
    },
]


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


def source_chunks(evidence_ids: list[str]) -> str:
    items = "\n".join(f"<li><code>{evidence_id}</code></li>" for evidence_id in evidence_ids)
    return (
        '<details class="source-chunks">\n'
        "<summary>Source records</summary>\n"
        '<ul class="source-chunk-list">\n'
        f"{items}\n"
        "</ul>\n"
        "</details>"
    )


def metadata(extra: list[str]) -> str:
    spans = "".join(f"<span>{item}</span>" for item in [YEAR, *extra])
    return f'<div class="chapter-meta">{spans}</div>'


def mermaid_label(text: str) -> str:
    return text.replace('"', "'")


def section_link(section: dict) -> str:
    if section["kind"] == "Step":
        return f"[Step {section['number']}: {section['title']}]({section['file']})"
    return f"[{section['title']}]({section['file']})"


def sentence_join(items: list[str], limit: int = 4) -> str:
    selected = items[:limit]
    if len(selected) == 1:
        return selected[0]
    return ", ".join(selected[:-1]) + f", and {selected[-1]}"


def concept_gloss(concept: str) -> str:
    return CONCEPT_GLOSSES[concept.lower()]


def display_title(section: dict) -> str:
    if section["kind"] == "Step":
        return f"Step {section['number']:02d}: {section['title']}"
    return section["title"]


def render_concept_map(section: dict) -> str:
    concepts = section["concepts"][:3]
    mechanisms = section["structure"][:3]
    implications = section["implications"][:2]
    label = f"Step {section['number']}" if section["kind"] == "Step" else section["kind"]
    lines = [
        "::: {.concept-map}",
        "```{mermaid}",
        "flowchart TD",
        f'  Problem["Problem: What use problem does {label} help solve?"]',
        f'  Central["Concept: {mermaid_label(section["title"])}"]',
    ]
    for idx, concept in enumerate(concepts, start=1):
        lines.append(f'  Concept{idx}["Concept: {mermaid_label(concept)}"]')
    for idx, mechanism in enumerate(mechanisms, start=1):
        lines.append(f'  Mechanism{idx}["Mechanism: {mermaid_label(mechanism)}"]')
    for idx, implication in enumerate(implications, start=1):
        lines.append(f'  Implication{idx}["Practice implication: {mermaid_label(implication)}"]')
    lines.append('  Question["Open question: What would make this usable in a live evaluation?"]')
    lines.extend(["", "  Problem --> Central", "  Central --> Question"])
    for idx in range(1, len(concepts) + 1):
        lines.append(f"  Central --> Concept{idx}")
    for idx in range(1, len(mechanisms) + 1):
        lines.append(f"  Concept{min(idx, len(concepts))} --> Mechanism{idx}")
    for idx in range(1, len(implications) + 1):
        lines.append(f"  Mechanism{min(idx, len(mechanisms))} --> Implication{idx}")
    lines.extend(
        [
            "  Implication1 --> Question",
            "",
            "  classDef problem fill:#fee2e2,stroke:#b91c1c,color:#7f1d1d;",
            "  classDef concept fill:#e6f3f1,stroke:#115e59,color:#134e4a;",
            "  classDef mechanism fill:#e8f1ff,stroke:#1d4ed8,color:#1e3a8a;",
            "  classDef implication fill:#fce7f3,stroke:#be185d,color:#831843;",
            "  class Problem problem;",
            "  class Central concept;",
            f"  class {','.join(f'Concept{idx}' for idx in range(1, len(concepts) + 1))} concept;",
            f"  class {','.join(f'Mechanism{idx}' for idx in range(1, len(mechanisms) + 1))} mechanism;",
            f"  class {','.join(f'Implication{idx}' for idx in range(1, len(implications) + 1))},Question implication;",
            "```",
            ":::",
        ]
    )
    return "\n".join(lines)


def render_book_connection(section: dict) -> str:
    group = section["group"]
    if group == "Foundations":
        return "Within the wider book, this section belongs to the foundations sequence: it establishes readiness, evaluator role, and the checklist/dynamic-systems frame for U-FE."
    if group == "User and Use Focus":
        return "Within the wider book, this step belongs to the user-and-use sequence: it identifies who will use the evaluation, what they will use it for, and how the process itself can support use."
    if group == "Design Focus":
        return "Within the wider book, this step belongs to the design-focus sequence: it turns intended uses into priority questions, fundamental inquiry checks, and a usable intervention model."
    if group == "Methods and Data":
        return "Within the wider book, this step belongs to the methods-and-data sequence: it negotiates credible evidence, tests use before data collection, and keeps fieldwork connected to utility."
    if group == "Interpretation and Use":
        return "Within the wider book, this step belongs to the interpretation-and-use sequence: it moves from data sense-making to reporting, follow-up, and accountability for actual use."
    return "Within the wider book, this conclusion synthesizes the checklist and complex dynamic systems views of utilization-focused evaluation."


def render_section(section: dict, prev_section: dict | None, next_section: dict | None) -> str:
    evidence_ids = section["evidence_ids"]
    title = display_title(section)
    label = f"Step {section['number']}" if section["kind"] == "Step" else section["kind"]
    body = [
        "---",
        f'title: "{title}"',
        f'description: "Detailed study notes for {title} in {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        f'note_type: "{section["kind"]}"',
    ]
    if section["kind"] == "Step":
        body.append(f'step_number: {section["number"]}')
    body.extend(
        [
            f'source_pages: "{section["pages"]}"',
            f'citation_key: "{CITATION}"',
            "evidence_ids:",
            yaml_list(evidence_ids),
            f'source_status: "{SOURCE_STATUS}"',
            "---",
            "",
            "## Source",
            "",
            metadata(["MCP evaluation-texts", "Status: needs_review", label, f"Source pages {section['pages']}"]),
            "",
            f"This note summarises {label.lower()}, \"{section['title']},\" from {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. It is a paraphrased study note based on source-linked MCP research-library retrieval records, not a substitute for the book section.",
            "",
            "The retrieval trail is retained in the source records at the bottom of the page. The note paraphrases the section's argument and procedures, and it does not reproduce textbook tables, checklists, exhibits, graphics, or extended passages. When a checklist, exhibit, or graphic is central, the note describes its function and leaves the source artifact in the evidence record.",
            "",
            "## Core Argument",
            "",
            section["core"],
            "",
            "## Study Summary",
            "",
        ]
    )
    for paragraph in section["summary"]:
        body.extend([paragraph, ""])
    body.extend(
        [
            f"For close reading, track how this section uses {sentence_join(section['concepts'])} while moving through {sentence_join(section['structure'], 3)}. The notes below identify what the section asks the evaluator to notice, what use problem it helps solve, and what should be checked against the saved evidence records before relying on the summary in applied work.",
            "",
            render_book_connection(section),
            "",
            "## Key Concepts",
            "",
        ]
    )
    body.extend(f"- **{concept}**: {concept_gloss(concept)}" for concept in section["concepts"])
    body.extend(["", "## Section Structure", ""])
    body.extend(f"- {item.capitalize()}." for item in section["structure"])
    body.extend(["", "## Practical Implications", ""])
    body.extend(f"- {item}" for item in section["implications"])
    body.extend(["", "## Concept Map", "", render_concept_map(section), "", "## Connections", ""])
    body.extend(
        [
            "- Book overview: [Overview](index.qmd)",
            "- Reading route: [Chapter Map](chapter-map.qmd)",
            "- Concepts synthesis: [Core Concepts](concepts.qmd)",
            "- Practice synthesis: [Practice Implications](practice-implications.qmd)",
        ]
    )
    if prev_section:
        body.append(f"- Previous: {section_link(prev_section)}")
    if next_section:
        body.append(f"- Next: {section_link(next_section)}")
    if section["id"] in {"introduction", "step-10", "summary-and-conclusion"}:
        for legacy_title, path in LEGACY_EXTRACTS:
            body.append(f"- Legacy extract retained: [{legacy_title}]({path})")
    body.extend(
        [
            "",
            "## Study Prompts",
            "",
            f"1. What use problem does {label.lower()} help solve?",
            "2. Which primary intended users would need to participate for this guidance to work?",
            "3. How would this section change scoping, methods, interpretation, reporting, or follow-up?",
            "4. Where could this guidance be misused if treated as a fixed template?",
            "",
            "## Source Records",
            "",
            source_chunks(evidence_ids),
            "",
            "## References",
            "",
            f"- Patton, M. Q. ({YEAR}). *{FULL_TITLE}*. {PUBLISHER}. {title}, pages {section['pages']}.",
            f"- Saved retrieval metadata: `data/research-library/evidence/{SLUG}/step-evidence-summary.json`.",
            "",
        ]
    )
    return "\n".join(body)


def render_index() -> str:
    evidence = [section["evidence_ids"][0] for section in SECTIONS]
    lines = [
        "---",
        f'title: "{TITLE}"',
        f'description: "Book overview and step study-note index for {TITLE}."',
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
        f"Study notes on *{FULL_TITLE}* [@{CITATION}]. These step-level notes are generated from source-linked MCP research-library records and are intended for study, comparison, and later refinement.",
        "",
        '<div class="page-metadata">',
        "  <span>19 intro/step/conclusion notes</span>",
        f"  <span>{YEAR}</span>",
        "  <span>Source status: needs_review</span>",
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
        "Recurring ideas and distinctions used across these step-level notes.",
        ":::",
        "",
        "::: {.section-card}",
        '<span class="page-badge badge-map">Map</span>',
        "",
        "### [Chapter Map](chapter-map.qmd)",
        "",
        "Full reading route for the introduction, 17 U-FE steps, and conclusion.",
        ":::",
        "",
        "::: {.section-card}",
        '<span class="page-badge badge-practice">Practice</span>',
        "",
        "### [Practice Implications](practice-implications.qmd)",
        "",
        "Practical utilization-focused evaluation habits drawn from the full step set.",
        ":::",
        ":::",
        "",
        "</div>",
        "",
        "## Source",
        "",
        metadata(["Book overview", "Step route"]),
        "",
        f"This index summarises generated study notes for {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. The generated pages use selected MCP research-library retrieval records and compact evidence summaries.",
        "",
        "## Core Argument",
        "",
        "Utilization-focused evaluation designs evaluation around intended use by intended users, treating readiness, users, uses, questions, methods, interpretation, reporting, follow-up, and metaevaluation as an interacting system rather than a linear technical sequence.",
        "",
        "## Step-Level Notes",
        "",
    ]
    for section in SECTIONS:
        lines.append(f"- {section_link(section)} - source pages {section['pages']}")
    lines.extend(["", "## Legacy Extracts", ""])
    for legacy_title, path in LEGACY_EXTRACTS:
        lines.append(f"- [{legacy_title}]({path})")
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_chapter_map() -> str:
    evidence = [section["evidence_ids"][0] for section in SECTIONS]
    groups = [
        ("Foundations", [section for section in SECTIONS if section["group"] == "Foundations"]),
        ("User and Use Focus", [section for section in SECTIONS if section["group"] == "User and Use Focus"]),
        ("Design Focus", [section for section in SECTIONS if section["group"] == "Design Focus"]),
        ("Methods and Data", [section for section in SECTIONS if section["group"] == "Methods and Data"]),
        ("Interpretation and Use", [section for section in SECTIONS if section["group"] == "Interpretation and Use"]),
        ("Synthesis", [section for section in SECTIONS if section["group"] == "Synthesis"]),
    ]
    lines = [
        "---",
        f'title: "{TITLE} Chapter Map"',
        f'description: "Full reading map for {TITLE} step-level notes."',
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
    for heading, sections in groups:
        lines.extend([f"### {heading}", ""])
        for section in sections:
            lines.append(f"- {section_link(section)} - pages {section['pages']}; `{section['section_path']}`")
        lines.append("")
    lines.extend(
        [
            "## How to Use This Map",
            "",
            "- Start with the introduction and Steps 1-2 to understand the checklist/dynamic-systems frame and readiness requirements.",
            "- Use Steps 3-6 to identify primary intended users, analyze the situation, prioritize uses, and design process uses.",
            "- Use Steps 7-9 to focus evaluation questions, check fundamental inquiry areas, and clarify the intervention model or theory of change.",
            "- Use Steps 10-13 to negotiate methods, explain methods controversies, simulate use, and gather data with ongoing attention to utility.",
            "- Use Steps 14-17 and the conclusion to organize findings for interpretation, report for use, follow up, and evaluate actual use.",
            "",
            "## Legacy Extracts",
            "",
        ]
    )
    for legacy_title, path in LEGACY_EXTRACTS:
        lines.append(f"- [{legacy_title}]({path})")
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = [section["evidence_ids"][0] for section in SECTIONS]
    concept_groups = [
        ("Use Logic", ["utilization-focused evaluation", "intended use", "primary intended users", "findings use", "process use"]),
        ("Readiness and Facilitation", ["program readiness", "evaluation facilitation", "personal factor", "situation analysis", "adaptive use"]),
        ("Design Focus", ["evaluation questions", "implementation", "attribution", "theory of change", "simulation"]),
        ("Methods and Credibility", ["methods negotiation", "credibility", "evaluative thinking", "analysis", "reporting"]),
        ("Use Accountability", ["dissemination", "follow-up", "metaevaluation", "decision-oriented use", "developmental evaluation"]),
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
        f"This synthesis draws across the step-level notes for *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Central Logic",
        "",
        "The book treats evaluation use as a design, facilitation, and accountability problem. Intended use by intended users governs readiness, user engagement, purposes, questions, methods, interpretation, reporting, follow-up, and metaevaluation.",
        "",
        "## Concepts",
        "",
    ]
    for heading, concepts in concept_groups:
        lines.extend([f"### {heading}", ""])
        for concept in concepts:
            lines.append(f"- {concept}: {concept_gloss(concept)}")
        lines.append("")
    lines.extend(
        [
            "## Dynamic Systems Thread",
            "",
            "Patton repeatedly pairs the 17-step checklist with complex dynamic systems interludes. The checklist is useful for planning and management, but the practice implication is iterative: decisions about users, uses, questions, methods, reporting, and follow-up feed back into one another.",
            "",
            "## Links",
            "",
        ]
    )
    lines.extend(f"- {section_link(section)}" for section in SECTIONS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = [section["evidence_ids"][0] for section in SECTIONS]
    implications = [
        "Start every evaluation design by asking who will use the evaluation and for what specific uses.",
        "Assess organizational readiness and evaluator readiness before promising utility.",
        "Distinguish broad stakeholders from primary intended users who will make or influence concrete decisions.",
        "Analyze political, organizational, and contextual forces with users before the design hardens.",
        "Prioritize intended uses and process uses; do not let the evaluation try to serve every possible purpose.",
        "Focus questions by actionability, importance to users, and feasibility of credible answers.",
        "Check user-prioritized questions against implementation, outcomes, and attribution.",
        "Clarify the intervention model or theory of change so evidence can support interpretation and claims.",
        "Negotiate methods around intended use, credibility to users, and feasible quality standards.",
        "Simulate use of findings before data collection to test whether the design is worth doing.",
        "Keep users appropriately informed during data collection when fieldwork changes affect credibility or utility.",
        "Organize data for user interpretation, judgment, and warranted action, not only for analyst completeness.",
        "Treat reporting, dissemination, and follow-up as distinct design problems.",
        "Evaluate actual use after the report, not only the quality or potential utility of the report.",
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
        f"This practice synthesis draws on the step-level notes from *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Evaluation Practice Implications",
        "",
    ]
    lines.extend(f"- {item}" for item in implications)
    lines.extend(["", "## Links", ""])
    lines.extend(f"- {section_link(section)}" for section in SECTIONS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_evidence_summary() -> dict:
    return {
        "schema_version": "1.0",
        "generated_at": GENERATED_AT,
        "collection_id": COLLECTION_ID,
        "book_id": BOOK_ID,
        "book_title": TITLE,
        "source_status": SOURCE_STATUS,
        "rag_status": RAG_STATUS,
        "source_tool": "mcp__researchlibrary.rag_evidence_pack",
        "copyright_note": "Stores retrieval IDs and source locations only; source text is not duplicated.",
        "records": [
            {
                "section_id": section["id"],
                "section_title": display_title(section),
                "source_pages": section["pages"],
                "section_path": section["section_path"],
                "evidence_ids": section["evidence_ids"],
                "media_ids": section["media_ids"],
                "target_path": f"notes/{SLUG}/{section['file']}",
            }
            for section in SECTIONS
        ],
    }


def render_step_evidence_summary() -> dict:
    return {
        "schema_version": "1.0",
        "generated_at": GENERATED_AT,
        "collection_id": COLLECTION_ID,
        "book_id": BOOK_ID,
        "book_title": TITLE,
        "source_status": SOURCE_STATUS,
        "source_tool": "mcp__researchlibrary.rag_evidence_pack",
        "evidence_pack_defaults": {
            "include_neighbors": True,
            "include_media": "true for full-book grounding and checklist/graphic-heavy sections",
            "limit": "targeted intro/step/conclusion retrieval plus broad full-book evidence pack before synthesis",
        },
        "sections": [
            {
                "id": section["id"],
                "title": display_title(section),
                "target_path": f"notes/{SLUG}/{section['file']}",
                "section_paths": [section["section_path"]],
                "source_pages": section["pages"],
                "evidence_ids": section["evidence_ids"],
                "media_ids": section["media_ids"],
                "status": "drafted",
            }
            for section in SECTIONS
        ],
    }


def update_manifest() -> None:
    path = ROOT / "data" / "research_library_notes_manifest.json"
    manifest = read_json(path)
    for book in manifest.get("books", []):
        if book.get("book_id") == BOOK_ID:
            book["generation_mode"] = "generated-step-notes"
            book["target_path"] = f"notes/{SLUG}/index.qmd"
            book["sections"] = [
                {
                    "id": section["id"],
                    "title": display_title(section),
                    "source_pages": section["pages"],
                    "section_path": section["section_path"],
                    "evidence_ids": section["evidence_ids"],
                    "target_path": f"notes/{SLUG}/{section['file']}",
                }
                for section in SECTIONS
            ]
            break
    else:
        raise SystemExit(f"{BOOK_ID} not found in manifest")
    write_json("data/research_library_notes_manifest.json", manifest)


def patch_overview_copy() -> None:
    home = ROOT / "index.qmd"
    text = home.read_text(encoding="utf-8")
    text = text.replace(
        "chapter-level Rossi/Lipsey and Chen notes, and generated notes for the wider collection.",
        "chapter-level Rossi/Lipsey and Chen notes, step-level Patton/U-FE notes, and generated notes for the wider collection.",
    )
    home.write_text(text, encoding="utf-8")

    notes = ROOT / "notes" / "index.qmd"
    text = notes.read_text(encoding="utf-8")
    text = text.replace(
        "chapter-level Rossi/Lipsey and Chen notes, and generated notes for the other ready evaluation texts.",
        "chapter-level Rossi/Lipsey and Chen notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.",
    )
    notes.write_text(text, encoding="utf-8")


def generate() -> None:
    base = f"notes/{SLUG}"
    for idx, section in enumerate(SECTIONS):
        prev_section = SECTIONS[idx - 1] if idx else None
        next_section = SECTIONS[idx + 1] if idx + 1 < len(SECTIONS) else None
        write_text(f"{base}/{section['file']}", render_section(section, prev_section, next_section))
    write_text(f"{base}/index.qmd", render_index())
    write_text(f"{base}/chapter-map.qmd", render_chapter_map())
    write_text(f"{base}/concepts.qmd", render_concepts())
    write_text(f"{base}/practice-implications.qmd", render_practice())
    write_json(f"data/research-library/evidence/{SLUG}/evidence-summary.json", render_evidence_summary())
    write_json(f"data/research-library/evidence/{SLUG}/step-evidence-summary.json", render_step_evidence_summary())
    update_manifest()
    patch_overview_copy()


if __name__ == "__main__":
    generate()
