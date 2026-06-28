#!/usr/bin/env python3
"""Generate chapter-level Rossi/Lipsey/Freeman study notes."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ID = "evaluation-systematic-approach"
SLUG = BOOK_ID
TITLE = "Evaluation: A Systematic Approach"
FULL_TITLE = TITLE
AUTHORS = "Peter H. Rossi, Mark W. Lipsey, and Howard E. Freeman"
CITATION = "rossi_lipsey_freeman_2004_evaluation_systematic_approach"
COLLECTION_ID = "evaluation-texts"
SOURCE_STATUS = "needs_review"
RAG_STATUS = "ready"
YEAR = "2004"
PUBLISHER = "SAGE Publications"
GENERATED_AT = "2026-06-27"


CONCEPT_GLOSSES = {
    "accountability": "Use of evaluation evidence to support judgments about program performance, resource use, and continuation.",
    "bias": "A systematic distortion in measurement, coverage, selection, comparison, or interpretation that can misstate program performance or effects.",
    "cost-benefit analysis": "Efficiency analysis that monetizes costs and benefits so their net relationship can be compared.",
    "cost-effectiveness analysis": "Efficiency analysis that compares costs with nonmonetized outcomes or effects.",
    "accounting perspective": "The standpoint from which costs and benefits are counted, such as program, participant, funder, or society.",
    "administrative standards": "Expected performance levels or requirements set by administrators, law, ethics, professional norms, or program theory.",
    "attrition": "Loss of participants or observations from measurement, which can weaken comparison and bias impact estimates.",
    "conceptual use": "Use of evaluation findings to reshape understanding, framing, debate, or assumptions rather than to trigger one immediate decision.",
    "coverage": "The extent to which a program reaches its intended target population.",
    "control group": "A comparison group used to estimate what would have happened to program targets without the intervention.",
    "counterfactual": "An estimate of the outcome status that would have occurred if the program had not been present.",
    "discounting": "Converting future costs or benefits into present value for efficiency analysis.",
    "dissemination": "Planned communication of findings to audiences who need evidence for action, debate, or accountability.",
    "effect size": "A standardized expression of the magnitude of a program effect.",
    "efficiency assessment": "Evaluation of the relationship between program costs and program benefits, effects, or outcomes.",
    "evaluation purpose": "The main reason for the evaluation, such as improvement, accountability, knowledge generation, or political positioning.",
    "evaluation question": "A question about program performance that guides the evaluation design and requires criteria for judgment.",
    "evaluation standards": "Criteria, guidelines, or ethical expectations used to judge evaluation quality and conduct.",
    "evaluation use": "Application of evaluation processes or findings to decisions, understanding, debate, accountability, or program improvement.",
    "evaluability assessment": "Joint investigation of whether a program is sufficiently clear, plausible, and ready for useful evaluation.",
    "impact assessment": "Evaluation that estimates whether and how much a program changed outcomes relative to what would have happened without it.",
    "impact theory": "A causal account of how program activities are expected to produce intended social benefits.",
    "implementation failure": "A situation where a program does not deliver the intended services, enough service, the right service, or consistent service.",
    "incidence": "The number of new cases of a condition or problem arising in a defined population during a defined period.",
    "instrumental use": "Direct use of evaluation findings in a specific program, policy, funding, or management decision.",
    "matching": "Constructing comparison groups by pairing or balancing units on variables expected to affect outcomes or selection.",
    "mediator variable": "A variable that helps explain how or why a program produces an effect.",
    "meta-analysis": "Quantitative synthesis of effect estimates across studies to inform one evaluation or the wider evidence base.",
    "moderator variable": "A variable that identifies for whom or under what conditions effects are larger, smaller, or different.",
    "needs assessment": "Systematic diagnosis of the social problem, target population, and service needs a program is intended to address.",
    "opportunity cost": "The value of the best alternative use of resources committed to a program or evaluation.",
    "organizational plan": "The program theory component describing the functions, activities, staffing, resources, and support needed for delivery.",
    "outcome change": "Difference in outcome level over time, which may or may not be attributable to the program.",
    "outcome level": "The observed status of an outcome at a point in time.",
    "outcome monitoring": "Routine tracking of outcome indicators, with care not to confuse outcome status or change with program impact.",
    "performance criteria": "The standards or dimensions used to judge whether observed program performance is good enough.",
    "practical significance": "The real-world importance of an estimated effect, beyond statistical detectability.",
    "prevalence": "The total number or rate of existing cases of a condition or problem in a defined population.",
    "process evaluation": "Evaluation of whether and how a program is implemented, delivered, accessed, and operated.",
    "process theory": "The combined service utilization and organizational plan describing how the program is expected to operate.",
    "program effect": "The change attributable to the program, distinct from outcome status or change that would have occurred anyway.",
    "program evaluation": "Systematic use of social research methods to judge social interventions and inform action.",
    "program monitoring": "Repeated measurement of program process, performance, or outcomes to support evaluation, accountability, or management.",
    "program outcome": "A social, behavioral, organizational, or participant condition the program is expected to change.",
    "program theory": "The assumptions and expectations connecting needs, program action, implementation, and intended outcomes.",
    "persuasive use": "Use of evaluation evidence to support, challenge, or reframe positions in policy and program debate.",
    "political context": "The policy, organizational, funding, stakeholder, and timing conditions that shape evaluation conduct and use.",
    "quasi-experimental design": "A nonrandomized impact design that uses constructed comparisons, timing, or statistical controls to estimate effects.",
    "random assignment": "Allocation by chance to program and comparison conditions to support unbiased impact estimates.",
    "randomized field experiment": "A real-world impact design comparing randomly assigned program and control groups.",
    "regression discontinuity": "A quasi-experimental design using a cutoff rule on an assignment variable to estimate program effects near the threshold.",
    "reliability": "The consistency or dependability of a measure, data collection procedure, or classification.",
    "selection bias": "Bias caused when program and comparison groups differ in ways that affect outcomes apart from program participation.",
    "service needs": "The kinds, amount, timing, and accessibility of services required by a target population given the diagnosed problem.",
    "service utilization plan": "The program theory component describing how intended participants are expected to enter, engage with, and complete services.",
    "social program": "An organized intervention intended to improve social conditions or ameliorate a social problem.",
    "social problem": "The condition or need a program is intended to ameliorate, defined precisely enough for diagnosis and action.",
    "social research methods": "Systematic observation, measurement, sampling, research design, and analysis used to describe program performance credibly.",
    "stakeholder": "A person, group, or organization with a significant interest in the program, evaluation, or findings.",
    "statistical controls": "Analytic adjustments intended to reduce nonrandom differences between program and comparison groups.",
    "statistical significance": "A judgment about whether observed differences are unlikely to be due to sampling error under a specified model.",
    "statistical power": "The ability of an impact assessment to detect an effect of a given size if that effect exists.",
    "target population": "The people, units, or conditions the program intends to affect directly or indirectly.",
    "time series": "A design or monitoring approach using repeated observations over time to examine trends and possible program-related change.",
    "validity": "The degree to which a measure, comparison, or interpretation supports the claim being made.",
}


CHAPTERS = [
    {
        "number": 1,
        "title": "An Overview of Program Evaluation",
        "pages": "12-38",
        "file": "chapter-01-an-overview-of-program-evaluation.qmd",
        "section_path": "Chapter 1: An Overview of Program Evaluation",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch01-chapter-1-an-overview-of-program-evaluation:c0027",
            "chunk:evaluation-systematic-approach:ch01-chapter-1-an-overview-of-program-evaluation:c0032",
            "chunk:evaluation-systematic-approach:ch01-chapter-1-an-overview-of-program-evaluation:c0034",
        ],
        "core": "Program evaluation adapts social research methods to judge social interventions in ways that fit political and organizational context and inform action.",
        "summary": [
            "The opening chapter defines program evaluation as systematic inquiry into social interventions. It treats evaluation as both empirical and practical: evaluators must describe program performance credibly, compare that performance with relevant criteria, and produce information that can inform social action.",
            "The chapter introduces the book's central domains of evaluation: need, program design and theory, implementation and service delivery, impact or outcomes, and efficiency. These domains become the structure for later chapters and keep evaluation from collapsing into one preferred method.",
            "Rossi, Lipsey, and Freeman also stress context. Programs are created, funded, defended, revised, and criticized in political and organizational settings. Evaluation findings compete with other interests, so the evaluator has to design for technical credibility and realistic use.",
            "The chapter positions evaluation as a response to scarce resources, accountability demands, and continuing claims that social programs can improve human conditions. It warns that evaluators need methodological skill, but also judgment about stakeholders, politics, purposes, and program circumstances.",
        ],
        "concepts": ["program evaluation", "social program", "social research methods", "stakeholder", "accountability", "evaluation use"],
        "structure": ["history and contemporary demand", "definition of program evaluation", "five domains of program performance", "political and organizational context", "evaluation practice and roles"],
        "implications": ["Define the program and performance domain before selecting methods.", "Treat political context as a design condition, not an afterthought.", "Ask how findings will inform action as well as whether they are technically sound."],
    },
    {
        "number": 2,
        "title": "Tailoring Evaluations",
        "pages": "38-67",
        "file": "chapter-02-tailoring-evaluations.qmd",
        "section_path": "Chapter 2: Tailoring Evaluations",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch02-chapter-2-tailoring-evaluations:c0002",
            "chunk:evaluation-systematic-approach:ch02-chapter-2-tailoring-evaluations:c0044",
            "chunk:evaluation-systematic-approach:ch02-chapter-2-tailoring-evaluations:c0060",
        ],
        "core": "Evaluation design is a fit problem: purpose, program circumstances, resources, stakeholder relationship, questions, and methods must be tailored together.",
        "summary": [
            "Chapter 2 rejects a one-size-fits-all evaluation model. A useful evaluation plan depends on why the evaluation is being commissioned, how the program is organized, what resources are available, and what kind of relationship the evaluator will have with sponsors and stakeholders.",
            "The chapter distinguishes purposes such as program improvement, accountability, knowledge generation, and hidden agendas. These purposes affect what questions should be asked, how much independence is needed, and what communication practices will support use.",
            "It also introduces the major question types that organize the rest of the book: needs assessment, program theory assessment, process evaluation, impact assessment, and efficiency assessment. The evaluator's task is to match questions to methods and program maturity.",
            "The stakeholder relationship is treated as a design choice. Independent, collaborative, participatory, and capacity-building orientations each change the evaluator's role, the flow of information, and the likely use and credibility of findings.",
        ],
        "concepts": ["evaluation purpose", "evaluation question", "stakeholder", "needs assessment", "impact assessment", "efficiency assessment"],
        "structure": ["purposes of evaluation", "program structure and circumstances", "resources", "evaluator-stakeholder relationships", "question types and methods"],
        "implications": ["Classify the evaluation's main purpose before designing the work.", "Check whether program maturity supports the requested question type.", "Make the stakeholder relationship explicit in the evaluation plan."],
    },
    {
        "number": 3,
        "title": "Identifying Issues and Formulating Questions",
        "pages": "67-93",
        "file": "chapter-03-identifying-issues-and-formulating-questions.qmd",
        "section_path": "Chapter 3: Identifying Issues and Formulating Questions",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch03-chapter-3-identifying-issues-and-formulating-questions:c0054",
            "chunk:evaluation-systematic-approach:ch03-chapter-3-identifying-issues-and-formulating-questions:c0055",
            "chunk:evaluation-systematic-approach:ch03-chapter-3-identifying-issues-and-formulating-questions:c0056",
        ],
        "core": "Evaluation questions turn stakeholder concerns and program assumptions into answerable, prioritized inquiries about performance and value.",
        "summary": [
            "Chapter 3 makes question formulation the control point for evaluation design. Questions focus the evaluation on the areas of program performance that matter and determine what evidence, criteria, and methods will be needed.",
            "Good evaluation questions are not just interesting topics. They must be reasonable, appropriate, answerable, and tied to observable dimensions of program performance. They also need criteria or standards so findings can support judgment rather than description alone.",
            "The chapter treats question development as both negotiated and analytical. Stakeholders help identify concerns and uses, but evaluators must also inspect program documents, assumptions, and theory to surface issues that stakeholders may miss.",
            "Prioritization is necessary because resources rarely allow every plausible question to be answered. The chapter also broadens use beyond immediate decisions: questions may support conceptual or persuasive use by shaping how a program and its problem are understood.",
        ],
        "concepts": ["evaluation question", "performance criteria", "stakeholder", "instrumental use", "conceptual use", "persuasive use"],
        "structure": ["sources of evaluation issues", "formulating answerable questions", "performance criteria", "question hierarchy", "collating and prioritizing questions"],
        "implications": ["Turn broad concerns into observable and answerable questions.", "Prioritize questions by purpose, use, and feasibility.", "Document criteria so interpretation is not improvised after results arrive."],
    },
    {
        "number": 4,
        "title": "Assessing the Need for a Program",
        "pages": "93-120",
        "file": "chapter-04-assessing-the-need-for-a-program.qmd",
        "section_path": "Chapter 4: Assessing the Need for a Program",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch04-chapter-4-assessing-the-need-for-a-program:c0001",
            "chunk:evaluation-systematic-approach:ch04-chapter-4-assessing-the-need-for-a-program:c0002",
            "chunk:evaluation-systematic-approach:ch04-chapter-4-assessing-the-need-for-a-program:c0052",
        ],
        "core": "Needs assessment tests whether a social problem exists, who is affected, what services are needed, and whether program action fits that diagnosis.",
        "summary": [
            "Chapter 4 begins the substantive evaluation sequence by asking whether the program addresses a real and significant social need. Without a defensible diagnosis of need, later assessments of theory, process, impact, and efficiency rest on weak foundations.",
            "The chapter describes needs assessment as systematic problem diagnosis. Evaluators define the problem, estimate its extent, identify trends, forecast needs, and use data sources such as records, indicators, surveys, censuses, key informants, and qualitative inquiry.",
            "Target specification is central. Evaluators have to distinguish direct and indirect targets, set target boundaries, describe target populations, and separate risk, need, and demand. These distinctions determine whether services are aligned with the problem.",
            "The chapter also emphasizes reproducibility and precision. Stakeholders may define problems differently, so the evaluator's role is to make the diagnosis careful, explicit, objective enough for deliberation, and useful for program design.",
        ],
        "concepts": ["needs assessment", "social problem", "target population", "incidence", "prevalence", "service needs"],
        "structure": ["defining the problem", "estimating extent and trends", "forecasting needs", "identifying targets", "describing service needs"],
        "implications": ["Do not assume the program's stated problem definition is adequate.", "Separate problem prevalence from demand for services.", "Use needs evidence to judge whether the intervention design is plausible."],
    },
    {
        "number": 5,
        "title": "Expressing and Assessing Program Theory",
        "pages": "120-150",
        "file": "chapter-05-expressing-and-assessing-program-theory.qmd",
        "section_path": "Chapter 5: Expressing and Assessing Program Theory",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch05-chapter-5-expressing-and-assessing-program-theory:c0001",
            "chunk:evaluation-systematic-approach:ch05-chapter-5-expressing-and-assessing-program-theory:c0059",
            "chunk:evaluation-systematic-approach:ch05-chapter-5-expressing-and-assessing-program-theory:c0061",
        ],
        "core": "Program theory is itself evaluable: evaluators should articulate and assess the logic connecting program action, use, organization, and intended change.",
        "summary": [
            "Chapter 5 shifts from diagnosing need to assessing the program's theory. A program may be well intentioned yet unlikely to succeed if its assumptions about causes, services, users, organizational capacity, or implementation are vague or implausible.",
            "The chapter distinguishes impact theory from process theory. Impact theory explains how program action should cause social benefits. Process theory combines the service utilization plan and organizational plan that specify how the program is supposed to operate.",
            "When theory is implicit, evaluators extract and articulate it from documents, interviews, observations, and stakeholder accounts. The result should be concrete enough to show goals, functions, activities, assumptions, sequences, and expected outcomes.",
            "Assessment compares the theory with social needs, logic and plausibility, research and practice evidence, and preliminary observation. If theory is weak, the evaluation may legitimately recommend redesign before impact assessment proceeds.",
        ],
        "concepts": ["program theory", "impact theory", "process theory", "service utilization plan", "organizational plan", "evaluability assessment"],
        "structure": ["evaluability perspective", "describing theory", "eliciting implicit theory", "corroborating theory", "assessing theory"],
        "implications": ["Articulate the program theory before estimating impact.", "Treat implausible theory as an evaluation finding in its own right.", "Use theory assessment to decide whether implementation or impact evaluation is premature."],
    },
    {
        "number": 6,
        "title": "Assessing and Monitoring Program Process",
        "pages": "150-177",
        "file": "chapter-06-assessing-and-monitoring-program-process.qmd",
        "section_path": "Chapter 6: Assessing and Monitoring Program Process",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch06-chapter-6-assessing-and-monitoring-program-process:c0002",
            "chunk:evaluation-systematic-approach:ch06-chapter-6-assessing-and-monitoring-program-process:c0055",
            "chunk:evaluation-systematic-approach:ch06-chapter-6-assessing-and-monitoring-program-process:c0056",
        ],
        "core": "Process evaluation asks whether the program is actually being delivered as intended, to whom, with what coverage, consistency, and organizational support.",
        "summary": [
            "Chapter 6 turns program process theory into evidence about implementation. A program cannot produce expected outcomes if it fails to deliver the intended services, reaches the wrong participants, or operates inconsistently across sites.",
            "The chapter distinguishes process evaluation from process monitoring. Process evaluation may be a stand-alone study or part of an impact evaluation. Monitoring is repeated measurement over time, often supported by management information systems.",
            "Criteria for judging process can come from program theory, administrative standards, legal and ethical requirements, professional expectations, and after-the-fact judgment. This makes process evaluation both descriptive and evaluative.",
            "The chapter's major domains are service utilization and organizational functions. Evaluators assess coverage, accessibility, bias, intensity, participant response, delivery systems, support functions, and whether actual operation conforms to design.",
        ],
        "concepts": ["process evaluation", "program monitoring", "coverage", "bias", "implementation failure", "administrative standards"],
        "structure": ["process theory and criteria", "process evaluation", "process monitoring", "service utilization", "organizational functions", "analysis of monitoring data"],
        "implications": ["Check implementation before interpreting weak outcomes as program failure.", "Track coverage and bias, not only service counts.", "Use process findings to decide whether impact assessment is appropriate."],
    },
    {
        "number": 7,
        "title": "Measuring and Monitoring Program Outcomes",
        "pages": "177-202",
        "file": "chapter-07-measuring-and-monitoring-program-outcomes.qmd",
        "section_path": "Chapter 7: Measuring and Monitoring Program Outcomes",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch07-chapter-7-measuring-and-monitoring-program-outcomes:c0001",
            "chunk:evaluation-systematic-approach:ch07-chapter-7-measuring-and-monitoring-program-outcomes:c0035",
            "chunk:evaluation-systematic-approach:ch07-chapter-7-measuring-and-monitoring-program-outcomes:c0049",
        ],
        "core": "Outcome evaluation requires identifying relevant outcomes, measuring them well, and interpreting outcome data without confusing outcome change with program effect.",
        "summary": [
            "Chapter 7 explains outcomes as the changed conditions a program is intended to produce. Outcome measurement is essential because programs ultimately aim to improve social conditions, not merely operate smoothly.",
            "The chapter separates outcome level, outcome change, and net effect. A target group can improve, decline, or remain stable for reasons unrelated to the program, so outcome monitoring alone cannot establish impact.",
            "Relevant outcomes are identified through stakeholder perspectives, program impact theory, prior research, and attention to unintended outcomes. Measures need reliability, validity, sensitivity, and enough fit to the expected magnitude and timing of change.",
            "Outcome monitoring can support management and accountability, but it carries pitfalls. Indicators must be practical and informative, and interpretation must acknowledge external influences, measurement limits, and the need for stronger designs when causal claims are required.",
        ],
        "concepts": ["program outcome", "outcome level", "outcome change", "program effect", "reliability", "validity", "outcome monitoring"],
        "structure": ["program outcomes", "identifying relevant outcomes", "measurement procedures", "reliability and validity", "monitoring indicators", "interpreting outcome data"],
        "implications": ["Separate outcome status from net program effect in reports.", "Select measures that are sensitive enough for expected changes.", "Use multiple outcome measures when the program theory is multidimensional."],
    },
    {
        "number": 8,
        "title": "Assessing Program Impact: Randomized Field Experiments",
        "pages": "202-229",
        "file": "chapter-08-assessing-program-impact-randomized-field-experiments.qmd",
        "section_path": "Chapter 8: Assessing Program Impact: Randomized Field Experiments",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch08-chapter-8-assessing-program-impact-randomized-field-experiments:c0001",
            "chunk:evaluation-systematic-approach:ch08-chapter-8-assessing-program-impact-randomized-field-experiments:c0002",
            "chunk:evaluation-systematic-approach:ch08-chapter-8-assessing-program-impact-randomized-field-experiments:c0052",
        ],
        "core": "Randomized field experiments provide the strongest basis for estimating program impact, but only when program, ethical, practical, and implementation conditions support them.",
        "summary": [
            "Chapter 8 begins impact assessment by framing effects as differences between observed outcomes and credible estimates of what would have happened without the program. Random assignment is the strongest way to create comparable program and control groups.",
            "The chapter explains why randomized field experiments matter even when they cannot be used. Their logic underlies impact assessment generally: comparison, assignment, outcome measurement, and protection against biased estimates.",
            "The authors also set limits. Randomized designs may be inappropriate for early-stage programs, ethically difficult, costly, politically resisted, or compromised when experimental delivery differs from ordinary program delivery.",
            "A good randomized impact assessment therefore requires more than assignment. Evaluators must attend to units of analysis, data collection before and after intervention, attrition, intervention integrity, analysis of complex designs, and the practical context in which findings will be used.",
        ],
        "concepts": ["impact assessment", "randomized field experiment", "random assignment", "control group", "counterfactual", "attrition"],
        "structure": ["appropriateness of impact assessment", "key concepts", "randomization logic", "field experiment prerequisites", "data collection and analysis", "limitations"],
        "implications": ["Use randomized designs when stakes are high and conditions permit.", "Protect implementation integrity and outcome measurement after assignment.", "Explain ethical and practical constraints when a randomized design is not feasible."],
    },
    {
        "number": 9,
        "title": "Assessing Program Impact: Alternative Designs",
        "pages": "229-258",
        "file": "chapter-09-assessing-program-impact-alternative-designs.qmd",
        "section_path": "Chapter 9: Assessing Program Impact: Alternative Designs",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch09-chapter-9-assessing-program-impact-alternative-designs:c0001",
            "chunk:evaluation-systematic-approach:ch09-chapter-9-assessing-program-impact-alternative-designs:c0017",
            "chunk:evaluation-systematic-approach:ch09-chapter-9-assessing-program-impact-alternative-designs:c0061",
        ],
        "core": "When random assignment is infeasible, alternative impact designs can be useful only if evaluators confront selection bias and other validity threats directly.",
        "summary": [
            "Chapter 9 covers nonrandomized impact designs. The authors are clear that these alternatives do not provide the same confidence as well-implemented randomized experiments, but they are often necessary in real program settings.",
            "The chapter begins with bias. Selection bias, secular trends, interfering events, maturation, and other influences can exaggerate or obscure program effects. The evaluator must identify plausible sources of bias before choosing a design or reporting findings.",
            "Quasi-experimental strategies include constructing control groups by matching, adjusting groups statistically, modeling outcomes and selection, and using regression-discontinuity designs. Reflexive controls include simple pre-post studies and time-series designs.",
            "The chapter's practical stance is conditional. Nonrandomized designs may be justified when the need for impact evidence is great and randomization is not feasible, but reports must communicate limitations, use strong controls where possible, and avoid definitive claims unsupported by design.",
        ],
        "concepts": ["quasi-experimental design", "selection bias", "matching", "statistical controls", "regression discontinuity", "time series"],
        "structure": ["bias in effect estimates", "selection and nonrandomized designs", "matching", "statistical adjustment", "regression discontinuity", "reflexive controls"],
        "implications": ["Name likely biases before choosing an alternative design.", "Use theory and prior research to select matching or control variables.", "Report nonrandomized estimates with explicit uncertainty and limitations."],
    },
    {
        "number": 10,
        "title": "Detecting, Interpreting, and Analyzing Program Effects",
        "pages": "258-283",
        "file": "chapter-10-detecting-interpreting-and-analyzing-program-effects.qmd",
        "section_path": "Chapter 10: Detecting, Interpreting, and Analyzing Program Effects",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch10-chapter-10-detecting-interpreting-and-analyzing-program-effects:c0001",
            "chunk:evaluation-systematic-approach:ch10-chapter-10-detecting-interpreting-and-analyzing-program-effects:c0002",
            "chunk:evaluation-systematic-approach:ch10-chapter-10-detecting-interpreting-and-analyzing-program-effects:c0052",
        ],
        "core": "Impact findings require interpretation of magnitude, uncertainty, practical significance, variation, and cumulative evidence, not only a design-based estimate.",
        "summary": [
            "Chapter 10 follows the design chapters by asking how effects are detected and interpreted. Even strong measurement and design do not automatically make program effects clear, important, or credible for decision purposes.",
            "The chapter covers effect magnitude, statistical significance, Type I and Type II errors, and statistical power. These topics matter because evaluations can miss meaningful effects or overstate noisy findings if analysis is poorly matched to expected effects.",
            "Practical significance is a separate judgment. A statistically detectable effect may be too small to justify action, while a substantively important effect may require careful interpretation when sample size or design limits precision.",
            "The chapter also examines variation in program effects through moderator and mediator analysis and links individual studies to meta-analysis. This connects a single impact assessment to broader knowledge about what works, for whom, and under what conditions.",
        ],
        "concepts": ["effect size", "statistical significance", "statistical power", "practical significance", "moderator variable", "mediator variable", "meta-analysis"],
        "structure": ["magnitude of effects", "detecting effects", "practical significance", "variation in effects", "meta-analysis"],
        "implications": ["Plan sample size and power around decision-relevant effects.", "Report practical significance alongside statistical tests.", "Analyze variation when program theory predicts differential effects."],
    },
    {
        "number": 11,
        "title": "Measuring Efficiency",
        "pages": "283-315",
        "file": "chapter-11-measuring-efficiency.qmd",
        "section_path": "Chapter 11: Measuring Efficiency",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch11-chapter-11-measuring-efficiency:c0001",
            "chunk:evaluation-systematic-approach:ch11-chapter-11-measuring-efficiency:c0049",
            "chunk:evaluation-systematic-approach:ch11-chapter-11-measuring-efficiency:c0060",
        ],
        "core": "Efficiency assessment relates program costs to benefits or effects so resource decisions can consider value as well as implementation and impact.",
        "summary": [
            "Chapter 11 adds the cost dimension to evaluation. A program may be implemented well and produce outcomes, but decision makers still need to know whether benefits justify costs or whether another intervention could produce similar effects more efficiently.",
            "The chapter distinguishes cost-benefit and cost-effectiveness analysis. Cost-benefit analysis monetizes both costs and benefits where possible, while cost-effectiveness analysis compares costs with outcome units that may remain nonmonetary.",
            "Efficiency analysis depends on perspective and assumptions. Evaluators have to assemble cost data, choose accounting perspectives, consider opportunity costs, shadow prices, secondary effects, distributional issues, and discounting.",
            "The authors present the technical material as something every evaluator should understand conceptually, even if specialist expertise is needed for full analysis. Efficiency questions often shape decisions about expansion, continuation, termination, and allocation across alternatives.",
        ],
        "concepts": ["efficiency assessment", "cost-benefit analysis", "cost-effectiveness analysis", "opportunity cost", "discounting", "accounting perspective"],
        "structure": ["key concepts", "ex ante and ex post analysis", "cost-benefit analysis", "measuring costs and benefits", "comparing costs and benefits", "cost-effectiveness analysis"],
        "implications": ["Plan cost data collection before impact findings arrive.", "State the accounting perspective behind efficiency claims.", "Avoid treating positive impact as sufficient evidence for resource allocation."],
    },
    {
        "number": 12,
        "title": "The Social Context of Evaluation",
        "pages": "315-358",
        "file": "chapter-12-the-social-context-of-evaluation.qmd",
        "section_path": "Chapter 12: The Social Context of Evaluation",
        "evidence_ids": [
            "chunk:evaluation-systematic-approach:ch12-chapter-12-the-social-context-of-evaluation:c0001",
            "chunk:evaluation-systematic-approach:ch12-chapter-12-the-social-context-of-evaluation:c0090",
            "chunk:evaluation-systematic-approach:ch12-chapter-12-the-social-context-of-evaluation:c0093",
        ],
        "core": "Evaluation is a real-world, political, professional, and use-oriented activity whose value depends on whether findings influence policy, programs, and practice.",
        "summary": [
            "Chapter 12 closes the book by returning to the social ecology of evaluation. Evaluation is not only a technical research exercise; it is undertaken among multiple stakeholders, political time pressures, professional norms, and contested policy interests.",
            "The chapter discusses dissemination, the political character of evaluation, the profession of evaluation, intellectual diversity, working arrangements, standards, guidelines, ethics, and evaluation use.",
            "Use is treated broadly. Direct or instrumental use matters, but conceptual use can change how programs and social problems are understood, and persuasive use can influence debate. These forms of use connect back to Chapter 3's advice on question priority.",
            "The chapter's closing message is pragmatic: evaluation is worthwhile when it improves decisions, programs, policies, or understanding. Technical quality remains necessary, but it is not the whole measure of success if findings never reach or affect the people positioned to act.",
        ],
        "concepts": ["evaluation use", "political context", "stakeholder", "dissemination", "instrumental use", "conceptual use", "evaluation standards"],
        "structure": ["social ecology", "multiple stakeholders", "politics and timing", "profession and standards", "utilization of results", "future of evaluation"],
        "implications": ["Plan dissemination and use as part of the evaluation design.", "Account for political timing without compromising evidence.", "Judge evaluation success partly by whether credible findings affect action or understanding."],
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
        "<summary>Source chunks</summary>\n"
        '<ul class="source-chunk-list">\n'
        f"{items}\n"
        "</ul>\n"
        "</details>"
    )


def mermaid_label(text: str) -> str:
    return text.replace('"', "'")


def render_concept_map(chapter: dict) -> str:
    concepts = chapter["concepts"][:3]
    mechanisms = chapter["structure"][:3]
    implications = chapter["implications"][:2]
    lines = [
        "::: {.concept-map}",
        "```{mermaid}",
        "flowchart TD",
        f'  Problem["Problem: What evaluation problem does Chapter {chapter["number"]} help diagnose?"]',
        f'  Central["Concept: {mermaid_label(chapter["title"])}"]',
    ]
    for idx, concept in enumerate(concepts, start=1):
        lines.append(f'  Concept{idx}["Concept: {mermaid_label(concept)}"]')
    for idx, mechanism in enumerate(mechanisms, start=1):
        lines.append(f'  Mechanism{idx}["Mechanism: {mermaid_label(mechanism)}"]')
    for idx, implication in enumerate(implications, start=1):
        lines.append(f'  Implication{idx}["Practice implication: {mermaid_label(implication)}"]')
    lines.append('  Question["Open question: What evidence would make this guidance credible in a live evaluation?"]')
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


def concept_gloss(concept: str, chapter: dict) -> str:
    gloss = CONCEPT_GLOSSES.get(concept.lower())
    if gloss:
        return gloss
    return (
        f"A chapter-specific term used in Chapter {chapter['number']}; check the cited source records "
        "before treating it as a portable evaluation concept."
    )


def render_book_connection(chapter: dict) -> str:
    number = chapter["number"]
    if number <= 3:
        return "Within the wider book, this chapter belongs to the framing sequence: it defines evaluation, explains how designs are tailored, and turns issues into usable questions."
    if number <= 6:
        return "Within the wider book, this chapter belongs to the pre-impact sequence: it checks need, theory, and implementation before outcome and impact claims are treated as meaningful."
    if number <= 10:
        return "Within the wider book, this chapter belongs to the outcome and impact sequence: it moves from outcome measurement to causal design and interpretation of effects."
    return "Within the wider book, this chapter extends the evaluation sequence beyond impact by addressing cost, social context, professional standards, politics, and use."


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
        "The retrieval trail is retained in the source chunks at the bottom of the page. The note paraphrases the chapter's argument and procedures, and it does not reproduce textbook tables, review questions, checklists, exhibits, or extended passages. When a table or exhibit is central, the note describes its function and leaves the source artifact in the evidence record.",
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
    body.extend(f"- **{concept}**: {concept_gloss(concept, chapter)}" for concept in chapter["concepts"])
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
    if chapter["number"] in {2, 3, 5}:
        body.append("- Legacy extract retained: [Tailoring Evaluations](section-01-tailoring-evaluations.qmd)")
        body.append("- Legacy extract retained: [Identifying Issues and Formulating Questions](section-02-formulating-questions.qmd)")
        body.append("- Legacy extract retained: [Expressing and Assessing Program Theory](section-03-program-theory-assessment.qmd)")
    body.extend(
        [
            "",
            "## Study Prompts",
            "",
            f"1. What evaluation problem does Chapter {chapter['number']} help diagnose?",
            "2. Which assumptions would need evidence before applying this chapter in a live evaluation?",
            "3. How would this chapter change the way an evaluator scopes questions, methods, reporting, or use?",
            "4. Where could the guidance be misused if treated as a fixed template?",
            "",
            "## Source Chunks",
            "",
            source_chunks(evidence_ids),
            "",
            "## References",
            "",
            f"- Rossi, P. H., Lipsey, M. W., & Freeman, H. E. ({YEAR}). *{FULL_TITLE}*. {PUBLISHER}. Chapter {chapter['number']}, pages {chapter['pages']}.",
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
        "  <span>12 chapter notes</span>",
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
        "Full reading route for all 12 chapters.",
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
        "Evaluation design should move from need and program theory through process, outcome, impact, efficiency, and use, with each question type matched to program circumstances and feasible evidence.",
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
            "- [Tailoring Evaluations](section-01-tailoring-evaluations.qmd)",
            "- [Identifying Issues and Formulating Questions](section-02-formulating-questions.qmd)",
            "- [Expressing and Assessing Program Theory](section-03-program-theory-assessment.qmd)",
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
    groups = [
        ("Framing and Design", CHAPTERS[:3]),
        ("Need, Theory, and Process", CHAPTERS[3:6]),
        ("Outcomes, Impact, and Interpretation", CHAPTERS[6:10]),
        ("Efficiency and Use", CHAPTERS[10:]),
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
            "- Start with Chapters 1-3 when scoping an evaluation and turning stakeholder concerns into answerable questions.",
            "- Use Chapters 4-6 before impact work to check need, theory, and implementation.",
            "- Use Chapters 7-10 for outcome measurement, impact design, and interpretation of program effects.",
            "- Use Chapters 11-12 to connect findings to resource allocation, politics, professional standards, and use.",
            "",
            "## Legacy Extracts",
            "",
            "- [Tailoring Evaluations](section-01-tailoring-evaluations.qmd)",
            "- [Identifying Issues and Formulating Questions](section-02-formulating-questions.qmd)",
            "- [Expressing and Assessing Program Theory](section-03-program-theory-assessment.qmd)",
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
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    concept_groups = [
        ("Evaluation Framing", ["program evaluation", "social program", "stakeholder", "evaluation use", "accountability"]),
        ("Question Types", ["needs assessment", "program theory", "process evaluation", "impact assessment", "efficiency assessment"]),
        ("Implementation and Outcomes", ["coverage", "bias", "implementation failure", "program outcome", "program effect"]),
        ("Impact Designs", ["randomized field experiment", "random assignment", "quasi-experimental design", "selection bias", "statistical controls"]),
        ("Interpretation and Use", ["effect size", "statistical power", "practical significance", "cost-benefit analysis", "conceptual use"]),
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
        "The book treats evaluation as a sequence of fit-for-purpose inquiries: diagnose need, articulate theory, assess process, measure outcomes, estimate impact, interpret effects, assess efficiency, and support use.",
        "",
        "## Concepts",
        "",
    ]
    for heading, concepts in concept_groups:
        lines.extend([f"### {heading}", ""])
        for concept in concepts:
            lines.append(f"- {concept}: {CONCEPT_GLOSSES.get(concept.lower(), 'a recurring idea used to frame evaluation design, evidence, interpretation, quality, or use.')}")
        lines.append("")
    lines.extend(["## Links", ""])
    lines.extend(f"- {chapter_link(chapter)}" for chapter in CHAPTERS)
    lines.extend(["", "## Source Chunks", "", source_chunks(evidence), "", "## References", ""])
    return "\n".join(lines)


def render_practice() -> str:
    evidence = [chapter["evidence_ids"][0] for chapter in CHAPTERS]
    implications = [
        "Classify the evaluation question type before selecting methods.",
        "Check need, program theory, and process before treating impact estimation as meaningful.",
        "Use program theory to identify relevant outcomes and plausible sources of variation.",
        "Treat outcome monitoring as useful but insufficient for causal claims.",
        "Use randomized designs when feasible, but explain practical, ethical, and implementation constraints.",
        "When using quasi-experimental designs, name likely biases and report limitations plainly.",
        "Interpret effects through magnitude, uncertainty, practical significance, and subgroup variation.",
        "Collect cost data early enough to support efficiency assessment.",
        "Plan dissemination and use around stakeholders, political timing, and professional standards.",
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
    lines.extend(["", "## Source Chunks", "", source_chunks(evidence), "", "## References", ""])
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
            "limit": "1-4 during implementation; supplement with chapter anchors and summary chunks",
            "include_media": "true for Chapter 11 efficiency evidence; otherwise false unless table evidence is central",
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
    home = ROOT / "index.qmd"
    text = home.read_text(encoding="utf-8")
    text = text.replace(
        "with detailed hand-authored notes for Purposeful Program Theory and generated major-section notes for the wider collection.",
        "with detailed notes for Purposeful Program Theory, chapter-level Rossi/Lipsey notes, and generated notes for the wider collection.",
    )
    home.write_text(text, encoding="utf-8")

    notes = ROOT / "notes" / "index.qmd"
    text = notes.read_text(encoding="utf-8")
    text = text.replace(
        "The notes combine the existing hand-authored Purposeful Program Theory section with generated major-section notes for the other ready evaluation texts.",
        "The notes combine the existing hand-authored Purposeful Program Theory section, chapter-level Rossi/Lipsey notes, and generated notes for the other ready evaluation texts.",
    )
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
