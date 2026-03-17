# ROI Model Guide

Worked examples, edge cases, and modeling guidance for non-standard feature types. Read this when the standard model in the SKILL.md doesn't cleanly fit the feature being evaluated.

---

## Table of Contents
1. [Standard SaaS Feature — Worked Example](#standard-saas-feature--worked-example)
2. [Cost Reduction Features](#cost-reduction-features)
3. [Platform & Infrastructure Investments](#platform--infrastructure-investments)
4. [Qualitative-Only Features](#qualitative-only-features)
5. [Features with Long Time-to-Impact](#features-with-long-time-to-impact)
6. [Multi-Segment Features](#multi-segment-features)
7. [Build vs. Buy vs. Wait Decisions](#build-vs-buy-vs-wait-decisions)
8. [Cost of Delay — Extended Guide](#cost-of-delay--extended-guide)

---

## Standard SaaS Feature — Worked Example

**Feature:** Guided onboarding checklist for a B2B SaaS product
**Metric target:** Activation rate (users who complete setup and use core feature within 7 days)
**Current state:** 35% activation rate, 2,000 new signups/month, $800 ACV

**Stage 1 — Pathway:**
Checklist → user completes setup steps → reaches core feature faster → experiences value in first session → activates within 7 days → D30 retention improves → fewer churned accounts → retained ARR

Pathway quality: **Direct** (2–3 steps, measurable within 30 days)

**Stage 2 — Inputs:**

| Input | Value | Confidence | Source |
|-------|-------|------------|--------|
| Baseline activation rate | 35% | High | Internal analytics |
| Expected lift | +12 pp (to 47%) | Medium | Industry benchmark: guided onboarding +10–25% activation |
| Monthly new signups | 2,000 | High | Internal data |
| ACV | $800 | High | Finance data |
| Time-to-impact | 30 days | High | Activation measured at D7 |
| Engineering cost | $40,000 | Medium | Engineering estimate: 2 engineers × 4 weeks |

**Stage 3 — Model:**

```
Incremental activations/month = 2,000 × 12% = 240 additional activations
Monthly revenue impact = 240 × ($800/12) = $16,000/month
Annual revenue impact = $192,000

Engineering cost = $40,000

Net ROI (Year 1) = $192,000 − $40,000 = $152,000
Payback period = $40,000 ÷ $16,000 = 2.5 months
Cost of delay = $16,000/month
```

**Conservative scenario:** +8pp lift → $128K annual → ROI $88K
**Base scenario:** +12pp lift → $192K annual → ROI $152K
**Optimistic scenario:** +18pp lift → $288K annual → ROI $248K

**Defensibility:** Strong — Direct pathway, High-confidence baseline, Medium-confidence lift from good analogues, payback in under 3 months under conservative scenario.

---

## Cost Reduction Features

For features that save costs rather than generate revenue, replace revenue variables with cost variables.

**Model adjustment:**

```
Instead of:
Expected Value = Population × Adoption × Lift × Revenue per Unit

Use:
Expected Value = Affected Volume × Deflection Rate × Cost per Incident
```

**Worked example — Support deflection chatbot:**

| Input | Value | Confidence |
|-------|-------|------------|
| Monthly support tickets (tier-1) | 8,000 | High |
| Average cost per ticket | $18 | High |
| Expected deflection rate | 25% | Medium |
| Implementation cost | $60,000 | Medium |

```
Monthly cost savings = 8,000 × 25% × $18 = $36,000
Annual savings = $432,000
Net ROI (Year 1) = $432,000 − $60,000 = $372,000
Payback period = $60,000 ÷ $36,000 = 1.7 months
```

**Important:** Cost savings don't always materialize as cash. If support is handled by a fixed headcount, deflection reduces load but doesn't reduce headcount costs without an explicit staffing decision. Distinguish between:
- **Hard savings:** Actual reduction in variable costs (vendor spend, contractor hours)
- **Soft savings:** Capacity freed up by existing staff (still valuable, but requires a decision to capture)

---

## Platform & Infrastructure Investments

Platform features don't generate revenue directly. Use the **optionality + velocity + risk** framework.

**Three value components:**

### 1. Velocity Value
Platform investment that makes the team faster at shipping features.

```
Velocity Value = (Hours saved per feature × Features per year × Blended engineering rate)
              + (Reduction in incident time × Incident frequency × Engineering hourly rate)
```

**Example:** A CI/CD pipeline improvement that saves 2 hours per deploy, with 3 deploys/week at $100/hr blended:
`2 hours × 3/week × 52 weeks × $100 = $31,200/year`

### 2. Optionality Value
Platform investment that enables future features not currently possible.

This is harder to quantify. Approach it as: *what features does this unblock, and what is the expected value of those features?*

List 2–3 features the platform enables. Apply a 30–50% probability discount to each (most optionality doesn't fully materialize). Sum the probability-weighted values.

### 3. Risk Reduction Value
Platform investment that reduces the probability or cost of failure.

```
Risk Reduction Value = Probability of incident × Cost of incident × Reduction in probability
```

**Example:** Database migration to reduce probability of data loss incident from 5% to 1% annually, where a data loss incident costs $500K in response + customer churn:
`(5% − 1%) × $500,000 = $20,000/year in risk reduction`

**Presenting platform ROI:** Add all three components. Flag that velocity and optionality values are estimates with low confidence. Present the result as a floor, not a ceiling — the true value of a good platform investment often exceeds the model.

---

## Qualitative-Only Features

Some features have genuine value that resists financial quantification: developer experience improvements, accessibility features, brand/trust features, and internal team tools.

**Don't force a financial model where none exists.** A forced model with five Low-confidence inputs produces a number that looks authoritative but isn't. It's worse than acknowledging the limits of quantification.

**Approach for qualitative-only features:**

1. **Identify the qualitative value clearly.** Name what value the feature creates, even if you can't price it. "This reduces the cognitive load of our core workflow for 3,000 daily active users" is a defensible statement.

2. **Find the nearest quantifiable proxy.** Even qualitative features usually have one measurable effect:
   - Accessibility → reduced legal risk (quantifiable) + expanded addressable market (estimable)
   - Developer experience → reduced time-to-hire + higher offer acceptance rate (estimable)
   - Trust features → reduced churn for trust-sensitive customers (estimable if you can identify them)

3. **State the cost clearly and ask whether it's justified.** "This costs $30,000 to build. We believe it is justified by [qualitative rationale]. We cannot model the financial return." This is honest and defensible.

4. **Flag it as a values-based decision, not an ROI decision.** Some things should be built because they're right, not because they pencil out. Accessibility is the clearest example. The skill's job is to surface that distinction, not to force a false ROI calculation.

---

## Features with Long Time-to-Impact

SEO, brand, platform investments, and ecosystem features have time-to-impact of 6–24 months. Standard 12-month models understate their value.

**Adjustments:**
- Use a 24-month model window for features with >6 month time-to-impact
- Apply a discount rate to future cash flows: 10–15% annually is appropriate for most SaaS companies
- Build in a ramp curve: impact doesn't arrive all at once. Model ramp as 0% in months 1–3, 25% in months 4–6, 75% in months 7–9, 100% from month 10+

**Discount rate application:**

```
Discounted Value = Monthly Value ÷ (1 + Annual Rate)^(Month/12)
```

For a feature generating $10K/month from month 10 onward with a 12% annual discount rate:
- Month 10: $10,000 ÷ (1.12)^(10/12) = $9,048
- Month 18: $10,000 ÷ (1.12)^(18/12) = $8,396
- Month 24: $10,000 ÷ (1.12)^(24/12) = $7,972

---

## Multi-Segment Features

Some features affect multiple user segments differently. Don't average across segments — model each separately and sum.

**When to split by segment:**
- Feature has meaningfully different adoption rates by segment
- Feature has different revenue impact per user by segment (e.g., enterprise vs. SMB)
- Feature is gated or valued differently by plan tier

**Format:** Run the Stage 3 model once per segment, then sum the scenarios:

| Segment | Conservative | Base | Optimistic |
|---------|-------------|------|------------|
| Enterprise (500 accounts, $12K ACV) | $X | $X | $X |
| SMB (5,000 accounts, $800 ACV) | $X | $X | $X |
| **Total** | **$X** | **$X** | **$X** |

---

## Build vs. Buy vs. Wait Decisions

When the question is not just "should we build this" but "should we build, buy, or wait," extend the model.

**Buy option analysis:**

```
Buy cost = License/SaaS cost + Integration cost + Ongoing maintenance
Build cost = Engineering cost + Ongoing maintenance

Break-even = Build cost ÷ (Monthly Build advantage − Monthly Buy cost)
```

Add: strategic value of owning vs. licensing (differentiation, data ownership, vendor dependency risk).

**Wait analysis:** Cost of delay (from Stage 3) × months of delay = cost of waiting. Compare to the benefit of waiting (better information, lower engineering cost, competitor validation).

**Framing the verdict:** "Build at $40K, Buy at $15K/year, Wait costs $16K/month. Buy wins on 2-year TCO unless differentiation is a strategic priority."

---

## Cost of Delay — Extended Guide

Cost of Delay (CD) is the value foregone per unit of time by not delivering a feature. It reframes prioritization from "what's most valuable" to "what's most urgent."

**CD3 (CD divided by Duration):** Prioritize features by CD ÷ engineering weeks. This produces a ranking that balances value and speed.

**Four CD profiles:**

| Profile | Shape | Example | Implication |
|---------|-------|---------|-------------|
| **Standard** | Linear accumulation | Activation improvement | Delay costs proportionally |
| **Urgent/Fixed date** | Step function at deadline | Regulatory compliance, seasonal | Cost spikes sharply at deadline |
| **Intangible/Increasing** | Accelerating | Trust/brand features | Delay compounds as competitors move |
| **Decaying** | Declining over time | Trend-dependent feature | Value window closes; urgency is now |

**For "Decaying" features:** If market conditions are driving the feature's value (a competitor just shipped it, a trend is peaking), the cost of delay is asymmetric. Model the value at 3 months, 6 months, and 12 months separately to show the decay.
