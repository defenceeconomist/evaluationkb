#!/usr/bin/env python3
"""Generate chapter-level Impact Evaluation in Practice study notes."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "impact-evaluation-in-practice"
SLUG = BOOK_ID
TITLE = "Impact Evaluation in Practice"
FULL_TITLE = TITLE
AUTHORS = "Paul J. Gertler, Sebastian Martinez, Patrick Premand, Laura B. Rawlings, and Christel M. J. Vermeersch"
CITATION = "gertler_martinez_premand_rawlings_vermeersch_2016_impact_evaluation_in_practice"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2016"
GENERATED_AT = "2026-06-28"


LEGACY_EXTRACTS = [
    ("What Is Impact Evaluation?", "section-01-what-is-impact-evaluation.qmd"),
    ("Constructing a Theory of Change", "section-02-constructing-theory-of-change.qmd"),
    ("Causal Inference and Counterfactuals", "section-03-causal-inference-counterfactuals.qmd"),
]


CONCEPT_GLOSSES = {
    "administrative data": "Existing service, registry, monitoring, or management data that may reduce collection burden if quality and coverage are adequate.",
    "attrition": "Loss of sample members between baseline and follow-up that can bias estimates if it differs across groups or correlates with outcomes.",
    "causal inference": "Reasoning that links observed outcome differences to the program rather than to other influences.",
    "comparison group": "Units used to estimate what would have happened to the treatment group without the program.",
    "cost-effectiveness": "Comparison of program costs with nonmonetized outcome units so decision makers can judge value across options.",
    "common support": "Overlap in characteristics or propensity scores that allows treated units to be compared with similar untreated units.",
    "counterfactual": "The unobserved outcome that treatment units would have experienced without the program.",
    "data quality": "The accuracy, completeness, consistency, confidentiality, and usability of data for impact estimation.",
    "difference-in-differences": "A quasi-experimental method that compares changes over time in treatment and comparison groups.",
    "dissemination strategy": "A planned approach to turning evaluation findings into products, channels, timing, and engagement for specific audiences.",
    "eligibility cutoff": "A threshold on an assignment index that determines treatment eligibility in a regression discontinuity design.",
    "ethics": "Protection of participants and fair assignment rules, combined with transparent and reproducible research practice.",
    "evaluation plan": "The management document that aligns questions, design, sampling, data, analysis, ethics, dissemination, roles, timeline, and budget.",
    "evaluation question": "A policy-relevant, testable question that specifies the intervention, comparison, outcome, and decision need.",
    "evidence use": "Application of evaluation findings to decisions about design, targeting, scale-up, continuation, reform, or termination.",
    "external validity": "The degree to which an impact estimate is relevant beyond the studied sample, setting, or local treatment effect.",
    "factorial design": "A design that assigns units across combinations of components so separate and joint treatment effects can be estimated.",
    "fieldwork": "The organized collection of new data, including enumerator training, piloting, supervision, quality checks, and respondent follow-up.",
    "human subjects protection": "Review, consent, confidentiality, and risk-management procedures for research involving people.",
    "impact evaluation": "Evaluation that estimates the causal effect of a program, policy, or intervention on outcomes.",
    "imperfect compliance": "A mismatch between assigned treatment status and actual participation or receipt of services.",
    "implementation fidelity": "The degree to which program assignment, uptake, delivery, and follow-up match the evaluation design.",
    "instrumental variables": "A method that uses external variation in program participation to estimate impacts when take-up or assignment is imperfect.",
    "intention-to-treat": "The effect of being assigned or offered treatment, regardless of whether the unit actually receives it.",
    "internal validity": "The credibility that an estimated difference is caused by the program being evaluated.",
    "local average treatment effect": "The impact estimated for a specific subgroup, such as compliers or units near a cutoff.",
    "matching": "A method that constructs a comparison group by pairing treated units with untreated units that have similar observed characteristics.",
    "minimum detectable effect": "The smallest impact an evaluation is powered to detect for a given sample, variance, significance level, and design.",
    "budget": "A management estimate of the resources needed for design, data collection, analysis, ethics, dissemination, and coordination.",
    "cluster": "A grouped assignment, sampling, or analysis unit such as a school, village, clinic, or community.",
    "multifaceted program": "A program with different components, treatment levels, or treatment arms whose separate and joint effects may need testing.",
    "operational rules": "Program rules governing eligibility, assignment, timing, scale-up, and delivery that shape feasible evaluation methods.",
    "open science": "Registration, preanalysis planning, transparent reporting, and data or code sharing that support credibility and replication.",
    "parallel trends": "The difference-in-differences assumption that treatment and comparison outcomes would have moved together without the program.",
    "policy impact": "The influence evaluation evidence has on program continuation, redesign, scale-up, termination, or wider learning.",
    "power calculation": "A calculation used to determine the sample size needed to detect a meaningful effect with acceptable probability.",
    "preanalysis plan": "A document specifying hypotheses, outcomes, methods, and analytic decisions before results are examined.",
    "propensity score": "The estimated probability that a unit participates in treatment, based on observed characteristics.",
    "randomized assignment": "A method that allocates eligible units to treatment and comparison groups by chance.",
    "randomized promotion": "An encouragement design that randomly varies outreach or incentives and uses that variation as an instrument for participation.",
    "regression discontinuity design": "A method that compares units just above and below a cutoff used to assign program eligibility.",
    "results chain": "A representation of how inputs and activities are expected to produce outputs, intermediate outcomes, and final outcomes.",
    "sample": "The units selected for data collection and analysis, ideally aligned with the treatment assignment unit and policy population.",
    "selection bias": "Bias that arises when treatment and comparison groups differ in ways that affect outcomes independently of the program.",
    "SMART indicators": "Indicators that are specific, measurable, attributable, realistic, and targeted.",
    "spillovers": "Effects of treatment on units outside the intended treatment group, which can contaminate comparison groups.",
    "stakeholder engagement": "Deliberate involvement of policy makers, implementers, analysts, and other users in shaping questions, timing, interpretation, and use.",
    "survey data": "New data collected from individuals, households, firms, facilities, or communities for the evaluation.",
    "team roles": "Explicit responsibilities across policy, research, data collection, analysis, ethics, and dissemination workstreams.",
    "theory of change": "A causal account of how a program is expected to move from activities to outcomes.",
    "time-varying differences": "Changes affecting treatment and comparison groups differently over time, which can invalidate difference-in-differences estimates.",
    "treatment arms": "Distinct groups assigned to different program versions, levels, combinations, or comparison conditions.",
    "treatment levels": "Different intensities, doses, or versions of a program whose impacts can be compared.",
}


def chapter(
    number: int,
    title: str,
    pages: str,
    file: str,
    section_path: str,
    evidence_ids: list[str],
    core: str,
    summary: list[str],
    concepts: list[str],
    structure: list[str],
    implications: list[str],
    group: str,
) -> dict:
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
        "Why Evaluate?",
        "33-59",
        "chapter-01-why-evaluate.qmd",
        "Part 1: Introduction to Impact Evaluation > Chapter 1: Why Evaluate?",
        [
            "chunk:impact-evaluation-in-practice:ch01-chapter-1-why-evaluate:c0001",
            "chunk:impact-evaluation-in-practice:evidence-based-policy-making:c0006",
            "chunk:impact-evaluation-in-practice:what-is-impact-evaluation:c0006",
            "chunk:impact-evaluation-in-practice:impact-evaluation-for-policy-decisions:c0007",
            "chunk:impact-evaluation-in-practice:ethical-considerations-regarding-impact-evaluation:c0003",
        ],
        "Impact evaluation is justified when a policy decision needs credible causal evidence about whether a program works, for whom, and under what implementation choices.",
        [
            "Chapter 1 frames impact evaluation as a tool for evidence-based policy making. Its central move is to distinguish impact evaluation from monitoring, descriptive assessment, and general performance reporting: impact evaluation asks what difference a program caused.",
            "The chapter stresses that causal evidence is useful when decision makers face choices about continuation, redesign, scale-up, or alternative modalities. It is not a ritual requirement for every program, but a design response to policy uncertainty.",
            "The chapter introduces the menu of methods that the book later develops: randomized assignment, instrumental variables, regression discontinuity design, difference-in-differences, and matching. Method choice is tied to operational rules rather than evaluator preference.",
            "Ethics appear early as part of evaluation design. Fair assignment rules, human subjects protection, transparency, preanalysis planning, and reproducibility are treated as part of credible causal inquiry rather than after-the-fact compliance work.",
        ],
        ["impact evaluation", "causal inference", "policy impact", "operational rules", "ethics"],
        ["evidence-based policy making", "what impact evaluation estimates", "when impact evaluation is useful", "method menu", "policy decisions", "ethical considerations"],
        ["Use impact evaluation when a real policy choice depends on causal evidence.", "Separate causal questions from monitoring and implementation questions.", "Treat fairness, transparency, and reproducibility as design constraints from the start."],
        "introduction",
    ),
    chapter(
        2,
        "Preparing for an Evaluation",
        "61-73",
        "chapter-02-preparing-for-an-evaluation.qmd",
        "Part 1: Introduction to Impact Evaluation > Chapter 2: Preparing for an Evaluation",
        [
            "chunk:impact-evaluation-in-practice:ch02-chapter-2-preparing-for-an-evaluation:c0001",
            "chunk:impact-evaluation-in-practice:initial-steps:c0001",
            "chunk:impact-evaluation-in-practice:developing-a-results-chain:c0001",
            "chunk:impact-evaluation-in-practice:specifying-evaluation-questions:c0001",
            "chunk:impact-evaluation-in-practice:selecting-outcome-and-performance-indicators:c0004",
        ],
        "A credible evaluation starts by turning program logic into a results chain, evaluation questions, and measurable indicators before any method is chosen.",
        [
            "Chapter 2 sets out the preparation work that makes later causal design possible. The first task is to clarify the theory of change and results chain so the program's inputs, activities, outputs, intermediate outcomes, and final outcomes are connected.",
            "The chapter treats evaluation questions as the bridge between policy need and research design. A useful question is specific enough to become a testable hypothesis, but still tied to the decisions stakeholders must make.",
            "Indicators must be selected for outcomes and for implementation. Outcome indicators support impact estimation, while implementation and performance indicators help interpret whether a null or weak result reflects theory failure or delivery failure.",
            "The chapter also points evaluators toward stakeholder engagement and data planning. A design that is technically strong but disconnected from decision makers, feasible indicators, or data risks will be hard to implement and use.",
        ],
        ["theory of change", "results chain", "evaluation question", "SMART indicators", "implementation fidelity"],
        ["initial steps", "constructing a theory of change", "developing a results chain", "specifying questions", "selecting indicators", "checking data availability"],
        ["Write the results chain before writing the identification strategy.", "Use evaluation questions to narrow method choice.", "Track implementation indicators so impact estimates can be interpreted."],
        "introduction",
    ),
    chapter(
        3,
        "Causal Inference and Counterfactuals",
        "77-93",
        "chapter-03-causal-inference-and-counterfactuals.qmd",
        "Part 2: How to Evaluate > Chapter 3: Causal Inference and Counterfactuals",
        [
            "chunk:impact-evaluation-in-practice:part-2:c0001",
            "chunk:impact-evaluation-in-practice:causal-inference:c0001",
            "chunk:impact-evaluation-in-practice:counterfeit-estimates-of-the-counterfactual:c0001",
            "chunk:impact-evaluation-in-practice:counterfeit-estimates-of-the-counterfactual:c0007",
        ],
        "The core problem of impact evaluation is constructing a valid estimate of the counterfactual: what would have happened to treated units without treatment.",
        [
            "Chapter 3 introduces the causal logic behind all later methods. Because the same unit cannot be observed both with and without treatment at the same time, the evaluator must approximate the missing counterfactual.",
            "The chapter warns against counterfeit counterfactuals. Before-and-after comparisons and simple participant/nonparticipant comparisons can be misleading when other changes, selection, or baseline differences drive outcomes.",
            "A valid comparison group should resemble the treatment group in all respects except for treatment exposure. The rest of Part 2 is organized around ways to create or defend that condition under different program rules.",
            "The practical implication is that causal inference is not created by statistical complexity alone. It depends on the assignment process, timing, data, and assumptions that make the comparison credible.",
        ],
        ["causal inference", "counterfactual", "comparison group", "internal validity", "selection bias"],
        ["impact as a causal contrast", "missing counterfactual", "counterfeit counterfactuals", "valid comparison groups", "method selection logic"],
        ["Do not treat baseline/follow-up change as impact without a counterfactual.", "Document why the comparison group is credible.", "Make assignment rules central to the evaluation design."],
        "methods",
    ),
    chapter(
        4,
        "Randomized Assignment",
        "97-116",
        "chapter-04-randomized-assignment.qmd",
        "Part 2: How to Evaluate > Chapter 4: Randomized Assignment",
        [
            "chunk:impact-evaluation-in-practice:randomized-assignment-of-treatment:c0013",
            "chunk:impact-evaluation-in-practice:randomized-assignment-of-treatment:c0033",
            "chunk:impact-evaluation-in-practice:checklist-randomized-assignment:c0008",
        ],
        "Randomized assignment creates treatment and comparison groups by chance, making average outcome differences a strong estimate of program impact when implementation preserves the design.",
        [
            "Chapter 4 explains randomized assignment as the benchmark design for internal validity. If eligible units are assigned by chance, observed and unobserved characteristics should be balanced on average before treatment.",
            "The impact estimate is conceptually simple: compare mean outcomes for the randomly assigned treatment and comparison groups. That simplicity depends on preserving the assignment process and measuring outcomes consistently.",
            "The chapter connects randomization to program operations. Lotteries, phased rollout, or oversubscription can create ethical and administratively feasible opportunities to randomize when resources are limited.",
            "It also flags operational vulnerabilities. Sample size, compliance, spillovers, political acceptability, and the treatment unit all affect whether randomization remains credible in practice.",
        ],
        ["randomized assignment", "comparison group", "internal validity", "sample", "implementation fidelity"],
        ["random assignment logic", "estimating impacts", "lotteries and rollout", "checking balance", "implementation risks", "checklist"],
        ["Use randomization when program rules make it fair and feasible.", "Specify the unit of assignment before launch.", "Protect the design during rollout, not only during analysis."],
        "methods",
    ),
    chapter(
        5,
        "Instrumental Variables",
        "119-140",
        "chapter-05-instrumental-variables.qmd",
        "Part 2: How to Evaluate > Chapter 5: Instrumental Variables",
        [
            "chunk:impact-evaluation-in-practice:evaluating-programs-when-not-everyone-complies-with-their-assignment:c0001",
            "chunk:impact-evaluation-in-practice:imperfect-compliance:c0006",
            "chunk:impact-evaluation-in-practice:randomized-promotion-as-an-instrumental-variable:c0001",
            "chunk:impact-evaluation-in-practice:randomized-promotion-as-an-instrumental-variable:c0018",
        ],
        "Instrumental variables recover causal impact when assignment or encouragement changes participation, especially when not everyone complies with the intended treatment status.",
        [
            "Chapter 5 begins from imperfect compliance. Some units assigned to treatment do not participate, and some units assigned to comparison may still receive services, so simple assignment contrasts no longer answer every causal question.",
            "The chapter distinguishes assignment, take-up, and treatment received. Randomized assignment or randomized promotion can be used as an instrument when it changes participation without directly affecting outcomes except through participation.",
            "The resulting estimate is local: it applies to units whose participation is changed by the instrument. The chapter's types of units, such as always-takers, never-takers, and compliers, make that limitation explicit.",
            "The method is powerful but assumption-heavy. Evaluators must defend the relevance of the instrument, the exclusion restriction, and the interpretation of local average treatment effects for policy decisions.",
        ],
        ["instrumental variables", "imperfect compliance", "randomized promotion", "local average treatment effect", "intention-to-treat"],
        ["noncompliance problem", "compliance types", "randomized promotion", "estimating participation effects", "local interpretation", "limitations"],
        ["Distinguish offer effects from participation effects.", "Use encouragement designs when universal access prevents direct randomization.", "Report clearly whose impact the IV estimate represents."],
        "methods",
    ),
    chapter(
        6,
        "Regression Discontinuity Design",
        "143-157",
        "chapter-06-regression-discontinuity-design.qmd",
        "Part 2: How to Evaluate > Chapter 6: Regression Discontinuity Design",
        [
            "chunk:impact-evaluation-in-practice:ch06-chapter-6-regression-discontinuity-design:c0001",
            "chunk:impact-evaluation-in-practice:evaluating-programs-that-use-an-eligibility-index:c0006",
            "chunk:impact-evaluation-in-practice:checking-the-validity-of-the-regression-discontinuity-design:c0005",
            "chunk:impact-evaluation-in-practice:limitations-and-interpretation-of-the-regression-discontinuity-design-method:c0001",
            "chunk:impact-evaluation-in-practice:limitations-and-interpretation-of-the-regression-discontinuity-design-method:c0004",
        ],
        "Regression discontinuity estimates impacts by comparing units just above and below a program eligibility cutoff, where units should be similar except for eligibility.",
        [
            "Chapter 6 applies counterfactual logic to programs that rank applicants with a continuous index and assign eligibility at a cutoff. The comparison is local: units near the cutoff are expected to be comparable.",
            "The chapter emphasizes diagnostics. Evaluators should check whether the assignment variable is continuous around the cutoff, whether units can manipulate their scores, and whether baseline characteristics are balanced near the threshold.",
            "The method handles some ethically attractive situations because eligible units do not need to be denied treatment solely for evaluation. Its trade-off is that the estimate applies near the cutoff rather than to all eligible units.",
            "Fuzzy discontinuity introduces imperfect compliance. When eligibility does not perfectly determine participation, the cutoff can function as an instrument, producing a local estimate for units whose participation is affected by eligibility.",
        ],
        ["regression discontinuity design", "eligibility cutoff", "local average treatment effect", "common support", "instrumental variables"],
        ["eligibility index", "cutoff comparison", "validity checks", "fuzzy RDD", "local interpretation", "limitations"],
        ["Use RDD when assignment already depends on a score and cutoff.", "Check manipulation and balance before interpreting impacts.", "Do not generalize local cutoff effects beyond the population they represent."],
        "methods",
    ),
    chapter(
        7,
        "Difference-in-Differences",
        "159-171",
        "chapter-07-difference-in-differences.qmd",
        "Part 2: How to Evaluate > Chapter 7: Difference-in-Differences",
        [
            "chunk:impact-evaluation-in-practice:ch07-chapter-7-difference-in-differences:c0001",
            "chunk:impact-evaluation-in-practice:evaluating-a-program-when-the-rule-of-assignment-is-less-clear:c0001",
            "chunk:impact-evaluation-in-practice:the-equal-trends-assumption-in-difference-in-differences:c0001",
            "chunk:impact-evaluation-in-practice:the-equal-trends-assumption-in-difference-in-differences:c0002",
        ],
        "Difference-in-differences estimates impact by comparing outcome changes over time between treatment and comparison groups, relying on the assumption that their trends would otherwise have moved together.",
        [
            "Chapter 7 introduces difference-in-differences for settings where assignment rules are less clear and evaluators have data before and after program exposure.",
            "The design subtracts baseline differences between groups and then compares changes over time. This can address time-invariant differences, but it cannot fix time-varying shocks that affect one group differently.",
            "The key identifying assumption is parallel or equal trends: without the program, treatment and comparison outcomes would have moved together. The chapter shows why violations of that assumption bias estimates.",
            "The method is practical in many policy settings, especially when randomization is unavailable, but it requires careful selection of comparison groups, pretrend checks where possible, and attention to other simultaneous changes.",
        ],
        ["difference-in-differences", "parallel trends", "comparison group", "counterfactual", "time-varying differences"],
        ["before-after logic", "treatment and comparison changes", "equal trends assumption", "threats", "implementation examples"],
        ["Use DD only when a credible comparison trend can be defended.", "Look for pre-program outcome histories rather than one baseline point.", "Document concurrent changes that could break the parallel trends assumption."],
        "methods",
    ),
    chapter(
        8,
        "Matching",
        "173-188",
        "chapter-08-matching.qmd",
        "Part 2: How to Evaluate > Chapter 8: Matching",
        [
            "chunk:impact-evaluation-in-practice:ch08-chapter-8-matching:c0001",
            "chunk:impact-evaluation-in-practice:propensity-score-matching:c0003",
            "chunk:impact-evaluation-in-practice:combining-matching-with-other-methods:c0001",
            "chunk:impact-evaluation-in-practice:limitations-of-the-matching-method:c0001",
        ],
        "Matching builds a comparison group from untreated units with similar observed characteristics, but it cannot eliminate bias from unobserved differences without stronger assumptions or complementary designs.",
        [
            "Chapter 8 presents matching as a nonexperimental approach for constructing comparison groups when assignment is not controlled by the evaluator.",
            "Propensity score matching compresses observed characteristics into a predicted probability of participation, restricts analysis to common support, and compares treated units with similar untreated units.",
            "The chapter is explicit about limitations. Matching requires rich data, large samples, common support, and the strong assumption that unobserved differences do not jointly affect participation and outcomes.",
            "The most convincing uses combine matching with other methods, especially matched difference-in-differences or synthetic control approaches, to reduce vulnerability to selection bias.",
        ],
        ["matching", "propensity score", "common support", "selection bias", "difference-in-differences"],
        ["matching logic", "propensity scores", "common support", "matched DD", "synthetic control", "limitations"],
        ["Use matching only when the dataset captures the drivers of participation and outcomes.", "Inspect common support before estimating effects.", "Prefer matching as a complement to stronger designs where possible."],
        "methods",
    ),
    chapter(
        9,
        "Addressing Methodological Challenges",
        "191-202",
        "chapter-09-addressing-methodological-challenges.qmd",
        "Part 2: How to Evaluate > Chapter 9: Addressing Methodological Challenges",
        [
            "chunk:impact-evaluation-in-practice:part-2:c0002",
            "chunk:impact-evaluation-in-practice:imperfect-compliance-2:c0001",
            "chunk:impact-evaluation-in-practice:imperfect-compliance-2:c0002",
            "chunk:impact-evaluation-in-practice:attrition:c0004",
            "chunk:impact-evaluation-in-practice:attrition:c0005",
        ],
        "Design problems such as imperfect compliance, spillovers, and attrition must be anticipated and analyzed because they can change what the estimated impact means.",
        [
            "Chapter 9 moves from ideal designs to implementation reality. Even carefully planned evaluations can face imperfect compliance, contamination, spillovers, and missing follow-up data.",
            "Imperfect compliance requires evaluators to distinguish assignment, offer, participation, and treatment received. The chapter links this challenge back to intention-to-treat and local average treatment effects.",
            "Spillovers matter because treatment can affect comparison units through information, markets, behavior, or geographic proximity. If spillovers are likely, the evaluation may need different units, buffers, or explicit spillover measurement.",
            "Attrition is treated as a data-validity threat. Evaluators should track loss rates, compare attrition across groups, compare baseline characteristics of respondents and nonrespondents, and consider corrections where justified.",
        ],
        ["imperfect compliance", "intention-to-treat", "local average treatment effect", "spillovers", "attrition"],
        ["imperfect compliance", "ITT and LATE", "spillovers", "attrition diagnosis", "statistical corrections", "interpretation"],
        ["Plan for noncompliance and missing data before baseline.", "Separate contamination problems from treatment-effect interpretation.", "Report attrition diagnostics, not only final sample sizes."],
        "methods",
    ),
    chapter(
        10,
        "Evaluating Multifaceted Programs",
        "205-213",
        "chapter-10-evaluating-multifaceted-programs.qmd",
        "Part 2: How to Evaluate > Chapter 10: Evaluating Multifaceted Programs",
        [
            "chunk:impact-evaluation-in-practice:ch10-chapter-10-evaluating-multifaceted-programs:c0001",
            "chunk:impact-evaluation-in-practice:evaluating-programs-that-combine-several-treatment-options:c0001",
            "chunk:impact-evaluation-in-practice:evaluating-programs-with-varying-treatment-levels:c0001",
            "chunk:impact-evaluation-in-practice:evaluating-multiple-interventions:c0001",
            "chunk:impact-evaluation-in-practice:evaluating-multiple-interventions:c0004",
        ],
        "Multifaceted programs can be evaluated by designing treatment arms that compare levels, components, or combinations of components, not only treatment versus no treatment.",
        [
            "Chapter 10 broadens impact evaluation beyond a binary program contrast. Policy makers often need to know which component, dosage, sequence, or package is most effective and cost-effective.",
            "The chapter discusses varying treatment levels, such as high- and low-intensity versions, as well as multiple treatment arms that compare distinct program modalities.",
            "When interventions may interact, factorial or cross-cutting designs can estimate both separate and combined effects. These designs answer richer policy questions but require larger samples and careful operational coordination.",
            "The chapter's practical message is to align evaluation arms with decisions. A design that only asks whether a package works may miss the more useful question of which part of the package is worth scaling.",
        ],
        ["multifaceted program", "treatment arms", "treatment levels", "factorial design", "cost-effectiveness"],
        ["multiple treatment options", "varying treatment levels", "multiple interventions", "combinations", "policy interpretation"],
        ["Design arms around real policy alternatives.", "Budget sample size for multiple contrasts.", "Use component designs when decision makers can change dosage or content."],
        "methods",
    ),
    chapter(
        11,
        "Choosing an Impact Evaluation Method",
        "217-229",
        "chapter-11-choosing-an-impact-evaluation-method.qmd",
        "Part 3: How to Implement an Impact Evaluation > Chapter 11: Choosing an Impact Evaluation Method",
        [
            "chunk:impact-evaluation-in-practice:determining-which-method-to-use-for-a-given-program:c0001",
            "chunk:impact-evaluation-in-practice:how-a-program-s-rules-of-operation-can-help-choose-an-impact-evaluation-method:c0008",
            "chunk:impact-evaluation-in-practice:a-comparison-of-impact-evaluation-methods:c0005",
        ],
        "Method choice should start from program rules, timing, and data, then select the strongest feasible design with the weakest necessary assumptions.",
        [
            "Chapter 11 turns the method menu into a decision process. Instead of asking which method is abstractly best, evaluators ask which methods are compatible with the program's operational rules.",
            "Rules about eligibility, oversubscription, rollout, assignment, participation, and geography determine whether randomized assignment, IV, RDD, DD, matching, or combined methods are plausible.",
            "The chapter recommends favoring methods that require weaker assumptions and fewer data demands when several designs are feasible. The smallest feasible unit of intervention is often preferable because it preserves sample size and design flexibility.",
            "The chapter also links method choice to implementation planning. A design is not selected once; it must be defended through assignment procedures, data collection, stakeholder agreement, and analysis plans.",
        ],
        ["operational rules", "randomized assignment", "instrumental variables", "regression discontinuity design", "difference-in-differences", "matching"],
        ["program rules", "feasible methods", "assumption strength", "data requirements", "unit of intervention", "design comparison"],
        ["Map program rules before proposing a method.", "Prefer designs with weaker identifying assumptions when feasible.", "Choose the intervention unit with power, ethics, and operations in view."],
        "implementation",
    ),
    chapter(
        12,
        "Managing an Impact Evaluation",
        "231-259",
        "chapter-12-managing-an-impact-evaluation.qmd",
        "Part 3: How to Implement an Impact Evaluation > Chapter 12: Managing an Impact Evaluation",
        [
            "chunk:impact-evaluation-in-practice:roles-and-responsibilities-of-the-research-and-policy-teams:c0012",
            "chunk:impact-evaluation-in-practice:how-to-budget-for-an-evaluation:c0002",
        ],
        "Impact evaluation management requires a documented plan that coordinates policy questions, design, sampling, data, analysis, ethics, dissemination, budget, timeline, and team roles.",
        [
            "Chapter 12 treats impact evaluation as project management as well as research design. The evaluation plan is the main coordination artifact for research and policy teams.",
            "The plan should state hypotheses, theory of change, policy questions, indicators, identification strategy, sampling, data sources, data collection, preanalysis commitments, deliverables, ethics, timeline, budget, and roles.",
            "The chapter emphasizes the division of responsibilities. Policy teams protect operational alignment and decision relevance; research teams protect technical credibility, data quality, and analytic transparency.",
            "Budgeting is framed against the cost of ignorance. Evaluation costs should be considered alongside the opportunity cost of scaling, continuing, or ending programs without reliable causal evidence.",
        ],
        ["evaluation plan", "preanalysis plan", "budget", "team roles", "data quality"],
        ["policy and research teams", "evaluation plan", "timeline", "budget", "deliverables", "risk management"],
        ["Create the evaluation plan before implementation changes become irreversible.", "Assign roles explicitly between policy and research teams.", "Treat evaluation cost as part of the policy decision, not an add-on."],
        "implementation",
    ),
    chapter(
        13,
        "The Ethics and Science of Impact Evaluation",
        "261-275",
        "chapter-13-the-ethics-and-science-of-impact-evaluation.qmd",
        "Part 3: How to Implement an Impact Evaluation > Chapter 13: The Ethics and Science of Impact Evaluation",
        [
            "chunk:impact-evaluation-in-practice:part-3:c0002",
            "chunk:impact-evaluation-in-practice:managing-ethical-and-credible-evaluations:c0001",
            "chunk:impact-evaluation-in-practice:ensuring-reliable-and-credible-evaluations-through-open-science:c0001",
            "chunk:impact-evaluation-in-practice:checklist-an-ethical-and-credible-impact-evaluation:c0001",
        ],
        "Ethical impact evaluation protects participants and fair access while open science practices protect the credibility, reliability, and usefulness of results.",
        [
            "Chapter 13 brings ethics and scientific transparency together. Protecting human subjects, avoiding unfair denial of benefits, and preventing disclosure of personal data are all part of credible impact evaluation.",
            "The chapter assigns policy makers responsibility for fair assignment rules and research teams responsibility for transparent methods, institutional review, consent, confidentiality, and data stewardship.",
            "Open science practices such as trial registration, preanalysis plans, transparent reporting, and replication materials reduce publication bias and make results more credible for policy learning.",
            "The chapter's checklist turns these concerns into management questions: who is excluded, whether ethical review is complete, whether consent and data protection are adequate, and whether the analysis is transparent enough to withstand scrutiny.",
        ],
        ["ethics", "human subjects protection", "open science", "preanalysis plan", "data quality"],
        ["ethical management", "fair assignment", "IRB review", "consent and confidentiality", "open science", "credibility checklist"],
        ["Schedule ethical review into the project timeline.", "Review assignment rules for fairness before launch.", "Register analysis plans and protect data confidentiality together."],
        "implementation",
    ),
    chapter(
        14,
        "Disseminating Results and Achieving Policy Impact",
        "277-287",
        "chapter-14-disseminating-results-and-achieving-policy-impact.qmd",
        "Part 3: How to Implement an Impact Evaluation > Chapter 14: Disseminating Results and Achieving Policy Impact",
        [
            "chunk:impact-evaluation-in-practice:ch14-chapter-14-disseminating-results-and-achieving-policy-impact:c0001",
            "chunk:impact-evaluation-in-practice:a-solid-evidence-base-for-policy:c0003",
            "chunk:impact-evaluation-in-practice:tailoring-a-communication-strategy-to-different-audiences:c0003",
            "chunk:impact-evaluation-in-practice:disseminating-results:c0001",
            "chunk:impact-evaluation-in-practice:disseminating-results:c0004",
        ],
        "Policy impact depends on planning dissemination early, asking decision-relevant questions, and tailoring products and timing to the audiences who can use the evidence.",
        [
            "Chapter 14 argues that dissemination begins before results are available. Evaluation questions and stakeholder engagement shape whether the final evidence can answer live policy questions.",
            "The chapter stresses audience tailoring. Technical reports, policy notes, briefs, presentations, videos, blogs, and other products serve different users and should be planned with their decisions and constraints in mind.",
            "Negative or unexpected findings are not communication failures. They may be especially useful when presented with enough context to support redesign, targeting, or theory revision.",
            "A dissemination strategy should identify objectives, audiences, channels, timing, budget, and responsibilities. The aim is not just publication, but credible evidence moving into policy deliberation.",
        ],
        ["dissemination strategy", "policy impact", "evaluation question", "stakeholder engagement", "evidence use"],
        ["policy relevance", "audiences", "communication products", "negative findings", "dissemination planning", "use pathways"],
        ["Plan dissemination while framing the evaluation questions.", "Produce different outputs for technical, policy, and public audiences.", "Treat unexpected results as opportunities for policy learning."],
        "implementation",
    ),
    chapter(
        15,
        "Choosing a Sample",
        "291-319",
        "chapter-15-choosing-a-sample.qmd",
        "Part 4: How to Get Data for an Impact Evaluation > Chapter 15: Choosing a Sample",
        [
            "chunk:impact-evaluation-in-practice:part-4:c0001",
            "chunk:impact-evaluation-in-practice:ch15-chapter-15-choosing-a-sample:c0001",
            "chunk:impact-evaluation-in-practice:deciding-on-the-size-of-a-sample-for-impact-evaluation-power-calculations:c0017",
        ],
        "Sampling decisions determine whether an evaluation can detect meaningful impacts for the population and subgroups that matter to the policy question.",
        [
            "Chapter 15 opens the data sequence by connecting sample design to causal design. The evaluation needs enough units, assigned and measured at the right level, to detect effects of policy relevance.",
            "Power calculations are the chapter's central management tool. They help determine sample size by specifying expected effect sizes, variance, significance, statistical power, clustering, and design features.",
            "The chapter also reminds evaluators that representativeness and assignment units matter. A sample can be statistically large but still poorly aligned with the target population or underpowered for subgroups.",
            "Sampling is therefore not merely a survey issue. It must be coordinated with rollout, treatment arms, attrition risk, data collection timing, and the policy decisions the evaluation is expected to inform.",
        ],
        ["sample", "power calculation", "minimum detectable effect", "cluster", "attrition"],
        ["sampling frame", "sample size", "power calculations", "clusters and subgroups", "implementation constraints", "attrition allowance"],
        ["Run power calculations before confirming treatment arms.", "Align the sampling unit with the assignment and analysis unit.", "Build attrition risk into sample planning."],
        "data",
    ),
    chapter(
        16,
        "Finding Adequate Sources of Data",
        "321-347",
        "chapter-16-finding-adequate-sources-of-data.qmd",
        "Part 4: How to Get Data for an Impact Evaluation > Chapter 16: Finding Adequate Sources of Data",
        [
            "chunk:impact-evaluation-in-practice:kinds-of-data-that-are-needed:c0001",
            "chunk:impact-evaluation-in-practice:kinds-of-data-that-are-needed:c0002",
            "chunk:impact-evaluation-in-practice:collecting-new-survey-data:c0007",
            "chunk:impact-evaluation-in-practice:collecting-new-survey-data:c0023",
            "chunk:impact-evaluation-in-practice:collecting-new-survey-data:c0030",
        ],
        "Impact evaluations need data sources that measure outcomes, intermediate outcomes, implementation, and context with enough quality, timing, and coverage to support causal claims.",
        [
            "Chapter 16 compares existing data and new survey data. Administrative, monitoring, and registry data can be valuable, but only if they cover the required indicators, units, and time periods with sufficient quality.",
            "The chapter ties data needs to the results chain. Evaluators should measure final outcomes, intermediate outcomes, implementation quality, program exposure, and relevant covariates rather than collecting generic survey batteries.",
            "When new survey data are needed, instrument development, piloting, field staff, fieldwork management, and quality control become part of the evaluation design.",
            "Data processing and storage are not clerical afterthoughts. Validation, confidentiality, cleaning, documentation, and attrition control protect the credibility and reusability of the evaluation evidence.",
        ],
        ["administrative data", "survey data", "results chain", "data quality", "fieldwork"],
        ["data types", "indicators across the results chain", "existing data", "new surveys", "piloting and fieldwork", "processing and storage"],
        ["Inventory existing data before commissioning new collection.", "Derive survey modules from the results chain and analysis plan.", "Budget quality control, validation, and storage as core evaluation tasks."],
        "data",
    ),
]


def wrap(text: str) -> str:
    return "\n".join(textwrap.wrap(text, width=100, break_long_words=False, replace_whitespace=False))


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


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


def chapter_link(chapter_item: dict) -> str:
    return f"[Chapter {chapter_item['number']}: {chapter_item['title']}]({chapter_item['file']})"


def concept_lines(concepts: list[str]) -> list[str]:
    return [
        f"- **{concept}**: {CONCEPT_GLOSSES.get(concept, 'Chapter-specific term; check the cited records before treating it as a portable evaluation concept.')}"
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
        lines.append(f'  Mechanism{idx}["Design element: {item}"]')
    for idx, implication in enumerate(implications, start=1):
        safe = implication.replace('"', "'")
        lines.append(f'  Implication{idx}["Practice implication: {safe}"]')
    lines.append('  Question["Open question: What has to be checked in the source records?"]')
    lines.extend(["", "  Problem --> Central", "  Central --> Question"])
    for idx in range(1, len(concepts) + 1):
        lines.append(f"  Central --> Concept{idx}")
    for idx in range(1, len(structures) + 1):
        concept_idx = min(idx, len(concepts))
        lines.append(f"  Concept{concept_idx} --> Mechanism{idx}")
    for idx in range(1, len(implications) + 1):
        mechanism_idx = min(idx, len(structures))
        lines.append(f"  Mechanism{mechanism_idx} --> Implication{idx}")
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
    ]
    lines.extend(["\n".join(textwrap.wrap(paragraph, width=100, break_long_words=False)) + "\n" for paragraph in chapter_item["summary"]])
    lines.extend(
        [
            wrap(
                f"For close reading, track how the chapter uses {', '.join(chapter_item['concepts'][:4])} while moving through {', '.join(chapter_item['structure'][:3])}. The notes identify the design problem the chapter helps solve and what should be checked against the saved evidence records before relying on the summary in applied work."
            ),
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
    lines.extend(
        [
            "",
            "## Concept Map",
            "",
            "::: {.concept-map}",
            "```{mermaid}",
            render_mermaid(chapter_item),
            "```",
            ":::",
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
    lines.extend(["", "## Study Prompts", ""])
    lines.extend(
        [
            f"- What does Chapter {chapter_item['number']} imply for selecting or defending an impact evaluation design?",
            f"- Which assumption in this chapter would be hardest to defend in a live policy setting?",
            "- Which source record should be reopened before using this note in applied work?",
        ]
    )
    lines.extend(["", "## Source Records", "", source_chunks(chapter_item["evidence_ids"]), "", "## References", ""])
    return "\n".join(lines)


def render_index() -> str:
    evidence = all_evidence_ids()
    by_group: dict[str, list[dict]] = {}
    for chapter_item in CHAPTERS:
        by_group.setdefault(chapter_item["group"], []).append(chapter_item)
    group_names = {
        "introduction": "Part 1: Introduction to Impact Evaluation",
        "methods": "Part 2: How to Evaluate",
        "implementation": "Part 3: How to Implement an Impact Evaluation",
        "data": "Part 4: How to Get Data for an Impact Evaluation",
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
        "Impact evaluation turns policy questions into causal designs by specifying the theory of change, constructing credible counterfactuals, managing implementation and ethics, and collecting data that can support defensible impact estimates.",
        "",
        "## Chapter Notes",
        "",
    ]
    for group, chapters in by_group.items():
        lines.extend(["", f"### {group_names[group]}", ""])
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
        "- **Start with policy fit**: Chapters 1-2 clarify why and how to prepare for impact evaluation.",
        "- **Build the causal design**: Chapters 3-10 cover counterfactual logic, five main methods, implementation threats, and multifaceted programs.",
        "- **Implement responsibly**: Chapters 11-14 connect method choice to management, ethics, transparency, and dissemination.",
        "- **Secure data quality**: Chapters 15-16 cover sampling, power, data sources, fieldwork, and storage.",
        "",
        "## Chapters",
        "",
        "| Chapter | Source Pages | Main Design Question | Link |",
        "|---|---:|---|---|",
    ]
    for chapter_item in CHAPTERS:
        lines.append(
            f"| {chapter_item['number']}. {chapter_item['title']} | {chapter_item['pages']} | {chapter_item['core']} | [{chapter_item['file']}]({chapter_item['file']}) |"
        )
    lines.extend(["", "## Legacy Extracts", ""])
    lines.extend(f"- [{title}]({file})" for title, file in LEGACY_EXTRACTS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_concepts() -> str:
    evidence = all_evidence_ids()
    used = []
    for chapter_item in CHAPTERS:
        for concept in chapter_item["concepts"]:
            if concept not in used:
                used.append(concept)
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
        "### Causal Design",
        "",
    ]
    causal = ["impact evaluation", "causal inference", "counterfactual", "comparison group", "internal validity", "external validity"]
    lines.extend(concept_lines([item for item in causal if item in used or item in CONCEPT_GLOSSES]))
    lines.extend(["", "### Methods", ""])
    methods = ["randomized assignment", "instrumental variables", "regression discontinuity design", "difference-in-differences", "matching", "multifaceted program"]
    lines.extend(concept_lines(methods))
    lines.extend(["", "### Implementation and Ethics", ""])
    implementation = ["operational rules", "implementation fidelity", "evaluation plan", "ethics", "human subjects protection", "open science", "dissemination strategy", "policy impact"]
    lines.extend(concept_lines([item for item in implementation if item in CONCEPT_GLOSSES]))
    lines.extend(["", "### Data", ""])
    data = ["results chain", "SMART indicators", "sample", "power calculation", "administrative data", "survey data", "data quality", "attrition"]
    lines.extend(concept_lines([item for item in data if item in CONCEPT_GLOSSES]))
    lines.extend(["", "## Chapter Links", ""])
    lines.extend(f"- {chapter_link(chapter_item)}" for chapter_item in CHAPTERS)
    lines.extend(["", "## Source Records", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = all_evidence_ids()
    implications = [
        "Begin with the policy decision and the theory of change, then choose the identification strategy that the program's operational rules can actually support.",
        "Treat the counterfactual as the central design problem; every method choice should explain how the comparison group approximates untreated outcomes for the treatment group.",
        "Use randomized assignment when it is fair and operationally feasible, but do not force it when rollout, eligibility, or ethics make another design more defensible.",
        "For quasi-experimental designs, state the identifying assumption in plain language and gather diagnostics that can challenge it.",
        "Plan for imperfect compliance, spillovers, attrition, and multiple treatment arms before baseline rather than treating them as analytic surprises.",
        "Keep evaluation management artifacts current: design memo, sampling plan, data plan, preanalysis plan, ethics review, dissemination plan, budget, and role assignments.",
        "Design samples around minimum detectable effects and policy-relevant subgroups, not only around available budget.",
        "Use existing administrative or monitoring data only after checking coverage, timing, indicators, and quality against the results chain.",
        "Build fieldwork quality control, validation, confidentiality, documentation, and storage into the evaluation budget.",
        "Plan communication products for different audiences early enough that evaluation results can enter real decision cycles.",
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


def patch_overview_copy() -> None:
    replacements = {
        "chapter-level Rossi/Lipsey and Chen notes, step-level Patton/U-FE notes, and generated notes for the wider collection.": "chapter-level Rossi/Lipsey, Chen, and Impact Evaluation in Practice notes, step-level Patton/U-FE notes, and generated notes for the wider collection.",
        "chapter-level Rossi/Lipsey and Chen notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.": "chapter-level Rossi/Lipsey, Chen, and Impact Evaluation in Practice notes, step-level Patton/U-FE notes, and generated notes for the other ready evaluation texts.",
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
