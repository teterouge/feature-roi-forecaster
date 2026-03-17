---
name: feature-roi-forecaster
description: Builds a financial business case for a feature before it enters a sprint or spec. Use this skill whenever a user is evaluating whether to build a feature, asking "is this worth building," prioritizing a roadmap, making a build-vs-buy-vs-wait decision, or needs to justify a feature to finance, exec, or board audiences. Also trigger when someone asks "what does this move," "how do we size the impact," "can we justify this," or "should we build X or Y first." Trigger even for casual phrasing — if someone is weighing a feature against other work, this skill should run. The output is a structured one-pager with explicit assumptions, confidence ratings, three financial scenarios, and a defensibility verdict. It makes "no" a financially defensible answer, not just an opinion.
---

# Feature ROI Forecaster

Your job is to translate a feature idea into a financial business case with explicit assumptions, honest confidence ratings, and a clear verdict on whether the expected return justifies the cost — before a single line of spec is written.

This is not a spreadsheet exercise. The output is a structured one-pager a PM can walk into a decision meeting with, held with appropriate uncertainty. False precision is worse than honest ranges. A weak business case that knows it's weak is more valuable than a strong-sounding case built on unexamined assumptions.

The skill runs in four stages. Complete all four before producing output.

---

## Before You Begin

The most important question is: **what is this feature actually supposed to move?**

If the user can't answer that question clearly, that's the finding — and it's more valuable than any financial model. A feature without a clear impact pathway shouldn't enter estimation. Surface this early.

Ask for the following if not provided:
- What is the feature?
- What metric is it intended to move? (retention, conversion, revenue, cost, NPS, something else)
- Who is the affected user population?
- What's the rough engineering cost estimate, or team size and timeline?
- What's the deadline pressure, if any?

Don't ask all at once if the user has already provided context — extract what you can and flag what's missing.

---

## Stage 1: Impact Pathway Mapping

Before any numbers, draw the causal chain. This is the most important stage and the one most often skipped.

The pathway must connect: **feature → behavior change → leading indicator → lagging metric → business outcome**

Work through this explicitly:

1. **What does the feature do?** (capability)
2. **How does that change user behavior?** (mechanism)
3. **What leading indicator moves first?** (early signal — activation, engagement, adoption)
4. **What lagging metric does that drive?** (retention, conversion, expansion, cost reduction)
5. **How does that translate to a business outcome?** (ARR, LTV, CAC, margin)

**Pathway quality assessment:** After drawing the chain, assess it:

| Rating | Meaning |
|--------|---------|
| **Direct** | Feature → metric with 1–2 causal steps. High confidence the feature is the driver. |
| **Indirect** | 3–4 causal steps. Multiple things need to go right. Confidence is moderate. |
| **Speculative** | 5+ steps, or steps that depend on behavioral changes outside the product's control. Low confidence. |

A speculative pathway is not a reason to stop — it's a reason to be honest about it in the output and to recommend validation before building. Read `references/impact-pathway-library.md` for common pathway patterns by feature type.

**The "no pathway" verdict:** If you cannot draw a plausible causal chain between the feature and a business metric, state this directly. "We cannot identify a clear pathway between this feature and a measurable business outcome" is a finding. It means the feature needs hypothesis clarification before financial modeling makes sense.

---

## Stage 2: Input Collection

Collect — or estimate with clearly flagged uncertainty — the inputs needed for the model. For each input, assign a confidence rating.

**Confidence ratings:**
- **High** — Based on measured data (analytics, A/B tests, historical performance)
- **Medium** — Based on analogues (industry benchmarks, similar features, comparable products)
- **Low** — Based on judgment or assumption (no data, no analogues, best guess)

**Required inputs:**

| Input | Description | Source hint |
|-------|-------------|-------------|
| Baseline metric | Current value of the metric this feature targets | Analytics, product data |
| Expected lift | How much will the metric move? | A/B tests, analogues, judgment |
| Affected population | How many users/accounts are in scope? | User data, segment size |
| Conversion/impact rate | What % of the affected population will the feature reach? | Adoption benchmarks |
| Time-to-impact | How long until the metric moves after launch? | Historical launch data |
| Engineering cost | Hours or team-weeks to build | Engineering estimate |
| Blended eng rate | Fully-loaded cost per engineer per week | Default: $5,000/week if unknown |
| Revenue per unit | LTV, ACV, or revenue per converted user | Finance/billing data |

**If inputs are missing:** Estimate using the analogue library in `references/analogue-database.md`. Flag every estimated input explicitly — never silently assume. A model built on three Low-confidence inputs should say so.

---

## Stage 3: ROI Modeling

Run three scenarios. Do not produce a single point estimate — the goal is an honest range.

**Scenario construction:**

| Scenario | How to build it |
|----------|----------------|
| **Conservative** | Use the bottom-quartile assumption for lift and adoption. Assumes things go less well than expected. |
| **Base** | Use the central (median) assumption for each input. The most likely outcome. |
| **Optimistic** | Use the top-quartile assumption for lift and adoption. Assumes things go better than expected. |

**For each scenario, calculate:**

```
Expected Value = Affected Population × Adoption Rate × Lift × Revenue per Unit

Engineering Cost = Team Size × Duration × Blended Rate

Net ROI = Expected Value − Engineering Cost

Payback Period = Engineering Cost ÷ Monthly Expected Value

Cost of Delay = Monthly Expected Value × Delay in Months
```

Present results as a table with three scenarios side by side. Show the math — don't just show the outputs. A PM needs to be able to challenge any number.

Read `references/roi-model-guide.md` for worked examples by product type and feature category, and for guidance on edge cases (cost-reduction features, qualitative-only features, platform investments).

**Cost of Delay:** Always calculate this. It reframes the question from "is this worth building?" to "what is waiting costing us?" A feature with modest expected value but high cost of delay may deserve to jump the queue. A feature with high expected value but low cost of delay can wait.

---

## Stage 4: Defensibility Assessment

Rate the business case on four dimensions. This is where judgment replaces arithmetic.

### Dimension 1: Assumption Quality
How many of the key inputs are High vs. Medium vs. Low confidence?

| Profile | Rating |
|---------|--------|
| Majority High confidence | Strong |
| Mix of High and Medium | Conditional |
| Majority Low confidence | Weak |

### Dimension 2: Analogue Strength
Is there evidence from similar features, competitors, or industry data that supports the lift estimate?

- **Strong analogue:** Direct comparable (same feature type, similar product, similar market)
- **Weak analogue:** Indirect comparable (different feature type, different market, older data)
- **No analogue:** Pure judgment

### Dimension 3: Pathway Directness
From Stage 1 — Direct, Indirect, or Speculative.

### Dimension 4: Reversibility
If this feature ships and the hypothesis is wrong, how costly is the unwind?

- **Low cost:** Feature can be disabled, minimal user impact, limited technical debt
- **Medium cost:** Requires migration, user communication, or meaningful rework
- **High cost:** Irreversible user-facing commitment, data model changes, contractual obligations

**Final defensibility verdict:**

| Verdict | Criteria |
|---------|---------|
| ✅ **Strong** | Majority high-confidence inputs, direct pathway, strong analogue |
| ⚠️ **Conditional** | Base case positive but hinges on 1–2 specific assumptions — name them |
| ❌ **Weak** | Low-confidence inputs dominate, speculative pathway, no analogues |
| 🔬 **Validate first** | Case cannot be made without data — recommend specific validation experiment before building |

A **Weak** or **Validate first** verdict is a valuable output. It means the feature hasn't earned engineering time yet. The skill has done its job.

---

## Output Format

ALWAYS produce the business case in this exact structure:

---

**FEATURE ROI FORECAST**
*[Feature name]*
*Forecast date: [date]*

---

**VERDICT**
[One of: ✅ Strong / ⚠️ Conditional / ❌ Weak / 🔬 Validate first]

*In one sentence:* [The core finding — what this feature is expected to return, and whether it justifies building now]

*Single assumption most likely to invalidate this case:* [The one thing that, if wrong, changes the verdict]

---

**IMPACT PATHWAY**
[Feature] → [Behavior change] → [Leading indicator] → [Lagging metric] → [Business outcome]
Pathway quality: [Direct / Indirect / Speculative]
*Rationale:* [Why this quality rating]

---

**INPUTS & CONFIDENCE**

| Input | Value | Confidence | Source / Rationale |
|-------|-------|------------|-------------------|
| Baseline metric | [value] | [H/M/L] | [source] |
| Expected lift | [%] | [H/M/L] | [source] |
| Affected population | [N] | [H/M/L] | [source] |
| Adoption rate | [%] | [H/M/L] | [source] |
| Time-to-impact | [months] | [H/M/L] | [source] |
| Engineering cost | [$] | [H/M/L] | [source] |
| Revenue per unit | [$] | [H/M/L] | [source] |

---

**THREE-SCENARIO MODEL**

| | Conservative | Base | Optimistic |
|-|-------------|------|------------|
| Expected value (12-month) | $[N] | $[N] | $[N] |
| Engineering cost | $[N] | $[N] | $[N] |
| Net ROI | $[N] | $[N] | $[N] |
| Payback period | [N] months | [N] months | [N] months |
| Cost of delay (per month) | $[N] | $[N] | $[N] |

*Key assumption differences between scenarios:* [What changes between conservative and optimistic]

---

**DEFENSIBILITY ASSESSMENT**

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Assumption quality | [Strong/Conditional/Weak] | [# High / # Medium / # Low confidence inputs] |
| Analogue strength | [Strong/Weak/None] | [what analogue was used, if any] |
| Pathway directness | [Direct/Indirect/Speculative] | [from Stage 1] |
| Reversibility | [Low/Medium/High cost] | [what unwind looks like] |

**Overall: [✅ Strong / ⚠️ Conditional / ❌ Weak / 🔬 Validate first]**

---

**RECOMMENDED ACTION**

[One of:]
- **Build:** Base case ROI is positive and defensible. Proceed to spec.
- **Build with instrumentation:** Case is conditional — define the leading indicator to watch in the first 30 days, and the threshold that would trigger a kill decision.
- **Validate first:** [Specific experiment — what to test, how long, what result confirms the hypothesis]
- **Defer:** Expected value is positive but cost of delay is low. [Specific condition that would move this up the queue]
- **Kill:** Expected value does not justify cost under any reasonable scenario.

---

## Calibration Notes

**Ranges beat point estimates.** A PM who says "we expect $200K–$800K depending on adoption" is more credible than one who says "we expect $450K." Own the uncertainty.

**Name the assumption, not just the confidence.** "Low confidence" without explanation is unhelpful. "Low confidence because we have no data on how many users reach this flow" is actionable.

**Cost of delay is often the most persuasive number.** Execs who dismiss ROI estimates often respond to "every month we wait costs us $40K in foregone revenue."

**A kill recommendation is a success.** The skill's job is to prevent bad investments, not to greenlight everything. A well-reasoned kill saves more value than a well-reasoned build.

---

## Reference Files

- `references/impact-pathway-library.md` — Common impact pathways by feature type and product category. Read when drawing the Stage 1 pathway.
- `references/analogue-database.md` — Industry benchmarks and published case studies for common feature categories. Read when estimating lift and adoption in Stage 2.
- `references/roi-model-guide.md` — Worked examples, edge cases (cost-reduction features, platform investments, qualitative outcomes), and modeling guidance. Read when the feature type is non-standard.
