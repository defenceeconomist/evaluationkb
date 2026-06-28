#!/usr/bin/env python3
"""Generate ETMA-style Magenta Book study notes from curated evidence metadata."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "magenta-book"
SLUG = BOOK_ID
TITLE = "Magenta Book"
FULL_TITLE = "Magenta Book: Central Government guidance on evaluation"
AUTHORS = "HM Treasury and Evaluation Task Force"
CITATION = "hm_treasury_evaluation_task_force_2020_magenta_book"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2020"
PUBLISHER = "HM Treasury"
GENERATED_AT = "2026-06-27"


CONCEPT_GLOSSES = {
    "accountability": "Use of evaluation evidence to support scrutiny, transparency, spending decisions, and public confidence.",
    "adaptive management": "Management that expects learning, review, and adjustment as intervention context and evidence change.",
    "administrative data": "Operational data collected by public services or delivery systems that can support evaluation if fit for purpose.",
    "analysis transparency": "Preserving and, where proportionate, sharing the materials, data, code, and choices behind evaluation analysis.",
    "benefits management": "Project discipline for defining, measuring, and realising intended benefits while evaluation tests contribution and value.",
    "capability": "The knowledge, skills, roles, and behaviours required to scope, manage, deliver, and use evaluation well.",
    "causal attribution": "Reasoning about whether observed outcomes were caused by the intervention rather than other factors.",
    "complexity": "Conditions such as uncertainty, interdependence, emergence, nonlinearity, and multiple stakeholder perspectives.",
    "counterfactual": "An estimate of what would have happened without the intervention, used to support impact claims.",
    "data access": "The legal, ethical, technical, and practical ability to obtain data needed for evaluation questions.",
    "data quality": "The fitness of evaluation data, including relevance, validity, completeness, timeliness, and bias control.",
    "dissemination": "Planned communication of findings to audiences who need evidence for decisions, scrutiny, or learning.",
    "evaluation design": "The plan that connects evaluation purpose, questions, theory, data, methods, governance, analysis, and use.",
    "evaluation ethics": "Attention to rights, consent, privacy, harm, fairness, and appropriate handling of participants and data.",
    "evaluation plan": "A practical specification of questions, methods, data, responsibilities, timing, resources, and use.",
    "evaluation question": "A focused question that determines what evidence and analysis an evaluation must provide.",
    "evaluation registry": "A transparency mechanism for recording planned, live, and completed government evaluations.",
    "evaluation use": "The application of evaluation evidence in policy decisions, delivery improvement, accountability, or learning.",
    "experimental methods": "Impact designs that use random assignment or controlled rollout to estimate causal effects.",
    "external validity": "The extent to which impact findings can inform decisions beyond the specific evaluated setting.",
    "impact evaluation": "Evaluation focused on whether, to what extent, how, and why an intervention caused outcomes.",
    "internal validity": "The credibility of the causal estimate for the intervention and setting being evaluated.",
    "learning": "Use of evaluation to reduce uncertainty, improve interventions, and strengthen future policy design.",
    "logic model": "A representation of how inputs, activities, outputs, outcomes, and impacts are expected to connect.",
    "mixed methods": "Use of qualitative, quantitative, and other evidence sources together to answer complementary questions.",
    "monitoring": "Routine tracking of delivery, outputs, performance, or benefits that can inform but does not replace evaluation.",
    "open science": "Practices that make research plans, materials, analysis, and outputs more transparent and accessible.",
    "policy impact evaluation": "Impact evaluation applied to government policy, with attention to attribution, design quality, and feasibility.",
    "pre-registration": "Documenting evaluation plans or analysis choices before data collection or analysis to reduce selective reporting.",
    "process evaluation": "Evaluation of whether and how an intervention is implemented, how it operates, and why delivery varies.",
    "proportionality": "Matching evaluation effort, design, cost, and transparency to risk, scale, uncertainty, and decision value.",
    "qualitative quality": "Judgment about whether qualitative design, sampling, data, analysis, and reporting are fit for purpose.",
    "quasi-experimental methods": "Impact designs that construct credible comparison groups without random assignment.",
    "realist evaluation": "Theory-based evaluation that tests context-mechanism-outcome explanations of what works, for whom, and how.",
    "reporting transparency": "Clear reporting of methods, uncertainty, robustness, limitations, and interpretation.",
    "robustness": "The extent to which findings remain credible under reasonable checks, assumptions, and alternative analyses.",
    "scoping": "Early work to clarify the intervention, theory of change, users, questions, data, methods, and feasibility.",
    "steering group": "A governance body that reviews design, quality, feasibility, emerging findings, and use.",
    "synthesis": "Combining evidence from multiple sources or studies to answer evaluation questions and support judgment.",
    "test and learn": "An iterative approach that tests assumptions, learns from real-world feedback, and adapts before scaling.",
    "theory of change": "An explanation of how an intervention is expected to produce outcomes, including assumptions and mechanisms.",
    "theory-based methods": "Impact methods that test causal explanations and contribution claims using multiple evidence sources.",
    "transparency": "Making evaluation plans, evidence, analysis, and findings open enough to support trust, challenge, and reuse.",
    "triangulation": "Using multiple evidence sources or methods to test, compare, and strengthen interpretation.",
    "value for money": "Evaluation of costs, benefits, efficiency, economy, effectiveness, equity, and overall public value.",
}


NOTES = [
    {
        "kind": "core",
        "number": 0,
        "title": "Executive Summary and Evaluation Types",
        "file": "executive-summary.qmd",
        "note_type": "Executive",
        "pages": "3",
        "section_path": "Executive summary",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-executive-summary:c0002",
            "chunk:magenta-book:magenta-book-executive-summary:c0003",
        ],
        "core": "The executive summary positions evaluation as a government learning and accountability discipline that must combine evaluation types, methods, stages, and standards.",
        "summary": [
            "The summary frames evaluation as a way to understand whether interventions are designed well, delivered as intended, producing results, and offering value for money. It resists treating process, impact, and economic evaluation as isolated exercises.",
            "Learning and accountability are the main reasons for evaluation. Learning helps government manage uncertainty, improve live interventions, and build evidence for future policy. Accountability helps departments explain outcomes, spending, and public value to decision-makers, scrutiny bodies, and the public.",
            "The summary also acts as a route map. It identifies the core chapters on scoping, methods, data, management, dissemination, and capability, then points to annexes that deepen specialist topics such as analytical methods, quality, realist evaluation, complexity, transparency, AI, and test-and-learn practice.",
        ],
        "concepts": ["learning", "accountability", "process evaluation", "impact evaluation", "value for money", "evaluation design", "proportionality"],
        "structure": ["learning and accountability purposes", "key evaluation terminology", "core chapter route", "annex and supplementary guidance route"],
        "implications": [
            "Treat evaluation type as a design decision linked to the decision problem, not a label added after commissioning.",
            "Plan process, impact, and value for money evidence together when the intervention needs an integrated judgment.",
            "Use the chapter and annex route to find the right level of technical detail for the evaluation decision at hand.",
        ],
    },
    {
        "kind": "core",
        "number": 1,
        "title": "Why, How and When to Evaluate?",
        "file": "chapter-01-why-how-and-when-to-evaluate.qmd",
        "note_type": "Chapter",
        "pages": "4",
        "section_path": "1. Why, how and when to evaluate?",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-1-why-how-and-when-to-evaluate:c0002",
            "chunk:magenta-book:magenta-book-1-why-how-and-when-to-evaluate:c0003",
            "chunk:magenta-book:magenta-book-1-why-how-and-when-to-evaluate:c0013",
            "chunk:magenta-book:magenta-book-1-why-how-and-when-to-evaluate:c0018",
            "chunk:magenta-book:magenta-book-1-why-how-and-when-to-evaluate:c0021",
        ],
        "core": "Evaluation should be planned early, proportionately, and around real decisions so government can learn, account for public spending, and improve outcomes.",
        "summary": [
            "Chapter 1 explains evaluation as planned inquiry into whether an intervention is working, why it is working or not, for whom, and at what value. It is written for decision-makers and analysts, but also signals expectations to suppliers and external commissioners.",
            "The chapter ties evaluation to the policy and project lifecycle. Evaluation needs should be considered during business case development, intervention design, monitoring, benefits management, and delivery, because waiting until the end can leave too little data or too few comparison options.",
            "A good evaluation is useful, credible, robust, proportionate, and transparent. Those qualities shape decisions about independence, stakeholder needs, data quality, method choice, communication, and the limits that must accompany findings.",
            "The chapter also distinguishes users of evaluation evidence. Ministers, accounting officers, policy teams, delivery teams, finance professionals, analysts, scrutiny bodies, the public, and researchers may need different products and timing from the same evaluation.",
        ],
        "concepts": ["learning", "accountability", "benefits management", "evaluation use", "proportionality", "transparency", "evaluation design"],
        "structure": ["what policy evaluation is", "why evaluate", "when to plan evaluation", "benefits management and monitoring", "good evaluation principles", "users and stages"],
        "implications": [
            "Build evaluation expectations into business cases and delivery plans before data options close.",
            "Clarify who will use findings and what decision or scrutiny need they serve.",
            "Use quality principles to choose a feasible design rather than maximising technical ambition in the abstract.",
        ],
    },
    {
        "kind": "core",
        "number": 2,
        "title": "Evaluation Scoping",
        "file": "chapter-02-evaluation-scoping.qmd",
        "note_type": "Chapter",
        "pages": "5",
        "section_path": "2. Evaluation scoping",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-2-evaluation-scoping:c0003",
            "chunk:magenta-book:magenta-book-2-evaluation-scoping:c0010",
            "chunk:magenta-book:magenta-book-2-evaluation-scoping:c0014",
            "chunk:magenta-book:magenta-book-2-evaluation-scoping:c0016",
            "chunk:magenta-book:magenta-book-2-evaluation-scoping:c0025",
        ],
        "core": "Scoping turns an intervention, its theory of change, users, and uncertainties into answerable evaluation questions and a feasible design route.",
        "summary": [
            "Chapter 2 treats scoping as the disciplined bridge between policy need and evaluation design. Evaluators need to understand the intervention, its context, its theory of change, and what decisions the evaluation must inform.",
            "A theory of change is used to identify assumptions, mechanisms, outcomes, data needs, and evidence gaps. The chapter stresses that evaluation approaches can be complementary: process evidence can support theory-based impact claims, and value for money work usually depends on impact evidence.",
            "Evaluation questions are a control point. A long list of possible questions has to be prioritised into a smaller set of high-level questions that can guide design and remain manageable across delivery.",
            "Scoping also includes practical feasibility: data access, timing, resources, stakeholder needs, ethical issues, transparency, and whether planned methods can answer the priority questions.",
        ],
        "concepts": ["scoping", "theory of change", "evaluation question", "evaluation design", "data access", "pre-registration", "proportionality"],
        "structure": ["understanding the intervention", "theory of change", "evaluation types and approaches", "evaluation questions", "design and feasibility", "registration"],
        "implications": [
            "Use the theory of change to decide what evidence matters, not only to describe the programme.",
            "Prioritise evaluation questions before committing to methods or supplier specifications.",
            "Document design changes transparently when feasibility or evidence changes during implementation.",
        ],
    },
    {
        "kind": "core",
        "number": 3,
        "title": "Evaluation Methods",
        "file": "chapter-03-evaluation-methods.qmd",
        "note_type": "Chapter",
        "pages": "6",
        "section_path": "3. Evaluation methods",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-3-evaluation-methods:c0001",
            "chunk:magenta-book:magenta-book-3-evaluation-methods:c0003",
            "chunk:magenta-book:magenta-book-3-evaluation-methods:c0006",
            "chunk:magenta-book:magenta-book-3-evaluation-methods:c0012",
            "chunk:magenta-book:magenta-book-3-evaluation-methods:c0015",
        ],
        "core": "Method choice should follow the evaluation questions, theory of change, assumptions, feasibility, and stakeholder need for causal, process, synthesis, or value for money evidence.",
        "summary": [
            "Chapter 3 surveys methods for government evaluation and groups them around generic research methods, theory-based impact evaluation, experimental and quasi-experimental impact evaluation, value for money analysis, and synthesis.",
            "The chapter warns against method-led evaluation. No single method answers every evaluation question, and most evaluations need mixed methods because process, impact, and economic questions illuminate different parts of the intervention.",
            "Theory-based methods are used when causal explanation, mechanisms, context, and contribution matter. Experimental and quasi-experimental methods are used when credible comparison is feasible and the evaluation needs stronger attribution.",
            "Value for money methods need to be planned early and aligned with appraisal and impact evidence. Synthesis methods help combine existing evidence, but the suitability of each approach depends on the evidence base and evaluation purpose.",
        ],
        "concepts": ["mixed methods", "theory-based methods", "experimental methods", "quasi-experimental methods", "value for money", "synthesis", "causal attribution"],
        "structure": ["method selection", "generic research methods", "theory-based impact methods", "experimental and quasi-experimental methods", "value for money methods", "synthesis methods"],
        "implications": [
            "Choose methods after clarifying questions, theory, assumptions, and feasible data.",
            "Use mixed methods when implementation, impact, and value questions all matter.",
            "Make tradeoffs explicit when cost, timing, ethics, or respondent burden limit the strongest method.",
        ],
    },
    {
        "kind": "core",
        "number": 4,
        "title": "Data Collection, Data Access and Data Linking",
        "file": "chapter-04-data-collection-data-access-and-data-linking.qmd",
        "note_type": "Chapter",
        "pages": "7",
        "section_path": "4. Data collection, data access and data linking",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-4-data-collection-data-access-and-data-linking:c0001",
            "chunk:magenta-book:magenta-book-4-data-collection-data-access-and-data-linking:c0002",
            "chunk:magenta-book:magenta-book-4-data-collection-data-access-and-data-linking:c0004",
            "chunk:magenta-book:magenta-book-4-data-collection-data-access-and-data-linking:c0005",
            "chunk:magenta-book:magenta-book-4-data-collection-data-access-and-data-linking:c0013",
        ],
        "core": "Evaluation data must be planned with the intervention, because evidence quality, access, linkage, and governance determine what questions can be answered.",
        "summary": [
            "Chapter 4 treats data planning as central to evaluation design. Data access, collection, and linkage need attention while the intervention is still being designed; otherwise the eventual evaluation may be weak, expensive, or impossible.",
            "The chapter distinguishes existing administrative and monitoring data, long-term surveys, and new primary data collection. Existing data can reduce cost and burden, but it may not align exactly with evaluation questions or collect measures at the right time.",
            "Triangulation strengthens confidence by combining sources such as monitoring data, surveys, interviews, social media data, and bespoke research. Data quality checks, piloting, bias reduction, and clear definitions matter across all sources.",
            "The chapter also foregrounds data protection, access protocols, and data linking. Linking can enrich evaluation datasets, but it raises governance, security, legal, ethical, and practical issues that must be resolved early.",
        ],
        "concepts": ["data quality", "data access", "administrative data", "monitoring", "triangulation", "data linking", "evaluation ethics"],
        "structure": ["data requirements", "existing and new data sources", "administrative and monitoring data", "data quality", "data protection", "linkage"],
        "implications": [
            "Specify data needs during intervention design, not after delivery is complete.",
            "Check whether existing administrative data measure the evaluation concepts directly enough.",
            "Plan data sharing, linkage, ethics, and quality assurance before fieldwork or analysis starts.",
        ],
    },
    {
        "kind": "core",
        "number": 5,
        "title": "Managing an Evaluation",
        "file": "chapter-05-managing-an-evaluation.qmd",
        "note_type": "Chapter",
        "pages": "8",
        "section_path": "5. Managing an evaluation",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-5-managing-an-evaluation:c0004",
            "chunk:magenta-book:magenta-book-5-managing-an-evaluation:c0005",
            "chunk:magenta-book:magenta-book-5-managing-an-evaluation:c0017",
            "chunk:magenta-book:magenta-book-5-managing-an-evaluation:c0018",
        ],
        "core": "Managing evaluation is an active governance task that protects usefulness, feasibility, quality, ethics, and adaptation across the evaluation lifecycle.",
        "summary": [
            "Chapter 5 moves from design to delivery management. A well-run evaluation needs clear governance, agreed roles, realistic timetables, quality assurance, stakeholder access, and alignment with intervention decisions.",
            "Steering groups are more than ceremonial. They review feasibility, provide access, quality assure design and tools, advise on changing circumstances, review emerging findings, and help ensure the work remains policy relevant.",
            "The chapter recognises tension between consistency and flexibility. Some designs require stable delivery and measurement, while complex or innovative interventions may need planned review points so evaluation and implementation can adapt without losing credibility.",
            "Quality assurance and ethics are continuous responsibilities. The project manager must plan independent scrutiny, analytical checks, peer review, objective reporting, participant protection, data governance, and appropriate use of emerging tools.",
        ],
        "concepts": ["steering group", "evaluation plan", "quality assurance", "adaptive management", "evaluation ethics", "governance", "benefits management"],
        "structure": ["governance", "linking evaluation to intervention design", "supplier and stakeholder management", "flexibility and consistency", "quality assurance", "ethics"],
        "implications": [
            "Create governance that can genuinely steer design, access, quality, and use.",
            "Build planned adaptation points into evaluations of changing or innovative interventions.",
            "Treat quality assurance and ethics as lifecycle responsibilities, not final report checks.",
        ],
    },
    {
        "kind": "core",
        "number": 6,
        "title": "The Use and Dissemination of Evaluation Findings",
        "file": "chapter-06-use-and-dissemination-of-evaluation-findings.qmd",
        "note_type": "Chapter",
        "pages": "9",
        "section_path": "6. The use and dissemination of evaluation findings",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-6-the-use-and-dissemination-of-evaluation-findings:c0002",
            "chunk:magenta-book:magenta-book-6-the-use-and-dissemination-of-evaluation-findings:c0004",
            "chunk:magenta-book:magenta-book-6-the-use-and-dissemination-of-evaluation-findings:c0007",
            "chunk:magenta-book:magenta-book-6-the-use-and-dissemination-of-evaluation-findings:c0008",
            "chunk:magenta-book:magenta-book-6-the-use-and-dissemination-of-evaluation-findings:c0010",
        ],
        "core": "Evaluation findings have value only if their users, decision points, products, publication route, and transparency commitments are planned from the start.",
        "summary": [
            "Chapter 6 treats use and dissemination as design issues, not communication tasks left until the report is drafted. Evaluators need to know which groups need what information, when they need it, and what form will make it usable.",
            "The chapter distinguishes direct and indirect users. Direct users may need findings for live policy decisions, spending reviews, or delivery improvement; indirect users may need learning for future policy, scrutiny, or wider public understanding.",
            "The dissemination plan should be agreed early with stakeholders, communication teams, and ministerial offices where relevant. This reduces surprises and protects publication decisions from appearing to depend on whether findings are favourable.",
            "Openness and transparency are central. Registration, published protocols, clear reporting, accessible limitations, and publication expectations strengthen trust and public value.",
        ],
        "concepts": ["evaluation use", "dissemination", "transparency", "evaluation registry", "reporting transparency", "pre-registration", "accountability"],
        "structure": ["users and evidence needs", "use and dissemination plan", "tailored reporting", "publication", "openness and transparency"],
        "implications": [
            "Start dissemination planning when the evaluation is scoped, not when findings arrive.",
            "Tailor outputs to audience decisions while keeping limitations and uncertainty visible.",
            "Agree publication and transparency expectations early enough to protect credibility.",
        ],
    },
    {
        "kind": "core",
        "number": 7,
        "title": "Evaluation Capabilities",
        "file": "chapter-07-evaluation-capabilities.qmd",
        "note_type": "Chapter",
        "pages": "10",
        "section_path": "7. Evaluation capabilities",
        "evidence_ids": [
            "chunk:magenta-book:magenta-book-7-evaluation-capabilities:c0001",
            "chunk:magenta-book:magenta-book-7-evaluation-capabilities:c0002",
            "chunk:magenta-book:magenta-book-7-evaluation-capabilities:c0004",
            "chunk:magenta-book:magenta-book-7-evaluation-capabilities:c0006",
            "chunk:magenta-book:magenta-book-7-evaluation-capabilities:c0007",
        ],
        "core": "Government evaluation quality depends on capability across scoping, leadership, methods, use, dissemination, and the ability to work with uncertainty.",
        "summary": [
            "Chapter 7 summarises the capabilities needed to design, manage, and use evaluations. It groups capability around scoping, leading and managing, methods, and use and dissemination.",
            "Scoping capability includes understanding rationale, constructing a theory of change, identifying a suitable approach, and producing a proportionate plan. Leading capability includes maintaining momentum, influencing stakeholders, adapting to change, and acting with integrity.",
            "Methods capability spans monitoring data, administrative data, primary research, process evaluation, theory-based impact evaluation, experimental and quasi-experimental approaches, value for money work, synthesis, and appropriate awareness of AI-assisted analysis.",
            "Use and dissemination capability means turning evidence into clear products, policy implications, publication routes, and stakeholder communication that make findings usable without overstating certainty.",
        ],
        "concepts": ["capability", "scoping", "theory of change", "mixed methods", "value for money", "synthesis", "evaluation use"],
        "structure": ["scoping capability", "leading and managing", "methods", "use and dissemination", "further detail"],
        "implications": [
            "Assess team capability against the evaluation's actual methods and use demands.",
            "Bring in specialist expertise when the design needs methods, data, or ethical skills the core team lacks.",
            "Treat capability building as part of institutional evaluation quality, not only individual training.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Annex A: Analytical Methods for Use Within an Evaluation",
        "file": "appendix-annex-a-analytical-methods.qmd",
        "note_type": "Appendix",
        "pages": "11-16",
        "section_path": "Appendices > Magenta Book Annex A analytical methods for use within an evaluation",
        "evidence_ids": [
            "chunk:magenta-book:annex-a-analytical-methods-annex-a-analytical-methods-for-use-within-an-evaluation:c0001",
            "chunk:magenta-book:annex-a-analytical-methods-a1-theory-based-methods-for-impact-evaluation:c0004",
            "chunk:magenta-book:annex-a-analytical-methods-a3-methods-for-value-for-money-evaluation:c0012",
            "chunk:magenta-book:annex-a-analytical-methods-a4-methods-for-synthesis-of-existing-evidence:c0010",
            "chunk:magenta-book:annex-a-analytical-methods-a5-generic-research-methods-used-in-both-process-and-impact-evaluatio:c0007",
        ],
        "core": "Annex A extends Chapter 3 by giving a method catalogue for theory-based impact evaluation, counterfactual designs, value for money analysis, synthesis, and generic research methods.",
        "summary": [
            "Annex A is the technical method companion to the main methods chapter. It groups approaches by the kind of evaluation question and causal claim they can support.",
            "Theory-based methods help evaluators test causal explanations when mechanisms, context, contribution, and complexity matter. Experimental and quasi-experimental methods help estimate effects when credible comparison is feasible.",
            "Value for money methods are presented as more than a benefit-cost ratio. They can combine economic appraisal, distributional evidence, qualitative judgment, and criteria where monetisation is incomplete.",
            "Synthesis and generic research methods support both process and impact evaluation by combining existing studies, monitoring, observation, surveys, interviews, and other evidence sources.",
        ],
        "concepts": ["theory-based methods", "experimental methods", "quasi-experimental methods", "value for money", "synthesis", "mixed methods", "realist evaluation"],
        "structure": ["A1 theory-based methods", "A2 experimental and quasi-experimental methods", "A3 value for money methods", "A4 synthesis methods", "A5 generic research methods"],
        "implications": [
            "Use Annex A as a method-selection reference after evaluation questions are prioritised.",
            "Check each method's assumptions, data needs, and limits before treating it as feasible.",
            "Combine approaches when the evaluation needs both attribution and explanation.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Government Analytical Evaluation Capabilities Framework",
        "file": "appendix-government-analytical-evaluation-capabilities-framework.qmd",
        "note_type": "Appendix",
        "pages": "17-36",
        "section_path": "Appendices > Government analytical evaluation capabilities framework",
        "evidence_ids": [
            "chunk:magenta-book:evaluation-capabilities-framework-introduction-to-the-evaluation-capabilities-framework-for-gove:c0001",
            "chunk:magenta-book:evaluation-capabilities-framework-framework-self-assessment-and-action-plan:c0001",
            "chunk:magenta-book:evaluation-capabilities-framework-scoping-2-understand-the-intervention-and-construct-a-theory-o:c0001",
            "chunk:magenta-book:evaluation-capabilities-framework-methods-1-use-of-monitoring-and-administrative-data:c0001",
            "chunk:magenta-book:evaluation-capabilities-framework-methods-3-process-evaluation:c0001",
            "chunk:magenta-book:evaluation-capabilities-framework-use-and-dissemination-2-considering-policy-implications-and-sh:c0001",
        ],
        "core": "The capabilities framework translates evaluation quality into the skills, behaviours, and development actions government analysts need across the evaluation lifecycle.",
        "summary": [
            "The framework is a workforce and project-planning tool. It describes the capabilities needed to scope, lead, manage, deliver, and use evaluation in government settings.",
            "It can be used for self-assessment, team planning, departmental capability review, and identifying training needs. The point is to make evaluation capability visible before a project fails because the right skills were missing.",
            "The capability areas mirror the main guidance: scoping and theory of change, leadership and management, methods and data, process and impact evaluation, value for money, synthesis, and use of findings.",
            "The framework also points analysts toward resources for capability development, making it a practical bridge between guidance and professional development.",
        ],
        "concepts": ["capability", "scoping", "theory of change", "administrative data", "process evaluation", "value for money", "evaluation use"],
        "structure": ["framework purpose", "self-assessment", "scoping capabilities", "leading and managing", "methods capabilities", "use and dissemination"],
        "implications": [
            "Use capability review before commissioning to identify gaps in methods, data, leadership, or use.",
            "Build teams around the evaluation design rather than expecting one analyst to cover every domain.",
            "Link professional development to live evaluation risks and departmental capability needs.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Guidance for Conducting Regulatory Post Implementation Review",
        "file": "appendix-regulatory-post-implementation-review.qmd",
        "note_type": "Appendix",
        "pages": "38-44",
        "section_path": "Appendices > Supplementary Guide: Guidance for conducting regulatory post implementation review",
        "evidence_ids": [
            "chunk:magenta-book:regulatory-post-implementation-review-glossary:c0001",
            "chunk:magenta-book:regulatory-post-implementation-review-2-preparing-for-a-pir:c0002",
            "chunk:magenta-book:regulatory-post-implementation-review-3-methods-for-delivering-a-pir:c0001",
            "chunk:magenta-book:regulatory-post-implementation-review-3-methods-for-delivering-a-pir:c0010",
            "chunk:magenta-book:regulatory-post-implementation-review-annex-1-pir-case-studies-footnote-10:c0012",
        ],
        "core": "The PIR guide adapts Magenta Book evaluation logic to regulatory review, where proportional evidence, monitoring data, stakeholder evidence, and feasible counterfactuals are central.",
        "summary": [
            "The regulatory post implementation review guide focuses on evaluating whether regulation remains justified, effective, proportionate, and fit for purpose after implementation.",
            "Preparation involves clarifying the measure, baseline, intended effects, monitoring arrangements, existing evidence, proportionality, and review obligations. Where early planning was missed, the guide still pushes reviewers to build the best feasible evidence base.",
            "PIR methods often combine monitoring data, stakeholder engagement, process evidence, impact evidence, and value for money considerations. Strong counterfactual impact designs may be difficult when regulation applies to all affected parties, so limitations need to be explicit.",
            "Case material is used to show how different review strategies can meet scrutiny needs when evidence, timing, or implementation constraints vary.",
        ],
        "concepts": ["monitoring", "counterfactual", "impact evaluation", "process evaluation", "proportionality", "value for money", "accountability"],
        "structure": ["glossary and scope", "preparing for a PIR", "monitoring data", "stakeholder engagement", "evaluation evidence", "case studies"],
        "implications": [
            "Plan review evidence while the regulation is being designed, not only when the PIR deadline arrives.",
            "Use monitoring and stakeholder evidence proportionately when causal comparison is infeasible.",
            "State clearly what can and cannot be attributed to regulation using the available evidence.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Handling Complexity in Policy Evaluation",
        "file": "appendix-handling-complexity-in-policy-evaluation.qmd",
        "note_type": "Appendix",
        "pages": "45-53",
        "section_path": "Appendices > Supplementary Guide: Handling complexity in policy evaluation",
        "evidence_ids": [
            "chunk:magenta-book:handling-complexity-1-why-complexity-matters:c0007",
            "chunk:magenta-book:handling-complexity-3-commissioning-and-managing-evaluations:c0001",
            "chunk:magenta-book:handling-complexity-3-commissioning-and-managing-evaluations:c0007",
            "chunk:magenta-book:handling-complexity-4-selecting-complexity-appropriate-approaches:c0001",
            "chunk:magenta-book:handling-complexity-4-selecting-complexity-appropriate-approaches:c0008",
        ],
        "core": "The complexity guide shows how evaluation design, commissioning, management, and methods must adapt when interventions operate in uncertain, changing, and interdependent systems.",
        "summary": [
            "This guide explains why complex policy settings weaken simple assumptions about stable interventions, linear causation, and fixed evaluation plans. Multiple perspectives, system responses, and changing context affect both delivery and evidence.",
            "Commissioning and management need more learning, reflection, and flexibility than routine evaluations. Commissioners may need iterative designs, regular review points, more stakeholder mapping, and procurement arrangements that allow adaptation.",
            "Theory of change work remains important but may need systems mapping, participatory approaches, or nonlinear causal models. Evaluations may need to examine how the intervention and surrounding system evolve together.",
            "The guide links method choice to purpose and system attributes. Complexity-appropriate evaluation can still support accountability, but it often needs a stronger learning function and more explicit treatment of uncertainty.",
        ],
        "concepts": ["complexity", "adaptive management", "theory of change", "systems mapping", "learning", "stakeholder engagement", "proportionality"],
        "structure": ["why complexity matters", "evaluation challenges", "commissioning and management", "building understanding", "complexity-appropriate approaches", "resources"],
        "implications": [
            "Diagnose complexity before specifying fixed methods, budgets, and deliverables.",
            "Build review points into governance so emerging evidence can reshape the evaluation design.",
            "Use systems and stakeholder mapping where linear programme models would hide important causal dynamics.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Quality in Qualitative Evaluation",
        "file": "appendix-quality-in-qualitative-evaluation.qmd",
        "note_type": "Appendix",
        "pages": "54-59",
        "section_path": "Appendices > Quality in qualitative evaluation",
        "evidence_ids": [
            "chunk:magenta-book:quality-qualitative-evaluation-1-introduction:c0001",
            "chunk:magenta-book:quality-qualitative-evaluation-2-scope-of-the-framework:c0001",
            "chunk:magenta-book:quality-qualitative-evaluation-3-application-of-the-framework:c0001",
            "chunk:magenta-book:quality-qualitative-evaluation-4-content-of-the-framework:c0001",
            "chunk:magenta-book:quality-qualitative-evaluation-4-content-of-the-framework:c0002",
        ],
        "core": "The qualitative quality guide provides a framework for judging whether qualitative evaluation evidence is defensible, transparent, useful, and fit for purpose.",
        "summary": [
            "This appendix gives a framework for appraising qualitative evaluations, especially those concerned with policy, programmes, and practice. It is built from literature review, government evaluation practice, existing quality frameworks, and expert consultation.",
            "The framework is mainly designed for assessing written outputs, but selected questions can also inform proposals, protocols, training, and research management.",
            "Quality assessment focuses on the findings and on the research process behind them: design, sampling, data collection, analysis, reporting, reflexivity, ethics, neutrality, and auditability.",
            "The guide emphasises professional judgment. Quality indicators support appraisal, but the assessor still has to decide what matters most for the evaluation's purpose, method, and policy context.",
        ],
        "concepts": ["qualitative quality", "data quality", "professional judgment", "auditability", "reflexivity", "evaluation ethics", "fitness for purpose"],
        "structure": ["framework purpose", "scope", "application", "guiding principles", "appraisal questions", "quality indicators"],
        "implications": [
            "Assess qualitative findings together with the design and analysis process that produced them.",
            "Use quality questions to strengthen proposals and protocols, not only completed reports.",
            "Keep judgment proportionate to the evaluation purpose and method rather than applying a mechanical checklist.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Quality in Policy Impact Evaluation",
        "file": "appendix-quality-in-policy-impact-evaluation.qmd",
        "note_type": "Appendix",
        "pages": "60-73",
        "section_path": "Appendices > Quality in policy impact evaluation",
        "evidence_ids": [
            "chunk:magenta-book:quality-policy-impact-evaluation-executive-summary:c0001",
            "chunk:magenta-book:quality-policy-impact-evaluation-1-introduction:c0001",
            "chunk:magenta-book:quality-policy-impact-evaluation-1-introduction:c0002",
            "chunk:magenta-book:quality-policy-impact-evaluation-2-quality-in-policy-impact-evaluation:c0001",
            "chunk:magenta-book:quality-policy-impact-evaluation-2-quality-in-policy-impact-evaluation:c0002",
        ],
        "core": "The policy impact quality guide helps users judge how strongly an impact design can support attribution and what conclusions are warranted.",
        "summary": [
            "This appendix focuses on empirical impact evaluations that quantify whether observed outcomes were caused by a policy. It aims to help policy makers and analysts choose designs with clear strengths and limits.",
            "The central issue is attribution. Monitoring outcomes can show change, but it cannot by itself establish whether the policy caused that change; stronger designs need a credible counterfactual.",
            "Design quality has to be proportionate to the policy's risk, scale, profile, and learning value. The guide asks users to consider whether they can afford not to conduct a robust impact evaluation when causal claims matter.",
            "The guide also recognises feasibility limits. Legal constraints, national rollout, small sample sizes, weak data, and statutory frameworks may restrict design options, but those constraints do not change what can validly be concluded.",
        ],
        "concepts": ["policy impact evaluation", "causal attribution", "counterfactual", "internal validity", "external validity", "robustness", "proportionality"],
        "structure": ["purpose", "impact questions", "quality and attribution", "design hierarchy", "feasibility constraints", "interpretation limits"],
        "implications": [
            "Match causal claims to the design's ability to construct a credible counterfactual.",
            "Be explicit when feasibility constraints limit attribution strength.",
            "Plan impact evaluation early enough to avoid avoidable data and rollout constraints.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Realist Evaluation",
        "file": "appendix-realist-evaluation.qmd",
        "note_type": "Appendix",
        "pages": "67-74",
        "section_path": "Appendices > Supplementary Guide: Realist evaluation",
        "evidence_ids": [
            "chunk:magenta-book:realist-evaluation-1-realist-evaluation-what-it-is-and-when-to-use-it:c0001",
            "chunk:magenta-book:realist-evaluation-2-introducing-realist-evaluation:c0001",
            "chunk:magenta-book:realist-evaluation-3-developing-realist-theory-context-mechanism-and-outcome:c0001",
            "chunk:magenta-book:realist-evaluation-5-applying-the-realist-frame-to-evaluation:c0001",
            "chunk:magenta-book:realist-evaluation-6-further-examples-of-realist-evaluation:c0003",
        ],
        "core": "The realist evaluation guide explains how to test and refine context-mechanism-outcome theories when evaluators need to know what works, for whom, how, and under what conditions.",
        "summary": [
            "The realist guide positions realist evaluation as a theory-based approach for programmes where average effects are not enough. It asks how the intervention creates opportunities that people respond to differently in different contexts.",
            "The central explanatory unit is the context-mechanism-outcome configuration. The intervention does not act mechanically; outcomes arise when people respond to resources, opportunities, incentives, or constraints in a context.",
            "Realist evaluation develops, tests, and refines hypotheses. It begins with programme theory, translates that theory into realist terms, collects evidence about how mechanisms operate, and revises explanations as evidence accumulates.",
            "The guide is especially useful where programmes are new, being scaled, producing mixed outcomes, or operating in complex systems where understanding why and for whom matters for future adaptation.",
        ],
        "concepts": ["realist evaluation", "theory-based methods", "context", "mechanism", "outcome", "causal attribution", "complexity"],
        "structure": ["what realist evaluation is", "introducing the realist frame", "context-mechanism-outcome theory", "realist cycle", "examples and resources"],
        "implications": [
            "Use realist evaluation when adaptation and transfer depend on understanding mechanisms in context.",
            "Write causal hypotheses in a form that can be tested with evidence.",
            "Avoid reducing realist work to broad narrative explanation without explicit CMO testing.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Guidance on the Impact Evaluation of AI Interventions",
        "file": "appendix-guidance-impact-evaluation-ai-interventions.qmd",
        "note_type": "Appendix",
        "pages": "75-90",
        "section_path": "Appendices > Guidance on the Impact Evaluation of AI Interventions",
        "evidence_ids": [
            "chunk:magenta-book:ai-impact-evaluation-summary:c0001",
            "chunk:magenta-book:ai-impact-evaluation-1-introduction:c0002",
            "chunk:magenta-book:ai-impact-evaluation-2-opportunities-and-challenges-for-the-evaluation-of-ai-interventions:c0001",
            "chunk:magenta-book:ai-impact-evaluation-2-1-choosing-the-evaluation-approach:c0002",
            "chunk:magenta-book:ai-impact-evaluation-2-1-choosing-the-evaluation-approach:c0007",
            "chunk:magenta-book:ai-impact-evaluation-a-2-practical-example-2-using-an-llm-based-application-to-help-civil-servan:c0001",
        ],
        "core": "The AI impact evaluation guide applies Magenta Book impact principles to AI interventions whose novelty, digital rollout, risks, and iteration create both opportunities and evaluation challenges.",
        "summary": [
            "This guide argues that the core principles of impact evaluation still apply to AI interventions, but the intervention context adds distinctive risks, opportunities, and feasibility issues.",
            "AI interventions often have high uncertainty, high learning value, and potential public trust implications. That means they may warrant more substantial evaluation than routine digital changes of similar cost.",
            "The digital nature of many AI interventions can make randomisation, phased rollout, and data collection more feasible. At the same time, iteration, changing models, public attitudes, bias, and unintended harms require broader theory and process evidence.",
            "The guide encourages evaluators to plan early, define objectives and theory of change, choose experimental, quasi-experimental, or theory-based designs as appropriate, and use case examples to reason through data and ethics.",
        ],
        "concepts": ["impact evaluation", "AI intervention", "experimental methods", "quasi-experimental methods", "theory-based methods", "evaluation ethics", "public trust"],
        "structure": ["summary principles", "introduction", "opportunities and challenges", "choosing approaches", "public attitudes and risks", "hypothetical case studies", "glossary"],
        "implications": [
            "Plan AI evaluation alongside design and rollout so randomisation or phased access remains possible.",
            "Treat bias, public attitudes, explainability, and unintended effects as evaluation issues, not only technical assurance issues.",
            "Combine quantitative impact evidence with theory-based and qualitative evidence when AI mechanisms or user responses matter.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Transparency in Government Evaluation Research",
        "file": "appendix-transparency-in-government-evaluation-research.qmd",
        "note_type": "Appendix",
        "pages": "91-103",
        "section_path": "Appendices > Transparency in Government Evaluation Research (T I G E R)",
        "evidence_ids": [
            "chunk:magenta-book:tiger-transparency-foreword:c0001",
            "chunk:magenta-book:tiger-transparency-introduction:c0001",
            "chunk:magenta-book:tiger-transparency-introduction:c0003",
            "chunk:magenta-book:tiger-transparency-planning-transparency:c0001",
            "chunk:magenta-book:tiger-transparency-analysis-transparency:c0001",
            "chunk:magenta-book:tiger-transparency-reporting-transparency:c0001",
        ],
        "core": "The TIGER annex operationalises open science for government evaluation through proportionate planning, analysis, and reporting transparency.",
        "summary": [
            "The transparency annex adapts open science practices to government evaluation. It aims to make evaluation plans, analysis, and reporting transparent enough to strengthen integrity, trust, reuse, and value for money.",
            "The annex is explicitly proportionate. Higher stakes, higher cost, high-profile, high learning value, novel, or complex evaluations should receive stronger transparency practices, while legal and data constraints still matter.",
            "Planning transparency includes registration, evaluation plans, protocols, statistical analysis plans, timestamping, and archiving. These practices create a record before data collection or analysis can be shaped by results.",
            "Analysis and reporting transparency require preserving materials, data, code, and methodological choices; communicating uncertainty; and showing whether findings are robust to reasonable alternative choices.",
        ],
        "concepts": ["transparency", "open science", "evaluation registry", "pre-registration", "analysis transparency", "reporting transparency", "robustness"],
        "structure": ["transparency rationale", "proportionality", "planning transparency", "analysis transparency", "reporting transparency", "tools and recommendations"],
        "implications": [
            "Decide transparency practices during design, before data collection or analysis begins.",
            "Archive plans, materials, code, and analysis decisions even when public release is not possible.",
            "Report uncertainty and robustness in language decision-makers can understand.",
        ],
    },
    {
        "kind": "appendix",
        "title": "Test and Learn",
        "file": "appendix-test-and-learn.qmd",
        "note_type": "Appendix",
        "pages": "104-110",
        "section_path": "Appendices > Test and Learn",
        "evidence_ids": [
            "chunk:magenta-book:test-and-learn-chapter-one-introduction-to-this-guide:c0001",
            "chunk:magenta-book:test-and-learn-chapter-one-introduction-to-this-guide:c0002",
            "chunk:magenta-book:test-and-learn-chapter-four-how-test-and-learn-supports-robust-evaluation:c0005",
            "chunk:magenta-book:test-and-learn-chapter-seven-annex:c0003",
        ],
        "core": "The Test and Learn annex shows how structured, iterative testing can build evidence, reduce uncertainty, and improve policy before full-scale evaluation or rollout.",
        "summary": [
            "Test and Learn is presented as a way of working rather than a separate evaluation type. It embeds structured testing, feedback, and adaptation into policy and service design.",
            "The approach is most useful when problems are complex or uncertain, assumptions are untested, and teams need rapid learning before committing to scale. It is less useful when requirements and solutions are already fixed.",
            "Test and Learn can strengthen later evaluation by clarifying theory of change, testing critical assumptions, improving delivery, and identifying where counterfactual or theory-based impact methods may be feasible.",
            "The annex links testing to robust evaluation by encouraging teams to define uncertainties, collect real-world evidence, examine context, and decide when to grow, adapt, stop, or move to formal evaluation.",
        ],
        "concepts": ["test and learn", "adaptive management", "theory of change", "learning", "counterfactual", "process evaluation", "impact evaluation"],
        "structure": ["introduction", "when to use test and learn", "testing assumptions", "supporting robust evaluation", "grow and adapt decisions", "resources"],
        "implications": [
            "Use Test and Learn before scaling when assumptions are uncertain and adaptation is still possible.",
            "Treat small tests as evidence-building exercises, not informal pilots without decision rules.",
            "Carry learning from tests into later process, impact, and value for money evaluation designs.",
        ],
    },
]


def wrap(text: str) -> str:
    return "\n".join(textwrap.wrap(text, width=100))


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(rel: str, payload: dict) -> None:
    write_text(rel, json.dumps(payload, indent=2) + "\n")


def yaml_quote(value: str) -> str:
    return json.dumps(value)


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {yaml_quote(item)}" for item in items)


def source_chunks(evidence_ids: list[str]) -> str:
    lines = [
        '<details class="source-chunks">',
        "<summary>Source chunks</summary>",
        '<ul class="source-chunk-list">',
    ]
    for evidence_id in evidence_ids:
        lines.append(f"<li><code>{evidence_id}</code></li>")
    lines.extend(["</ul>", "</details>"])
    return "\n".join(lines)


def mermaid_label(text: str) -> str:
    return text.replace('"', "'").replace("\n", " ")


def default_map_data(note: dict) -> dict:
    return {
        "map_problem": f"What evaluation problem does {note['title']} help government handle?",
        "map_concepts": note["concepts"][:3],
        "map_mechanisms": note["structure"][:3],
        "map_implications": note["implications"][:2],
        "map_question": "What evidence would make this guidance credible in a live evaluation?",
    }


def render_concept_map(map_data: dict, central_label: str) -> str:
    concepts = map_data.get("map_concepts", [])[:3]
    mechanisms = map_data.get("map_mechanisms", [])[:3]
    implications = map_data.get("map_implications", [])[:2]
    lines = [
        "::: {.concept-map}",
        "```{mermaid}",
        "flowchart TD",
        f'  Problem["Problem: {mermaid_label(map_data["map_problem"])}"]',
        f'  Central["Concept: {mermaid_label(central_label)}"]',
    ]
    for idx, concept in enumerate(concepts, start=1):
        lines.append(f'  Concept{idx}["Concept: {mermaid_label(concept)}"]')
    for idx, mechanism in enumerate(mechanisms, start=1):
        lines.append(f'  Mechanism{idx}["Mechanism: {mermaid_label(mechanism)}"]')
    for idx, implication in enumerate(implications, start=1):
        lines.append(f'  Implication{idx}["Policy implication: {mermaid_label(implication)}"]')
    lines.append(f'  Question["Open question: {mermaid_label(map_data["map_question"])}"]')
    lines.extend(["", "  Problem --> Central", "  Central --> Question"])
    for idx in range(1, len(concepts) + 1):
        lines.append(f"  Central --> Concept{idx}")
    for idx in range(1, len(mechanisms) + 1):
        concept_idx = min(idx, max(1, len(concepts)))
        if concepts:
            lines.append(f"  Concept{concept_idx} --> Mechanism{idx}")
        else:
            lines.append(f"  Central --> Mechanism{idx}")
    for idx in range(1, len(implications) + 1):
        mechanism_idx = min(idx, max(1, len(mechanisms)))
        if mechanisms:
            lines.append(f"  Mechanism{mechanism_idx} --> Implication{idx}")
        else:
            lines.append(f"  Central --> Implication{idx}")
    if implications:
        lines.append("  Implication1 --> Question")
    lines.extend(
        [
            "",
            "  classDef problem fill:#fee2e2,stroke:#b91c1c,color:#7f1d1d;",
            "  classDef concept fill:#e6f3f1,stroke:#115e59,color:#134e4a;",
            "  classDef mechanism fill:#e8f1ff,stroke:#1d4ed8,color:#1e3a8a;",
            "  classDef implication fill:#fce7f3,stroke:#be185d,color:#831843;",
            "  class Problem problem;",
            "  class Central concept;",
        ]
    )
    if concepts:
        lines.append(f"  class {','.join(f'Concept{idx}' for idx in range(1, len(concepts) + 1))} concept;")
    if mechanisms:
        lines.append(f"  class {','.join(f'Mechanism{idx}' for idx in range(1, len(mechanisms) + 1))} mechanism;")
    implication_nodes = [f"Implication{idx}" for idx in range(1, len(implications) + 1)] + ["Question"]
    lines.append(f"  class {','.join(implication_nodes)} implication;")
    lines.extend(["```", ":::"])
    return "\n".join(lines)


def metadata(extra: list[str]) -> str:
    items = [YEAR, "MCP evaluation-texts", f"Status: {SOURCE_STATUS}", *extra]
    spans = "".join(f"<span>{item}</span>" for item in items)
    return f'<div class="chapter-meta">{spans}</div>'


def note_label(note: dict) -> str:
    if note["kind"] == "core" and note.get("number", 0) > 0:
        return f"Chapter {note['number']}: {note['title']}"
    return note["title"]


def note_link(note: dict) -> str:
    return f"[{note_label(note)}]({note['file']})"


def sentence_join(items: list[str], limit: int = 4) -> str:
    selected = items[:limit]
    if len(selected) <= 1:
        return "".join(selected)
    return ", ".join(selected[:-1]) + f", and {selected[-1]}"


def concept_gloss(concept: str) -> str:
    return CONCEPT_GLOSSES.get(concept, "A recurring idea used to frame evaluation design, evidence, interpretation, quality, or use.")


def render_reading_note(note: dict) -> str:
    concepts = sentence_join(note["concepts"], 4)
    moves = sentence_join(note["structure"], 3)
    return (
        f"For close reading, track how this note uses {concepts} while moving through {moves}. "
        "The notes below treat those moves as study scaffolding: they identify what the guidance asks "
        "the evaluator to notice, what judgment problem it helps solve, and what should be checked "
        "against the saved evidence records before relying on the summary in applied work."
    )


def render_book_connection(note: dict) -> str:
    if note["kind"] == "appendix":
        return (
            "Within the wider Magenta Book route, this appendix supplies specialist depth for the main "
            "guidance. It should be read after the relevant chapter has established the evaluation purpose, "
            "questions, data constraints, and use needs."
        )
    if note.get("number", 0) == 0:
        return (
            "Within the wider Magenta Book route, the executive summary is the orientation point: it explains "
            "why process, impact, and value for money evidence need to be planned together across the guidance."
        )
    return (
        "Within the wider Magenta Book route, this chapter is part of the core sequence from rationale and "
        "scoping through methods, data, management, dissemination, and capability."
    )


def render_note(note: dict, prev_note: dict | None, next_note: dict | None) -> str:
    evidence_ids = note["evidence_ids"]
    title = note_label(note)
    extra_meta = [note["section_path"], f"Source pages {note['pages']}", note["note_type"]]
    body = [
        "---",
        f"title: {yaml_quote(title)}",
        f"description: {yaml_quote(f'Detailed study notes for {title} in {FULL_TITLE}.')}",
        f"book_id: {yaml_quote(BOOK_ID)}",
        f"collection_id: {yaml_quote(COLLECTION_ID)}",
        f"note_type: {yaml_quote(note['note_type'])}",
    ]
    if note["kind"] == "core" and note.get("number", 0) > 0:
        body.append(f"chapter_number: {note['number']}")
    if note["kind"] == "appendix":
        body.append('part: "Appendices and supplementary guidance"')
    body.extend(
        [
            f"source_pages: {yaml_quote(note['pages'])}",
            f"citation_key: {yaml_quote(CITATION)}",
            "evidence_ids:",
            yaml_list(evidence_ids),
            f"source_status: {yaml_quote(SOURCE_STATUS)}",
            "---",
            "",
            "## Source",
            "",
            metadata(extra_meta),
            "",
            f"This note summarises {note['section_path']} from {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. It is a paraphrased study note based on source-linked MCP research-library retrieval records, not a substitute for the source text.",
            "",
            "The retrieval trail is retained in the source chunks at the bottom of the page. The note paraphrases the guidance and does not reproduce tables, checklists, figures, exhibits, or extended passages. When a checklist or table is central, the note describes its function and leaves the source artifact in the evidence record.",
            "",
            "## Core Argument",
            "",
            wrap(note["core"]),
            "",
            "## Study Summary",
            "",
        ]
    )
    for paragraph in note["summary"]:
        body.extend([wrap(paragraph), ""])
    body.extend(
        [
            wrap(render_reading_note(note)),
            "",
            wrap(render_book_connection(note)),
            "",
            "## Key Concepts",
            "",
        ]
    )
    for concept in note["concepts"]:
        body.append(f"- **{concept}**: {concept_gloss(concept)}")
    body.extend(["", f"## {note['note_type']} Structure", ""])
    for item in note["structure"]:
        body.append(f"- {item.capitalize()}.")
    body.extend(["", "## Practical Implications", ""])
    for item in note["implications"]:
        body.append(f"- {item}")
    body.extend(["", "## Concept Map", "", render_concept_map(default_map_data(note), note["title"]), "", "## Connections", ""])
    body.extend(
        [
            "- Book overview: [Overview](index.qmd)",
            "- Reading route: [Chapter Map](chapter-map.qmd)",
            "- Concepts synthesis: [Core Concepts](concepts.qmd)",
            "- Practice synthesis: [Practice Implications](practice-implications.qmd)",
        ]
    )
    if prev_note:
        body.append(f"- Previous: {note_link(prev_note)}")
    if next_note:
        body.append(f"- Next: {note_link(next_note)}")
    body.extend(
        [
            "",
            "## Study Prompts",
            "",
            f"1. What evaluation problem does {note['title']} help diagnose?",
            "2. Which assumptions would need evidence before applying this guidance in a live evaluation?",
            "3. How would this change the way an evaluator scopes questions, methods, reporting, or use?",
            "4. Where could the guidance be misused if treated as a fixed template?",
            "",
            "## Source Chunks",
            "",
            source_chunks(evidence_ids),
            "",
            "## References",
            "",
            f"- {AUTHORS}. ({YEAR}). *{FULL_TITLE}*. {PUBLISHER}. {note['section_path']}, pages {note['pages']}.",
            f"- Saved retrieval metadata: `data/research-library/evidence/{SLUG}/chapter-evidence-summary.json`.",
            "",
        ]
    )
    return "\n".join(body)


def render_index() -> str:
    evidence = [note["evidence_ids"][0] for note in NOTES]
    lines = [
        "---",
        f"title: {yaml_quote(TITLE)}",
        f"description: {yaml_quote(f'Book overview and expanded study-note index for {TITLE}.')}",
        f"book_id: {yaml_quote(BOOK_ID)}",
        f"collection_id: {yaml_quote(COLLECTION_ID)}",
        'note_type: "Book"',
        f"citation_key: {yaml_quote(CITATION)}",
        "evidence_ids:",
        yaml_list(evidence),
        f"source_status: {yaml_quote(SOURCE_STATUS)}",
        "---",
        "",
        '<div class="landing-stack">',
        "",
        "::: {.directory-hero}",
        '<span class="hero-eyebrow">Book notes</span>',
        "",
        f"# {TITLE}",
        "",
        f"Study notes on *{FULL_TITLE}* [@{CITATION}]. These notes are generated from source-linked MCP research-library records and are intended for study, comparison, and later refinement.",
        "",
        '<div class="page-metadata">',
        f"  <span>{len([n for n in NOTES if n['kind'] == 'core'])} core guidance notes</span>",
        f"  <span>{len([n for n in NOTES if n['kind'] == 'appendix'])} appendix notes</span>",
        f"  <span>{YEAR}</span>",
        "  <span>Source status: needs_review</span>",
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
        "Recurring ideas and distinctions used across the expanded notes.",
        ":::",
        "",
        "::: {.section-card}",
        '<span class="page-badge badge-map">Map</span>',
        "",
        "### [Chapter Map](chapter-map.qmd)",
        "",
        "Core guidance and appendix reading route.",
        ":::",
        "",
        "::: {.section-card}",
        '<span class="page-badge badge-practice">Practice</span>',
        "",
        "### [Practice Implications](practice-implications.qmd)",
        "",
        "Practical evaluation design habits drawn from the full note set.",
        ":::",
        ":::",
        "",
        "</div>",
        "",
        "## Source",
        "",
        metadata(["Book overview", "Core guidance and appendix route"]),
        "",
        f"This index summarises generated study notes for {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. The generated pages use selected MCP research-library retrieval records and compact evidence summaries.",
        "",
        "## Core Argument",
        "",
        "Government evaluation should be planned early and proportionately around learning, accountability, robust methods, useful data, quality assurance, transparent reporting, and actual use of findings.",
        "",
        "## Concept Map",
        "",
        render_concept_map(
            {
                "map_problem": "How should government plan and use evaluation evidence?",
                "map_concepts": ["learning", "accountability", "evaluation design"],
                "map_mechanisms": ["scoping", "methods and data", "use and transparency"],
                "map_implications": ["Plan evaluation with the intervention, not after it.", "Match design and transparency to risk, use, and feasibility."],
                "map_question": "Which evidence route best supports the policy decision at hand?",
            },
            TITLE,
        ),
        "",
        "## Core Guidance Notes",
        "",
    ]
    for note in [item for item in NOTES if item["kind"] == "core"]:
        lines.append(f"- {note_link(note)} - source pages {note['pages']}")
    lines.extend(["", "## Appendix and Supplementary Notes", ""])
    for note in [item for item in NOTES if item["kind"] == "appendix"]:
        lines.append(f"- {note_link(note)} - source pages {note['pages']}")
    lines.extend(["", "## Source Chunks", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_chapter_map() -> str:
    evidence = [note["evidence_ids"][0] for note in NOTES]
    lines = [
        "---",
        f"title: {yaml_quote(f'{TITLE} Chapter and Appendix Map')}",
        f"description: {yaml_quote(f'Expanded reading map for {TITLE} study notes.')}",
        f"book_id: {yaml_quote(BOOK_ID)}",
        f"collection_id: {yaml_quote(COLLECTION_ID)}",
        'note_type: "Map"',
        f"citation_key: {yaml_quote(CITATION)}",
        "evidence_ids:",
        yaml_list(evidence),
        f"source_status: {yaml_quote(SOURCE_STATUS)}",
        "---",
        "",
        "## Source",
        "",
        f"This map uses selected MCP research-library sections from *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Reading Route",
        "",
        "### Core Guidance",
        "",
    ]
    for note in [item for item in NOTES if item["kind"] == "core"]:
        lines.append(f"- {note_link(note)} - pages {note['pages']}; `{note['section_path']}`")
    lines.extend(["", "### Appendices and Supplementary Guides", ""])
    for note in [item for item in NOTES if item["kind"] == "appendix"]:
        lines.append(f"- {note_link(note)} - pages {note['pages']}; `{note['section_path']}`")
    lines.extend(
        [
            "",
            "## How to Use This Map",
            "",
            "- Start with the executive summary and Chapter 1 to clarify evaluation purpose and quality principles.",
            "- Use Chapters 2-4 to connect theory of change, questions, methods, and data.",
            "- Use Chapters 5-7 to manage quality, use, dissemination, and capability.",
            "- Use appendix notes when the evaluation needs specialist method, quality, transparency, complexity, AI, regulatory, realist, or test-and-learn guidance.",
            "",
            "## Concept Map",
            "",
            render_concept_map(
                {
                    "map_problem": "How does the Magenta Book move from evaluation purpose to specialist guidance?",
                    "map_concepts": ["core guidance", "appendix methods", "use and transparency"],
                    "map_mechanisms": ["scoping and design", "quality and capability", "specialist annexes"],
                    "map_implications": ["Read appendix guidance through the evaluation question it supports.", "Keep use, quality, and transparency connected across the route."],
                    "map_question": "Which chapter or appendix resolves the live evaluation design risk?",
                },
                "Magenta Book reading route",
            ),
            "",
            "## Source Chunks",
            "",
            source_chunks(evidence),
            "",
            "## References",
            "",
        ]
    )
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = [note["evidence_ids"][0] for note in NOTES]
    concept_groups = [
        ("Purpose and Use", ["learning", "accountability", "evaluation use", "dissemination", "transparency"]),
        ("Design and Scoping", ["scoping", "theory of change", "evaluation question", "evaluation design", "proportionality"]),
        ("Methods and Causality", ["process evaluation", "impact evaluation", "counterfactual", "theory-based methods", "experimental methods", "value for money"]),
        ("Data and Quality", ["data quality", "data access", "administrative data", "triangulation", "quality assurance", "evaluation ethics"]),
        ("Specialist Guidance", ["complexity", "realist evaluation", "test and learn", "policy impact evaluation", "qualitative quality", "open science"]),
    ]
    lines = [
        "---",
        f"title: {yaml_quote(f'Core Concepts in {TITLE}')}",
        f"description: {yaml_quote(f'Synthesis note on recurring concepts in {TITLE}.')}",
        f"book_id: {yaml_quote(BOOK_ID)}",
        f"collection_id: {yaml_quote(COLLECTION_ID)}",
        'note_type: "Synthesis"',
        f"citation_key: {yaml_quote(CITATION)}",
        "evidence_ids:",
        yaml_list(evidence),
        f"source_status: {yaml_quote(SOURCE_STATUS)}",
        "---",
        "",
        "## Source",
        "",
        f"This synthesis draws across the expanded notes for *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Central Logic",
        "",
        "The guidance treats evaluation as a lifecycle discipline: clarify the intervention and decision need, choose proportionate methods and data, manage quality and ethics, communicate findings transparently, and build capability for use.",
        "",
        "## Concept Map",
        "",
        render_concept_map(
            {
                "map_problem": "What concepts hold the Magenta Book's evaluation logic together?",
                "map_concepts": ["learning and accountability", "theory of change and questions", "methods, data, and use"],
                "map_mechanisms": ["scoping", "triangulation and quality assurance", "transparent dissemination"],
                "map_implications": ["Make evaluation questions and use visible before choosing methods.", "Treat transparency and capability as part of evaluation quality."],
                "map_question": "Which concept cluster is doing the most work in a given evaluation design?",
            },
            "Core concepts",
        ),
        "",
        "## Concepts",
        "",
    ]
    for heading, concepts in concept_groups:
        lines.extend([f"### {heading}", ""])
        for concept in concepts:
            lines.append(f"- **{concept}**: {concept_gloss(concept)}")
        lines.append("")
    lines.extend(["## Links", ""])
    for note in NOTES:
        lines.append(f"- {note_link(note)}")
    lines.extend(["", "## Source Chunks", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = [note["evidence_ids"][0] for note in NOTES]
    implications = [
        "Plan evaluation with the intervention, business case, monitoring, and benefits management arrangements.",
        "Start scoping with users, decisions, theory of change, assumptions, and priority evaluation questions.",
        "Choose methods by question, causal claim, data feasibility, ethics, burden, and use rather than by familiarity.",
        "Use mixed methods when process, impact, value for money, explanation, and implementation learning all matter.",
        "Resolve data access, linkage, data quality, and protection issues before the evaluation depends on them.",
        "Create governance that can quality assure design, tools, analysis, interpretation, and reporting while still adapting to change.",
        "Plan dissemination, publication, and transparency at the start so findings can be used and trusted.",
        "Use appendix guidance when specialist risks arise: complexity, realist explanation, AI interventions, qualitative quality, transparency, PIRs, or test-and-learn work.",
        "Review capability before commissioning and build teams around the skills the evaluation actually requires.",
    ]
    lines = [
        "---",
        f"title: {yaml_quote(f'{TITLE} Practice Implications')}",
        f"description: {yaml_quote(f'Practice synthesis for {TITLE}.')}",
        f"book_id: {yaml_quote(BOOK_ID)}",
        f"collection_id: {yaml_quote(COLLECTION_ID)}",
        'note_type: "Practice"',
        f"citation_key: {yaml_quote(CITATION)}",
        "evidence_ids:",
        yaml_list(evidence),
        f"source_status: {yaml_quote(SOURCE_STATUS)}",
        "---",
        "",
        "## Source",
        "",
        f"This practice synthesis draws on the expanded notes from *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Evaluation Practice Implications",
        "",
        *[f"- {item}" for item in implications],
        "",
        "## Applying the Notes",
        "",
        "Use these implications as checks during scoping, proposal decisions, design review, method selection, data planning, governance, reporting, publication, and capability development. They should be adapted to the evaluation's context, stakes, resources, data constraints, stakeholder needs, and transparency obligations.",
        "",
        "## Concept Map",
        "",
        render_concept_map(
            {
                "map_problem": "How should the Magenta Book change evaluation practice?",
                "map_concepts": ["users and questions", "methods and data", "quality and transparency"],
                "map_mechanisms": ["early scoping", "governance and QA", "publication and use planning"],
                "map_implications": ["Build evaluation into the intervention lifecycle.", "Use specialist annexes to manage specific design risks."],
                "map_question": "What has to be true for these notes to improve a live evaluation?",
            },
            "Practice implications",
        ),
        "",
        "## Links",
        "",
        *[f"- {note_link(note)}" for note in NOTES],
        "",
        "## Source Chunks",
        "",
        source_chunks(evidence),
        "",
        "## References",
        "",
    ]
    return "\n".join(lines)


def render_evidence_summary() -> dict:
    return {
        "schema_version": "1.0",
        "generated_at": GENERATED_AT,
        "collection_id": COLLECTION_ID,
        "book_id": BOOK_ID,
        "book_title": FULL_TITLE,
        "source_status": SOURCE_STATUS,
        "rag_status": RAG_STATUS,
        "source_tool": "mcp__researchlibrary.rag_evidence_pack",
        "copyright_note": "Stores retrieval IDs and source locations only; source text is not duplicated.",
        "records": [
            {
                "section_id": note["file"].removesuffix(".qmd"),
                "section_title": note_label(note),
                "source_pages": note["pages"],
                "section_path": note["section_path"],
                "evidence_ids": note["evidence_ids"],
                "target_path": f"notes/{SLUG}/{note['file']}",
            }
            for note in NOTES
        ],
    }


def render_chapter_evidence_summary() -> dict:
    return {
        "schema_version": "1.0",
        "generated_at": GENERATED_AT,
        "collection_id": COLLECTION_ID,
        "book_id": BOOK_ID,
        "book_title": FULL_TITLE,
        "source_status": SOURCE_STATUS,
        "source_tool": "mcp__researchlibrary.rag_evidence_pack",
        "evidence_pack_defaults": {
            "include_neighbors": True,
            "limit": "8-12",
            "include_media": "only where central tables, checklists, figures, exhibits, or frameworks are needed",
        },
        "chapters": [
            {
                "chapter_number": note.get("number"),
                "chapter_title": note_label(note),
                "target_path": f"notes/{SLUG}/{note['file']}",
                "section_paths": [note["section_path"]],
                "source_pages": note["pages"],
                "evidence_ids": note["evidence_ids"],
                "media_ids": [],
                "status": "drafted",
                "note_type": note["note_type"],
            }
            for note in NOTES
        ],
    }


def update_manifest() -> None:
    path = ROOT / "data" / "research_library_notes_manifest.json"
    manifest = read_json(path)
    for book in manifest.get("books", []):
        if book.get("book_id") == BOOK_ID:
            book.update(
                {
                    "generation_mode": "generated-chapter-and-appendix-notes",
                    "target_path": f"notes/{SLUG}/index.qmd",
                    "sections": [
                        {
                            "id": re.sub(r"[^a-z0-9]+", "-", note["file"].removesuffix(".qmd").lower()).strip("-"),
                            "title": note_label(note),
                            "source_pages": note["pages"],
                            "section_path": note["section_path"],
                            "evidence_ids": note["evidence_ids"],
                            "target_path": f"notes/{SLUG}/{note['file']}",
                        }
                        for note in NOTES
                    ],
                }
            )
            break
    else:
        raise SystemExit(f"{BOOK_ID} not found in manifest")
    write_json("data/research_library_notes_manifest.json", manifest)


def generate() -> None:
    base = f"notes/{SLUG}"
    for idx, note in enumerate(NOTES):
        prev_note = NOTES[idx - 1] if idx else None
        next_note = NOTES[idx + 1] if idx + 1 < len(NOTES) else None
        write_text(f"{base}/{note['file']}", render_note(note, prev_note, next_note))
    write_text(f"{base}/index.qmd", render_index())
    write_text(f"{base}/chapter-map.qmd", render_chapter_map())
    write_text(f"{base}/concepts.qmd", render_concepts())
    write_text(f"{base}/practice-implications.qmd", render_practice())
    write_json(f"data/research-library/evidence/{SLUG}/evidence-summary.json", render_evidence_summary())
    write_json(f"data/research-library/evidence/{SLUG}/chapter-evidence-summary.json", render_chapter_evidence_summary())
    update_manifest()


if __name__ == "__main__":
    generate()
