#!/usr/bin/env python3
"""Generate chapter-level Chen Practical Program Evaluation study notes."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "practical-program-evaluation"
SLUG = BOOK_ID
TITLE = "Practical Program Evaluation"
FULL_TITLE = TITLE
AUTHORS = "Huey T. Chen"
CITATION = "chen_2015_practical_program_evaluation"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2015"
PUBLISHER = "SAGE Publications"
GENERATED_AT = "2026-06-28"


LEGACY_EXTRACTS = [
    ("Evaluation Design and Its Components", "section-01-evaluation-design-components.qmd"),
    ("Logic Models and the Action Model/Change Model Schema", "section-02-logic-models-and-program-theory.qmd"),
    ("When Logic Models Do Not Work as Expected", "section-03-logic-model-limits.qmd"),
]


CONCEPT_GLOSSES = {
    "accountability": "Use of evaluation evidence to support responsibility, reporting, judgment, and program oversight.",
    "action model": "The program theory component specifying the organizations, implementers, partners, context, target population, and delivery arrangements needed for action.",
    "action plan": "The planning account of how the intervention will be organized, staffed, delivered, supported, and adapted in practice.",
    "adjuvant": "A real-world support, adaptation, or contextual aid that helps an intervention work but may look like a validity threat in conventional experiments.",
    "bilateral empowerment evaluation": "A partnership form in which evaluators and stakeholders jointly use evaluation information while developing and stabilizing a program.",
    "bottom-up approach": "A dissemination route that begins with real-world viability and effectiveness before moving toward more controlled efficacy evidence.",
    "change model": "The program theory component explaining how intervention activities are expected to change determinants and outcomes.",
    "causal mechanism": "The process through which an intervention is expected to affect determinants or outcomes.",
    "checklist": "A structured set of criteria used to rate or review evaluation quality, readiness, or completeness.",
    "cogency": "The clarity, logic, and persuasiveness of evaluation evidence for a given practical claim.",
    "comprehensive evaluation typology": "Chen's map of evaluation approaches by program stage, evaluation function, and strategy.",
    "conceptualization facilitation": "Evaluator support for helping stakeholders articulate program scope, action plan, and underlying assumptions.",
    "conclusive evaluation": "Evaluation used to judge merit, worth, performance, effectiveness, or accountability.",
    "conclusive assessment": "The judgment-oriented component of an evaluation, especially about implementation quality or real-world effects.",
    "conclusive outcome evaluation": "Outcome evaluation used to judge whether an intervention achieved intended effects or merit.",
    "consensus building": "Evaluator-facilitated agreement among stakeholder groups about goals, outcomes, assumptions, or evaluation focus.",
    "contextual factors": "Setting conditions, resources, relationships, constraints, and supports that shape implementation or outcomes.",
    "constructive evaluation": "Evaluation used to improve, clarify, develop, or strengthen a program before or during implementation.",
    "constructive assessment": "The improvement-oriented component of an evaluation that checks coherence, capacity, vulnerabilities, and readiness.",
    "constructive outcome evaluation": "Outcome-stage work that strengthens goals, evaluability, coherence, and stakeholder agreement before conclusive outcome assessment.",
    "development facilitation": "A strategy that uses evaluation tools to help stakeholders design, clarify, or improve a program.",
    "determinants": "The conditions, behaviors, beliefs, capacities, or mechanisms an intervention must change to reach desired outcomes.",
    "ecological context": "The surrounding social, organizational, community, policy, and interpersonal conditions that support or constrain implementation.",
    "effectual cogency": "Evidence about whether an intervention affects intended outcomes.",
    "evaluability assessment": "Assessment of whether a program is coherent, measurable, and ready for credible outcome evaluation.",
    "evaluation design": "The integrated plan for purpose, program description, stage, evaluation type, approach, methods, and use.",
    "evaluation strategy": "The broad purpose and orientation that links program stage, stakeholder need, evaluation approach, and use.",
    "evidence-based intervention": "An intervention promoted for wider use because evidence supports claims about its effectiveness or suitability.",
    "experimentation evaluation approach": "Outcome evaluation that prioritizes experimental or quasi-experimental logic to estimate pure causal effects.",
    "fidelity evaluation": "Assessment of whether implementation matches the intended intervention, delivery, referral, or target-population design.",
    "formal theory": "A theory from research literature or a scientific tradition used to design or explain an intervention.",
    "formative evaluation": "Development-oriented evaluation during implementation that identifies barriers, facilitators, and remedies.",
    "formative research": "Background inquiry used during planning to understand needs, culture, setting, and stakeholder or client perspectives.",
    "fundamental evaluation typology": "Chen's early matrix distinguishing constructive and conclusive functions across process and outcome stages.",
    "feedback loops": "Information paths through which monitoring, process, or outcome evidence can improve program design and implementation.",
    "goal trap": "A problem created when official goals are accepted uncritically even though they are vague, implausible, symbolic, or disconnected from program reality.",
    "holistic effectuality evaluation": "A real-world outcome approach that combines constructive and conclusive assessment and examines joint effects of intervention and adjuvants.",
    "hybrid evaluation": "Evaluation that intentionally combines constructive and conclusive functions, or spans more than one program stage.",
    "implementation success": "A state in which action model delivery activates the intended change process, while still requiring evidence that the change model works.",
    "implementation problem": "A barrier, failure, inconsistency, or unexpected condition that interferes with delivering the program as intended.",
    "implementation quality": "The degree to which actual delivery is adequate, consistent, appropriate, and aligned with the program plan.",
    "implementing organization": "The organization responsible for arranging resources, staff, partnerships, and routines needed to deliver the intervention.",
    "indicator": "A measurable sign of process or outcome performance used in monitoring or evaluation.",
    "initial implementation": "The early delivery stage when routines are still being established and constructive troubleshooting is often needed.",
    "integrated evaluation perspective": "Chen's stance that evaluation should synthesize scientific credibility and stakeholder responsiveness.",
    "integrative cogency model": "A model that treats credible evidence as multidimensional: viable, effectual, and transferable.",
    "integrative process/outcome evaluation": "Theory-driven evaluation that jointly examines implementation assumptions, causal processes, and outcomes.",
    "intervening mechanism": "A mediator-like causal process through which an intervention affects determinants or outcomes.",
    "internal validity": "The credibility of a causal claim that observed outcomes were produced by the intervention rather than confounding influences.",
    "intervention protocol": "The specification of intervention content, sequence, dosage, materials, activities, and delivery expectations.",
    "joint effects": "Effects produced by an intervention together with real-world supports, adaptations, and contextual adjuvants.",
    "logic model": "A compact representation of program inputs, activities, outputs, and outcomes used for planning and communication.",
    "mature implementation": "A program stage in which delivery routines and rules are sufficiently established for fidelity, monitoring, or hybrid process assessment.",
    "moderating mechanism": "A conditioning process or factor that changes whether, how, or for whom an intervention affects outcomes.",
    "monitoring system": "The organizational data routines, indicators, tools, and information infrastructure used for ongoing program monitoring.",
    "multiple-entry evaluation": "An evaluation design that addresses two or more program stages rather than one isolated stage.",
    "needs assessment": "Planning-stage inquiry into unmet needs, service gaps, target groups, and priorities.",
    "outcome monitoring": "Periodic tracking of client or program outcomes that informs progress but does not by itself establish effectiveness.",
    "operative goals": "Goals actually pursued through program behavior, whether or not they match official goals.",
    "performance assessment": "A merit-assessment strategy that uses more rigorous evidence to judge implementation or outcome performance.",
    "performance monitoring": "A merit-assessment strategy that repeatedly tracks indicators of process or outcome performance.",
    "pilot testing": "Small-scale trial of intervention or implementation arrangements before full-scale launch.",
    "plausibility assessment": "Inquiry into which official, operative, intended, and unintended goals are credible enough to guide evaluation.",
    "proactive approach": "A strategy of using the action model/change model schema early when logic-model limitations are predictable.",
    "process monitoring": "Repeated tracking of implementation and service-delivery indicators.",
    "program monitoring": "Periodic quantitative tracking of program process and outcomes to support management and accountability.",
    "program review/development meeting": "A facilitated internal meeting used to identify implementation difficulties and possible remedies.",
    "program scope": "The planning account of problem, goals, target population, intervention, determinants, and expected outcomes.",
    "program stage": "A phase in the program life cycle, such as planning, initial implementation, mature implementation, or outcome.",
    "program theory": "The explicit or implicit assumptions linking action, context, mechanisms, and outcomes in an intervention.",
    "pure independent effects": "Effects attributed to an intervention after removing or controlling for other influences and supports.",
    "randomized experiment": "A causal design that uses random assignment to strengthen claims about intervention effects.",
    "relevancy testing": "A troubleshooting approach for checking whether program scope assumptions fit the problem, target group, and proposed intervention.",
    "reactive approach": "A strategy of continuing with a logic model until limitations appear, then adding the action model/change model schema.",
    "real-world outcome evaluation": "Outcome evaluation focused on how an intervention works under practical delivery conditions, including supports and adaptations.",
    "reinvention": "Local modification or adaptation of an intervention during implementation.",
    "scientific credibility": "The degree to which an evaluation is judged technically sound, systematic, and governed by defensible inquiry principles.",
    "service delivery protocols": "Procedures that specify how, where, when, and by whom services are delivered to participants.",
    "single-entry evaluation": "An evaluation design focused on one program stage.",
    "smart goals": "Goals specified so they can be meaningfully understood, measured, and used for outcome evaluation.",
    "stakeholder credibility": "The degree to which stakeholders judge that an evaluation reflects their views, concerns, needs, and practical realities.",
    "stakeholder theory": "Program theory based primarily on stakeholders' experience, assumptions, and local knowledge.",
    "system change": "Intervention work aimed at changing organizational, community, partnership, or contextual arrangements, not only delivering a discrete service.",
    "target population": "The people, groups, organizations, or communities the program intends to reach or affect.",
    "theory-driven outcome evaluation": "Outcome evaluation that examines causal mechanisms and implementation processes, not only whether outcomes changed.",
    "theory-driven process evaluation": "Hybrid process evaluation that examines how implementation components contribute to program quality and performance.",
    "threats to validity": "Alternative explanations, biases, or design problems that can weaken causal or evaluative claims.",
    "top-down approach": "A dissemination route that privileges efficacy evidence, often from controlled trials, before real-world spread.",
    "transferable cogency": "Evidence about whether viability and effectuality can transfer across real-world settings.",
    "troubleshooting": "A strategy for quickly identifying implementation problems and supporting stakeholders in fixing them.",
    "validity-focused outcome evaluation": "Outcome evaluation guided by experimentation logic and the priority of ruling out threats to internal validity.",
    "viability evaluation": "Assessment of whether an intervention is practical, affordable, acceptable, and workable in real-world settings.",
    "viable cogency": "Evidence about whether an intervention can work as a feasible real-world program.",
}


CHAPTERS = [
    {
        "number": 1,
        "title": "Fundamentals of Program Evaluation",
        "pages": "23-56",
        "file": "chapter-01-fundamentals-of-program-evaluation.qmd",
        "section_path": "Chapter 1: Fundamentals of Program Evaluation",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch01-a-fundamental-evaluation-typology:c0001",
            "chunk:practical-program-evaluation:ch01-evaluations-must-address-both-scientific-and-stakeholder-credibility:c0001",
            "chunk:practical-program-evaluation:ch01-integrated-evaluation-perspective:c0001",
            "chunk:practical-program-evaluation:ch01-introducing-the-rest-of-the-chapters:c0001",
        ],
        "media_ids": [],
        "core": "Evaluation is an applied practice that must balance scientific credibility, stakeholder credibility, program stage, and practical usefulness.",
        "summary": [
            "Chapter 1 introduces Chen's practical orientation to evaluation. It treats program evaluation as more than method selection: evaluators need to understand intervention programs, stakeholder needs, program politics, and the purposes that evidence is expected to serve.",
            "The chapter extends the familiar formative/summative distinction into a fundamental typology. Evaluation can serve constructive or conclusive functions, and it can focus on process, outcome, or hybrid combinations of the two.",
            "A central tension is the need to address both scientific and stakeholder credibility. Scientific credibility asks whether evidence is technically sound; stakeholder credibility asks whether the evaluation takes users' concerns, practices, and decisions seriously enough to be useful.",
            "The integrated evaluation perspective sets up the rest of the book. Instead of privileging method-driven rigor or stakeholder responsiveness alone, Chen argues for designs that synthesize both requirements in ways that fit real programs.",
        ],
        "concepts": ["fundamental evaluation typology", "constructive evaluation", "conclusive evaluation", "hybrid evaluation", "scientific credibility", "stakeholder credibility", "integrated evaluation perspective"],
        "structure": ["intervention programs and feedback", "fundamental evaluation typology", "internal and external evaluators", "stakeholder credibility", "scientific credibility", "integrated evaluation perspective"],
        "implications": ["Classify the evaluation function before choosing methods.", "Treat stakeholder credibility as a design requirement, not a courtesy.", "Use the integrated perspective to avoid rigid method-first evaluation."],
    },
    {
        "number": 2,
        "title": "Understand Approaches to Evaluation and Select Ones That Work: The Comprehensive Evaluation Typology",
        "pages": "57-78",
        "file": "chapter-02-understand-approaches-to-evaluation-and-select-ones-that-work.qmd",
        "section_path": "Chapter 2: Understand Approaches to Evaluation and Select Ones That Work: the Comprehensive Evaluation Typology",
        "evidence_ids": [
            "table_segment:practical-program-evaluation:table:2.1:s001",
            "chunk:practical-program-evaluation:ch02-the-comprehensive-evaluation-typology-means-and-ends:c0001",
            "chunk:practical-program-evaluation:ch02-applying-the-typology-steps-to-take:c0001",
            "chunk:practical-program-evaluation:ch02-2-multiple-entry-evaluation:c0001",
        ],
        "media_ids": ["practical-program-evaluation:table:2.1:image"],
        "core": "The comprehensive evaluation typology matches program stage, stakeholder purpose, evaluation approach, and strategy so evaluators can choose approaches that fit the situation.",
        "summary": [
            "Chapter 2 expands the Chapter 1 typology into a life-cycle map. It organizes evaluation around four program stages: planning, initial implementation, mature implementation, and outcome.",
            "The comprehensive typology is the book's main routing device. It associates each stage with purposes, approaches, and strategies such as background information provision, development facilitation, troubleshooting, merit assessment, performance monitoring, performance assessment, enlightenment, and partnership.",
            "The chapter stresses that evaluation is situational. An approach that is useful for a mature program can be premature or misleading for an immature program, and a method that supports accountability may not help stakeholders fix urgent implementation problems.",
            "Chen also distinguishes single-entry and multiple-entry evaluation. Readers can enter the book at the chapter that matches the current program stage, or combine chapters when an evaluation spans planning, implementation, monitoring, and outcomes.",
        ],
        "concepts": ["comprehensive evaluation typology", "program stage", "evaluation strategy", "single-entry evaluation", "multiple-entry evaluation", "performance assessment", "development facilitation"],
        "structure": ["program life cycle", "evaluation purposes", "approaches by stage", "strategies underlying approaches", "applying the typology", "single-entry and multiple-entry routes"],
        "implications": ["Use program stage as the first routing question.", "Select approaches by stakeholder need, not by evaluator preference.", "Use multiple-entry designs when a real assignment crosses stages."],
    },
    {
        "number": 3,
        "title": "Logic Models and the Action Model/Change Model Schema (Program Theory)",
        "pages": "79-114",
        "file": "chapter-03-logic-models-and-the-action-model-change-model-schema.qmd",
        "section_path": "Chapter 3: Logic Models and the Action Model/change Model Schema (program Theory)",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch03-logic-models-and-the-action-model-change-model-schema-program-theory:c0001",
            "chunk:practical-program-evaluation:ch03-program-theory:c0001",
            "chunk:practical-program-evaluation:ch03-components-of-the-change-model:c0001",
            "chunk:practical-program-evaluation:ch03-components-of-the-action-model:c0002",
            "chunk:practical-program-evaluation:ch03-applications-of-logic-models-and-the-action-model-change-model-schema:c0001",
        ],
        "media_ids": [],
        "core": "Logic models and the action model/change model schema are complementary tools for describing programs, with the schema adding context, implementation, and causal mechanisms when a simple logic model is too thin.",
        "summary": [
            "Chapter 3 gives evaluators two program-description tools. Logic models are compact and useful for communication, grant requirements, and reducing complexity into manageable components.",
            "Program theory is treated as a richer framework. Chen's action model/change model schema separates the causal logic of change from the practical arrangements required to deliver the intervention.",
            "The change model focuses on goals, determinants, and interventions. The action model focuses on implementing organizations, implementers, partners, context, target population, and service delivery protocols.",
            "The chapter does not reject logic models. It argues that evaluators should choose the representation that fits the program and evaluation purpose, using the fuller schema when causal mechanisms, context, feedback loops, or implementation assumptions matter.",
        ],
        "concepts": ["logic model", "program theory", "action model", "change model", "causal mechanism", "contextual factors", "feedback loops"],
        "structure": ["logic models", "program theory", "change model components", "action model components", "relationships among components", "applications"],
        "implications": ["Use logic models when communication and basic structure are enough.", "Use the action model/change model schema when context and mechanisms drive evaluation risk.", "Clarify stakeholder theory before designing data collection."],
    },
    {
        "number": 4,
        "title": "Helping Stakeholders Clarify a Program Plan: Program Scope",
        "pages": "117-137",
        "file": "chapter-04-helping-stakeholders-clarify-a-program-plan-program-scope.qmd",
        "section_path": "Chapter 4: Helping Stakeholders Clarify a Program Plan: Program Scope",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch04-the-program-plan-program-scope-and-action-plan:c0001",
            "chunk:practical-program-evaluation:ch04-background-information-provision-strategy-and-approaches:c0001",
            "chunk:practical-program-evaluation:ch04-needs-assessment:c0001",
            "chunk:practical-program-evaluation:ch04-the-relevancy-testing-approach-a-part-of-the-troubleshooting-strategy:c0002",
        ],
        "media_ids": [],
        "core": "Program-scope work clarifies the problem, goals, target population, intervention, determinants, and expected outcomes before stakeholders commit to an action plan.",
        "summary": [
            "Chapter 4 begins the planning-stage sequence by distinguishing program scope from action plan. Program scope explains what problem the program addresses, why it matters, who is targeted, what intervention is proposed, and how the intervention should produce outcomes.",
            "Needs assessment and formative research provide background information for program scope. Needs assessment helps identify unmet needs and target priorities; formative research deepens understanding of clients, implementers, culture, and setting.",
            "The chapter uses the change model to help evaluators and stakeholders specify goals, determinants, interventions, and target populations. This makes the program's rationale explicit enough to be tested and improved.",
            "Relevancy testing is presented as a troubleshooting approach. It checks whether goals are realistic, whether target groups fit the problem, and whether the proposed intervention is relevant to the determinants and needs identified.",
        ],
        "concepts": ["program scope", "change model", "needs assessment", "formative research", "target population", "relevancy testing", "determinants"],
        "structure": ["program plan", "program scope", "background information provision", "needs assessment", "formative research", "relevancy testing"],
        "implications": ["Do not let action planning proceed without a coherent program scope.", "Use needs and formative evidence to correct weak assumptions early.", "Test whether goals, target groups, determinants, and interventions fit one another."],
    },
    {
        "number": 5,
        "title": "Helping Stakeholders Clarify a Program Plan: Action Plan",
        "pages": "139-171",
        "file": "chapter-05-helping-stakeholders-clarify-a-program-plan-action-plan.qmd",
        "section_path": "Chapter 5: Helping Stakeholders Clarify a Program Plan: Action Plan",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch05-the-action-model-framework-and-the-action-plan:c0003",
            "chunk:practical-program-evaluation:ch05-the-conceptualization-facilitation-approach-under-development-facilitation-strat:c0002",
            "chunk:practical-program-evaluation:ch05-designing-pilot-testing:c0001",
            "chunk:practical-program-evaluation:ch05-questions-to-inform-the-evaluator-s-commentary-on-an-action-plan:c0001",
        ],
        "media_ids": [],
        "core": "Action-plan evaluation tests whether the program has the organizational, human, partnership, contextual, and delivery arrangements needed to implement the intervention.",
        "summary": [
            "Chapter 5 completes the planning-stage sequence by focusing on the action model. If Chapter 4 clarifies what change is intended, Chapter 5 asks whether stakeholders have a practical plan for making that change happen.",
            "The action model framework directs attention to implementers, implementing organizations, partners, ecological context, target populations, and delivery protocols. These components are interdependent, so a change to one component can alter the feasibility of the whole plan.",
            "Conceptualization facilitation helps stakeholders develop or improve the action plan. The evaluator's role is not merely to review documents, but to surface missing components, weak assumptions, and practical implementation risks.",
            "Pilot testing then provides field-based feedback before full implementation. It tests whether proposed activities, dosage, scheduling, settings, staff roles, and client responses are workable at a smaller scale.",
        ],
        "concepts": ["action plan", "action model", "conceptualization facilitation", "pilot testing", "implementing organization", "ecological context", "service delivery protocols"],
        "structure": ["action model framework", "conceptualization facilitation", "commentary on action plans", "pilot testing principles", "designing pilot tests", "revising the plan"],
        "implications": ["Assess implementer capacity and organizational support before launch.", "Use pilot testing to find practical delivery problems early.", "Treat the action plan as a theory that can be improved, not as an administrative formality."],
    },
    {
        "number": 6,
        "title": "Constructive Process Evaluation Tailored for the Initial Implementation",
        "pages": "174-196",
        "file": "chapter-06-constructive-process-evaluation-tailored-for-initial-implementation.qmd",
        "section_path": "Chapter 6: Constructive Process Evaluation Tailored for the Initial Implementation",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch06-constructive-process-evaluation-tailored-for-the-initial-implementation:c0001",
            "chunk:practical-program-evaluation:ch06-the-formative-evaluation-approach-under-the-troubleshooting-strategy:c0001",
            "chunk:practical-program-evaluation:ch06-the-program-review-development-meeting-under-the-troubleshooting-strategy:c0002",
            "chunk:practical-program-evaluation:ch06-pros-and-cons-of-bilateral-empowerment-evaluation:c0001",
        ],
        "media_ids": [],
        "core": "Initial implementation requires constructive process evaluation that rapidly identifies delivery problems, supports troubleshooting, and helps stakeholders stabilize the program.",
        "summary": [
            "Chapter 6 moves from planning to early implementation. At this stage, rules, procedures, staffing, recruitment, and delivery routines are still fluid, so the main evaluation need is timely information for improvement.",
            "Formative evaluation is the main troubleshooting approach. It uses flexible methods to identify barriers and facilitators, distinguish implementation problems from design problems, and help stakeholders make corrections while the program is still taking shape.",
            "Program review/development meetings are another troubleshooting tool, especially for surfacing staff experience and building shared understanding of implementation problems. Chen is clear that these meetings are mainly internal improvement tools, not substitutes for accountability evaluation.",
            "Bilateral empowerment evaluation extends the evaluator role into partnership. It can maximize the use of evaluation information during development, but it also creates limits for later independent accountability assessment.",
        ],
        "concepts": ["initial implementation", "constructive evaluation", "formative evaluation", "troubleshooting", "program review/development meeting", "bilateral empowerment evaluation", "implementation problem"],
        "structure": ["initial implementation concerns", "formative evaluation", "program review/development meetings", "bilateral empowerment evaluation", "pros and cons", "selection of approaches"],
        "implications": ["Use fast feedback when implementation routines are unstable.", "Do not confuse internal troubleshooting meetings with accountability evidence.", "Plan for role changes if evaluators later need to provide independent assessment."],
    },
    {
        "number": 7,
        "title": "Assessing Implementation in the Mature Implementation Stage",
        "pages": "197-220",
        "file": "chapter-07-assessing-implementation-in-the-mature-implementation-stage.qmd",
        "section_path": "Chapter 7: Assessing Implementation in the Mature Implementation Stage",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch07-assessing-implementation-in-the-mature-implementation-stage:c0001",
            "chunk:practical-program-evaluation:ch07-approaches-of-conclusive-process-evaluation:c0001",
            "chunk:practical-program-evaluation:ch07-fidelity-versus-reinvention-in-conclusive-process-evaluation:c0002",
            "chunk:practical-program-evaluation:ch07-hybrid-process-evaluation-theory-driven-process-evaluation:c0001",
        ],
        "media_ids": [],
        "core": "Mature implementation can support conclusive process evaluation, but evaluators may still need constructive or hybrid designs when accountability and improvement both matter.",
        "summary": [
            "Chapter 7 asks how to evaluate implementation once program procedures are routine. At this stage, stakeholders may need accountability evidence about whether the intervention is being delivered as intended.",
            "Fidelity evaluation is the main conclusive process approach. It can focus on intervention fidelity, referral fidelity, service delivery fidelity, target population fidelity, or other action-model components.",
            "The chapter also addresses the tension between fidelity and reinvention. Adaptation can be valuable during early development, but excessive deviation in mature implementation can dilute program integrity unless a defensible reason for change exists.",
            "Theory-driven process evaluation provides a hybrid alternative. It asks not only whether implementation matches the plan, but how implementation components contribute to the program's quality and performance.",
        ],
        "concepts": ["mature implementation", "conclusive evaluation", "fidelity evaluation", "reinvention", "theory-driven process evaluation", "hybrid evaluation", "implementation quality"],
        "structure": ["constructive process evaluation in maturity", "conclusive process evaluation", "fidelity approaches", "fidelity versus reinvention", "theory-driven process evaluation", "design fit"],
        "implications": ["Use fidelity evaluation when accountability for implementation quality is central.", "Distinguish useful adaptation from damaging drift.", "Use theory-driven process evaluation when stakeholders need both judgment and explanation."],
    },
    {
        "number": 8,
        "title": "Program Monitoring and the Development of a Monitoring System",
        "pages": "223-250",
        "file": "chapter-08-program-monitoring-and-the-development-of-a-monitoring-system.qmd",
        "section_path": "Chapter 8: Program Monitoring and the Development of a Monitoring System",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch08-what-is-program-monitoring:c0001",
            "chunk:practical-program-evaluation:ch08-program-monitoring-systems-within-organizations:c0001",
            "chunk:practical-program-evaluation:ch08-questions-for-reflection:c0001",
            "chunk:practical-program-evaluation:part-iv:c0001",
        ],
        "media_ids": [],
        "core": "Program monitoring supplies periodic process and outcome indicators for management and accountability, but it complements rather than replaces deeper process or outcome evaluation.",
        "summary": [
            "Chapter 8 explains program monitoring as periodic quantitative collection of process and outcome information. It provides vital statistics about implementation and client progress.",
            "Chen distinguishes monitoring from evaluation. Monitoring indicators can show direction, volume, coverage, and progress, but they usually do not provide the depth needed to explain implementation quality or establish outcome effectiveness.",
            "Process monitoring tracks service delivery and implementation. Outcome monitoring tracks client or program outcomes over time. The chapter argues that organizations often need an integrated monitoring system that connects both.",
            "Monitoring systems require organizational capacity, data routines, information systems, and accountability uses. Their value depends on whether indicators are meaningful and whether stakeholders understand the limits of what monitoring can claim.",
        ],
        "concepts": ["program monitoring", "process monitoring", "outcome monitoring", "performance monitoring", "indicator", "monitoring system", "accountability"],
        "structure": ["definition of monitoring", "process monitoring", "outcome monitoring", "monitoring versus evaluation", "organizational systems", "using monitoring data"],
        "implications": ["Build monitoring indicators around decisions and accountability needs.", "Avoid treating monitoring trends as causal impact evidence.", "Integrate process and outcome monitoring when both implementation and progress matter."],
    },
    {
        "number": 9,
        "title": "Constructive Outcome Evaluations",
        "pages": "252-267",
        "file": "chapter-09-constructive-outcome-evaluations.qmd",
        "section_path": "Chapter 9: Constructive Outcome Evaluations",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch09-constructive-outcome-evaluation:c0002",
            "chunk:practical-program-evaluation:ch09-plausibility-assessment-consensus-building-approach:c0001",
            "chunk:practical-program-evaluation:ch09-plausibility-assessment-consensus-building-approach-2:c0001",
            "chunk:practical-program-evaluation:ch09-plausibility-assessment-consensus-building-approach-2:c0009",
        ],
        "media_ids": [],
        "core": "Constructive outcome evaluation improves goals, evaluability, plausibility, and stakeholder consensus before a program is judged by outcome evidence.",
        "summary": [
            "Chapter 9 focuses on outcome-stage work that is still developmental. The aim is to strengthen the program's coherence and readiness for conclusive outcome evaluation.",
            "SMART goals help stakeholders develop goals that are specific and measurable. Evaluability assessment checks whether the program is organized well enough for a rigorous outcome evaluation to be meaningful.",
            "Plausibility assessment/consensus building addresses two common problems: official goals may not reflect what the program is actually doing, and stakeholder groups may not agree on which goals should be evaluated.",
            "Chen also warns against the goal trap. Evaluators should not take official goals at face value when they are symbolic, unrealistic, vague, or disconnected from operative practice.",
        ],
        "concepts": ["constructive outcome evaluation", "SMART goals", "evaluability assessment", "plausibility assessment", "goal trap", "operative goals", "consensus building"],
        "structure": ["purpose of constructive outcome work", "SMART goals", "evaluability assessment", "goal traps", "plausibility assessment", "consensus building"],
        "implications": ["Clarify and test goals before measuring them.", "Use evaluability assessment to avoid premature outcome evaluation.", "Surface operative and unintended goals before finalizing evaluation outcomes."],
    },
    {
        "number": 10,
        "title": "The Experimentation Evaluation Approach to Outcome Evaluation",
        "pages": "268-280",
        "file": "chapter-10-the-experimentation-evaluation-approach-to-outcome-evaluation.qmd",
        "section_path": "Chapter 10: The Experimentation Evaluation Approach to Outcome Evaluation",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch10-the-experimentation-evaluation-approach-to-outcome-evaluation:c0001",
            "chunk:practical-program-evaluation:ch10-research-designs-for-ruling-out-threats-to-internal-validity:c0001",
            "chunk:practical-program-evaluation:ch10-questions-for-reflection:c0001",
            "chunk:practical-program-evaluation:ch02-outcome-stage:c0001",
        ],
        "media_ids": [],
        "core": "The experimentation approach prioritizes internal validity and pure independent effects, making it valuable for some conclusive outcome questions but incomplete for many real-world evaluation needs.",
        "summary": [
            "Chapter 10 presents the dominant conclusive outcome tradition: validity-focused outcome evaluation guided by experimentation logic.",
            "The approach asks whether an intervention caused intended outcomes by ruling out threats to internal validity. It therefore values research designs that support credible causal inference, especially experimental and strong quasi-experimental designs.",
            "Chen treats the approach seriously but conditionally. It is appropriate when stakeholders need rigorous evidence about whether an intervention affected outcomes apart from confounding factors.",
            "The chapter also prepares the critique developed in Chapter 11. A design that maximizes internal validity may bracket the real-world supports and adaptations that stakeholders actually use to make interventions work.",
        ],
        "concepts": ["validity-focused outcome evaluation", "experimentation evaluation approach", "internal validity", "pure independent effects", "randomized experiment", "threats to validity", "conclusive outcome evaluation"],
        "structure": ["experimentation approach", "Campbellian validity logic", "threats to internal validity", "research designs", "strengths", "limits"],
        "implications": ["Use experimentation logic when pure causal attribution is the central question.", "Make validity threats explicit in outcome design.", "Do not assume internal-validity priority answers every stakeholder question."],
    },
    {
        "number": 11,
        "title": "The Holistic Effectuality Evaluation Approach to Outcome Evaluation",
        "pages": "283-324",
        "file": "chapter-11-the-holistic-effectuality-evaluation-approach-to-outcome-evaluation.qmd",
        "section_path": "Chapter 11: The Holistic Effectuality Evaluation Approach to Outcome Evaluation",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch11-the-holistic-effectuality-approach-s-conceptualization-of-outcome-evaluation:c0001",
            "chunk:practical-program-evaluation:ch11-conclusive-assessment:c0001",
            "chunk:practical-program-evaluation:ch11-methodology-for-real-world-outcome-evaluation:c0001",
            "chunk:practical-program-evaluation:ch11-checklist-for-ranking-real-world-evaluations:c0001",
        ],
        "media_ids": ["practical-program-evaluation:table:11.1:image"],
        "core": "Holistic effectuality evaluation reframes real-world outcome evaluation as a hybrid assessment of program coherence, capacity, joint effects, adjuvants, and bias.",
        "summary": [
            "Chapter 11 develops an alternative to the experimentation approach. Chen argues that real-world outcome evaluation often needs to assess the joint effects of an intervention and the adjuvants that help it work.",
            "The approach is hybrid. Constructive assessment first checks coherence, capacity, program theory, stakeholder participation, and vulnerabilities. Conclusive assessment then examines real-world effects without automatically treating every support or adaptation as a validity threat.",
            "The chapter is not anti-experimentation. It argues that the experimentation approach and holistic effectuality approach serve different priorities, and evaluators should choose by stakeholder need and program circumstance.",
            "The checklist for ranking real-world evaluations operationalizes this approach by rating constructive and conclusive components together, rather than ranking designs only by conventional experimental hierarchy.",
        ],
        "concepts": ["holistic effectuality evaluation", "real-world outcome evaluation", "adjuvant", "constructive assessment", "conclusive assessment", "joint effects", "checklist"],
        "structure": ["limits of experimentation logic", "hybrid real-world outcome evaluation", "constructive assessment", "conclusive assessment", "adjuvants", "ranking real-world evaluations"],
        "implications": ["Assess whether real-world supports are part of the intervention rather than mere threats.", "Combine readiness work with outcome assessment when programs are not yet coherent.", "Use design hierarchy cautiously when stakeholder usefulness depends on real-world effectuality."],
    },
    {
        "number": 12,
        "title": "The Theory-driven Approach to Outcome Evaluation",
        "pages": "325-360",
        "file": "chapter-12-the-theory-driven-approach-to-outcome-evaluation.qmd",
        "section_path": "Chapter 12: The Theory-driven Approach to Outcome Evaluation",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch12-the-theory-driven-approach-to-outcome-evaluation:c0001",
            "chunk:practical-program-evaluation:ch12-types-of-theory-driven-outcome-evaluation:c0001",
            "chunk:practical-program-evaluation:ch12-the-moderating-mechanism-evaluation-approach:c0001",
            "chunk:practical-program-evaluation:ch12-the-integrative-process-outcome-evaluation-approach:c0001",
        ],
        "media_ids": [],
        "core": "Theory-driven outcome evaluation explains how, why, and under what implementation conditions outcomes occur by examining mechanisms as well as effects.",
        "summary": [
            "Chapter 12 upgrades outcome evaluation from a works-or-does-not-work question to an explanatory assessment of transformation processes.",
            "The theory-driven approach examines program theory, causal mechanisms, and implementation. It is placed under the enlightenment strategy because it helps stakeholders understand why a program succeeds, fails, or works only under certain conditions.",
            "Chen distinguishes intervening mechanism evaluation, moderating mechanism evaluation, and integrative process/outcome evaluation. These designs focus respectively on mediating processes, conditioning factors, and the full connection between implementation and outcomes.",
            "The integrative process/outcome approach is the most comprehensive. It checks implementation assumptions and causal processes together, showing that implementation success is necessary but not sufficient for program success.",
        ],
        "concepts": ["theory-driven outcome evaluation", "intervening mechanism", "moderating mechanism", "integrative process/outcome evaluation", "implementation success", "causal mechanism", "program theory"],
        "structure": ["rationale for theory-driven outcome evaluation", "clarifying stakeholder theory", "types of mechanism evaluation", "moderating mechanisms", "integrative process/outcome evaluation", "mixed methods"],
        "implications": ["Use theory-driven outcome evaluation when stakeholders need explanation, not only verdicts.", "Match design to whether the question concerns mediation, moderation, or whole-program operation.", "Interpret implementation success as necessary but not sufficient for outcome success."],
    },
    {
        "number": 13,
        "title": "What to Do If Your Logic Model Does Not Work as Well as Expected",
        "pages": "364-385",
        "file": "chapter-13-what-to-do-if-your-logic-model-does-not-work-as-well-as-expected.qmd",
        "section_path": "Chapter 13: What to Do If Your Logic Model Does Not Work as Well as Expected",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch13-what-to-do-if-your-logic-model-does-not-work-as-well-as-expected:c0001",
            "chunk:practical-program-evaluation:ch13-applying-the-logic-model:c0001",
            "chunk:practical-program-evaluation:ch13-applying-the-action-model-change-model-schema-2:c0002",
            "chunk:practical-program-evaluation:ch13-a-guide-to-productively-applying-the-logic-model-and-the-action-model-change-mod:c0001",
            "chunk:practical-program-evaluation:ch13-a-guide-to-productively-applying-the-logic-model-and-the-action-model-change-mod:c0003",
        ],
        "media_ids": [],
        "core": "Logic models often help, but programs that mix intervention delivery with system change may need the action model/change model schema to clarify context, partnership, and causal mechanisms.",
        "summary": [
            "Chapter 13 revisits logic models through two applied cases. The point is not that logic models are useless, but that they can be too limited for programs where system change is part of the intervention.",
            "In such cases, stakeholders may struggle to distinguish activities, contextual change, intervention components, and outcomes. A standard logic model can compress these distinctions until the model becomes confusing or misleading.",
            "The action model/change model schema helps by making context, partnership, community awareness, needs assessment, interventions, and mechanisms more explicit.",
            "Chen offers reactive and proactive options. Evaluators can continue with logic models and add the schema when problems arise, or use the schema from the outset when they know the program involves system change and contextual mechanisms.",
        ],
        "concepts": ["logic model", "system change", "action model", "change model", "reactive approach", "proactive approach", "contextual factors"],
        "structure": ["logic-model limitations", "diversity enhancement case", "community health initiative case", "action model/change model clarification", "reactive approach", "proactive approach"],
        "implications": ["Check whether a logic model is hiding system-change work.", "Use the action model/change model schema when context and partnership are central.", "Choose reactive or proactive supplementation based on foreseeable model risk."],
    },
    {
        "number": 14,
        "title": "Formal Theories versus Stakeholder Theories in Interventions: Relative Strengths and Limitations",
        "pages": "387-410",
        "file": "chapter-14-formal-theories-versus-stakeholder-theories-in-interventions.qmd",
        "section_path": "Chapter 14: Formal Theories versus Stakeholder Theories in Interventions: Relative Strengths and Limitations",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch14-efforts-to-clarify-the-change-model-and-action-model-in-program-theory:c0001",
            "chunk:practical-program-evaluation:ch04-determinants-and-types-of-action-model-change-model-schemas:c0001",
            "chunk:practical-program-evaluation:ch03-program-theory:c0001",
            "chunk:practical-program-evaluation:ch03-applying-the-action-model-change-model-schema-an-example:c0001",
        ],
        "media_ids": [],
        "core": "Formal theory and stakeholder theory each strengthen and weaken different parts of program theory, so evaluators must clarify both change logic and action arrangements before judging an intervention.",
        "summary": [
            "Chapter 14 compares interventions grounded mainly in formal theory with interventions grounded mainly in stakeholder theory.",
            "Formal theory can provide a clearer literature-based change model, especially about determinants and causal assumptions. It may also come with protocols that help specify the intervention.",
            "Stakeholder theory is often more locally grounded and practice-sensitive, but it is usually less explicit in documents and literature. Evaluators therefore need to help stakeholders articulate assumptions that may otherwise remain implicit.",
            "The chapter's practical lesson is diagnostic. Evaluators should ask which part of program theory is strong or weak: the change model, the action model, the intervention protocol, implementation arrangements, or the fit between local practice and formal theory.",
        ],
        "concepts": ["formal theory", "stakeholder theory", "program theory", "change model", "action model", "intervention protocol", "determinants"],
        "structure": ["formal theory-based interventions", "stakeholder theory-based interventions", "change model clarification", "action model clarification", "relative strengths", "relative limitations"],
        "implications": ["Use formal theory where it clarifies determinants and mechanisms.", "Do not assume local stakeholder theory is explicit enough for evaluation.", "Assess change and action models separately when comparing intervention theories."],
    },
    {
        "number": 15,
        "title": "Evaluation and Dissemination: Top-down Approach versus Bottom-up Approach",
        "pages": "413-432",
        "file": "chapter-15-evaluation-and-dissemination-top-down-approach-versus-bottom-up-approach.qmd",
        "section_path": "Chapter 15: Evaluation and Dissemination: Top-down Approach versus Bottom-up Approach",
        "evidence_ids": [
            "chunk:practical-program-evaluation:ch15-integrative-cogency-model-the-integrated-evaluation-perspective:c0001",
            "chunk:practical-program-evaluation:ch15-integrative-cogency-model-the-integrated-evaluation-perspective:c0002",
            "chunk:practical-program-evaluation:ch15-the-bottom-up-approach:c0001",
            "chunk:practical-program-evaluation:ch15-the-current-version-of-evidence-based-interventions-limitations-and-strategies-t:c0006",
            "chunk:practical-program-evaluation:ch15-the-usefulness-of-the-bottom-up-approach-and-the-integrative-cogency-model:c0003",
        ],
        "media_ids": [],
        "core": "Dissemination should not rely only on top-down efficacy evidence; real-world evaluation also needs viable, effectual, and transferable cogency.",
        "summary": [
            "Chapter 15 closes the book by connecting evaluation to dissemination and evidence-based intervention debates.",
            "The top-down approach privileges efficacy evidence, often from randomized controlled trials, before intervention spread. Chen argues that this can be too narrow for social betterment and health promotion programs, where stakeholder practice, feasibility, and context matter.",
            "The integrative cogency model reframes credible evidence as multidimensional. Evaluators need evidence about viability, effectuality, and transferability rather than only a single internal-validity-centered claim.",
            "The bottom-up approach reverses the usual order: begin with real-world viability and effectiveness, improve the intervention through practical feedback, and then use more controlled efficacy evidence when it adds value.",
        ],
        "concepts": ["top-down approach", "bottom-up approach", "integrative cogency model", "viable cogency", "effectual cogency", "transferable cogency", "evidence-based intervention"],
        "structure": ["top-down dissemination", "limits of evidence-based intervention", "integrative cogency model", "bottom-up approach", "viability and effectiveness", "method contingency"],
        "implications": ["Assess real-world viability before assuming an intervention is ready to disseminate.", "Use evidence standards that match social-program complexity.", "Treat RCT evidence as powerful for some questions, not as the only credible evidence."],
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


def mermaid_label(text: str) -> str:
    return text.replace('"', "'")


def metadata(extra: list[str]) -> str:
    spans = "".join(f"<span>{item}</span>" for item in [YEAR, *extra])
    return f'<div class="chapter-meta">{spans}</div>'


def chapter_link(chapter: dict) -> str:
    return f"[Chapter {chapter['number']}: {chapter['title']}]({chapter['file']})"


def sentence_join(items: list[str], limit: int = 4) -> str:
    selected = items[:limit]
    if len(selected) == 1:
        return selected[0]
    return ", ".join(selected[:-1]) + f", and {selected[-1]}"


def concept_gloss(concept: str) -> str:
    return CONCEPT_GLOSSES[concept.lower()]


def render_concept_map(chapter: dict) -> str:
    concepts = chapter["concepts"][:3]
    mechanisms = chapter["structure"][:3]
    implications = chapter["implications"][:2]
    lines = [
        "::: {.concept-map}",
        "```{mermaid}",
        "flowchart TD",
        f'  Problem["Problem: What does Chapter {chapter["number"]} help decide?"]',
        f'  Central["Concept: {mermaid_label(chapter["title"])}"]',
    ]
    for idx, concept in enumerate(concepts, start=1):
        lines.append(f'  Concept{idx}["Concept: {mermaid_label(concept)}"]')
    for idx, mechanism in enumerate(mechanisms, start=1):
        lines.append(f'  Mechanism{idx}["Mechanism: {mermaid_label(mechanism)}"]')
    for idx, implication in enumerate(implications, start=1):
        lines.append(f'  Implication{idx}["Practice implication: {mermaid_label(implication)}"]')
    lines.append('  Question["Open question: What evidence would make this usable in a live evaluation?"]')
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


def render_book_connection(chapter: dict) -> str:
    number = chapter["number"]
    if number <= 3:
        return "Within the wider book, this chapter belongs to the foundations sequence: it defines evaluation fit, typology, and program theory before any stage-specific evaluation is selected."
    if number <= 5:
        return "Within the wider book, this chapter belongs to the planning sequence: it helps stakeholders clarify program scope and action plan before implementation begins."
    if number <= 8:
        return "Within the wider book, this chapter belongs to the implementation sequence: it separates early troubleshooting, mature implementation assessment, and routine monitoring."
    if number <= 12:
        return "Within the wider book, this chapter belongs to the outcome sequence: it moves from readiness for outcome evaluation to experimentation, real-world effectuality, and theory-driven explanation."
    return "Within the wider book, this chapter belongs to the advanced sequence: it tests the limits of common tools and connects evaluation evidence to theory, system change, and dissemination."


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
        f'source_pages: "{chapter["pages"]}"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence_ids),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        metadata(["MCP evaluation-texts", "Status: needs_review", f"Chapter {chapter['number']}", f"Source pages {chapter['pages']}"]),
        "",
        f"This note summarises Chapter {chapter['number']}, \"{chapter['title']},\" from {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. It is a paraphrased study note based on source-linked MCP research-library retrieval records, not a substitute for the chapter.",
        "",
        "The retrieval trail is retained in the source records at the bottom of the page. The note paraphrases the chapter's argument and procedures, and it does not reproduce textbook tables, review questions, checklists, exhibits, or extended passages. When a table or figure is central, the note describes its function and leaves the source artifact in the evidence record.",
        "",
        "## Core Argument",
        "",
        chapter["core"],
        "",
        "## Study Summary",
        "",
    ]
    for paragraph in chapter["summary"]:
        body.extend([paragraph, ""])
    body.extend(
        [
            f"For close reading, track how the chapter uses {sentence_join(chapter['concepts'])} while moving through {sentence_join(chapter['structure'], 3)}. The notes below identify what the chapter asks the evaluator to notice, what design problem it helps solve, and what should be checked against the saved evidence records before relying on the summary in applied work.",
            "",
            render_book_connection(chapter),
            "",
            "## Key Concepts",
            "",
        ]
    )
    body.extend(f"- **{concept}**: {concept_gloss(concept)}" for concept in chapter["concepts"])
    body.extend(["", "## Chapter Structure", ""])
    body.extend(f"- {item.capitalize()}." for item in chapter["structure"])
    body.extend(["", "## Practical Implications", ""])
    body.extend(f"- {item}" for item in chapter["implications"])
    body.extend(["", "## Concept Map", "", render_concept_map(chapter), "", "## Connections", ""])
    body.extend(
        [
            "- Book overview: [Overview](index.qmd)",
            "- Reading route: [Chapter Map](chapter-map.qmd)",
            "- Concepts synthesis: [Core Concepts](concepts.qmd)",
            "- Practice synthesis: [Practice Implications](practice-implications.qmd)",
        ]
    )
    if prev_chapter:
        body.append(f"- Previous: {chapter_link(prev_chapter)}")
    if next_chapter:
        body.append(f"- Next: {chapter_link(next_chapter)}")
    if chapter["number"] in {1, 3, 13}:
        for title, path in LEGACY_EXTRACTS:
            body.append(f"- Legacy extract retained: [{title}]({path})")
    body.extend(
        [
            "",
            "## Study Prompts",
            "",
            f"1. What evaluation design decision does Chapter {chapter['number']} help make?",
            "2. Which stakeholder assumptions would need evidence before applying this guidance?",
            "3. How would this chapter change scoping, data collection, interpretation, or use?",
            "4. Where could this guidance be misused if treated as a fixed template?",
            "",
            "## Source Records",
            "",
            source_chunks(evidence_ids),
            "",
            "## References",
            "",
            f"- Chen, H. T. ({YEAR}). *{FULL_TITLE}*. {PUBLISHER}. Chapter {chapter['number']}, pages {chapter['pages']}.",
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
        "::: {.directory-hero}",
        '<span class="hero-eyebrow">Book notes</span>',
        "",
        f"# {TITLE}",
        "",
        f"Study notes on *{FULL_TITLE}* [@{CITATION}]. These chapter notes are generated from source-linked MCP research-library records and are intended for study, comparison, and later refinement.",
        "",
        '<div class="page-metadata">',
        "  <span>15 chapter notes</span>",
        f"  <span>{YEAR}</span>",
        "  <span>Source status: needs_review</span>",
        "  <span>MCP evaluation-texts</span>",
        "</div>",
        ":::",
        "",
        "```{=html}",
        '<nav class="book-nav" aria-label="Book navigation">',
        '  <a href="index.qmd">Overview</a>',
        '  <a href="concepts.qmd">Core Concepts</a>',
        '  <a href="chapter-map.qmd">Chapter Map</a>',
        '  <a href="practice-implications.qmd">Practice</a>',
        "</nav>",
        "```",
        "",
        "::: {.section-grid synthesis-grid}",
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
        "Full reading route for all 15 chapters.",
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
        "Practical evaluation design should match program stage, stakeholder needs, program theory, and intended use, choosing among constructive, conclusive, and hybrid approaches rather than defaulting to one method or one model of evidence.",
        "",
        "## Chapter Notes",
        "",
    ]
    for chapter in CHAPTERS:
        lines.append(f"- {chapter_link(chapter)} - source pages {chapter['pages']}")
    lines.extend(
        [
            "",
            "## Legacy Extracts",
            "",
        ]
    )
    for title, path in LEGACY_EXTRACTS:
        lines.append(f"- [{title}]({path})")
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_chapter_map() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    groups = [
        ("Foundations", CHAPTERS[:3]),
        ("Planning", CHAPTERS[3:5]),
        ("Implementation and Monitoring", CHAPTERS[5:8]),
        ("Outcome Evaluation", CHAPTERS[8:12]),
        ("Advanced Issues and Dissemination", CHAPTERS[12:]),
    ]
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
    for heading, chapters in groups:
        lines.extend([f"### {heading}", ""])
        for chapter in chapters:
            lines.append(f"- {chapter_link(chapter)} - pages {chapter['pages']}; `{chapter['section_path']}`")
        lines.append("")
    lines.extend(
        [
            "## How to Use This Map",
            "",
            "- Start with Chapters 1-3 to select the evaluation route and clarify program theory.",
            "- Use Chapters 4-5 when the program is still being planned and needs program-scope or action-plan work.",
            "- Use Chapters 6-8 for early implementation, mature implementation, and monitoring-system questions.",
            "- Use Chapters 9-12 for outcome readiness, causal rigor, real-world effectuality, and theory-driven explanation.",
            "- Use Chapters 13-15 when logic models, theory sources, or dissemination assumptions need more advanced treatment.",
            "",
            "## Legacy Extracts",
            "",
        ]
    )
    for title, path in LEGACY_EXTRACTS:
        lines.append(f"- [{title}]({path})")
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    concept_groups = [
        ("Evaluation Fit", ["fundamental evaluation typology", "comprehensive evaluation typology", "constructive evaluation", "conclusive evaluation", "hybrid evaluation"]),
        ("Program Theory", ["logic model", "program theory", "action model", "change model", "stakeholder theory", "formal theory"]),
        ("Planning and Implementation", ["program scope", "action plan", "needs assessment", "pilot testing", "formative evaluation", "fidelity evaluation"]),
        ("Monitoring and Outcomes", ["program monitoring", "constructive outcome evaluation", "validity-focused outcome evaluation", "holistic effectuality evaluation", "theory-driven outcome evaluation"]),
        ("Evidence and Dissemination", ["adjuvant", "system change", "integrative cogency model", "viable cogency", "effectual cogency", "transferable cogency"]),
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
        "The book treats practical evaluation as a staged, contingent design problem: clarify the program, identify its stage, select constructive, conclusive, or hybrid approaches, and judge evidence by usefulness as well as technical credibility.",
        "",
        "## Concepts",
        "",
    ]
    for heading, concepts in concept_groups:
        lines.extend([f"### {heading}", ""])
        for concept in concepts:
            lines.append(f"- {concept}: {concept_gloss(concept)}")
        lines.append("")
    lines.extend(["## Links", ""])
    lines.extend(f"- {chapter_link(chapter)}" for chapter in CHAPTERS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    implications = [
        "Begin by identifying the program stage and the evaluation function: constructive, conclusive, or hybrid.",
        "Use the comprehensive typology as a routing tool, not as a rigid checklist.",
        "Clarify program theory before choosing measures or causal designs.",
        "Separate program scope from action plan so change logic and implementation arrangements can both be tested.",
        "Use formative and troubleshooting approaches during initial implementation rather than demanding premature accountability evidence.",
        "Use fidelity or theory-driven process evaluation once implementation is mature enough to judge.",
        "Treat monitoring as useful for performance tracking, but insufficient for causal claims.",
        "Use constructive outcome evaluation before conclusive outcome evaluation when goals, evaluability, or stakeholder consensus are weak.",
        "Choose experimentation, holistic effectuality, or theory-driven outcome evaluation according to the question stakeholders actually need answered.",
        "Use logic models carefully when programs involve system change, contextual mechanisms, or partnership work.",
        "Assess dissemination evidence through viability, effectuality, and transferability rather than efficacy alone.",
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
    ]
    lines.extend(f"- {item}" for item in implications)
    lines.extend(["", "## Links", ""])
    lines.extend(f"- {chapter_link(chapter)}" for chapter in CHAPTERS)
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
                "section_id": f"chapter-{chapter['number']:02d}",
                "section_title": f"Chapter {chapter['number']}: {chapter['title']}",
                "source_pages": chapter["pages"],
                "section_path": chapter["section_path"],
                "evidence_ids": chapter["evidence_ids"],
                "media_ids": chapter["media_ids"],
                "target_path": f"notes/{SLUG}/{chapter['file']}",
            }
            for chapter in CHAPTERS
        ],
    }


def render_chapter_evidence_summary() -> dict:
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
            "limit": "targeted chapter retrieval; broad full-book evidence pack used before synthesis",
            "include_media": "true for full-book grounding and table/figure-heavy chapters",
        },
        "chapters": [
            {
                "chapter_number": chapter["number"],
                "chapter_title": chapter["title"],
                "target_path": f"notes/{SLUG}/{chapter['file']}",
                "section_paths": [chapter["section_path"]],
                "source_pages": chapter["pages"],
                "evidence_ids": chapter["evidence_ids"],
                "media_ids": chapter["media_ids"],
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
            book["generation_mode"] = "generated-chapter-notes"
            book["target_path"] = f"notes/{SLUG}/index.qmd"
            book["sections"] = [
                {
                    "id": f"chapter-{chapter['number']:02d}",
                    "title": f"Chapter {chapter['number']}: {chapter['title']}",
                    "source_pages": chapter["pages"],
                    "section_path": chapter["section_path"],
                    "evidence_ids": chapter["evidence_ids"],
                    "target_path": f"notes/{SLUG}/{chapter['file']}",
                }
                for chapter in CHAPTERS
            ]
            break
    else:
        raise SystemExit(f"{BOOK_ID} not found in manifest")
    write_json("data/research_library_notes_manifest.json", manifest)


def patch_overview_copy() -> None:
    replacements = {
        "with detailed notes for Purposeful Program Theory, chapter-level Rossi/Lipsey notes, and generated notes for the wider collection.": (
            "with detailed notes for Purposeful Program Theory, chapter-level Rossi/Lipsey and Chen notes, and generated notes for the wider collection."
        ),
        "with detailed hand-authored notes for Purposeful Program Theory and generated major-section notes for the wider collection.": (
            "with detailed notes for Purposeful Program Theory, chapter-level Rossi/Lipsey and Chen notes, and generated notes for the wider collection."
        ),
    }
    home = ROOT / "index.qmd"
    text = home.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    home.write_text(text, encoding="utf-8")

    notes_replacements = {
        "The notes combine the existing hand-authored Purposeful Program Theory section, chapter-level Rossi/Lipsey notes, and generated notes for the other ready evaluation texts.": (
            "The notes combine the existing hand-authored Purposeful Program Theory section, chapter-level Rossi/Lipsey and Chen notes, and generated notes for the other ready evaluation texts."
        ),
        "The notes combine the existing hand-authored Purposeful Program Theory section with generated major-section notes for the other ready evaluation texts.": (
            "The notes combine the existing hand-authored Purposeful Program Theory section, chapter-level Rossi/Lipsey and Chen notes, and generated notes for the other ready evaluation texts."
        ),
    }
    notes = ROOT / "notes" / "index.qmd"
    text = notes.read_text(encoding="utf-8")
    for old, new in notes_replacements.items():
        text = text.replace(old, new)
    notes.write_text(text, encoding="utf-8")


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
    patch_overview_copy()


if __name__ == "__main__":
    generate()
