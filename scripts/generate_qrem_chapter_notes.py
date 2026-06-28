#!/usr/bin/env python3
"""Generate chapter-level Qualitative Research & Evaluation Methods study notes."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "qualitative-research-evaluation-methods"
SLUG = BOOK_ID
TITLE = "Qualitative Research & Evaluation Methods"
FULL_TITLE = TITLE
AUTHORS = "Michael Quinn Patton"
CITATION = "patton_2015_qualitative_research_evaluation_methods"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2015"
GENERATED_AT = "2026-06-28"


LEGACY_EXTRACTS = [
    ("Strategic Qualitative Principles in Practice", "section-01-strategic-qualitative-principles.qmd"),
    ("Practical and Actionable Qualitative Inquiry", "section-02-practical-actionable-qualitative-inquiry.qmd"),
    ("Program Models, Theories of Change, and Qualitative Methods", "section-03-program-models-and-theories-of-change.qmd"),
]


CONCEPT_GLOSSES = {
    "qualitative inquiry": "Systematic inquiry using observations, interviews, documents, cases, and interpretation to understand meaning, context, and process.",
    "qualitative data": "Detailed descriptions, direct quotations, observations, documents, and other nonnumeric evidence preserved with context.",
    "mixed methods": "Intentional integration of qualitative and quantitative approaches to answer questions neither approach can fully answer alone.",
    "methods decision": "A design choice made in relation to purpose, question, context, resources, use, and credibility requirements.",
    "naturalistic inquiry": "Studying phenomena in real-world settings without attempting to control them as laboratory conditions.",
    "emergent design": "A design that remains open, responsive, and flexible as new field understandings arise.",
    "purposeful sampling": "Selecting information-rich cases because they illuminate the inquiry purpose.",
    "information-rich case": "A case from which one can learn deeply about issues central to the inquiry.",
    "thick description": "Rich, contextualized description that supports interpretation, transferability, and reader understanding.",
    "empathetic neutrality": "A stance that combines openness and care with disciplined attention to evidence.",
    "systems perspective": "Attention to dynamic relationships, interdependence, feedback, and changing contexts.",
    "unique case orientation": "A qualitative commitment to understanding each case as particular before cross-case abstraction.",
    "inductive analysis": "Building patterns, themes, categories, and explanations from data rather than imposing only pre-set variables.",
    "inquiry framework": "A paradigmatic, philosophical, or theoretical orientation that shapes questions, evidence, interpretation, and quality criteria.",
    "pragmatism": "A practical inquiry orientation that judges methods by their usefulness for the question and action context.",
    "utilization-focused evaluation": "Evaluation designed for intended use by intended users.",
    "program theory": "An account of how an intervention is expected to work, including processes, implementation, and outcomes.",
    "actionable answer": "A finding framed so decision makers can use it to inform action, judgment, improvement, or learning.",
    "design alignment": "Fit among purpose, question, sampling, data collection, analysis, resources, credibility, and intended use.",
    "case study": "An in-depth inquiry into a bounded case, setting, person, group, program, event, or process.",
    "sample size": "The number of cases or observations, judged in qualitative inquiry by information richness, purpose, variation, and feasibility.",
    "fieldwork": "Entering real-world settings to observe, listen, document, interact, and learn systematically.",
    "observation": "Watching, listening, and documenting what occurs in context, including activities, interactions, routines, and settings.",
    "field notes": "Systematic written records of field observations, including description, context, quotations, and analytic reflections.",
    "triangulation": "Using multiple data sources, methods, analysts, or theories to test and deepen findings.",
    "interviewing": "Qualitative data collection through open-ended questioning and disciplined listening.",
    "interview protocol": "A guide or format for asking questions while preserving qualitative openness and responsiveness.",
    "question format": "The structure and wording of questions used to elicit experience, meaning, interpretation, examples, or stories.",
    "analysis": "The systematic process of organizing, reducing, comparing, interpreting, and representing qualitative data.",
    "pattern analysis": "Identifying recurring themes, relationships, categories, and variations across qualitative data.",
    "case analysis": "Making sense of a case holistically before or alongside cross-case comparison.",
    "content analysis": "Systematic identification and interpretation of meanings, patterns, categories, or themes in texts or records.",
    "credibility": "The trustworthiness and believability of qualitative findings, shaped by data quality, analysis, inquirer credibility, and user judgment.",
    "transferability": "Reasoned judgment about whether findings, principles, or lessons may apply in other contexts.",
    "quality criteria": "Standards used to judge qualitative inquiry, varying across scientific, constructivist, participatory, critical, systems, pragmatic, and use-oriented traditions.",
    "inquirer credibility": "The trust placed in the analyst based on training, experience, reflexivity, transparency, and presentation of self.",
}


def chapter(number: int, title: str, pages: str, file: str, section_path: str, evidence_ids: list[str], core: str, summary: list[str], concepts: list[str], structure: list[str], implications: list[str], group: str) -> dict:
    return {
        "number": number,
        "title": title,
        "pages": pages,
        "file": file,
        "section_path": section_path,
        "evidence_ids": evidence_ids,
        "media_ids": [],
        "core": core,
        "summary": summary,
        "concepts": concepts,
        "structure": structure,
        "implications": implications,
        "group": group,
    }


CHAPTERS = [
    chapter(
        1,
        "The Nature, Niche, Value, and Fruit of Qualitative Inquiry",
        "37-87",
        "chapter-01-nature-niche-value-fruit-of-qualitative-inquiry.qmd",
        "Part 1: Framing Qualitative Inquiry: Theory Informs Practice, Practice Informs Theory > Chapter 1: The Nature, Niche, Value, and Fruit of Qualitative Inquiry",
        [
            "chunk:qualitative-research-evaluation-methods:ch01-chapter-1-the-nature-niche-value-and-fruit-of-qualitative-inquiry:c0001",
            "chunk:qualitative-research-evaluation-methods:mod04-module-4-the-fruit-of-qualitative-methods-chapter-summary-and-conclusion:c0004",
        ],
        "Qualitative inquiry is valuable when decision makers, researchers, or evaluators need contextual, descriptive, interpretive, and use-oriented understanding that numbers alone cannot provide.",
        [
            "Chapter 1 introduces the whole book as a journey into qualitative inquiry for research and evaluation. It distinguishes qualitative evidence from quantitative evidence while emphasizing that methods decisions should serve inquiry purposes.",
            "The chapter presents qualitative data as observations, interviews, and documents preserved with context. The value of these data lies in their capacity to show process, meaning, experience, variation, and the particularity of cases.",
            "Patton links qualitative and quantitative approaches through mixed methods. The question is not which paradigm should dominate, but which evidence is needed to answer the question well.",
            "The chapter's closing summary frames the fruit of qualitative methods as insight, understanding, and practical wisdom generated by systematic attention to real-world experience.",
        ],
        ["qualitative inquiry", "qualitative data", "mixed methods", "methods decision", "case study"],
        ["book overview", "qualitative data", "methods choices", "mixed methods", "fruit of qualitative inquiry"],
        ["Start with the inquiry purpose before defending any method.", "Use qualitative data when context, meaning, process, and variation matter.", "Treat mixed methods as a design option rather than a compromise."],
        "framing",
    ),
    chapter(
        2,
        "Strategic Themes in Qualitative Inquiry",
        "89-147",
        "chapter-02-strategic-themes-in-qualitative-inquiry.qmd",
        "Part 1: Framing Qualitative Inquiry: Theory Informs Practice, Practice Informs Theory > Chapter 2: Strategic Themes in Qualitative Inquiry",
        [
            "chunk:qualitative-research-evaluation-methods:mod08-module-8-integrating-the-12-strategic-qualitative-principles-in-practice-chapter:c0001",
            "chunk:qualitative-research-evaluation-methods:mod08-module-8-integrating-the-12-strategic-qualitative-principles-in-practice-chapter:c0010",
            "chunk:qualitative-research-evaluation-methods:mod08-module-8-integrating-the-12-strategic-qualitative-principles-in-practice-chapter:c0017",
        ],
        "The chapter's 12 strategic principles define qualitative inquiry as naturalistic, emergent, purposeful, richly descriptive, personally engaged, systems-sensitive, inductive, holistic, context-aware, and reflexive.",
        [
            "Chapter 2 gives the book its strategic grammar. Patton treats qualitative inquiry as a set of guiding principles rather than a single technique.",
            "The principles include naturalistic inquiry, emergent design flexibility, purposeful sampling, rich data, personal engagement, empathetic neutrality, systems sensitivity, unique case orientation, inductive analysis, holistic perspective, context sensitivity, and voice or reflexivity.",
            "These principles are strategic ideals. Real inquiries adapt them to purpose, setting, resources, politics, ethics, and use.",
            "The chapter prepares the rest of the book by showing that observation, interviewing, sampling, analysis, and credibility are connected practices, not isolated procedures.",
        ],
        ["naturalistic inquiry", "emergent design", "purposeful sampling", "thick description", "empathetic neutrality", "systems perspective", "inductive analysis"],
        ["12 strategic principles", "design principles", "data collection principles", "analysis principles", "integration in practice"],
        ["Use the 12 principles as design checks.", "Name which principles are central for a given study.", "Adapt strategic ideals to real-world constraints without losing qualitative integrity."],
        "framing",
    ),
    chapter(
        3,
        "Variety of Qualitative Inquiry Frameworks",
        "148-264",
        "chapter-03-variety-of-qualitative-inquiry-frameworks.qmd",
        "Part 1: Framing Qualitative Inquiry: Theory Informs Practice, Practice Informs Theory > Chapter 3: Variety of Qualitative Inquiry Frameworks: Paradigmatic, Philosophical, and Theoretical Orientations",
        [
            "chunk:qualitative-research-evaluation-methods:ch03-chapter-3-variety-of-qualitative-inquiry-frameworks-paradigmatic-philosophical-a:c0001",
            "chunk:qualitative-research-evaluation-methods:ch03-chapter-3-variety-of-qualitative-inquiry-frameworks-paradigmatic-philosophical-a:c0002",
            "chunk:qualitative-research-evaluation-methods:mod19-module-19-patterns-and-themes-across-inquiry-frameworks-chapter-summary-and-conc:c0029",
            "chunk:qualitative-research-evaluation-methods:mod19-module-19-patterns-and-themes-across-inquiry-frameworks-chapter-summary-and-conc:c0030",
        ],
        "Qualitative inquiry is a family of frameworks, and evaluators must understand how philosophical and theoretical orientations shape questions, evidence, interpretation, and credibility.",
        [
            "Chapter 3 reviews 16 qualitative inquiry frameworks, from ethnography and grounded theory to realism, phenomenology, constructivism, systems theory, complexity theory, pragmatism, and generic qualitative inquiry.",
            "The chapter situates these frameworks in the history of qualitative/quantitative debates while refusing to reduce qualitative inquiry to a single paradigm.",
            "Patton emphasizes that frameworks should be understood through their foundational questions. Different orientations ask different kinds of questions and imply different standards for evidence and interpretation.",
            "The chapter closes with crosscutting themes: definitions vary, fidelity disputes occur, frameworks combine and evolve, and the choice of framework should be explicit enough to guide methods decisions.",
        ],
        ["inquiry framework", "pragmatism", "mixed methods", "quality criteria", "methods decision"],
        ["paradigms debate", "16 inquiry frameworks", "foundational questions", "crosscutting themes", "framework fidelity"],
        ["Make the inquiry framework explicit before judging evidence quality.", "Avoid treating qualitative inquiry as one undifferentiated paradigm.", "Use frameworks to sharpen questions and interpretation, not to impose jargon."],
        "framing",
    ),
    chapter(
        4,
        "Practical and Actionable Qualitative Applications",
        "266-371",
        "chapter-04-practical-and-actionable-qualitative-applications.qmd",
        "Part 1: Framing Qualitative Inquiry: Theory Informs Practice, Practice Informs Theory > Chapter 4: Practical and Actionable Qualitative Applications",
        [
            "chunk:qualitative-research-evaluation-methods:ch04-chapter-4-practical-and-actionable-qualitative-applications:c0005",
            "chunk:qualitative-research-evaluation-methods:mod20-module-20-practical-purposes-concrete-questions-and-actionable-answers-illuminat:c0005",
            "chunk:qualitative-research-evaluation-methods:mod23-module-23-evaluating-program-models-and-theories-of-change-and-evaluation-models:c0024",
            "chunk:qualitative-research-evaluation-methods:mod27-module-27-a-vision-of-the-utility-of-qualitative-methods-chapter-summary-and-con:c0004",
            "chunk:qualitative-research-evaluation-methods:mod27-module-27-a-vision-of-the-utility-of-qualitative-methods-chapter-summary-and-con:c0005",
        ],
        "Qualitative methods are especially useful for practical questions that require actionable answers about quality, outcomes, interventions, participation, process, theory, and use.",
        [
            "Chapter 4 turns from theory to application. It asks where qualitative inquiry is particularly powerful for practice, policy, program evaluation, organizational learning, and action.",
            "The chapter emphasizes concrete questions and actionable answers. Qualitative evidence can illuminate quality, uncover unanticipated outcomes, explain implementation, document development, and compare diverse cases.",
            "Program evaluation applications are central. Patton connects qualitative inquiry to outcomes, individualized outcomes, process evaluation, implementation evaluation, principles-focused evaluation, program models, theories of change, and utilization-focused evaluation.",
            "The chapter's application checklist stresses simple but demanding habits: pay attention, listen and watch, remain open, document systematically, analyze inductively, and apply what is learned.",
        ],
        ["actionable answer", "utilization-focused evaluation", "program theory", "case study", "qualitative inquiry"],
        ["practical purposes", "quality", "program evaluation applications", "interventions", "participatory applications", "qualitative methods utility"],
        ["Use qualitative methods when decisions require explanation, context, or practical learning.", "Connect qualitative evidence to theories of change and implementation.", "Report findings in forms that support action."],
        "applications",
    ),
    chapter(
        5,
        "Designing Qualitative Studies",
        "373-491",
        "chapter-05-designing-qualitative-studies.qmd",
        "Part 2: Qualitative Designs and Data Collection > Chapter 5: Designing Qualitative Studies",
        [
            "chunk:qualitative-research-evaluation-methods:ch05-chapter-5-designing-qualitative-studies:c0003",
            "chunk:qualitative-research-evaluation-methods:ch05-chapter-5-designing-qualitative-studies:c0004",
            "chunk:qualitative-research-evaluation-methods:mod30-module-30-purposeful-sampling-and-case-selection-overview-of-strategies-and-opti:c0002",
            "chunk:qualitative-research-evaluation-methods:mod30-module-30-purposeful-sampling-and-case-selection-overview-of-strategies-and-opti:c0003",
            "chunk:qualitative-research-evaluation-methods:mod40-module-40-sample-size-for-qualitative-designs:c0009",
            "chunk:qualitative-research-evaluation-methods:mod42-module-42-qualitative-design-chapter-summary-and-conclusion-methods-choices-and-:c0001",
        ],
        "Qualitative design aligns purpose, questions, cases, sampling, data collection, analysis, credibility, resources, and intended use, with purposeful sampling as a central design logic.",
        [
            "Chapter 5 is the pivot chapter on design. It connects the philosophical and practical foundations from Part 1 to the fieldwork, interviewing, analysis, and credibility work that follows.",
            "Patton treats design as a plan anchored in inquiry purpose. Design answers questions, so the quality of a qualitative study depends on the fit among purpose, question, case, sampling, data, analysis, context, and use.",
            "Purposeful sampling is central because what is sampled determines what the study can illuminate. Information-rich cases are selected for depth, insight, variation, comparison, theory development, or intended use.",
            "The chapter also stresses trade-offs: breadth versus depth, single cases versus multiple cases, emergent flexibility versus advance specification, and small focused samples versus larger qualitative datasets.",
        ],
        ["design alignment", "purposeful sampling", "information-rich case", "case study", "sample size", "mixed methods"],
        ["design thinking", "inquiry questions", "data collection options", "purposeful sampling", "sample size", "methods choices"],
        ["Treat design as fit among purpose, question, sampling, analysis, and use.", "Select cases because they are information-rich for the inquiry purpose.", "Explain depth/breadth trade-offs transparently."],
        "design",
    ),
    chapter(
        6,
        "Fieldwork Strategies and Observation Methods",
        "493-615",
        "chapter-06-fieldwork-strategies-and-observation-methods.qmd",
        "Part 2: Qualitative Designs and Data Collection > Chapter 6: Fieldwork Strategies and Observation Methods",
        [
            "chunk:qualitative-research-evaluation-methods:ch06-chapter-6-fieldwork-strategies-and-observation-methods:c0003",
            "chunk:qualitative-research-evaluation-methods:mod56-module-56-chapter-summary-and-conclusion-guidelines-for-fieldwork:c0006",
        ],
        "Fieldwork turns design into disciplined real-world observation, requiring systematic attention to context, detail, openness, triangulation, and high-quality field notes.",
        [
            "Chapter 6 moves the reader into the field. Fieldwork is the work of qualitative inquiry: observing, listening, documenting, interacting, and learning in real-world settings.",
            "Observation and interviewing are linked. Observation creates interview opportunities, and every interview is also an occasion for observation.",
            "Patton emphasizes disciplined field notes. High-quality fieldwork separates description from interpretation, captures rich detail and direct quotations, and remains open to unexpected leads.",
            "The chapter's fieldwork guidelines stress duration, focus, triangulation, opportunistic learning, multiple data sources, and systematic documentation.",
        ],
        ["fieldwork", "observation", "field notes", "thick description", "triangulation", "emergent design"],
        ["entering the field", "observation stance", "field notes", "openness", "triangulation", "guidelines"],
        ["Write field notes as soon and as fully as possible.", "Separate observed description from interpretation.", "Use observations, documents, interviews, artifacts, and photographs to triangulate."],
        "data",
    ),
    chapter(
        7,
        "Qualitative Interviewing",
        "617-741",
        "chapter-07-qualitative-interviewing.qmd",
        "Part 2: Qualitative Designs and Data Collection > Chapter 7: Qualitative Interviewing",
        [
            "chunk:qualitative-research-evaluation-methods:mod58-module-58-distinguishing-interview-approaches-and-types-of-interviews:c0002",
            "chunk:qualitative-research-evaluation-methods:mod64-module-64-personal-reflections-on-interviewing-and-chapter-summary-and-conclusio:c0009",
        ],
        "Qualitative interviewing is disciplined asking and listening, shaped by inquiry purpose, interview approach, question format, relationship, ethics, and the responsibility to elicit meaningful accounts.",
        [
            "Chapter 7 focuses on in-depth interviewing. Patton treats questions as instruments of inquiry that must be designed, tested, asked, listened to, and interpreted responsibly.",
            "The chapter distinguishes interview approaches and question formats. Informal conversational interviews, interview guides, standardized open-ended interviews, and different theoretical interviewing traditions serve different purposes.",
            "Interviewing is not just asking. It involves listening, probing, sequencing, rapport, neutrality, sensitivity, ethics, and awareness that the questions themselves shape what can be learned.",
            "The chapter closes by emphasizing responsibility: asking involves power and consequence; listening is a privilege; evaluators will be evaluated by their questions.",
        ],
        ["interviewing", "interview protocol", "question format", "empathetic neutrality", "qualitative data"],
        ["interview approaches", "question formats", "open-ended questions", "probing and listening", "reflections on interviewing"],
        ["Choose an interview approach that fits the inquiry purpose.", "Pilot question wording and sequence.", "Treat listening as a core analytic responsibility."],
        "data",
    ),
    chapter(
        8,
        "Qualitative Analysis and Interpretation",
        "759-939",
        "chapter-08-qualitative-analysis-and-interpretation.qmd",
        "Part 3: Analysis, Interpretation, and Reporting > Chapter 8: Qualitative Analysis and Interpretation",
        [
            "chunk:qualitative-research-evaluation-methods:ch08-chapter-8-qualitative-analysis-and-interpretation:c0002",
            "chunk:qualitative-research-evaluation-methods:mod66-module-66-thick-description-and-case-studies-the-bedrock-of-qualitative-analysis:c0021",
            "chunk:qualitative-research-evaluation-methods:mod75-module-75-chapter-summary-and-conclusion-plus-case-study-exhibits:c0038",
        ],
        "Qualitative analysis transforms fieldwork records into credible description, cases, patterns, themes, interpretations, and reports through systematic engagement with the data.",
        [
            "Chapter 8 begins Part 3 by establishing the foundations of qualitative analysis. Analysis is not a final clerical step; it begins with how data are documented, organized, and preserved.",
            "Thick description and case studies are treated as the bedrock of qualitative analysis. Cases must be understood holistically before cross-case patterns are responsibly abstracted.",
            "The chapter then moves through patterns, themes, content analysis, interpretation, and reporting. The analyst's task is to make data meaningful without stripping away context or overclaiming.",
            "The final case-study exhibits show the practical infrastructure of analysis: coding, categories, stakeholder interactions, expectations for use, evaluator roles, and decision-maker roles.",
        ],
        ["analysis", "thick description", "case analysis", "pattern analysis", "content analysis", "qualitative data"],
        ["analysis basics", "thick description", "case studies", "patterns and themes", "interpretation", "reporting"],
        ["Organize data so the analysis trail can be followed.", "Build case understanding before cross-case claims.", "Keep interpretation connected to evidence and context."],
        "analysis",
    ),
    chapter(
        9,
        "Enhancing the Quality and Credibility of Qualitative Studies",
        "942-1056",
        "chapter-09-enhancing-quality-and-credibility-of-qualitative-studies.qmd",
        "Part 3: Analysis, Interpretation, and Reporting > Chapter 9: Enhancing the Quality and Credibility of Qualitative Studies",
        [
            "chunk:qualitative-research-evaluation-methods:ch09-chapter-9-enhancing-the-quality-and-credibility-of-qualitative-studies:c0003",
            "chunk:qualitative-research-evaluation-methods:mod76-module-76-analytical-processes-for-enhancing-credibility-systematically-engaging:c0001",
            "chunk:qualitative-research-evaluation-methods:mod76-module-76-analytical-processes-for-enhancing-credibility-systematically-engaging:c0028",
            "chunk:qualitative-research-evaluation-methods:mod77-module-77-four-triangulation-processes-for-enhancing-credibility:c0020",
            "chunk:qualitative-research-evaluation-methods:mod78-module-78-alternative-and-competing-criteria-for-judging-the-quality-of-qualitat:c0011",
            "chunk:qualitative-research-evaluation-methods:mod82-module-82-enhancing-the-credibility-and-utility-of-qualitative-inquiry-by-addres:c0045",
        ],
        "Credibility depends on high-quality fieldwork, systematic analysis, inquirer credibility, appropriate quality criteria, triangulation, transferability, and philosophical clarity about qualitative evidence.",
        [
            "Chapter 9 closes the book by asking how qualitative inquiry can be judged as credible and useful. Patton identifies credibility as a product of data quality, analytic rigor, inquirer credibility, and users' appreciation of qualitative inquiry.",
            "The chapter presents analytic practices for systematically engaging and questioning the data. It also emphasizes triangulation across data sources, methods, analysts, theories, and mixed-methods evidence.",
            "Quality criteria are plural. Traditional scientific, constructivist, participatory, critical, systems, pragmatic, and utilization-focused criteria each illuminate different ways of judging qualitative work.",
            "The final modules address generalization, transferability, principles, lessons learned, and philosophy-of-science issues, ending with a pragmatic emphasis on use and technical adequacy in context.",
        ],
        ["credibility", "triangulation", "quality criteria", "transferability", "inquirer credibility", "pragmatism"],
        ["credibility elements", "questioning the data", "triangulation", "quality criteria", "transferability", "philosophy of science"],
        ["Report the credibility logic used for the study.", "Use triangulation to deepen and challenge findings.", "Match quality criteria to the inquiry framework and intended use."],
        "analysis",
    ),
]


def wrap(text: str) -> str:
    return "\n".join(textwrap.wrap(text, width=100, break_long_words=False, replace_whitespace=False))


def yaml_list(values: list[str]) -> str:
    return "\n".join(f'  - "{value}"' for value in values)


def all_evidence_ids() -> list[str]:
    seen: set[str] = set()
    values: list[str] = []
    for chapter_item in CHAPTERS:
        for evidence_id in chapter_item["evidence_ids"]:
            if evidence_id not in seen:
                values.append(evidence_id)
                seen.add(evidence_id)
    return values


def write_text(relative: str, text: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(relative: str, payload: dict) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def chapter_label(chapter_item: dict) -> str:
    return f"Chapter {chapter_item['number']}: {chapter_item['title']}"


def chapter_link(chapter_item: dict) -> str:
    return f"[{chapter_label(chapter_item)}]({chapter_item['file']})"


def concept_lines(concepts: list[str]) -> list[str]:
    return [
        f"- **{concept}**: {CONCEPT_GLOSSES.get(concept, 'Check the cited records before relying on this concept in applied work.')}"
        for concept in concepts
    ]


def source_chunks(evidence_ids: list[str]) -> str:
    return "\n".join(f"- `{evidence_id}`" for evidence_id in evidence_ids)


def render_mermaid(chapter_item: dict) -> str:
    concepts = chapter_item["concepts"][:3]
    structures = chapter_item["structure"][:3]
    implications = chapter_item["implications"][:2]
    lines = [
        "flowchart TD",
        f'  Problem["Problem: What does Chapter {chapter_item["number"]} help decide?"]',
        f'  Central["Concept: {chapter_item["title"]}"]',
    ]
    for idx, concept in enumerate(concepts, start=1):
        lines.append(f'  Concept{idx}["Concept: {concept}"]')
    for idx, item in enumerate(structures, start=1):
        lines.append(f'  Element{idx}["Inquiry element: {item}"]')
    for idx, implication in enumerate(implications, start=1):
        lines.append(f'  Implication{idx}["Practice implication: {implication.replace(chr(34), chr(39))}"]')
    lines.extend(["  Question[\"Open question: What evidence would strengthen the claim?\"]", "", "  Problem --> Central", "  Central --> Question"])
    for idx in range(1, len(concepts) + 1):
        lines.append(f"  Central --> Concept{idx}")
    for idx in range(1, len(structures) + 1):
        lines.append(f"  Concept{min(idx, len(concepts))} --> Element{idx}")
    for idx in range(1, len(implications) + 1):
        lines.append(f"  Element{min(idx, len(structures))} --> Implication{idx}")
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
            f"  class {','.join(f'Concept{i}' for i in range(1, len(concepts) + 1))} concept;",
            f"  class {','.join(f'Element{i}' for i in range(1, len(structures) + 1))} mechanism;",
            f"  class {','.join(f'Implication{i}' for i in range(1, len(implications) + 1))},Question implication;",
        ]
    )
    return "\n".join(lines)


def render_chapter(chapter_item: dict, prev_chapter: dict | None, next_chapter: dict | None) -> str:
    label = chapter_label(chapter_item)
    lines = [
        "---",
        f'title: "{label}"',
        f'description: "Detailed study notes for {label} of {TITLE}."',
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
        f'<div class="chapter-meta"><span>{YEAR}</span><span>MCP evaluation-texts</span><span>Status: {SOURCE_STATUS}</span><span>{label}</span><span>Source pages {chapter_item["pages"]}</span></div>',
        "",
        wrap(f'This note summarises {label} from {AUTHORS}\'s *{FULL_TITLE}* [@{CITATION}]. It is a paraphrased study note based on source-linked MCP research-library retrieval records, not a substitute for the chapter.'),
        "",
        "The retrieval trail is retained in the source records at the bottom of the page. The note paraphrases the chapter's argument and procedures, and it does not reproduce textbook exhibits, checklists, cartoons, figures, tables, exercises, or extended passages.",
        "",
        "## Core Argument",
        "",
        chapter_item["core"],
        "",
        "## Study Summary",
        "",
    ]
    for paragraph in chapter_item["summary"]:
        lines.extend([wrap(paragraph), ""])
    lines.extend(
        [
            wrap(f"For close reading, track how the chapter uses {', '.join(chapter_item['concepts'][:4])} while moving through {', '.join(chapter_item['structure'][:3])}. The note identifies the design or practice decision the chapter helps strengthen."),
            "",
            f"Within the wider book, this chapter belongs to the {chapter_item['group']} sequence.",
            "",
            "## Key Concepts",
            "",
        ]
    )
    lines.extend(concept_lines(chapter_item["concepts"]))
    lines.extend(["", "## Chapter Structure", ""])
    lines.extend(f"- {item[:1].upper() + item[1:]}." for item in chapter_item["structure"])
    lines.extend(["", "## Practical Implications", ""])
    lines.extend(f"- {item}" for item in chapter_item["implications"])
    lines.extend(["", "## Concept Map", "", "::: {.concept-map}", "```{mermaid}", render_mermaid(chapter_item), "```", ":::", "", "## Connections", ""])
    lines.extend(
        [
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
    lines.extend(["", "## Study Prompts", ""])
    lines.extend(
        [
            f"- What design or evaluation-use decision does {label} help clarify?",
            "- Which concept in this chapter would be most important to explain to a commissioner or stakeholder?",
            "- Which source record should be reopened before using this note in applied work?",
        ]
    )
    lines.extend(["", "## Source Records", "", source_chunks(chapter_item["evidence_ids"]), "", "## References", ""])
    return "\n".join(lines)


def render_index() -> str:
    evidence = all_evidence_ids()
    group_names = {
        "framing": "Part 1: Framing Qualitative Inquiry",
        "applications": "Practical Applications",
        "design": "Part 2: Designs and Data Collection",
        "data": "Data Collection",
        "analysis": "Part 3: Analysis, Interpretation, and Reporting",
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
        "Qualitative inquiry supports research and evaluation by aligning inquiry purpose, theoretical framework, design, purposeful sampling, fieldwork, interviewing, analysis, credibility, and intended use.",
        "",
        "## Chapter Notes",
        "",
    ]
    for group, group_title in group_names.items():
        chapters = [chapter_item for chapter_item in CHAPTERS if chapter_item["group"] == group]
        if chapters:
            lines.extend(["", f"### {group_title}", ""])
            lines.extend(f"- {chapter_link(chapter_item)} - source pages {chapter_item['pages']}" for chapter_item in chapters)
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
        "- **Frame qualitative inquiry**: Chapters 1-4 cover qualitative evidence, strategic principles, frameworks, and applications.",
        "- **Design and collect data**: Chapters 5-7 cover design, purposeful sampling, fieldwork, observation, and interviewing.",
        "- **Analyze and defend quality**: Chapters 8-9 cover analysis, interpretation, credibility, transferability, and quality criteria.",
        "",
        "## Chapters",
        "",
        "| Chapter | Source Pages | Main Design Question | Link |",
        "|---|---:|---|---|",
    ]
    for chapter_item in CHAPTERS:
        lines.append(f"| {chapter_label(chapter_item)} | {chapter_item['pages']} | {chapter_item['core']} | [{chapter_item['file']}]({chapter_item['file']}) |")
    lines.extend(["", "## Legacy Extracts", ""])
    lines.extend(f"- [{title}]({file})" for title, file in LEGACY_EXTRACTS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = all_evidence_ids()
    clusters = {
        "Framing and Purpose": ["qualitative inquiry", "qualitative data", "mixed methods", "methods decision", "inquiry framework", "pragmatism"],
        "Design and Data Collection": ["design alignment", "purposeful sampling", "information-rich case", "case study", "fieldwork", "observation", "field notes", "interviewing"],
        "Analysis and Credibility": ["analysis", "thick description", "case analysis", "pattern analysis", "triangulation", "credibility", "quality criteria", "transferability"],
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
        lines.extend(concept_lines(concepts))
        lines.append("")
    lines.extend(["## Chapter Links", ""])
    lines.extend(f"- {chapter_link(chapter_item)}" for chapter_item in CHAPTERS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = all_evidence_ids()
    implications = [
        "Begin methods decisions with purpose, use, question, context, and credibility requirements.",
        "Use the 12 strategic qualitative principles as a design and reporting checklist.",
        "Make the inquiry framework explicit enough that readers can understand how questions, evidence, interpretation, and quality criteria fit together.",
        "Choose qualitative methods when practical decisions need explanation, context, meaning, process, variation, or unanticipated outcomes.",
        "Select purposeful samples because they are information-rich for the inquiry purpose, and report the sampling logic plainly.",
        "Write field notes that preserve description, context, direct quotation, and analytic reflection.",
        "Design interview questions as inquiry instruments and treat listening as a core analytic skill.",
        "Build analysis from thick description and case understanding toward patterns, themes, interpretation, and reporting.",
        "Use triangulation, transparency, inquirer credibility, and appropriate quality criteria to strengthen qualitative findings.",
        "Frame findings as actionable answers, transferable lessons, or practice principles only when the evidence and context support that use.",
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
                "section_id": f"chapter-{chapter_item['number']:02d}",
                "section_title": chapter_label(chapter_item),
                "source_pages": chapter_item["pages"],
                "section_path": chapter_item["section_path"],
                "evidence_ids": chapter_item["evidence_ids"],
                "media_ids": chapter_item["media_ids"],
                "target_path": f"notes/{SLUG}/{chapter_item['file']}",
            }
            for chapter_item in CHAPTERS
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
            "limit": "targeted chapter and module retrieval; broad evidence pack used before synthesis",
            "include_media": "true for full-book grounding and exhibit-heavy chapters",
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
                    "title": chapter_label(chapter_item),
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


def patch_overview_copy() -> None:
    replacements = {
        "chapter-level Rossi/Lipsey, Chen, Impact Evaluation in Practice, and Realistic Evaluation notes, step-level Patton/U-FE notes, and generated notes for the wider collection.": "chapter-level Rossi/Lipsey, Chen, Impact Evaluation in Practice, Realistic Evaluation, and Qualitative Research & Evaluation Methods notes, step-level Patton/U-FE notes, and generated notes for the wider collection.",
        "chapter-level Rossi/Lipsey, Chen, Impact Evaluation in Practice, and Realistic Evaluation notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.": "chapter-level Rossi/Lipsey, Chen, Impact Evaluation in Practice, Realistic Evaluation, and Qualitative Research & Evaluation Methods notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.",
    }
    for relative in ("index.qmd", "notes/index.qmd"):
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


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
    patch_overview_copy()


if __name__ == "__main__":
    generate()
