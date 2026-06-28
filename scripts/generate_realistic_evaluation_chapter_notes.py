#!/usr/bin/env python3
"""Generate chapter-level Realistic Evaluation study notes."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "realistic-evaluation"
SLUG = BOOK_ID
TITLE = "Realistic Evaluation"
FULL_TITLE = TITLE
AUTHORS = "Ray Pawson and Nick Tilley"
CITATION = "pawson_tilley_1997_realistic_evaluation"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "1997"
GENERATED_AT = "2026-06-28"


LEGACY_EXTRACTS = [
    ("Reader's Guide to Context, Mechanism, and Outcome", "section-01-reader-guide-cmo.qmd"),
    ("Scientific Realism and CMO Hypotheses", "section-02-scientific-realism-and-cmo.qmd"),
    ("The New Rules and CMO Configurations", "section-03-new-rules-cmo-configurations.qmd"),
]


CONCEPT_GLOSSES = {
    "CMO configuration": "A context-mechanism-outcome proposition about what works, for whom, in what circumstances, and why.",
    "context": "The social, cultural, institutional, relational, and material conditions that shape whether a mechanism can operate.",
    "mechanism": "The reasoning, resource, opportunity, constraint, or causal process triggered by a program in a given context.",
    "outcome pattern": "The observed pattern of effects or responses that a realist evaluation explains by reference to mechanisms and contexts.",
    "generative causation": "A view of causation that asks how underlying powers or processes produce outcomes when activated in suitable conditions.",
    "successionist causation": "A causation model focused on observed regularities between events, which Pawson and Tilley critique as too thin for social programs.",
    "scientific realism": "A philosophy of science that explains observable events through underlying mechanisms operating in open systems.",
    "realistic evaluation": "Pawson and Tilley's approach to evaluation that tests and refines theories of how programs work in particular contexts.",
    "theory testing": "Using empirical evidence to assess and refine a conjectured explanation rather than only measuring whether a program worked.",
    "realist design": "An evaluation design that begins with conjectured CMO configurations and selects comparisons and data to test them.",
    "specification": "The realist alternative to universal generalization: stating the circumstances under which a pattern is expected to hold.",
    "open system": "A social setting where new contexts, actors, learning, and causal forces continually affect program operation.",
    "cumulation": "The progressive refinement of program theory across studies, cases, and replications.",
    "middle-range theory": "A theory abstract enough to travel across cases but specific enough to guide empirical evaluation.",
    "replication": "A follow-on test that refines where and how a CMO configuration holds, rather than expecting identical effects everywhere.",
    "configuration focusing": "Refining CMO configurations by adapting and testing a known mechanism across new local contexts.",
    "stakeholder knowledge": "Practitioner, participant, and policy-maker knowledge used as evidence about program theories and mechanisms.",
    "realist interview": "An interview strategy that invites respondents to inspect, correct, and refine the evaluator's program-theory propositions.",
    "teacher-learner cycle": "A realist relationship in which evaluators learn stakeholder theories and teach back refined CMO explanations.",
    "program theory": "An account of how a program is expected to trigger mechanisms and outcomes in specific contexts.",
    "policy learning": "The use of evaluation to improve program design, adaptation, commissioning, and termination decisions.",
    "realization": "The process by which a program actualizes causal potential in particular contexts and accomplishes policy objectives.",
    "stakeholder theory": "The ideas held by policy makers, practitioners, and participants about how a program works.",
    "causal powers": "Underlying capacities or tendencies that may generate outcomes when suitable contexts activate them.",
    "black box evaluation": "Evaluation that estimates whether outcomes changed without explaining how or why the program produced them.",
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
        0,
        "Introduction",
        "10-18",
        "chapter-00-introduction.qmd",
        "Introduction",
        [
            "chunk:realistic-evaluation:introduction:c0004",
            "chunk:realistic-evaluation:introduction:c0008",
            "chunk:realistic-evaluation:introduction:c0010",
            "chunk:realistic-evaluation:introduction:c0011",
            "chunk:realistic-evaluation:introduction:c0013",
            "chunk:realistic-evaluation:introduction:c0014",
        ],
        "The introduction positions realistic evaluation as a constructive alternative to evaluation traditions that ask whether programs work without explaining why, for whom, and in what circumstances.",
        [
            "The introduction sets the agenda for a realist reconstruction of evaluation. Pawson and Tilley argue that evaluation needs a scientific account of policy learning, but one suited to the messy, open character of social programs.",
            "The reader's guide presents the book as a staged argument: a history of evaluation, a critique of experimental evaluation, a philosophical account of scientific realism, and then practical chapters on design, cumulation, data construction, consultation, policy, and rules.",
            "The introduction names context, mechanism, and outcome as the conceptual backbone of realistic evaluation. Programs are not treated as simple treatments that cause effects, but as resources and ideas that may trigger mechanisms under particular conditions.",
            "The practical stance is neither method rejection nor paradigm warfare. The book asks evaluators to recover objectivity by improving explanation: to learn why a program works, for whom, in which settings, and how that knowledge can guide future decisions.",
        ],
        ["realistic evaluation", "CMO configuration", "context", "mechanism", "outcome pattern", "policy learning"],
        ["evaluation at a watershed", "being real, realist, and realistic", "reader's guide", "CMO vocabulary", "book argument"],
        ["Frame evaluation questions as explanatory questions, not only effect questions.", "Use CMO language before choosing methods.", "Treat the book as a route from critique to practical design."],
        "orientation",
    ),
    chapter(
        1,
        "A History of Evaluation in 28 1/2 Pages",
        "18-46",
        "chapter-01-a-history-of-evaluation-in-28-and-a-half-pages.qmd",
        "Chapter 1: A History of Evaluation in 28 1/2 Pages",
        [
            "chunk:realistic-evaluation:ch01-chapter-1-a-history-of-evaluation-in-28-1-2-pages:c0003",
            "chunk:realistic-evaluation:ch01-chapter-1-a-history-of-evaluation-in-28-1-2-pages:c0006",
            "chunk:realistic-evaluation:ch01-chapter-1-a-history-of-evaluation-in-28-1-2-pages:c0045",
            "chunk:realistic-evaluation:ch01-chapter-1-a-history-of-evaluation-in-28-1-2-pages:c0054",
            "chunk:realistic-evaluation:ch01-chapter-1-a-history-of-evaluation-in-28-1-2-pages:c0067",
        ],
        "Evaluation history shows repeated attempts to solve the same problem: how to produce useful, objective knowledge about complex programs without collapsing into method dogma or ungrounded pluralism.",
        [
            "Chapter 1 surveys major evaluation traditions and uses that history to position the realist alternative. The chapter begins from the proliferation of evaluation approaches and the danger that evaluation becomes a label rather than a disciplined methodology.",
            "The discussion moves through experimental, pragmatic, naturalistic, constructivist, pluralist, and comprehensive evaluation traditions. Each contributes something useful, but each also leaves unresolved tensions about explanation, objectivity, stakeholder knowledge, and policy use.",
            "Pawson and Tilley are especially wary of easy pluralism. They recognize the appeal of combining rigor, policy usefulness, and stakeholder sensitivity, but argue that a synthesis needs a stronger theory of causation and explanation.",
            "The chapter prepares the realist stance by retaining the aspiration to learn from interventions while rejecting both simple effectism and the idea that all stakeholder accounts are equally adequate explanations.",
        ],
        ["realistic evaluation", "black box evaluation", "policy learning", "stakeholder theory", "scientific realism"],
        ["evaluation proliferation", "experimental tradition", "pragmatic and naturalistic turns", "constructivism", "pluralism", "realist positioning"],
        ["Use evaluation history as a warning against method-first design.", "Do not mistake plural coverage for explanatory clarity.", "Preserve objectivity by improving the theory of how programs generate change."],
        "critique",
    ),
    chapter(
        2,
        "Out with the Old: Weaknesses in Experimental Evaluation",
        "47-71",
        "chapter-02-out-with-the-old-weaknesses-in-experimental-evaluation.qmd",
        "Chapter 2: Out with the Old: Weaknesses in Experimental Evaluation",
        [
            "chunk:realistic-evaluation:ch02-chapter-2-out-with-the-old-weaknesses-in-experimental-evaluation:c0001",
            "chunk:realistic-evaluation:ch02-chapter-2-out-with-the-old-weaknesses-in-experimental-evaluation:c0002",
            "chunk:realistic-evaluation:ch02-chapter-2-out-with-the-old-weaknesses-in-experimental-evaluation:c0010",
            "chunk:realistic-evaluation:ch02-chapter-2-out-with-the-old-weaknesses-in-experimental-evaluation:c0044",
        ],
        "The experimental tradition is criticized for treating causation as external regularity, which can estimate net effects while missing the mechanisms and contexts that make social programs work or fail.",
        [
            "Chapter 2 offers a constructive critique of experimental evaluation. Pawson and Tilley do not reject scientific ambition; they argue that experimental evaluation has relied on an inadequate model of scientific explanation.",
            "The target is successionist causation: the idea that causal explanation is established by constant conjunction between treatment and outcome under controlled conditions. For social programs, this can leave the causal process itself in a black box.",
            "The chapter contrasts that view with generative causation. Programs work by activating powers, reasoning, opportunities, and constraints within particular contexts, so explanation has to reach inside the treatment-outcome relationship.",
            "Examples such as community policing show why net differences between treatment and control areas are not enough. Evaluators need to know which causal agents were omitted, how implementation interacted with context, and why apparent effects varied.",
        ],
        ["successionist causation", "generative causation", "black box evaluation", "mechanism", "context"],
        ["constructive critique", "experiments and causation", "missing causal agents", "program integrity", "community policing", "realist remedy"],
        ["Use experiments to support explanation, not replace it.", "Identify the causal process a program is expected to trigger.", "Treat subgroup and site variation as evidence, not nuisance."],
        "critique",
    ),
    chapter(
        3,
        "In with the New: Introducing Scientific Realism",
        "72-100",
        "chapter-03-in-with-the-new-introducing-scientific-realism.qmd",
        "Chapter 3: In with the New: Introducing Scientific Realism",
        [
            "chunk:realistic-evaluation:ch03-chapter-3-in-with-the-new-introducing-scientific-realism:c0005",
            "chunk:realistic-evaluation:ch03-chapter-3-in-with-the-new-introducing-scientific-realism:c0011",
            "chunk:realistic-evaluation:ch03-chapter-3-in-with-the-new-introducing-scientific-realism:c0033",
            "chunk:realistic-evaluation:ch03-chapter-3-in-with-the-new-introducing-scientific-realism:c0050",
            "chunk:realistic-evaluation:ch03-chapter-3-in-with-the-new-introducing-scientific-realism:c0051",
        ],
        "Scientific realism gives evaluation its central explanatory formula: outcomes are generated when mechanisms are activated in contexts, and evaluation tests CMO configurations.",
        [
            "Chapter 3 develops the philosophical and methodological foundation of realistic evaluation. It argues that the task of science is to explain observed events by identifying the mechanisms and conditions that produce them.",
            "The chapter translates that philosophy into evaluation. Programs work only insofar as they introduce ideas, resources, constraints, and opportunities that trigger mechanisms for particular people in particular social and cultural contexts.",
            "This produces the book's core formula: context, mechanism, and outcome belong together. The evaluation task is to identify, articulate, test, and refine conjectured CMO configurations.",
            "The CCTV car park example shows why programs cannot be treated as uniform causal packages. A single intervention can fire multiple mechanisms and generate different outcome patterns depending on location, users, routines, and local norms.",
        ],
        ["scientific realism", "CMO configuration", "generative causation", "mechanism", "context", "outcome pattern"],
        ["realist explanation", "real experiments", "mechanism question", "context question", "CMO configurations", "car park example"],
        ["Write hypotheses as CMO configurations.", "Design comparisons around mechanism-context variation.", "Use contradictory outcomes to refine the program theory."],
        "foundation",
    ),
    chapter(
        4,
        "How to Design a Realistic Evaluation",
        "100-130",
        "chapter-04-how-to-design-a-realistic-evaluation.qmd",
        "Chapter 4: How to Design a Realistic Evaluation",
        [
            "chunk:realistic-evaluation:ch04-chapter-4-how-to-design-a-realistic-evaluation:c0003",
            "chunk:realistic-evaluation:ch04-chapter-4-how-to-design-a-realistic-evaluation:c0004",
            "chunk:realistic-evaluation:ch04-chapter-4-how-to-design-a-realistic-evaluation:c0006",
            "chunk:realistic-evaluation:ch04-chapter-4-how-to-design-a-realistic-evaluation:c0038",
        ],
        "Realist design starts from theory, derives hypotheses about mechanisms and contexts, then selects empirical comparisons that can test and refine those explanations.",
        [
            "Chapter 4 turns realist principles into design practice. Pawson and Tilley keep the broad research cycle of theory, hypothesis, observation, and refinement, but change its content.",
            "The realist evaluation cycle begins with candidate program theories. The evaluator specifies expected CMO configurations, gathers evidence about where they do or do not appear, and returns refined explanations rather than unconditional generalizations.",
            "The chapter's exemplars show that no single method is uniquely realist. Qualitative, quantitative, contemporaneous, retrospective, active, and passive designs can all be realist when they test how mechanisms operate in contexts.",
            "The design task is therefore imaginative and disciplined. The evaluator asks what comparisons, cases, measures, interviews, observations, and outcome patterns would put the conjectured CMO theory at risk.",
        ],
        ["realist design", "theory testing", "specification", "CMO configuration", "outcome pattern"],
        ["research cycle", "realist evaluation cycle", "three exemplars", "comparison logic", "outcome patterns", "theory refinement"],
        ["Select methods by the CMO proposition being tested.", "Prefer comparisons that expose context-mechanism variation.", "Report specified conditions rather than universal claims."],
        "design",
    ),
    chapter(
        5,
        "How to Make Evaluations Cumulate",
        "132-170",
        "chapter-05-how-to-make-evaluations-cumulate.qmd",
        "Chapter 5: How to Make Evaluations Cumulate",
        [
            "chunk:realistic-evaluation:ch05-chapter-5-how-to-make-evaluations-cumulate:c0007",
            "chunk:realistic-evaluation:ch05-chapter-5-how-to-make-evaluations-cumulate:c0015",
            "chunk:realistic-evaluation:ch05-chapter-5-how-to-make-evaluations-cumulate:c0016",
            "chunk:realistic-evaluation:ch05-chapter-5-how-to-make-evaluations-cumulate:c0030",
            "chunk:realistic-evaluation:ch05-chapter-5-how-to-make-evaluations-cumulate:c0070",
        ],
        "Evaluation knowledge cumulates when studies refine middle-range CMO theories across cases, rather than merely aggregating average effects or replicating interventions mechanically.",
        [
            "Chapter 5 addresses how evaluation can build knowledge over time. Pawson and Tilley reject cumulation as simple empirical generalization and instead propose cumulation as theory development.",
            "The chapter connects CMO configurations to middle-range theory. A useful evaluation finding should be abstract enough to guide future inquiry, but concrete enough to specify where mechanisms should operate.",
            "Replication becomes configuration focusing. Subsequent studies do not expect the same program to produce the same result everywhere; they test how a mechanism behaves under new contextual conditions.",
            "The Kirkholt burglary example illustrates the messy but progressive character of realist cumulation. Evidence accumulates by preserving the relationship among mechanisms, contexts, and outcomes, not by stripping cases down to undifferentiated effects.",
        ],
        ["cumulation", "middle-range theory", "replication", "configuration focusing", "CMO configuration"],
        ["realistic cumulation", "typology of theory", "ladder of abstraction", "replication", "Kirkholt case", "accumulated wisdom"],
        ["Treat every evaluation as a contribution to a larger program theory.", "Use replication to refine CMO boundaries.", "Reject reports that only state whether change occurred."],
        "design",
    ),
    chapter(
        6,
        "How to Construct Realistic Data: Utilizing Stakeholders' Knowledge",
        "171-199",
        "chapter-06-how-to-construct-realistic-data-utilizing-stakeholders-knowledge.qmd",
        "Chapter 6: How to Construct Realistic Data: Utilizing Stakeholders' Knowledge",
        [
            "chunk:realistic-evaluation:introduction:c0013",
            "chunk:realistic-evaluation:ch06-chapter-6-how-to-construct-realistic-data-utilizing-stakeholders-knowledge:c0019",
            "chunk:realistic-evaluation:ch06-chapter-6-how-to-construct-realistic-data-utilizing-stakeholders-knowledge:c0061",
        ],
        "Realist data are constructed by using stakeholder knowledge to inspect, challenge, and refine program theories about mechanisms, contexts, and outcomes.",
        [
            "Chapter 6 develops a realist account of data collection. The question is not whether to choose controlled measurement or empathetic immersion, but how to gather evidence that tests program theories.",
            "Stakeholders are treated as holders of partial but valuable knowledge. Practitioners and participants can explain routines, constraints, interpretations, and mechanisms that are otherwise invisible to external measurement.",
            "The realist interview is the chapter's signature strategy. Rather than asking only for attitudes or experiences, evaluators share candidate theories with respondents and invite them to confirm, correct, or complicate those theories.",
            "Data construction is therefore dialogic and theory-driven. The evaluator moves between teaching and learning, using stakeholder accounts as evidence about how mechanisms may operate in particular contexts.",
        ],
        ["stakeholder knowledge", "realist interview", "teacher-learner cycle", "program theory", "mechanism", "context"],
        ["research relationship", "stakeholder theories", "realist interview", "data construction", "quantitative and qualitative routes", "conclusion"],
        ["Ask stakeholders to reason about candidate mechanisms, not only describe experiences.", "Use interviews to test program theory.", "Treat respondent disagreement as theory-refining evidence."],
        "data",
    ),
    chapter(
        7,
        "No Smoking Without Firing Mechanisms: A 'Realistic' Consultation",
        "200-216",
        "chapter-07-no-smoking-without-firing-mechanisms.qmd",
        "Chapter 7: No Smoking Without Firing Mechanisms: A 'Realistic' Consultation",
        [
            "chunk:realistic-evaluation:introduction:c0014",
            "chunk:realistic-evaluation:ch07-chapter-7-no-smoking-without-firing-mechanisms-a-realistic-consultation:c0001",
            "chunk:realistic-evaluation:ch07-chapter-7-no-smoking-without-firing-mechanisms-a-realistic-consultation:c0026",
            "chunk:realistic-evaluation:ch07-chapter-7-no-smoking-without-firing-mechanisms-a-realistic-consultation:c0040",
        ],
        "The smoking consultation demonstrates how realist evaluation translates research evidence and policy ideas into testable program theories and differentiated demonstration designs.",
        [
            "Chapter 7 is a worked consultation rather than a conventional methods chapter. It shows how the realist approach can move outside the criminal justice examples used earlier and apply to smoking cessation.",
            "The dialogue form makes visible the evaluator's reasoning. Existing research, policy expectations, and practical options are converted into candidate mechanisms, contexts, and possible program designs.",
            "The chapter insists that theory is practical. Anti-smoking programs embody ideas about health warnings, identity, social support, addiction, medical authority, and readiness to change, and these ideas should be made explicit.",
            "The resulting advice is to test families of tailored interventions rather than launch a single blockbuster. Different programs can be designed to fire mechanisms in contexts where they are most likely to matter.",
        ],
        ["program theory", "mechanism", "context", "realist design", "stakeholder theory"],
        ["fictional consultation", "smoking cessation evidence", "program theories", "mechanism selection", "demonstration projects", "tailored designs"],
        ["Translate policy ideas into explicit program theories.", "Design related interventions to test different mechanism-context combinations.", "Use consultation to surface the assumptions behind program choice."],
        "application",
    ),
    chapter(
        8,
        "Evaluation, Policy and Practice: Realizing the Potential",
        "217-230",
        "chapter-08-evaluation-policy-and-practice-realizing-the-potential.qmd",
        "Chapter 8: Evaluation, Policy and Practice: Realizing the Potential",
        [
            "chunk:realistic-evaluation:ch08-chapter-8-evaluation-policy-and-practice-realizing-the-potential:c0001",
            "chunk:realistic-evaluation:ch08-chapter-8-evaluation-policy-and-practice-realizing-the-potential:c0004",
            "chunk:realistic-evaluation:ch08-chapter-8-evaluation-policy-and-practice-realizing-the-potential:c0014",
            "chunk:realistic-evaluation:ch08-chapter-8-evaluation-policy-and-practice-realizing-the-potential:c0019",
            "chunk:realistic-evaluation:ch08-chapter-8-evaluation-policy-and-practice-realizing-the-potential:c0025",
        ],
        "Realistic evaluation supports policy and practice by creating a teacher-learner cycle in which evaluators reconstruct, test, and feed back stakeholder theories for program improvement.",
        [
            "Chapter 8 extends the teacher-learner cycle to policy makers. Policy makers commission, authorize, maintain, modify, or terminate programs, but their knowledge is partial and embedded in political and organizational constraints.",
            "The realist evaluator treats the policy maker's account as one source of testable theory. It is not merely a preference to be negotiated, nor a fixed design specification, but a claim about how the program can realize objectives.",
            "The chapter brings together policy makers, practitioners, participants, and evaluators in a cycle of mutual teaching and learning. Evaluators learn stakeholder theories and teach back refined CMO explanations.",
            "The concept of realization links understanding and action. Evaluation should help policy actors understand how change is brought about, actualize causal potential in context, and improve accomplishment of policy objectives.",
        ],
        ["teacher-learner cycle", "policy learning", "stakeholder theory", "realization", "CMO configuration"],
        ["policy maker role", "teacher-learner cycle", "Safer Cities example", "realization", "feedback", "policy practice"],
        ["Treat policy-maker assumptions as testable program theory.", "Feed back findings as refined CMO explanations.", "Use evaluation to improve future program realization, not only judge past performance."],
        "policy",
    ),
    chapter(
        9,
        "The New Rules of Realistic Evaluation",
        "231-236",
        "chapter-09-the-new-rules-of-realistic-evaluation.qmd",
        "Chapter 9: The New Rules of Realistic Evaluation",
        [
            "chunk:realistic-evaluation:ch09-chapter-9-the-new-rules-of-realistic-evaluation:c0001",
            "chunk:realistic-evaluation:ch09-chapter-9-the-new-rules-of-realistic-evaluation:c0004",
            "chunk:realistic-evaluation:ch09-chapter-9-the-new-rules-of-realistic-evaluation:c0007",
            "chunk:realistic-evaluation:ch09-chapter-9-the-new-rules-of-realistic-evaluation:c0008",
            "chunk:realistic-evaluation:ch09-chapter-9-the-new-rules-of-realistic-evaluation:c0010",
            "chunk:realistic-evaluation:ch09-chapter-9-the-new-rules-of-realistic-evaluation:c0012",
        ],
        "The final rules condense the book into a realist evaluation language: generative causation, ontological depth, mechanisms, contexts, outcomes, CMO configurations, teacher-learner processes, and open systems.",
        [
            "Chapter 9 recapitulates the book as a set of methodological rules. The rules are not a checklist detached from the argument; they summarize how realist evaluation understands causation, evidence, stakeholders, and use.",
            "The rules begin with generative causation and ontological depth. Evaluators should look beneath observed inputs and outputs to the causal powers, choices, constraints, and social forces that make outcomes possible.",
            "Mechanisms, contexts, and outcomes are treated as mutually explanatory. Programs produce multiple outcomes by firing mechanisms differently for different people in different situations.",
            "The chapter ends with CMO configurations, teacher-learner processes, and open systems. Realistic evaluation remains cumulative and objective, but it accepts that social programs operate in changing, permeable worlds where explanation must be refined continually.",
        ],
        ["generative causation", "open system", "CMO configuration", "teacher-learner cycle", "outcome pattern"],
        ["new rules", "generative causation", "ontological depth", "mechanisms and contexts", "CMO configurations", "open systems"],
        ["Use the rules as design tests for realist evaluations.", "State findings as refined CMO configurations.", "Expect even strong explanations to remain open to new contexts and mechanisms."],
        "synthesis",
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
    return "Introduction" if chapter_item["number"] == 0 else f"Chapter {chapter_item['number']}: {chapter_item['title']}"


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
    title = chapter_label(chapter_item).replace('"', "'")
    lines = ["flowchart TD", f'  Problem["Problem: What does {title} help explain?"]', f'  Central["Concept: {chapter_item["title"]}"]']
    for idx, concept in enumerate(concepts, start=1):
        lines.append(f'  Concept{idx}["Concept: {concept}"]')
    for idx, item in enumerate(structures, start=1):
        lines.append(f'  Mechanism{idx}["Inquiry element: {item}"]')
    for idx, implication in enumerate(implications, start=1):
        lines.append(f'  Implication{idx}["Practice implication: {implication.replace(chr(34), chr(39))}"]')
    lines.extend(["  Question[\"Open question: Which CMO claim needs source checking?\"]", "", "  Problem --> Central", "  Central --> Question"])
    for idx in range(1, len(concepts) + 1):
        lines.append(f"  Central --> Concept{idx}")
    for idx in range(1, len(structures) + 1):
        lines.append(f"  Concept{min(idx, len(concepts))} --> Mechanism{idx}")
    for idx in range(1, len(implications) + 1):
        lines.append(f"  Mechanism{min(idx, len(structures))} --> Implication{idx}")
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
            f"  class {','.join(f'Mechanism{i}' for i in range(1, len(structures) + 1))} mechanism;",
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
        "The retrieval trail is retained in the source records at the bottom of the page. The note paraphrases the chapter's argument and procedures, and it does not reproduce textbook tables, figures, boxes, or extended passages.",
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
            wrap(f"For close reading, track how the chapter uses {', '.join(chapter_item['concepts'][:4])} while moving through {', '.join(chapter_item['structure'][:3])}. The note identifies which CMO claim the chapter helps formulate, test, or refine."),
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
            f"- What CMO configuration does {label} help formulate or refine?",
            "- Which mechanism and context claims would need stronger empirical evidence?",
            "- Which source record should be reopened before using this note in applied work?",
        ]
    )
    lines.extend(["", "## Source Records", "", source_chunks(chapter_item["evidence_ids"]), "", "## References", ""])
    return "\n".join(lines)


def render_index() -> str:
    evidence = all_evidence_ids()
    group_names = {
        "orientation": "Orientation",
        "critique": "Critique of Existing Evaluation Traditions",
        "foundation": "Realist Foundation",
        "design": "Design and Cumulation",
        "data": "Data Construction",
        "application": "Worked Application",
        "policy": "Policy and Practice",
        "synthesis": "Synthesis",
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
        "Realistic evaluation explains programs through CMO configurations: programs trigger mechanisms in contexts to produce outcome patterns, and evaluation tests and refines those explanations for policy and practice.",
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
        "- **Start with the problem of evaluation**: Introduction and Chapter 1 explain why existing traditions need a stronger account of explanation.",
        "- **Understand the realist foundation**: Chapters 2-3 move from critique of experimental causation to CMO configurations.",
        "- **Design and build knowledge**: Chapters 4-6 cover realist design, cumulation, and stakeholder-informed data.",
        "- **Apply and use the approach**: Chapters 7-9 show consultation, policy learning, and the final rules.",
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
        "Core Explanation": ["CMO configuration", "context", "mechanism", "outcome pattern", "generative causation", "scientific realism"],
        "Design and Evidence": ["realist design", "theory testing", "specification", "open system", "cumulation", "middle-range theory", "replication", "configuration focusing"],
        "Stakeholders and Use": ["stakeholder knowledge", "realist interview", "teacher-learner cycle", "program theory", "policy learning", "realization", "stakeholder theory"],
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
        "State evaluation questions as what works, for whom, in what circumstances, and why.",
        "Translate each program theory into a conjectured CMO configuration before selecting methods.",
        "Use variation across places, people, implementation forms, and outcome patterns as explanatory evidence.",
        "Choose methods because they test a mechanism-context proposition, not because they belong to a favored paradigm.",
        "Use stakeholder interviews to inspect and refine program theories, not only to collect opinions.",
        "Report findings as specified explanations that can guide adaptation, replication, and future testing.",
        "Treat cumulation as theory refinement across cases rather than simple aggregation of effect sizes.",
        "Feed findings back to policy makers, practitioners, and participants as part of a teacher-learner cycle.",
        "Expect realist explanations to remain open to revision as programs enter new contexts and causal forces emerge.",
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
                "section_id": "introduction" if chapter_item["number"] == 0 else f"chapter-{chapter_item['number']:02d}",
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
            "limit": "targeted chapter retrieval; broad full-book evidence pack used before synthesis",
            "include_media": "true for full-book grounding and figure-heavy chapters",
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
                    "id": "introduction" if chapter_item["number"] == 0 else f"chapter-{chapter_item['number']:02d}",
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
        "chapter-level Rossi/Lipsey, Chen, and Impact Evaluation in Practice notes, step-level Patton/U-FE notes, and generated notes for the wider collection.": "chapter-level Rossi/Lipsey, Chen, Impact Evaluation in Practice, and Realistic Evaluation notes, step-level Patton/U-FE notes, and generated notes for the wider collection.",
        "chapter-level Rossi/Lipsey, Chen, and Impact Evaluation in Practice notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.": "chapter-level Rossi/Lipsey, Chen, Impact Evaluation in Practice, and Realistic Evaluation notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.",
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
