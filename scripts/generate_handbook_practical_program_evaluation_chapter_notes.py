#!/usr/bin/env python3
"""Generate chapter-level Handbook of Practical Program Evaluation notes."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "handbook-practical-program-evaluation"
SLUG = BOOK_ID
TITLE = "Handbook of Practical Program Evaluation"
FULL_TITLE = TITLE
AUTHORS = "Kathryn E. Newcomer, Harry P. Hatry, and Joseph S. Wholey"
CITATION = "newcomer_hatry_wholey_2015_handbook_practical_program_evaluation"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2015"
GENERATED_AT = "2026-06-28"


LEGACY_EXTRACTS = [
    ("Evaluation Planning and Design", "section-01-planning-and-design.qmd"),
    ("Planning and Designing Useful Evaluations", "section-02-planning-useful-evaluations.qmd"),
    ("Performance Measurement and Program Evaluation", "section-03-performance-measurement.qmd"),
]


CONCEPT_GLOSSES = {
    "evaluation design": "The plan linking questions, evidence, analysis, reporting, and intended use.",
    "intended use": "The decision, learning, accountability, or improvement purpose the evaluation is meant to serve.",
    "stakeholder engagement": "Deliberate work with intended users and affected parties to shape useful, credible evaluation.",
    "logic model": "A representation of program resources, activities, outputs, outcomes, context, and assumptions.",
    "evaluability assessment": "An exploratory process that checks whether a program is ready for useful evaluation and which questions are worth pursuing.",
    "performance measurement": "Ongoing measurement of outputs, outcomes, service quality, or efficiency for management and improvement.",
    "comparison group": "A group used to estimate what would have happened without the program or policy.",
    "randomized controlled trial": "A design that assigns eligible units to treatment or control by chance to support causal inference.",
    "case study": "A bounded inquiry that integrates multiple evidence sources to understand implementation, context, and effects.",
    "recruitment": "Processes for enrolling the right number and type of study participants.",
    "retention": "Processes for keeping participants engaged and measured across the evaluation period.",
    "multisite evaluation": "Evaluation of a policy or program across two or more sites with attention to common and site-specific evidence.",
    "community change": "Place-based or community-level intervention where boundaries, timing, context, and causal attribution are difficult.",
    "culturally responsive evaluation": "Evaluation that treats culture, context, relationships, validity, and responsibility as integral to design and use.",
    "agency records": "Administrative, archival, or service records used as evaluation data.",
    "data quality": "The completeness, accuracy, consistency, accessibility, and interpretability of data for evaluation purposes.",
    "survey": "A structured data collection method used to obtain comparable responses from a population or sample.",
    "role playing": "A data collection method in which trained actors test service encounters or transactions.",
    "trained observer rating": "Structured observation by trained raters using defined and anchored rating scales.",
    "fieldwork": "Systematic in-person inquiry using interviews, observations, documents, and site-level evidence.",
    "internet data collection": "Online or web-enabled data collection, recruitment, communication, or observation for evaluation.",
    "semistructured interview": "An interview guided by prepared topics while preserving open-ended probing and adaptation.",
    "focus group": "A moderated group discussion used to gather interactional, interpretive, or formative evidence.",
    "stories": "Narrative evidence used to communicate experience, meaning, change, and evaluation findings.",
    "qualitative analysis": "Systematic coding, display, interpretation, and verification of qualitative data.",
    "statistics": "Quantitative techniques used to describe data, estimate relationships, test differences, and present uncertainty.",
    "cost-effectiveness analysis": "Analysis that relates costs to nonmonetized units of effectiveness.",
    "cost-benefit analysis": "Analysis that compares costs and benefits after expressing both in monetary terms where defensible.",
    "meta-analysis": "Statistical synthesis of findings across studies.",
    "systematic review": "A transparent, replicable synthesis process for locating, assessing, and summarizing prior evidence.",
    "pitfall": "A recurring evaluation problem that can weaken validity, reliability, credibility, feasibility, or use.",
    "recommendation": "A finding-linked suggestion, option, or action statement for decision makers.",
    "evaluation report": "A communication product that explains findings, methods, limitations, implications, and recommended action.",
    "contracting": "Procurement and management of external evaluation products or services.",
    "politics of evaluation": "The institutional, bureaucratic, and stakeholder dynamics that shape whether evaluation is feasible and used.",
    "evaluation capacity": "Organizational capability to commission, conduct, interpret, and use evaluation work.",
    "quality control": "Processes for checking design, data collection, analysis, reporting, and use across an evaluation.",
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def chunk_id(number: int, title: str, ordinal: int = 1) -> str:
    return f"chunk:{BOOK_ID}:ch{number:02d}-chapter-{number}-{slugify(title)}:c{ordinal:04d}"


def chapter(
    number: int,
    title: str,
    pages: str,
    group: str,
    concepts: list[str],
    core: str,
    focus: str,
    method: str,
    risk: str,
    implications: list[str],
    evidence_ids: list[str] | None = None,
) -> dict[str, Any]:
    file = f"chapter-{number:02d}-{slugify(title)}.qmd"
    section_path = f"{GROUP_PATHS[group]} > Chapter {number}: {title}"
    return {
        "number": number,
        "title": title,
        "pages": pages,
        "file": file,
        "section_path": section_path,
        "evidence_ids": evidence_ids or [chunk_id(number, title), PART_EVIDENCE[group]],
        "media_ids": [],
        "group": group,
        "concepts": concepts,
        "core": core,
        "focus": focus,
        "method": method,
        "risk": risk,
        "implications": implications,
    }


GROUP_PATHS = {
    "planning": "Part 1: Evaluation Planning and Design",
    "data": "Part 2: Practical Data Collection Procedures",
    "analysis": "Part 3: Data Analysis",
    "use": "Part 4: Use of Evaluation",
}

GROUP_TITLES = {
    "planning": "Part 1: Evaluation Planning and Design",
    "data": "Part 2: Practical Data Collection Procedures",
    "analysis": "Part 3: Data Analysis",
    "use": "Part 4: Use of Evaluation",
}

PART_EVIDENCE = {
    "planning": "chunk:handbook-practical-program-evaluation:part-1:c0001",
    "data": "chunk:handbook-practical-program-evaluation:part-2:c0001",
    "analysis": "chunk:handbook-practical-program-evaluation:part-3:c0002",
    "use": "chunk:handbook-practical-program-evaluation:part-4:c0001",
}


CHAPTERS = [
    chapter(
        1,
        "Planning and Designing Useful Evaluations",
        "49-77",
        "planning",
        ["evaluation design", "intended use", "stakeholder engagement"],
        "Useful evaluation begins by matching information needs, contextual constraints, rigor, and communication to the decisions the evaluation must inform.",
        "The opening chapter frames the handbook around evaluations that improve public and nonprofit programs, not only satisfy accountability demands.",
        "It links evaluation questions to design, data collection, analysis, reporting, and use, including the need to negotiate evaluable questions with sponsors and intended users.",
        "The main risk is designing a technically impressive study that answers questions no one can use or trust.",
        ["Begin every design with the intended users and decisions.", "Use a design matrix to connect questions, data, analysis, and reporting.", "Treat communication and use as design requirements."],
        ["chunk:handbook-practical-program-evaluation:ch01-chapter-1-planning-and-designing-useful-evaluations:c0003", "table:handbook-practical-program-evaluation:table:table-1-1:p0069:r0254", PART_EVIDENCE["planning"]],
    ),
    chapter(
        2,
        "Analyzing and Engaging Stakeholders",
        "78-103",
        "planning",
        ["stakeholder engagement", "intended use", "culturally responsive evaluation"],
        "Stakeholder analysis should precede and guide engagement so evaluations have clear users, purposes, roles, and adaptive strategies for changing settings.",
        "The chapter treats stakeholder work as both practical and ethical, especially for utilization-focused evaluation.",
        "It offers techniques for identifying key stakeholders, clarifying evaluation purposes, mapping influence, and deciding who should be engaged at each stage.",
        "The main risk is mistaking participation for use, or engaging stakeholders without understanding power, culture, and changing circumstances.",
        ["Analyze stakeholders before designing engagement.", "Name primary intended users explicitly.", "Adapt engagement as evaluation purposes and stakeholder relationships change."],
    ),
    chapter(
        3,
        "Using Logic Models",
        "104-129",
        "planning",
        ["logic model", "evaluation design", "performance measurement"],
        "Logic models help evaluators and program staff clarify program theory, identify measures, and frame performance stories without treating the model as final truth.",
        "The chapter presents logic models as tools for planning, communication, management, monitoring, and evaluation design.",
        "It describes building and verifying models from documents, stakeholder interviews, problem definitions, activities, outputs, outcomes, context, and assumptions.",
        "The main risk is using a model mechanically, without testing whether it represents how the program actually works.",
        ["Use logic models to surface assumptions before selecting measures.", "Revise models as evidence accumulates.", "Keep context and external factors visible."],
    ),
    chapter(
        4,
        "Exploratory Evaluation",
        "130-149",
        "planning",
        ["evaluability assessment", "evaluation design", "performance measurement"],
        "Exploratory evaluation helps programs clarify goals, feasibility, data, measures, and next evaluation steps before committing to a definitive study.",
        "The chapter covers evaluability assessment, rapid feedback evaluation, evaluation synthesis, and small-sample studies.",
        "Each approach is positioned as a way to produce useful preliminary findings while focusing or testing future evaluation work.",
        "The main risk is launching a large evaluation before program logic, measures, stakeholders, and intended uses are stable enough.",
        ["Use exploratory work when readiness is uncertain.", "Test measures and data access before scaling evaluation.", "Use short-cycle findings to focus later studies."],
    ),
    chapter(
        5,
        "Performance Measurement",
        "150-178",
        "planning",
        ["performance measurement", "logic model", "intended use"],
        "Performance measurement systems can support improvement when measures are valid, understandable, affordable, and presented for decisions rather than compliance alone.",
        "The chapter explains how ongoing outcome and performance data can inform management and public accountability.",
        "It emphasizes selecting good measures, implementing measurement systems, and presenting performance information effectively.",
        "The main risk is creating disruptive or low-validity measurement routines that absorb resources without improving performance.",
        ["Choose measures users can interpret and act on.", "Balance information value against burden.", "Report performance in formats that support management action."],
    ),
    chapter(
        6,
        "Comparison Group Designs",
        "179-201",
        "planning",
        ["comparison group", "evaluation design", "statistics"],
        "Comparison group designs estimate program effects when randomization is unavailable, but their credibility depends on how well they approximate the counterfactual.",
        "The chapter introduces nonrandomized alternatives for assessing impacts and the logic of comparing treated units with similar untreated units.",
        "It emphasizes design choices that reduce selection bias and make causal claims more credible.",
        "The main risk is presenting weak comparisons as causal evidence without acknowledging alternative explanations.",
        ["Document why the comparison group is credible.", "Use baseline and contextual evidence to test comparability.", "Report design limitations plainly."],
    ),
    chapter(
        7,
        "Randomized Controlled Trials",
        "202-224",
        "planning",
        ["randomized controlled trial", "comparison group", "evaluation design"],
        "Randomized controlled trials can provide strong causal evidence when assignment, implementation, measurement, ethics, and analysis remain aligned.",
        "The chapter explains how random assignment supports impact estimation and what implementation conditions must hold.",
        "It addresses design choices, threats, practical constraints, and the role of RCTs in public and nonprofit evaluation.",
        "The main risk is treating randomization as sufficient when recruitment, compliance, attrition, or ethics compromise the design.",
        ["Randomize only when it is ethical and operationally feasible.", "Protect assignment and follow-up procedures.", "Track implementation conditions that affect interpretation."],
    ),
    chapter(
        8,
        "Conducting Case Studies",
        "225-248",
        "planning",
        ["case study", "fieldwork", "qualitative analysis"],
        "Case studies integrate multiple sources to understand programs in context, including exploratory, descriptive, and explanatory evaluation questions.",
        "The chapter distinguishes types of case studies and shows how to design, collect, analyze, and report case evidence.",
        "It emphasizes documents, interviews, observations, site visits, pilot testing, training, and audience-sensitive reporting.",
        "The main risk is collecting rich site evidence without enough structure to support credible cross-case or causal interpretation.",
        ["Define the case and case-study purpose early.", "Use multiple data sources for corroboration.", "Plan analysis and reporting before fieldwork begins."],
    ),
    chapter(
        9,
        "Recruitment and Retention of Study Participants",
        "249-267",
        "planning",
        ["recruitment", "retention", "evaluation design"],
        "Recruitment and retention are design-quality issues because sample coverage and continued participation determine whether evaluation findings are credible.",
        "The chapter identifies common barriers to enrolling and keeping participants in evaluation studies.",
        "It offers practical strategies for clearance, outreach, participant tracking, incentives, staff roles, and realistic scheduling.",
        "The main risk is underestimating the time, permissions, and relationship work needed to secure usable data.",
        ["Plan recruitment and retention before data collection.", "Budget time for IRB and administrative clearance.", "Monitor enrollment and follow-up continuously."],
    ),
    chapter(
        10,
        "Designing, Managing, and Analyzing Multisite Evaluations",
        "268-299",
        "planning",
        ["multisite evaluation", "evaluation design", "quality control"],
        "Multisite evaluations require common design discipline while preserving enough site-level detail to explain variation across contexts.",
        "The chapter provides principles and tools for designing, managing, collecting, analyzing, and reporting across multiple sites.",
        "It covers common and single-site data, monitoring implementation, quality control, data management, analysis, and communication.",
        "The main risk is forcing sites into a common template that hides meaningful differences or allowing local variation to defeat synthesis.",
        ["Specify common data requirements across sites.", "Track site-level implementation and context.", "Build quality control into field and analysis plans."],
    ),
    chapter(
        11,
        "Evaluating Community Change Programs",
        "300-322",
        "planning",
        ["community change", "case study", "comparison group"],
        "Community change evaluation must handle broad aims, place-based complexity, shifting implementation, difficult units of analysis, and weak causal leverage.",
        "The chapter identifies why multiservice and place-based interventions need special evaluation design attention.",
        "It offers guidance on metrics, units of analysis, time periods, available data, data systems, and feasible methods.",
        "The main risk is applying individual-level impact logic to community-level change without adapting to context and scale.",
        ["Choose units of analysis deliberately.", "Match time horizons to plausible change pathways.", "Use mixed evidence when causal attribution is limited."],
    ),
    chapter(
        12,
        "Culturally Responsive Evaluation",
        "323-357",
        "planning",
        ["culturally responsive evaluation", "stakeholder engagement", "quality control"],
        "Culturally responsive evaluation strengthens validity, rigor, and responsibility by making culture and context integral to every evaluation stage.",
        "The chapter reviews CRE theory, practice, history, and applications in diverse communities.",
        "It frames culture as a design and validity issue, not an optional sensitivity add-on.",
        "The main risk is using standardized evaluation routines that ignore local meanings, relationships, histories, and consequences.",
        ["Build cultural inquiry into design, sampling, data collection, and interpretation.", "Engage stakeholders in culturally appropriate ways.", "Judge rigor partly by contextual validity and responsibility."],
    ),
    chapter(
        13,
        "Using Agency Records",
        "367-384",
        "data",
        ["agency records", "data quality", "performance measurement"],
        "Agency records can be efficient evaluation data, but only after checking definitions, completeness, access, consistency, and fit with evaluation questions.",
        "The chapter discusses administrative and archival records as common sources for public program evaluation.",
        "It addresses missing records, inconsistent definitions, access barriers, data element quality, and practical ways to improve usability.",
        "The main risk is assuming that existing records are evaluation-ready because they already exist.",
        ["Audit administrative data before relying on it.", "Check whether definitions match evaluation measures.", "Document access, missingness, and quality limits."],
    ),
    chapter(
        14,
        "Using Surveys",
        "385-424",
        "data",
        ["survey", "data quality", "statistics"],
        "Surveys can provide comparable evidence from clients, households, organizations, or officials when sampling, question wording, mode, and response quality are managed well.",
        "The chapter reviews survey design, administration modes, question construction, pretesting, sampling, and response-rate concerns.",
        "It emphasizes reliable measurement of perceptions, experiences, behaviors, demographics, and service outcomes.",
        "The main risk is treating survey administration as routine while question design or nonresponse undermines validity.",
        ["Pretest survey instruments with target respondents.", "Choose mode and sample to fit the population.", "Report response limits and measurement choices."],
    ),
    chapter(
        15,
        "Role Playing",
        "425-453",
        "data",
        ["role playing", "data quality", "evaluation design"],
        "Role playing can reveal service quality and differential treatment by observing standardized transactions that other methods may miss.",
        "The chapter describes trained role players or testers who document service encounters for empirical analysis.",
        "It covers sampling, scripts, data collection forms, training, management, quality control, ethics, and legal considerations.",
        "The main risk is collecting vivid transaction evidence without adequate standardization, documentation, or ethical review.",
        ["Train role players carefully.", "Standardize scenarios and recording forms.", "Address legal and ethical constraints before fieldwork."],
    ),
    chapter(
        16,
        "Using Ratings by Trained Observers",
        "454-487",
        "data",
        ["trained observer rating", "data quality", "fieldwork"],
        "Trained observer ratings turn observed conditions into systematic data when definitions, rating anchors, sampling, training, and supervision are explicit.",
        "The chapter explains how anchored ratings can assess physical conditions, service settings, functioning, or maintenance quality.",
        "It covers deciding what to observe, defining rating scales, preparing forms, training raters, pretesting, sampling, and collating data.",
        "The main risk is producing subjective labels that cannot be verified, compared, or acted on.",
        ["Define every rating category concretely.", "Use training and trial runs before data collection.", "Plan how observations will be stored, checked, and reported."],
    ),
    chapter(
        17,
        "Collecting Data in the Field",
        "488-518",
        "data",
        ["fieldwork", "case study", "qualitative analysis"],
        "Field data collection makes evaluation evidence more contextual and credible when site visits, interviews, observations, and records are organized systematically.",
        "The chapter focuses on field studies for implementation, process, organizational, and outcome questions.",
        "It addresses models of fieldwork, staffing, site protocols, data maintenance, analysis, coding, and reliability.",
        "The main risk is accumulating unstructured site notes that are hard to compare, verify, or use.",
        ["Prepare site protocols and topic guides.", "Train field staff for consistency and adaptation.", "Code and maintain field data throughout collection."],
    ),
    chapter(
        18,
        "Using the Internet",
        "519-537",
        "data",
        ["internet data collection", "survey", "data quality"],
        "Internet tools can support evaluation data collection and communication, but they require attention to coverage, access, privacy, usability, and data integrity.",
        "The chapter reviews web-enabled options for collecting, managing, and communicating evaluation information.",
        "It positions online methods as useful when they fit respondents, questions, and data protection requirements.",
        "The main risk is choosing online methods for convenience while excluding participants or weakening data quality.",
        ["Check digital access and coverage before using online methods.", "Protect privacy and data security.", "Match online tools to the evaluation question and population."],
    ),
    chapter(
        19,
        "Semi-Structured Interviews",
        "538-551",
        "data",
        ["semistructured interview", "fieldwork", "qualitative analysis"],
        "Semi-structured interviews help evaluators learn from knowledgeable respondents while preserving enough consistency for analysis.",
        "The chapter focuses on open-ended, person-to-person interviews used in field studies and case studies.",
        "It covers arranging interviews, developing guides, probing, recording, analysis, and reporting.",
        "The main risk is relying on informal conversation without enough preparation, documentation, or analytic structure.",
        ["Prepare interview guides around evaluation questions.", "Use probes without leading respondents.", "Plan how interview data will be coded and reported."],
    ),
    chapter(
        20,
        "Focus Group Interviewing",
        "552-576",
        "data",
        ["focus group", "semistructured interview", "qualitative analysis"],
        "Focus groups generate interactional evidence that can inform design, interpretation, and understanding of program experiences.",
        "The chapter presents focus groups as useful in design, pilot testing, implementation assessment, and interpretation of findings.",
        "It covers recruiting, moderation, question routes, note taking, recording, analysis, and reporting.",
        "The main risk is treating group discussion as representative survey evidence or allowing moderation problems to distort findings.",
        ["Use focus groups for depth and interaction, not prevalence estimates.", "Recruit groups deliberately.", "Use skilled moderation and systematic analysis."],
    ),
    chapter(
        21,
        "Using Stories in Evaluation",
        "577-597",
        "data",
        ["stories", "qualitative analysis", "evaluation report"],
        "Stories can deepen evaluation understanding and communication when collected and analyzed with qualitative discipline.",
        "The chapter explains how stories can illuminate experience, change, meaning, and findings for audiences.",
        "It covers when stories are useful, how to elicit them, how to analyze them, and how to avoid misleading anecdotal use.",
        "The main risk is using compelling narratives as evidence without transparent selection and analysis.",
        ["Collect stories with explicit questions and criteria.", "Analyze stories alongside other evidence.", "Use stories to illuminate findings, not replace evidence."],
    ),
    chapter(
        22,
        "Analyzing Qualitative Data",
        "603-635",
        "analysis",
        ["qualitative analysis", "case study", "data quality"],
        "Qualitative analysis turns observations, documents, and interviews into credible findings through coding, display, interpretation, triangulation, and verification.",
        "The chapter reviews enumerative, descriptive, hermeneutic, and explanatory approaches to qualitative data analysis.",
        "It emphasizes content analysis, data reduction, displays, conclusion drawing, credibility checks, and transparent analytic choices.",
        "The main risk is presenting themes without showing how they were developed, challenged, and verified.",
        ["Develop an explicit coding and display strategy.", "Use triangulation and peer checks to strengthen credibility.", "Document analytic decisions and limitations."],
    ),
    chapter(
        23,
        "Using Statistics in Evaluation",
        "636-677",
        "analysis",
        ["statistics", "survey", "data quality"],
        "Statistical analysis strengthens evaluation conclusions when techniques match questions, samples, measurement scales, assumptions, and reporting needs.",
        "The chapter introduces practical statistical tools for evaluators, including sampling, significance tests, regression, and visualization.",
        "It emphasizes choosing appropriate analyses and reporting quantitative findings clearly.",
        "The main risk is using statistical procedures mechanically or reporting precision that the data cannot support.",
        ["Match statistical tests to the evaluation question and data.", "Report uncertainty and assumptions clearly.", "Use visualization to aid interpretation."],
    ),
    chapter(
        24,
        "Cost-Effectiveness and Cost-Benefit Analysis",
        "678-714",
        "analysis",
        ["cost-effectiveness analysis", "cost-benefit analysis", "statistics"],
        "Economic analysis helps decision makers compare value by relating program costs to effects or monetized benefits.",
        "The chapter differentiates cost-effectiveness and cost-benefit analysis and explains when each is appropriate.",
        "It covers identifying costs, valuing benefits, choosing effectiveness measures, common problems, and presenting results.",
        "The main risk is hiding value judgments or uncertain assumptions inside apparently precise monetary estimates.",
        ["State the perspective for costs and benefits.", "Use cost-effectiveness when monetizing benefits is not defensible.", "Show sensitivity to valuation assumptions."],
        ["chunk:handbook-practical-program-evaluation:ch24-chapter-24-cost-effectiveness-and-cost-benefit-analysis:c0023", "table_segment:handbook-practical-program-evaluation:table:table-24-6:p0695:r0254:s002", PART_EVIDENCE["analysis"]],
    ),
    chapter(
        25,
        "Meta-Analyses, Systematic Reviews, and Evaluation Syntheses",
        "715-740",
        "analysis",
        ["meta-analysis", "systematic review", "statistics"],
        "Evidence synthesis helps evaluators learn from prior studies by making search, inclusion, quality assessment, and synthesis procedures explicit.",
        "The chapter distinguishes meta-analysis, systematic review, and research synthesis.",
        "It covers benefits, logistics, resources, obstacles, and how synthesis can identify strong, absent, or ambiguous evidence.",
        "The main risk is summarizing prior evaluations without transparent criteria for study quality and inclusion.",
        ["Use explicit search and inclusion procedures.", "Assess study quality before synthesis.", "Distinguish absence of evidence from evidence of no effect."],
    ),
    chapter(
        26,
        "Pitfalls in Evaluations",
        "745-776",
        "use",
        ["pitfall", "quality control", "evaluation report"],
        "Recognizing evaluation pitfalls strengthens credibility because every evaluation has limitations that should be anticipated, reduced, and explained.",
        "The chapter provides a checklist for reviewing potential weaknesses in planning, implementation, validity, reliability, and credibility.",
        "It encourages evaluators to acknowledge limits and explain their implications for interpretation and use.",
        "The main risk is concealing or overlooking threats that users need to understand before acting on findings.",
        ["Use pitfall checklists during design and review.", "Explain limitations directly.", "Link each limitation to its likely effect on interpretation."],
    ),
    chapter(
        27,
        "Writing Recommendations",
        "777-790",
        "use",
        ["recommendation", "intended use", "evaluation report"],
        "Recommendations are useful when they flow from findings, respect decision contexts, and offer practical options for improving programs.",
        "The chapter focuses on turning findings into suggestions and options that managers and policymakers can act on.",
        "It treats recommendations as a bridge between evidence and improvement, not as unsupported evaluator preference.",
        "The main risk is making recommendations that outrun the evidence or ignore feasibility and user context.",
        ["Tie every recommendation to findings.", "Offer options when evidence supports more than one path.", "Check feasibility with intended users."],
    ),
    chapter(
        28,
        "Writing Evaluation Reports",
        "791-806",
        "use",
        ["evaluation report", "recommendation", "intended use"],
        "Evaluation reports should convey findings, methods, limits, and implications clearly enough to stimulate constructive action.",
        "The chapter addresses how to craft a core message, communicate findings, and explain methods efficiently.",
        "It emphasizes clarity, audience fit, concise presentation, and methodological transparency.",
        "The main risk is producing reports that are technically complete but unreadable or unusable.",
        ["Shape reports around the core message and audience needs.", "Explain methods and limitations without burying findings.", "Use concise language and structure."],
    ),
    chapter(
        29,
        "Contracting for Evaluation Products and Services",
        "807-840",
        "use",
        ["contracting", "quality control", "evaluation report"],
        "Evaluation contracting requires clear plans, realistic requests, qualified contractors, active monitoring, and product-quality management.",
        "The chapter guides sponsors through procuring and managing evaluation services.",
        "It covers evaluation plans, RFPs, contractor selection, progress monitoring, report development, and quality assurance.",
        "The main risk is treating procurement as paperwork rather than a core determinant of evaluation quality and usefulness.",
        ["Write feasible RFPs tied to evaluation purpose.", "Monitor contractor progress and data quality.", "Agree on report outlines and review milestones early."],
    ),
    chapter(
        30,
        "Evaluation in Government and the Politics of Evaluation",
        "841-857",
        "use",
        ["politics of evaluation", "intended use", "stakeholder engagement"],
        "Government evaluation use depends on navigating political and bureaucratic realities while protecting credibility and improvement purposes.",
        "The chapter discusses how evaluation operates in government and nonprofit settings where information, accountability, and politics interact.",
        "It offers guidance for overcoming institutional barriers, getting findings used, and improving policies and programs.",
        "The main risk is assuming that evidence will be used automatically without attention to timing, incentives, and politics.",
        ["Map political and bureaucratic constraints.", "Protect evaluation credibility while engaging decision makers.", "Time findings for real policy and management cycles."],
    ),
    chapter(
        31,
        "Evaluation Challenges, Issues, and Trends",
        "858-874",
        "use",
        ["evaluation capacity", "quality control", "performance measurement"],
        "The final chapter frames evaluation quality, evaluator capacity, standards, ethics, use, and future trends as continuing responsibilities.",
        "The editors synthesize challenges around quality control, evaluator selection and training, standards and ethics, and using findings to improve programs.",
        "They also discuss the relationship between performance monitoring and evaluation studies and likely future directions for the field.",
        "The main risk is treating evaluation as isolated projects rather than an organizational capacity for learning and improvement.",
        ["Build organizational capacity for evaluation use.", "Apply standards and ethics across the whole process.", "Connect performance monitoring with deeper evaluation studies."],
        ["chunk:handbook-practical-program-evaluation:ch31-chapter-31-evaluation-challenges-issues-and-trends:c0001", "chunk:handbook-practical-program-evaluation:ch31-chapter-31-evaluation-challenges-issues-and-trends:c0009", PART_EVIDENCE["use"]],
    ),
]


def wrap(text: str) -> str:
    return "\n".join(textwrap.wrap(text, width=100, break_long_words=False, replace_whitespace=False))


def yaml_list(values: list[str]) -> str:
    return "\n".join(f'  - "{value}"' for value in values)


def all_evidence_ids() -> list[str]:
    seen: set[str] = set()
    evidence: list[str] = []
    for chapter_item in CHAPTERS:
        for evidence_id in chapter_item["evidence_ids"]:
            if evidence_id not in seen:
                seen.add(evidence_id)
                evidence.append(evidence_id)
    return evidence


def write_text(relative: str, text: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(relative: str, payload: dict[str, Any]) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_chunks(evidence_ids: list[str]) -> str:
    return "\n".join(f"- `{evidence_id}`" for evidence_id in evidence_ids)


def chapter_link(chapter_item: dict[str, Any]) -> str:
    return f"[Chapter {chapter_item['number']}: {chapter_item['title']}]({chapter_item['file']})"


def concept_lines(concepts: list[str]) -> list[str]:
    return [f"- **{concept}**: {CONCEPT_GLOSSES[concept]}" for concept in concepts]


def render_chapter(chapter_item: dict[str, Any], prev_chapter: dict[str, Any] | None, next_chapter: dict[str, Any] | None) -> str:
    lines = [
        "---",
        f'title: "Chapter {chapter_item["number"]:02d}: {chapter_item["title"]}"',
        f'description: "Detailed study notes for Chapter {chapter_item["number"]} of {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Chapter"',
        f'chapter_number: {chapter_item["number"]}',
        f'source_pages: "{chapter_item["pages"]}"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(chapter_item["evidence_ids"]),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        f'<div class="chapter-meta"><span>{YEAR}</span><span>MCP evaluation-texts</span><span>Status: {SOURCE_STATUS}</span><span>Chapter {chapter_item["number"]}</span><span>Source pages {chapter_item["pages"]}</span></div>',
        "",
        wrap(f'This note summarises Chapter {chapter_item["number"]}, "{chapter_item["title"]}," from {AUTHORS}\'s *{FULL_TITLE}* [@{CITATION}]. It is a paraphrased study note based on source-linked MCP research-library retrieval records, not a substitute for the chapter.'),
        "",
        "The retrieval trail is retained in the source records at the bottom of the page. The note paraphrases the chapter's argument and procedures, and it does not reproduce textbook tables, checklists, figures, boxes, or extended passages.",
        "",
        "## Core Argument",
        "",
        chapter_item["core"],
        "",
        "## Study Summary",
        "",
        wrap(chapter_item["focus"]),
        "",
        wrap(chapter_item["method"]),
        "",
        wrap(chapter_item["risk"]),
        "",
        wrap(f"Within the wider book, this chapter belongs to {GROUP_TITLES[chapter_item['group']]}. It should be read alongside the neighboring chapters because the handbook treats design, data collection, analysis, and use as connected evaluation work."),
        "",
        "## Key Concepts",
        "",
    ]
    lines.extend(concept_lines(chapter_item["concepts"]))
    lines.extend(["", "## Chapter Structure", ""])
    lines.extend(
        [
            f"- Design problem: {chapter_item['core']}",
            f"- Evidence focus: {chapter_item['focus']}",
            f"- Practice method: {chapter_item['method']}",
            f"- Quality risk: {chapter_item['risk']}",
        ]
    )
    lines.extend(["", "## Practical Implications", ""])
    lines.extend(f"- {item}" for item in chapter_item["implications"])
    lines.extend(
        [
            "",
            "## Connections",
            "",
            "- Book overview: [Overview](index.qmd)",
            "- Reading route: [Chapter Map](chapter-map.qmd)",
            "- Concepts synthesis: [Core Concepts](concepts.qmd)",
            "- Practice synthesis: [Practice Implications](practice-implications.qmd)",
        ]
    )
    if prev_chapter:
        lines.append(f"- Previous: {chapter_link(prev_chapter)}")
    if next_chapter:
        lines.append(f"- Next: {chapter_link(next_chapter)}")
    lines.extend(f"- Legacy extract retained: [{title}]({file})" for title, file in LEGACY_EXTRACTS)
    lines.extend(
        [
            "",
            "## Study Prompts",
            "",
            f"- What decision or design problem does Chapter {chapter_item['number']} help resolve?",
            "- Which evidence source should be reopened before using this summary in applied work?",
            "- Which quality risk in the chapter is most likely to affect a live evaluation?",
            "",
            "## Source Records",
            "",
            source_chunks(chapter_item["evidence_ids"]),
            "",
            "## References",
            "",
        ]
    )
    return "\n".join(lines)


def render_index() -> str:
    evidence = all_evidence_ids()
    lines = [
        "---",
        f'title: "{TITLE}"',
        f'description: "Book overview and chapter-level study-note index for {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Book"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence[:12]),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        '<div class="landing-stack">',
        "",
        "::: {.directory-hero}",
        '<span class="hero-eyebrow">Book notes</span>',
        "",
        f"# {TITLE}",
        "",
        wrap(f"Chapter-level study notes on *{FULL_TITLE}* [@{CITATION}]. These notes are generated from source-linked MCP research-library records and are intended for study, comparison, and later refinement."),
        "",
        '<div class="page-metadata">',
        f"  <span>{len(CHAPTERS)} chapter notes</span>",
        f"  <span>{YEAR}</span>",
        f"  <span>Source status: {SOURCE_STATUS}</span>",
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
        '::: {.section-card}',
        '<span class="page-badge badge-synthesis">Synthesis</span>',
        "",
        "### [Core Concepts](concepts.qmd)",
        "",
        "Recurring ideas and distinctions used across these chapter notes.",
        ":::",
        "",
        '::: {.section-card}',
        '<span class="page-badge badge-map">Map</span>',
        "",
        "### [Chapter Map](chapter-map.qmd)",
        "",
        "Source chapters, page ranges, and reading routes.",
        ":::",
        "",
        '::: {.section-card}',
        '<span class="page-badge badge-practice">Practice</span>',
        "",
        "### [Practice Implications](practice-implications.qmd)",
        "",
        "Practical evaluation design habits drawn from the notes.",
        ":::",
        ":::",
        "",
        "</div>",
        "",
        "## Source",
        "",
        f'<div class="chapter-meta"><span>{YEAR}</span><span>MCP evaluation-texts</span><span>Status: {SOURCE_STATUS}</span><span>Book overview</span></div>',
        "",
        wrap(f"This index summarises generated chapter-level study notes for {AUTHORS}'s *{FULL_TITLE}* [@{CITATION}]. The generated pages use selected MCP research-library retrieval records and compact evidence summaries."),
        "",
        "## Core Argument",
        "",
        "Practical evaluation improves programs when evaluators align design, data collection, analysis, reporting, contracting, and use with real information needs and credible evidence standards.",
        "",
        "## Chapter Notes",
        "",
    ]
    for group, title in GROUP_TITLES.items():
        lines.extend(["", f"### {title}", ""])
        lines.extend(f"- {chapter_link(chapter_item)} - source pages {chapter_item['pages']}" for chapter_item in CHAPTERS if chapter_item["group"] == group)
    lines.extend(["", "## Legacy Extracts", ""])
    lines.extend(f"- [{title}]({file})" for title, file in LEGACY_EXTRACTS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_chapter_map() -> str:
    evidence = all_evidence_ids()
    lines = [
        "---",
        f'title: "{TITLE} Chapter Map"',
        f'description: "Chapter-level reading map for {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Map"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence[:12]),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        f"This map organises the generated chapter notes for *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Reading Route",
        "",
        "- **Plan useful evaluations**: Chapters 1-12 cover design, stakeholders, logic, exploratory work, monitoring, causal designs, case studies, multisite work, community change, and culturally responsive evaluation.",
        "- **Collect defensible data**: Chapters 13-21 cover records, surveys, role playing, trained observation, fieldwork, internet methods, interviews, focus groups, and stories.",
        "- **Analyze transparently**: Chapters 22-25 cover qualitative analysis, statistics, economic analysis, and evidence synthesis.",
        "- **Support use**: Chapters 26-31 cover pitfalls, recommendations, reports, contracting, politics, quality, standards, and evaluation capacity.",
        "",
        "## Chapters",
        "",
        "| Chapter | Source Pages | Main Design Question | Link |",
        "|---|---:|---|---|",
    ]
    for chapter_item in CHAPTERS:
        lines.append(f"| {chapter_item['number']}. {chapter_item['title']} | {chapter_item['pages']} | {chapter_item['core']} | [{chapter_item['file']}]({chapter_item['file']}) |")
    lines.extend(["", "## Legacy Extracts", ""])
    lines.extend(f"- [{title}]({file})" for title, file in LEGACY_EXTRACTS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = all_evidence_ids()
    used: list[str] = []
    for chapter_item in CHAPTERS:
        for concept in chapter_item["concepts"]:
            if concept not in used:
                used.append(concept)
    clusters = {
        "Design and Use": ["evaluation design", "intended use", "stakeholder engagement", "logic model", "evaluability assessment", "performance measurement"],
        "Design Options": ["comparison group", "randomized controlled trial", "case study", "multisite evaluation", "community change", "culturally responsive evaluation"],
        "Data Collection": ["agency records", "survey", "role playing", "trained observer rating", "fieldwork", "internet data collection", "semistructured interview", "focus group", "stories"],
        "Analysis and Synthesis": ["qualitative analysis", "statistics", "cost-effectiveness analysis", "cost-benefit analysis", "meta-analysis", "systematic review"],
        "Use and Management": ["pitfall", "recommendation", "evaluation report", "contracting", "politics of evaluation", "evaluation capacity", "quality control"],
    }
    lines = [
        "---",
        f'title: "{TITLE} Core Concepts"',
        f'description: "Concept synthesis for {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Synthesis"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence[:12]),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        "## Source",
        "",
        f"This synthesis draws on the generated chapter notes from *{FULL_TITLE}* [@{CITATION}].",
        "",
        "## Concept Clusters",
        "",
    ]
    for title, concepts in clusters.items():
        lines.extend([f"### {title}", ""])
        lines.extend(concept_lines([concept for concept in concepts if concept in used]))
        lines.append("")
    lines.extend(["## Chapter Links", ""])
    lines.extend(f"- {chapter_link(chapter_item)}" for chapter_item in CHAPTERS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = all_evidence_ids()
    implications = [
        "Start with intended users, information needs, and feasible decisions before choosing methods.",
        "Use logic models, exploratory evaluation, and evaluability assessment to clarify whether a program is ready for more definitive evaluation.",
        "Treat data collection as a design problem: records, surveys, fieldwork, interviews, observations, focus groups, and stories each answer different questions.",
        "Use causal designs only when assignment, comparison, measurement, and implementation conditions support the claim being made.",
        "Build quality checks into recruitment, retention, fieldwork, coding, statistical analysis, reporting, and contracting.",
        "Make analysis transparent enough that users can see how findings were produced and where limitations remain.",
        "Use cost-effectiveness, cost-benefit analysis, and evidence synthesis when decision makers need to compare value or prior evidence.",
        "Write recommendations and reports that flow from findings and are shaped for the audience that can act on them.",
        "Treat politics, procurement, standards, ethics, and organizational evaluation capacity as central to whether evaluation evidence is used.",
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
        yaml_list(evidence[:12]),
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
    lines.extend(f"- {chapter_link(chapter_item)}" for chapter_item in CHAPTERS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_evidence_summary() -> dict[str, Any]:
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
                "section_id": f"chapter-{chapter_item['number']:02d}",
                "section_title": f"Chapter {chapter_item['number']}: {chapter_item['title']}",
                "source_pages": chapter_item["pages"],
                "section_path": chapter_item["section_path"],
                "evidence_ids": chapter_item["evidence_ids"],
                "media_ids": chapter_item["media_ids"],
                "target_path": f"notes/{SLUG}/{chapter_item['file']}",
            }
            for chapter_item in CHAPTERS
        ],
    }


def render_chapter_evidence_summary() -> dict[str, Any]:
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
            "include_media": False,
            "basis": "Part introductions plus chapter-start records and selected chapter-specific records.",
        },
        "chapters": [
            {
                "chapter_number": chapter_item["number"],
                "chapter_title": chapter_item["title"],
                "target_path": f"notes/{SLUG}/{chapter_item['file']}",
                "section_paths": [chapter_item["section_path"]],
                "source_pages": chapter_item["pages"],
                "evidence_ids": chapter_item["evidence_ids"],
                "media_ids": chapter_item["media_ids"],
                "status": "drafted",
            }
            for chapter_item in CHAPTERS
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
                    "id": f"chapter-{chapter_item['number']:02d}",
                    "title": f"Chapter {chapter_item['number']}: {chapter_item['title']}",
                    "source_pages": chapter_item["pages"],
                    "section_path": chapter_item["section_path"],
                    "evidence_ids": chapter_item["evidence_ids"],
                    "target_path": f"notes/{SLUG}/{chapter_item['file']}",
                }
                for chapter_item in CHAPTERS
            ]
            break
    else:
        raise SystemExit(f"{BOOK_ID} not found in manifest")
    write_json("data/research_library_notes_manifest.json", manifest)


def generate() -> None:
    base = f"notes/{SLUG}"
    for idx, chapter_item in enumerate(CHAPTERS):
        prev_chapter = CHAPTERS[idx - 1] if idx else None
        next_chapter = CHAPTERS[idx + 1] if idx + 1 < len(CHAPTERS) else None
        write_text(f"{base}/{chapter_item['file']}", render_chapter(chapter_item, prev_chapter, next_chapter))
    write_text(f"{base}/index.qmd", render_index())
    write_text(f"{base}/chapter-map.qmd", render_chapter_map())
    write_text(f"{base}/concepts.qmd", render_concepts())
    write_text(f"{base}/practice-implications.qmd", render_practice())
    write_json(f"data/research-library/evidence/{SLUG}/evidence-summary.json", render_evidence_summary())
    write_json(f"data/research-library/evidence/{SLUG}/chapter-evidence-summary.json", render_chapter_evidence_summary())
    update_manifest()


if __name__ == "__main__":
    generate()
