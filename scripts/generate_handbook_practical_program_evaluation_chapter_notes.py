#!/usr/bin/env python3
"""Generate chapter-level Handbook of Practical Program Evaluation study notes."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "handbook-practical-program-evaluation"
SLUG = BOOK_ID
TITLE = "Handbook of Practical Program Evaluation"
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
    "administrative data": "Existing agency, archival, or management records used as evaluation evidence.",
    "case study": "A design for describing or explaining program operation, context, and outcomes in bounded cases.",
    "comparison group design": "A nonrandomized impact design that estimates program effects by comparing participants with a credible comparison group.",
    "contracting": "Procurement and management of external evaluation products and services.",
    "cost-benefit analysis": "Economic analysis that monetizes costs and benefits to compare net value.",
    "cost-effectiveness analysis": "Economic analysis comparing costs with nonmonetized units of effect.",
    "culturally responsive evaluation": "Evaluation that attends to cultural context, stakeholder voice, and equity in design and use.",
    "data collection plan": "The operational plan linking evaluation questions to information sources, instruments, fieldwork, and staffing.",
    "evaluation question": "A decision-relevant question that determines design, data collection, analysis, and reporting.",
    "evaluation synthesis": "Systematic combination of existing studies or findings to assess what is known.",
    "evaluability assessment": "Exploratory work to test whether a program is ready for useful evaluation.",
    "fieldwork": "On-site or direct data collection used to understand implementation, context, and outcomes.",
    "focus group": "A facilitated group interview used to elicit perceptions, experiences, and interpretation.",
    "logic model": "A representation of program resources, activities, outputs, outcomes, and assumptions.",
    "meta-analysis": "Quantitative synthesis of results from prior studies.",
    "multisite evaluation": "Evaluation across multiple locations requiring cross-site design, management, and analysis.",
    "performance measurement": "Ongoing monitoring of indicators to support accountability and improvement.",
    "recommendations": "Actionable options or suggested improvements grounded in evaluation findings.",
    "recruitment and retention": "Procedures for obtaining and keeping study participants through data collection.",
    "role playing": "A data collection method using trained actors or testers to observe service transactions.",
    "semi-structured interview": "Interviewing that uses a guide while allowing probing and open-ended response.",
    "stakeholder engagement": "Deliberate identification, analysis, and involvement of intended users and affected parties.",
    "stories": "Narrative evidence used to communicate experience, meaning, and findings memorably.",
    "survey": "Structured data collection from a population or sample.",
    "trained observer rating": "Systematic rating by observers using explicit scales or criteria.",
    "use": "Application of evaluation evidence to decisions, improvement, accountability, or learning.",
    "writing for impact": "Reporting practices that sharpen messages, evidence, methods, formats, and communication for intended users.",
}


PART_EVIDENCE = {
    "planning": "chunk:handbook-practical-program-evaluation:part-1:c0001",
    "data_collection": "chunk:handbook-practical-program-evaluation:part-2:c0001",
    "analysis": "chunk:handbook-practical-program-evaluation:part-3:c0002",
    "use": "chunk:handbook-practical-program-evaluation:part-4:c0001",
}


def slugify(text: str) -> str:
    text = text.lower()
    text = text.replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text


def chapter(
    number: int,
    title: str,
    pages: str,
    part: str,
    core: str,
    details: list[str],
    concepts: list[str],
    implications: list[str],
    section_slug: str | None = None,
) -> dict:
    section_slug = section_slug or f"ch{number:02d}-chapter-{number}-{slugify(title)}"
    return {
        "number": number,
        "title": title,
        "pages": pages,
        "part": part,
        "file": f"chapter-{number:02d}-{slugify(title)}.qmd",
        "section_path": f"{part_title(part)} > Chapter {number}: {title}",
        "evidence_ids": [
            f"chunk:{BOOK_ID}:{section_slug}:c0001",
            PART_EVIDENCE[part],
        ],
        "core": core,
        "details": details,
        "concepts": concepts,
        "implications": implications,
    }


def part_title(part: str) -> str:
    return {
        "planning": "Part 1: Evaluation Planning and Design",
        "data_collection": "Part 2: Practical Data Collection Procedures",
        "analysis": "Part 3: Data Analysis",
        "use": "Part 4: Use of Evaluation",
    }[part]


CHAPTERS = [
    chapter(1, "Planning and Designing Useful Evaluations", "49-78", "planning", "Useful evaluation design starts by matching information needs, context, rigor, and use before methods are chosen.", ["The chapter frames design as a practical alignment problem: evaluators must understand the decisions, stakeholders, program context, and evidence standards before committing to a design.", "It links evaluation questions to data, analysis, and use, stressing that credibility depends on both methodological rigor and responsiveness to the setting.", "A recurring message is that evaluation products should be envisioned early, because the eventual audience and decision use shape what data must be credible and how findings should be reported."], ["evaluation question", "stakeholder engagement", "use"], ["Start every design with intended users and information needs.", "Connect questions, measures, analysis, reporting, and use in one design logic.", "Define credibility standards before data collection begins."], "ch01-chapter-1-planning-and-designing-useful-evaluations"),
    chapter(2, "Analyzing and Engaging Stakeholders", "79-103", "planning", "Stakeholder analysis is a design task that clarifies intended users, influence, interests, and feasible engagement.", ["The chapter treats stakeholder engagement as deliberate work rather than a courtesy. Evaluators identify who can use, block, support, or be affected by evaluation information.", "It emphasizes flexibility: stakeholder interests and political context can shift during an evaluation, so engagement plans need active management.", "Engagement is tied to usefulness because the mission, goals, questions, and reporting routes are negotiated with the people who will act on the findings."], ["stakeholder engagement", "use", "evaluation question"], ["Map users, decision makers, implementers, participants, and affected groups separately.", "Use engagement to sharpen questions and intended uses.", "Build room for adaptation when stakeholder needs change."], "ch02-chapter-2-analyzing-and-engaging-stakeholders"),
    chapter(3, "Using Logic Models", "104-129", "planning", "Logic models organize program components, assumptions, outcomes, and contextual factors so evaluation questions can be focused.", ["The chapter presents logic models as tools for planning, design, management, performance monitoring, and reporting.", "Logic modeling helps evaluators and program staff surface assumptions about how activities should lead to outputs, outcomes, and longer-term change.", "The chapter also treats models as communication devices: they let evaluation findings tell a performance story that links evidence back to program elements."], ["logic model", "performance measurement", "evaluation question"], ["Use logic models to focus measures and questions.", "Verify models with staff and stakeholders rather than treating them as desk products.", "Use the model to interpret whether findings reflect theory, implementation, or measurement problems."], "ch03-chapter-3-using-logic-models"),
    chapter(4, "Exploratory Evaluation", "130-149", "planning", "Exploratory evaluation improves feasibility and usefulness when program goals, boundaries, data, or uses are unclear.", ["The chapter covers evaluability assessment, rapid feedback evaluation, evaluation synthesis, and small-sample studies.", "These approaches produce findings while also clarifying program goals, criteria, information needs, and options for more definitive evaluation.", "The central design habit is to avoid launching a large evaluation when a rapid, low-cost exploratory step would expose feasibility, data, or use problems."], ["evaluability assessment", "evaluation synthesis", "use"], ["Use evaluability assessment when program theory or stakeholder agreement is weak.", "Use rapid feedback to support timely management decisions.", "Treat exploratory work as evidence-producing, not merely preparatory."], "ch04-chapter-4-exploratory-evaluation"),
    chapter(5, "Performance Measurement", "150-177", "planning", "Performance measurement systems monitor outcomes and operations so managers can improve programs without waiting for episodic studies.", ["The chapter explains how to design measures that are meaningful, credible, and useful to decision makers.", "It cautions that monitoring systems can create burden or distort behavior if measures are poorly chosen or presented.", "Performance information is most valuable when it is reported in ways that invite interpretation, learning, and corrective action."], ["performance measurement", "use", "administrative data"], ["Select measures that matter for program improvement.", "Anticipate unintended consequences of measurement systems.", "Present performance information in forms managers can act on."], "ch05-chapter-5-performance-measurement"),
    chapter(6, "Comparison Group Designs", "178-213", "planning", "Comparison group designs estimate program impact when randomized assignment is not feasible but credible counterfactual evidence is still needed.", ["The chapter reviews alternatives to randomized trials for estimating causal effects.", "Its practical focus is improving the design, implementation, analysis, and interpretation of nonrandomized comparisons.", "The chapter pushes evaluators to document why the comparison group represents what would have happened without the program."], ["comparison group design", "evaluation question", "use"], ["Treat comparison group construction as the core validity problem.", "Document assumptions and remaining threats clearly.", "Use the design only when the evaluation question requires causal evidence."], "ch06-chapter-6-comparison-group-designs"),
    chapter(7, "Randomized Controlled Trials", "214-237", "planning", "Randomized controlled trials strengthen causal claims when assignment, implementation, ethics, and operations can support the design.", ["The chapter positions random assignment as a strong design for causal questions, but not as a default for every evaluation.", "It attends to operational requirements: eligibility, recruitment, compliance, retention, and preserving assignment integrity.", "RCTs are framed as practical studies that must still produce useful findings for stakeholders and program decisions."], ["evaluation question", "recruitment and retention", "use"], ["Use randomization only when assignment is ethical and operationally feasible.", "Protect the assignment process through implementation.", "Plan communication so causal findings are understandable to users."], "ch07-chapter-7-randomized-controlled-trials"),
    chapter(8, "Case Studies", "238-267", "planning", "Case studies answer descriptive and explanatory questions by examining programs in context.", ["The chapter treats case study designs as disciplined inquiry rather than informal illustration.", "Case studies are useful for understanding implementation, mechanisms, context, variation, and why outcomes occurred.", "The design challenge is to define cases, select evidence sources, maintain chain of evidence, and report findings so readers understand both case detail and cross-case lessons."], ["case study", "fieldwork", "evaluation question"], ["Use case studies for how and why questions.", "Define the case boundary before data collection.", "Connect narrative detail to analytic claims."], "ch08-chapter-8-case-studies"),
    chapter(9, "Recruitment and Retention of Study Participants", "238-267", "planning", "Recruitment and retention are design-critical because missing or unrepresentative participants can undermine evidence quality.", ["The chapter identifies common overconfidence about how many participants can be recruited and retained.", "It covers procedures for obtaining participants with needed characteristics and keeping them engaged through data collection.", "It also flags institutional review, burden, incentives, and tracking as practical constraints that affect sample quality."], ["recruitment and retention", "data collection plan", "use"], ["Budget more time for recruitment than optimistic plans suggest.", "Track retention risk as an evidence-quality issue.", "Align recruitment methods with ethics and participant burden."], "ch09-chapter-9-recruitment-and-retention-of-study-participants"),
    chapter(10, "Designing, Managing, and Analyzing Multisite Evaluations", "268-302", "planning", "Multisite evaluation requires coordinated design, site-level management, and cross-site analysis.", ["The chapter focuses on evaluations that must learn from multiple locations without flattening site differences.", "It highlights the need to manage shared protocols, local variation, data comparability, and cross-site interpretation.", "The design task is to decide what must be common across sites and what must remain locally responsive."], ["multisite evaluation", "data collection plan", "use"], ["Clarify common and site-specific questions.", "Create protocols that support comparability without suppressing context.", "Plan cross-site analysis before fieldwork starts."], "ch10-chapter-10-designing-managing-and-analyzing-multisite-evaluations"),
    chapter(11, "Evaluating Community Change Programs", "303-330", "planning", "Community change evaluation must handle complex interventions, shifting context, multiple actors, and long time horizons.", ["The chapter addresses initiatives whose effects emerge through partnerships, neighborhoods, systems, and community conditions.", "It emphasizes designs that can track implementation, contextual change, intermediate outcomes, and contribution rather than relying on simple single-program attribution.", "The evaluator's task is to make credible claims while respecting the open and adaptive character of community change work."], ["case study", "multisite evaluation", "performance measurement"], ["Use mixed evidence for complex community change.", "Track context and implementation alongside outcomes.", "Avoid overclaiming attribution when contribution is the defensible claim."], "ch11-chapter-11-evaluating-community-change-programs"),
    chapter(12, "Culturally Responsive Evaluation", "331-360", "planning", "Culturally responsive evaluation embeds cultural context, equity, and stakeholder voice in evaluation design and use.", ["The chapter extends design beyond technical fit to cultural fit.", "It asks evaluators to attend to communities, values, language, power, and interpretation when framing questions and judging evidence.", "Cultural responsiveness affects the full evaluation cycle: engagement, data collection, analysis, reporting, and use."], ["culturally responsive evaluation", "stakeholder engagement", "use"], ["Build cultural context into the design, not only dissemination.", "Use engagement to test whether questions and methods are respectful and valid.", "Interpret findings with attention to power and context."], "ch12-chapter-12-culturally-responsive-evaluation"),
    chapter(13, "Using Agency Records", "369-388", "data_collection", "Agency and administrative records are common evaluation data sources, but access, definitions, missingness, and quality must be assessed.", ["The chapter treats agency records as attractive but risky: they can provide counts, service histories, and outcomes, yet may be incomplete or inconsistently defined.", "Evaluators need to understand how records were created, why fields exist, and whether data elements mean the same thing across units and time.", "Administrative data become useful only when quality checks, access agreements, confidentiality, and documentation are handled carefully."], ["administrative data", "data collection plan", "performance measurement"], ["Audit record definitions before analysis.", "Check missingness and comparability across sites or time.", "Negotiate access and confidentiality early."], "ch13-chapter-13-using-agency-records"),
    chapter(14, "Using Surveys", "389-424", "data_collection", "Surveys provide structured evidence from clients, households, agencies, or other populations when questions, samples, and response processes are well designed.", ["The chapter covers population and sample surveys, including mail and electronic approaches.", "It stresses question wording, sampling, response rates, mode choice, and reliable measurement of factual information and perceptions.", "Surveys are useful when evaluators need systematic evidence that can be summarized across respondents."], ["survey", "data collection plan", "evaluation question"], ["Use surveys when structured respondent evidence is needed.", "Invest in sampling and question design before fielding.", "Plan response-rate strategies as part of validity."], "ch14-chapter-14-using-surveys"),
    chapter(15, "Role Playing", "425-453", "data_collection", "Role playing uses trained testers to observe transactions and service quality that may otherwise be hidden.", ["The chapter describes role playing, testing, and audit-study methods.", "Role players can provide evidence about service quality, access, treatment differences, and customer experience.", "The method requires careful training, ethical review, data capture, and analysis because it places researchers directly into service transactions."], ["role playing", "data collection plan", "comparison group design"], ["Use role playing when direct service encounters must be observed.", "Treat ethics and legality as design constraints.", "Train testers and document interactions consistently."], "ch15-chapter-15-role-playing"),
    chapter(16, "Using Ratings by Trained Observers", "454-486", "data_collection", "Trained observer ratings turn direct observation into systematic evidence through explicit scales and procedures.", ["The chapter covers ratings of physical conditions, interactions, facilities, and service environments.", "Anchored scales and trained raters can generate comparable data, but reliability depends on training, calibration, and quality control.", "Observer ratings are especially useful when conditions can be seen directly but are not captured well in administrative records or surveys."], ["trained observer rating", "data collection plan", "performance measurement"], ["Use explicit rating anchors and training protocols.", "Check inter-rater consistency.", "Match observation schedules to the program conditions being assessed."], "ch16-chapter-16-using-ratings-by-trained-observers"),
    chapter(17, "Collecting Data in the Field", "487-515", "data_collection", "Field data collection turns evaluation questions into systematic on-site evidence about implementation, quality, context, and outcomes.", ["The chapter addresses site visits, field staffing, interview planning, implementation evidence, and ways to avoid overcollection.", "It emphasizes frameworks that clarify what information is required for each evaluation question and which data collection strategies will gather it.", "Fieldwork should produce credible, organized evidence rather than disconnected impressions."], ["fieldwork", "data collection plan", "logic model"], ["Build a fieldwork plan from the evaluation questions.", "Specify information needs before choosing instruments.", "Use fieldwork to understand implementation and context."], "ch17-chapter-17-collecting-data-in-the-field"),
    chapter(18, "Using the Internet", "516-538", "data_collection", "Internet-based tools support literature review, online data collection, project communication, and evidence dissemination.", ["The chapter discusses Internet use for literature searches, online polls or surveys, and project web sites.", "It treats the Internet as a practical extension of evaluation data collection and communication rather than a separate method family.", "The evaluator still has to assess search quality, source credibility, coverage, respondent access, and the fit between online tools and evaluation questions."], ["data collection plan", "survey", "evaluation synthesis"], ["Use online tools only when coverage and quality fit the question.", "Document search and retrieval procedures.", "Pair Internet tools with other data sources when needed."], "ch18-chapter-18-using-the-internet"),
    chapter(19, "Semi-Structured Interviewing", "539-546", "data_collection", "Semi-structured interviews use guides and probes to collect comparable but open-ended evidence.", ["The chapter focuses on person-to-person interviewing with open-ended questions.", "It covers arranging interviews, preparing guides, interviewing techniques, and analysis/reporting of interview results.", "Semi-structured interviewing is especially important for field studies and case studies where evaluators need depth, explanation, and stakeholder interpretation."], ["semi-structured interview", "fieldwork", "case study"], ["Use interview guides to connect conversation to evaluation questions.", "Train interviewers in probing and listening.", "Plan analysis before collecting large volumes of interview data."], "ch19-chapter-19-semi-structured-interviewing"),
    chapter(20, "Focus Group Interviewing", "547-576", "data_collection", "Focus groups collect interactive qualitative evidence that can support design, interpretation, and understanding of stakeholder experience.", ["The chapter explains when focus groups are useful and when they are not intended to provide statistically representative evidence.", "Focus groups can help design interventions, pilot instruments, interpret data, and understand how a program is experienced.", "The method depends on careful group composition, questioning routes, moderation, recording, and analysis."], ["focus group", "stakeholder engagement", "semi-structured interview"], ["Use focus groups for interaction and interpretation, not numeric representation.", "Prepare questioning routes that fit the evaluation purpose.", "Analyze group data systematically after collection."], "ch20-chapter-20-focus-group-interviewing"),
    chapter(21, "Using Stories in Evaluation", "577-598", "data_collection", "Stories can make evaluation findings vivid and memorable when collected and presented systematically.", ["The chapter argues that stories can enrich evaluation by communicating experience, emotion, and meaning.", "It does not treat stories as replacements for quantitative evidence; instead, stories can complement other evidence and help audiences understand findings.", "Credibility depends on systematic collection, careful selection, preservation of intent, and transparency about what the story represents."], ["stories", "use", "case study"], ["Collect stories with a clear topic or evaluation question.", "Use stories to illuminate evidence, not to replace it.", "Preserve key details while editing for clarity and ethics."], "ch21-chapter-21-using-stories-in-evaluation"),
    chapter(22, "Qualitative Data Analysis", "605-638", "analysis", "Qualitative analysis turns field notes, documents, observations, and interviews into credible patterns, explanations, and findings.", ["The chapter outlines enumerative, descriptive, hermeneutic, and explanatory approaches to qualitative analysis.", "It covers coding, categorizing, abstracting, transforming, and comparing data while keeping analysis tied to evaluation questions.", "The chapter treats qualitative analysis as systematic work that requires judgment, transparency, and fit with the evaluation purpose."], ["fieldwork", "case study", "evaluation question"], ["Choose analysis strategies that fit the question and evidence.", "Document coding and category decisions.", "Connect themes to findings and actionable interpretation."], "ch22-chapter-22-qualitative-data-analysis"),
    chapter(23, "Using Statistics in Evaluation", "639-684", "analysis", "Statistical analysis helps evaluators draw clearer conclusions when sampling, measurement, assumptions, and reporting are handled carefully.", ["The chapter introduces statistical tools in practical terms, including sampling, tests, regression, and visualization.", "It emphasizes choosing techniques according to the evaluation question and data rather than applying methods mechanically.", "Reporting should explain statistical results clearly, including limitations, uncertainty, and practical significance."], ["survey", "comparison group design", "performance measurement"], ["Match statistical tools to the question and data structure.", "Report uncertainty and practical meaning, not only significance.", "Use visualizations to clarify rather than decorate findings."], "ch23-chapter-23-using-statistics-in-evaluation"),
    chapter(24, "Cost-Effectiveness and Cost-Benefit Analysis", "685-716", "analysis", "Economic analysis compares program costs with effects or monetized benefits so decision makers can judge value.", ["The chapter explains when to use cost-effectiveness and benefit-cost techniques.", "It covers identifying costs, measuring benefits or effects, discounting, sensitivity, and interpreting ratios or net value.", "The practical point is to make economic assumptions visible enough for decision makers to use and challenge them."], ["cost-effectiveness analysis", "cost-benefit analysis", "use"], ["Define the decision alternative before calculating ratios.", "Document cost categories and assumptions.", "Use sensitivity analysis for uncertain prices, effects, and discount rates."], "ch24-chapter-24-cost-effectiveness-and-cost-benefit-analysis"),
    chapter(25, "Meta-Analyses, Systematic Reviews, and Evaluation Syntheses", "717-740", "analysis", "Evidence synthesis clarifies where evaluation evidence is strong, absent, ambiguous, or not comparable.", ["The chapter distinguishes meta-analysis, systematic review, and research synthesis.", "It emphasizes transparent search, study selection, quality appraisal, and interpretation of prior studies.", "Synthesis can help evaluators and decision makers avoid overreliance on one study and identify where new evaluation is needed."], ["meta-analysis", "evaluation synthesis", "use"], ["Use explicit inclusion criteria and search procedures.", "Assess study quality before combining evidence.", "Report where evidence is absent or ambiguous."], "ch25-chapter-25-meta-analyses-systematic-reviews-and-evaluation-syntheses"),
    chapter(26, "Pitfalls in Evaluations", "745-766", "use", "Evaluation pitfalls are predictable design, data, analysis, and use problems that can be anticipated and reduced.", ["The chapter catalogues common problems that undermine evaluations, including weak design, intrusive data collection, attrition, and misaligned expectations.", "Its value is diagnostic: evaluators can use the pitfalls as a pre-mortem before committing to a design.", "The chapter links technical risks to practical consequences for credibility and use."], ["data collection plan", "recruitment and retention", "use"], ["Run a pitfalls check during design review.", "Treat attrition and implementation disruption as threats to usefulness.", "Build mitigation plans before fieldwork starts."], "ch26-chapter-26-pitfalls-in-evaluations"),
    chapter(27, "Providing Recommendations, Suggestions, and Options for Improvement", "767-780", "use", "Recommendations are most useful when they flow from findings, address causes or effects, and give decision makers feasible options.", ["The chapter distinguishes recommendations, suggestions, and options depending on authority, context, and audience.", "It emphasizes that evaluators should offer reasoned, practical solutions rather than unsupported preferences.", "Good recommendations are analytically linked to findings, feasible, minimally disruptive, and owned by the evaluator."], ["recommendations", "use", "writing for impact"], ["Make recommendations traceable to findings.", "Offer options when decision makers need room to choose.", "Screen ideas for feasibility, cost, side effects, and authority."], "ch27-chapter-27-providing-recommendations-suggestions-and-options-for-improvement"),
    chapter(28, "Writing for Impact", "781-805", "use", "Evaluation writing should convey a clear message, credible evidence, useful methods detail, and formats suited to intended audiences.", ["The chapter focuses on communication choices that make evaluation reports readable and action-oriented.", "It stresses message discipline, reasonable tone, concise findings, methods transparency, and formats that fit how audiences consume information.", "Writing for impact is not cosmetic: it affects whether evidence is understood, trusted, and acted upon."], ["writing for impact", "recommendations", "use"], ["Define the core message before drafting.", "Use methods detail to build credibility without burying the message.", "Adapt formats to audience needs and decision timing."], "ch28-chapter-28-writing-for-impact"),
    chapter(29, "Evaluation Contracting", "807-830", "use", "Evaluation contracting translates information needs into feasible plans, RFPs, contractor selection, monitoring, and usable products.", ["The chapter addresses how organizations procure evaluation services.", "It covers developing feasible evaluation plans and requests for proposals, selecting qualified contractors, monitoring progress, and ensuring useful reports.", "Contracting is treated as a quality-control process that shapes whether the evaluation can deliver credible and useful evidence."], ["contracting", "data collection plan", "use"], ["Write RFPs that specify questions, products, roles, and feasibility constraints.", "Assess contractor qualifications against the evaluation task.", "Monitor progress and deliverables throughout the contract."], "ch29-chapter-29-evaluation-contracting"),
    chapter(30, "Use of Evaluation in Government", "831-857", "use", "Government evaluation use depends on politics, bureaucracy, evidence agendas, and strategies for overcoming institutional barriers.", ["The chapter discusses evaluation in public-sector settings where political and bureaucratic contexts affect what is asked, funded, reported, and used.", "It provides guidance on building support, navigating resistance, and connecting evaluation evidence to government decisions.", "The chapter treats use as an active strategy rather than a passive consequence of producing a report."], ["use", "stakeholder engagement", "performance measurement"], ["Plan for political and bureaucratic barriers.", "Connect evaluation agendas to real government decisions.", "Build routines that help agencies use evidence for improvement."], "ch30-chapter-30-use-of-evaluation-in-government"),
    chapter(31, "Evaluation Challenges, Issues, and Trends", "858-870", "use", "The concluding chapter identifies cross-cutting challenges in evaluation quality, evaluator capacity, standards, ethics, and evidence use.", ["The chapter returns to the handbook's practical aim: helping organizations improve program design and performance.", "It addresses quality control, evaluator selection and training, standards and ethics, and getting others to use findings.", "It also connects performance monitoring and evaluation studies while noting trends that affect public and nonprofit evaluation practice."], ["use", "performance measurement", "stakeholder engagement"], ["Treat quality control as an evaluation-management responsibility.", "Invest in evaluator capacity and ethical standards.", "Link monitoring systems and evaluation studies so evidence supports improvement."], "ch31-chapter-31-evaluation-challenges-issues-and-trends"),
]


def yaml_list(values: list[str]) -> str:
    return "\n".join(f'  - "{value}"' for value in values)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text())


def write(path: str, text: str) -> None:
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(text.rstrip() + "\n")


def write_json(path: str, data: dict) -> None:
    write(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def source_chunks(evidence_ids: list[str]) -> str:
    return "\n".join(f"- `{eid}`" for eid in evidence_ids)


def chapter_label(ch: dict) -> str:
    return f"Chapter {ch['number']}: {ch['title']}"


def all_evidence_ids() -> list[str]:
    seen: list[str] = []
    for ch in CHAPTERS:
        for eid in ch["evidence_ids"]:
            if eid not in seen:
                seen.append(eid)
    return seen


def concept_lines(concepts: list[str]) -> list[str]:
    return [f"- **{concept}**: {CONCEPT_GLOSSES[concept]}" for concept in concepts]


def render_chapter(ch: dict) -> str:
    evidence = ch["evidence_ids"]
    summary = "\n\n".join(ch["details"])
    return "\n".join([
        "---",
        f'title: "{chapter_label(ch)}"',
        f'description: "Chapter-level study notes for {TITLE}."',
        f'book_id: "{BOOK_ID}"',
        f'collection_id: "{COLLECTION_ID}"',
        'note_type: "Chapter"',
        f"chapter_number: {ch['number']}",
        f'source_pages: "{ch["pages"]}"',
        f'citation_key: "{CITATION}"',
        "evidence_ids:",
        yaml_list(evidence),
        f'source_status: "{SOURCE_STATUS}"',
        "---",
        "",
        f"# {chapter_label(ch)}",
        "",
        f"<div class=\"chapter-meta\"><span>{ch['pages']}</span><span>{part_title(ch['part'])}</span><span>Source status: {SOURCE_STATUS}</span></div>",
        "",
        "## Core Claim",
        "",
        ch["core"],
        "",
        "## Summary",
        "",
        summary,
        "",
        "## Key Concepts",
        "",
        *concept_lines(ch["concepts"]),
        "",
        "## Practice Implications",
        "",
        *(f"- {item}" for item in ch["implications"]),
        "",
        "## Source Records",
        "",
        source_chunks(evidence),
        "",
        "## References",
        "",
        f"These notes summarise source-linked records from *{TITLE}* [@{CITATION}].",
    ])


def render_index() -> str:
    evidence = all_evidence_ids()
    grouped = {
        "Evaluation Planning and Design": [ch for ch in CHAPTERS if ch["part"] == "planning"],
        "Practical Data Collection Procedures": [ch for ch in CHAPTERS if ch["part"] == "data_collection"],
        "Data Analysis": [ch for ch in CHAPTERS if ch["part"] == "analysis"],
        "Use of Evaluation": [ch for ch in CHAPTERS if ch["part"] == "use"],
    }
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
        "::: {.landing-hero}",
        '<span class="hero-eyebrow">Book notes</span>',
        "",
        f"# {TITLE}",
        "",
        f"Chapter-level study notes on *{TITLE}* [@{CITATION}]. These notes are generated from source-linked MCP research-library records and are intended for study, comparison, and later refinement.",
        "",
        '<div class="page-metadata">',
        f"  <span>{len(CHAPTERS)} chapter notes</span>",
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
        "Recurring ideas and distinctions used across these notes.",
        ":::",
        "",
        "::: {.section-card}",
        '<span class="page-badge badge-map">Map</span>',
        "",
        "### [Chapter Map](chapter-map.qmd)",
        "",
        "Source sections, page ranges, and reading routes.",
        ":::",
        "",
        "::: {.section-card}",
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
        f"<div class=\"chapter-meta\"><span>{YEAR}</span><span>MCP evaluation-texts</span><span>Status: {SOURCE_STATUS}</span><span>Book overview</span></div>",
        "",
        f"This index summarises generated chapter notes for {AUTHORS}'s *{TITLE}* [@{CITATION}].",
        "",
        "## Core Argument",
        "",
        "Practical program evaluation should align credible design, workable data collection, useful analysis, and deliberate strategies for evaluation use.",
        "",
        "## Chapter Notes",
        "",
    ]
    for heading, chapters in grouped.items():
        lines.extend([f"### {heading}", ""])
        lines.extend(f"- [{chapter_label(ch)}]({ch['file']}) - source pages {ch['pages']}" for ch in chapters)
        lines.append("")
    lines.extend(["## Legacy Extracts", ""])
    lines.extend(f"- [{title}]({file})" for title, file in LEGACY_EXTRACTS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence[:20]), "", "## References", ""])
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
        f"This map organises the generated chapter notes for *{TITLE}* [@{CITATION}].",
        "",
        "## Reading Route",
        "",
        "- **Plan useful evaluations**: Chapters 1-12 cover stakeholder engagement, logic models, exploratory evaluation, monitoring, causal designs, case studies, multisite work, community change, and cultural responsiveness.",
        "- **Collect practical data**: Chapters 13-21 cover records, surveys, role playing, observation, fieldwork, Internet tools, interviews, focus groups, and stories.",
        "- **Analyze and synthesize**: Chapters 22-25 cover qualitative analysis, statistics, economic analysis, and evidence synthesis.",
        "- **Support use**: Chapters 26-31 cover pitfalls, recommendations, writing, contracting, government use, quality, ethics, and trends.",
        "",
        "## Chapters",
        "",
        "| Chapter | Source Pages | Main Design Question | Link |",
        "|---|---:|---|---|",
    ]
    lines.extend(f"| {chapter_label(ch)} | {ch['pages']} | {ch['core']} | [{ch['file']}]({ch['file']}) |" for ch in CHAPTERS)
    lines.extend(["", "## Legacy Extracts", ""])
    lines.extend(f"- [{title}]({file})" for title, file in LEGACY_EXTRACTS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence[:20]), "", "## References", ""])
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = all_evidence_ids()
    clusters = {
        "Design and Use": ["evaluation question", "stakeholder engagement", "logic model", "evaluability assessment", "performance measurement", "use"],
        "Data Collection": ["administrative data", "survey", "role playing", "trained observer rating", "fieldwork", "semi-structured interview", "focus group", "stories"],
        "Analysis and Value": ["comparison group design", "case study", "cost-effectiveness analysis", "cost-benefit analysis", "meta-analysis", "evaluation synthesis"],
        "Action and Governance": ["recommendations", "writing for impact", "contracting", "culturally responsive evaluation", "recruitment and retention"],
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
        f"This synthesis draws on the generated chapter notes from *{TITLE}* [@{CITATION}].",
        "",
        "## Concept Clusters",
        "",
    ]
    for heading, concepts in clusters.items():
        lines.extend([f"### {heading}", ""])
        lines.extend(concept_lines(concepts))
        lines.append("")
    lines.extend(["## Chapter Links", ""])
    lines.extend(f"- [{chapter_label(ch)}]({ch['file']})" for ch in CHAPTERS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence[:20]), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = all_evidence_ids()
    implications = [
        "Start evaluation design with the decision, intended users, context, and credibility requirements.",
        "Use stakeholder analysis, logic models, and exploratory evaluation to prevent premature method selection.",
        "Choose causal, descriptive, case, monitoring, or synthesis designs according to the question the evaluation must answer.",
        "Build data collection plans that specify information needs, sources, instruments, staffing, and quality checks.",
        "Treat recruitment, retention, access, missing records, observer reliability, response rates, and field burden as validity issues.",
        "Use qualitative, statistical, economic, and synthesis methods in ways that fit the evidence and audience.",
        "Check common pitfalls before launch and before reporting.",
        "Make recommendations and options traceable to findings and realistic for the authority that must act.",
        "Write and format reports around the message, evidence, methods limitations, and intended use.",
        "Manage contracts, government context, standards, ethics, and evidence-use routines as part of evaluation quality.",
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
        f"This practice synthesis draws on the chapter notes from *{TITLE}* [@{CITATION}].",
        "",
        "## Evaluation Practice Implications",
        "",
    ]
    lines.extend(f"- {item}" for item in implications)
    lines.extend(["", "## Links", ""])
    lines.extend(f"- [{chapter_label(ch)}]({ch['file']})" for ch in CHAPTERS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence[:20]), "", "## References", ""])
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
                "section_id": f"chapter-{ch['number']:02d}",
                "section_title": chapter_label(ch),
                "source_pages": ch["pages"],
                "section_path": ch["section_path"],
                "evidence_ids": ch["evidence_ids"],
                "target_path": f"notes/{SLUG}/{ch['file']}",
            }
            for ch in CHAPTERS
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
            "include_media": "true for full-book grounding and exhibit-heavy chapters",
            "limit": "targeted chapter openings plus part-overview records",
        },
        "chapters": [
            {
                "chapter_number": ch["number"],
                "chapter_title": ch["title"],
                "target_path": f"notes/{SLUG}/{ch['file']}",
                "section_paths": [ch["section_path"]],
                "source_pages": ch["pages"],
                "evidence_ids": ch["evidence_ids"],
                "status": "drafted",
            }
            for ch in CHAPTERS
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
                    "id": f"chapter-{ch['number']:02d}",
                    "title": chapter_label(ch),
                    "source_pages": ch["pages"],
                    "section_path": ch["section_path"],
                    "evidence_ids": ch["evidence_ids"],
                    "target_path": f"notes/{SLUG}/{ch['file']}",
                }
                for ch in CHAPTERS
            ]
            break
    else:
        raise SystemExit(f"{BOOK_ID} not found in manifest")
    write_json("data/research_library_notes_manifest.json", manifest)


def update_overview_copy() -> None:
    replacements = [
        (
            ROOT / "index.qmd",
            "Qualitative Research & Evaluation Methods notes, step-level Patton/U-FE notes, and generated notes for the wider collection.",
            "Qualitative Research & Evaluation Methods and Handbook of Practical Program Evaluation notes, step-level Patton/U-FE notes, and generated notes for the wider collection.",
        ),
        (
            ROOT / "notes" / "index.qmd",
            "Qualitative Research & Evaluation Methods notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.",
            "Qualitative Research & Evaluation Methods and Handbook of Practical Program Evaluation notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.",
        ),
    ]
    for path, old, new in replacements:
        text = path.read_text()
        if new in text:
            continue
        if old not in text:
            raise SystemExit(f"Could not find overview text in {path}")
        path.write_text(text.replace(old, new))


def main() -> None:
    for ch in CHAPTERS:
        write(f"notes/{SLUG}/{ch['file']}", render_chapter(ch))
    write(f"notes/{SLUG}/index.qmd", render_index())
    write(f"notes/{SLUG}/chapter-map.qmd", render_chapter_map())
    write(f"notes/{SLUG}/concepts.qmd", render_concepts())
    write(f"notes/{SLUG}/practice-implications.qmd", render_practice())
    write_json(f"data/research-library/evidence/{SLUG}/evidence-summary.json", render_evidence_summary())
    write_json(f"data/research-library/evidence/{SLUG}/chapter-evidence-summary.json", render_chapter_evidence_summary())
    update_manifest()
    update_overview_copy()


if __name__ == "__main__":
    main()
