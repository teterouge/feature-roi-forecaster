---
name: feature-roi-forecaster
description: Builds a financial business case for a feature before it enters a sprint or spec. Use this skill whenever a user is evaluating whether to build a feature, asking "is this worth building," prioritizing a roadmap, making a build-vs-buy-vs-wait decision, or needs to justify a feature to finance, exec, or board audiences. Also trigger when someone asks "what does this move," "how do we size the impact," "can we justify this," or "should we build X or Y first." Trigger even for casual phrasing — if someone is weighing a feature against other work, this skill should run. The output is a structured one-pager with explicit assumptions, confidence ratings, three financial scenarios, a model integrity score, pathway stress test, opportunity cost comparison, pre-committed kill triggers, and a defensibility verdict. It makes "no" a financially defensible answer, not just an opinion.
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

### Pathway Stress Test (mandatory second pass)

After drawing the pathway, argue against it. This is not optional — a pathway that can't survive adversarial scrutiny shouldn't be the basis for a financial model.

Answer all four:

1. **What breaks this pathway?** Name the single step most likely to fail. If the feature ships but that step doesn't happen, what does the outcome look like?

2. **What is the weakest assumption?** Not the lowest-confidence input (that comes in Stage 2) — the assumption *embedded in the causal logic itself*. Example: "This assumes users who complete onboarding will return within 7 days. We have no evidence of that timing."

3. **What external factor could invalidate it?** Competitor move, seasonality, market shift, platform change, or user behavior trend that could render the pathway irrelevant even if the feature works.

4. **What does "it worked but didn't move the metric" look like?** Describe the scenario where the feature gets built and used, but the target metric still doesn't move. This is the "false success" trap — features that show adoption but not impact.

Document these stress test answers. They feed directly into the Pathway Stress Test section of the output and into the Kill Triggers in the Recommended Action.

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

### Opportunity Cost Context

Before modeling, ask: **what else could this engineering time build?**

If the user has mentioned other features in the queue, or if this is a prioritization decision between options, collect them. You don't need full models for the alternatives — just enough for a directional comparison:

- Feature name
- Rough expected monthly value (even a range)
- Engineering cost estimate

If the user hasn't provided alternatives, include a placeholder in the output that explicitly flags the comparison as missing. A feature that looks good in isolation may look weak relative to what the team is trading away. Conversely, a marginal feature may be the best available use of a team's current sprint.

**If no alternatives are provided:** Include the section in the output with the note: *"No alternatives provided — this case is evaluated in isolation. ROI should be compared against the next-best use of the same engineering capacity before committing."*

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

### Model Integrity Score (run this first)

Before assessing defensibility, calculate the Model Integrity Score. This is the headline number that tells a reader whether they're looking at a data-backed case or a structured guess.

**Count the inputs from Stage 2 by confidence tier:**

```
High-confidence inputs:   N / [total]
Medium-confidence inputs: N / [total]
Low-confidence inputs:    N / [total]
```

**Assign an integrity tier:**

| Profile | Integrity Tier | Interpretation |
|---------|---------------|----------------|
| ≥ 60% High, 0 Low | **Decision-grade** | Numbers can support a go/no-go call |
| Mixed High/Medium, ≤ 1 Low | **Directional** | Useful for prioritization; validate before committing major resources |
| Majority Medium, any Low | **Indicative** | Order-of-magnitude signal only; don't defend specific numbers |
| Majority Low, or pathway Speculative | **Hypothesis only** | Financial model is illustrative; needs validation before it means anything |

**Primary risk statement:** Name the single input or assumption that, if wrong by 2×, flips the base-case verdict. This is the sentence an exec will remember when the post-launch retro happens.

The Model Integrity Score appears in the output as its own block — not buried in the Defensibility table. It is the first thing a reader should see after the verdict, because it tells them how much weight to put on the numbers that follow.

---

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

**MODEL INTEGRITY**
High-confidence inputs: [N] / [total]
Medium-confidence inputs: [N] / [total]
Low-confidence inputs: [N] / [total]
Integrity tier: [Decision-grade / Directional / Indicative / Hypothesis only]
Primary risk: [The single input that, if wrong by 2×, flips the verdict]
Interpretation: [One sentence on how much weight to give these numbers]

---

**IMPACT PATHWAY**
[Feature] → [Behavior change] → [Leading indicator] → [Lagging metric] → [Business outcome]
Pathway quality: [Direct / Indirect / Speculative]
*Rationale:* [Why this quality rating]

*Stress test:*
- What breaks this pathway: [The step most likely to fail]
- Weakest embedded assumption: [The logic assumption, not just a low-confidence input]
- External invalidator: [Competitor, market, or platform factor that could kill the pathway]
- False success scenario: [How the feature ships and gets used but the metric still doesn't move]

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

**ALTERNATIVE USES OF TIME**

*[If alternatives were provided:]*

The same engineering capacity could alternatively deliver:

| Alternative | Est. monthly value | Engineering cost | Net ROI delta vs. this feature |
|-------------|-------------------|-----------------|-------------------------------|
| [Feature A] | $[N] | $[N] | [+/− $N] |
| [Feature B] | $[N] | $[N] | [+/− $N] |

*Opportunity cost verdict:* [One sentence — does this feature beat its alternatives on ROI, cost of delay, or strategic fit? Or does it lose?]

*[If no alternatives were provided:]*
No alternatives provided — this case is evaluated in isolation. Base-case ROI should be compared against the next-best use of the same engineering capacity before committing.

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
- **Build with instrumentation:** Case is conditional. Pre-commit to the following kill logic before a line of code is written:
  - *Leading indicator to watch:* [Specific metric]
  - *Measurement window:* [e.g., 30 days post-launch]
  - *Kill threshold:* If [metric] does not reach [value] by [date], kill or pivot the feature. Do not wait for the lagging metric.
  - *Named assumption to validate:* [The one assumption from the stress test that this instrumentation will confirm or refute]
- **Validate first:** [Specific experiment — what to test, how long, what result confirms the hypothesis]
- **Defer:** Expected value is positive but cost of delay is low. [Specific condition that would move this up the queue]
- **Kill:** Expected value does not justify cost under any reasonable scenario.

---

## Calibration Notes

**Ranges beat point estimates.** A PM who says "we expect $200K–$800K depending on adoption" is more credible than one who says "we expect $450K." Own the uncertainty.

**Name the assumption, not just the confidence.** "Low confidence" without explanation is unhelpful. "Low confidence because we have no data on how many users reach this flow" is actionable.

**Cost of delay is often the most persuasive number.** Execs who dismiss ROI estimates often respond to "every month we wait costs us $40K in foregone revenue."

**A kill recommendation is a success.** The skill's job is to prevent bad investments, not to greenlight everything. A well-reasoned kill saves more value than a well-reasoned build.

**Model Integrity Score protects your credibility.** When you label a model "Hypothesis only," you're not undermining your case — you're establishing that you understand its limits. Execs who are burned by overconfident projections will trust the next one less. The integrity score preempts that.

**Kill triggers are commitments, not caveats.** "We'll watch the leading indicator" is a caveat. "If [metric] doesn't hit [threshold] by [date], we kill it" is a commitment. The difference is whether the decision logic is written down before anyone has sunk cost into the feature.

**Stress testing is arguing in good faith.** The point isn't to kill the feature — it's to surface the most dangerous assumptions before they're discovered post-launch. A pathway that survives adversarial scrutiny is worth building on. One that doesn't survive it would have failed in production anyway.

**Opportunity cost makes the case relative.** A feature with a $100K expected return looks strong in isolation and weak when the alternative is a $400K return. Always ask what the denominator is.

---

## Reference Files

- `references/impact-pathway-library.md` — Common impact pathways by feature type and product category. Read when drawing the Stage 1 pathway.
- `references/analogue-database.md` — Industry benchmarks and published case studies for common feature categories. Read when estimating lift and adoption in Stage 2.
- `references/roi-model-guide.md` — Worked examples, edge cases (cost-reduction features, platform investments, qualitative outcomes), and modeling guidance. Read when the feature type is non-standard.
