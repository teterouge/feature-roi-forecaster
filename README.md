# feature-roi-forecaster

A financial business case skill for Claude Code. Translates a feature idea into a structured ROI forecast with explicit assumptions, confidence ratings, three financial scenarios, and a defensibility verdict — before a single line of spec is written.

Makes "no" a financially defensible answer, not just an opinion.

---

## Why This Exists

Most feature decisions are made on intuition, stakeholder pressure, or a vague sense that "users want this." When the expected return is made explicit — with honest uncertainty ranges — a lot of features can't justify themselves. The ones that can justify themselves get built with more confidence and better instrumentation.

This skill forces the "what does this actually move, and by how much?" question before engineering capacity is committed.

---

## What It Does

Four sequential stages:

**Stage 1 — Impact Pathway Mapping**
Draws the causal chain: feature → behavior change → leading indicator → lagging metric → business outcome. Rates the pathway quality (Direct / Indirect / Speculative). If no clear pathway can be drawn, that's the finding.

**Stage 2 — Input Collection with Confidence Ratings**
Collects baseline metrics, expected lift, affected population, engineering cost, and revenue per unit. Each input is rated High / Medium / Low confidence based on its source (measured data vs. analogues vs. judgment). Missing inputs are estimated from the analogue library — never silently assumed.

**Stage 3 — Three-Scenario ROI Model**
Conservative, base, and optimistic scenarios. For each: expected annual value, engineering cost, net ROI, payback period, cost of delay per month. Ranges, not point estimates.

**Stage 4 — Defensibility Assessment**
Rates the case on assumption quality, analogue strength, pathway directness, and reversibility. Produces one of four verdicts:
- ✅ **Strong** — Build
- ⚠️ **Conditional** — Build with named assumption to validate
- ❌ **Weak** — Needs better data before committing
- 🔬 **Validate first** — Recommend specific experiment before building

---

## Installation

```bash
/plugin install feature-roi-forecaster@pm-discipline
```

---

## Usage

Triggers automatically when evaluating features:

```
"Should we build X?"
"Is this feature worth the engineering time?"
"Help me build a business case for [feature]"
"We're debating X vs Y — which should we prioritize?"
"How do I justify this to the exec team?"
"What would this move?"
```

Also works with the script directly for structured input:

```bash
# Interactive mode
python skills/feature-roi-forecaster/scripts/roi_model.py --interactive

# JSON input
python skills/feature-roi-forecaster/scripts/roi_model.py --input my_feature.json

# JSON output for integration
python skills/feature-roi-forecaster/scripts/roi_model.py --input my_feature.json --format json
```

**Example input JSON:**
```json
{
  "feature_name": "Guided Onboarding Checklist",
  "metric_type": "revenue",
  "affected_population": 2000,
  "baseline_metric": 0.35,
  "lift_conservative": 0.08,
  "lift_base": 0.12,
  "lift_optimistic": 0.18,
  "adoption_rate": 1.0,
  "revenue_per_unit": 66.67,
  "engineering_cost": 40000,
  "time_to_impact_months": 1,
  "model_window_months": 12
}
```

---

## Structure

```
feature-roi-forecaster/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── feature-roi-forecaster/
│       ├── SKILL.md
│       ├── references/
│       │   ├── impact-pathway-library.md
│       │   ├── analogue-database.md
│       │   └── roi-model-guide.md
│       ├── scripts/
│       │   └── roi_model.py
│       └── evals/
│           └── evals.json
└── README.md
```

---

## Design Notes

**Pathway first, numbers second.** A feature without a clear causal pathway to a business metric shouldn't be modeled — the model would be fiction. The pathway check is the most important gate.

**Ranges beat point estimates.** The three-scenario model exists to force honest acknowledgment of uncertainty. A PM who says "$200K–$800K depending on adoption" is more credible than one who says "$450K."

**A kill recommendation is a success.** The skill's job is to prevent bad investments. A well-reasoned kill saves more value than a well-reasoned build.

**Ongoing costs matter.** Features with ongoing infrastructure costs (LLM API, data storage, third-party services) must include those costs in the model, not just the build cost.

---

## Part of the pm-discipline Suite

- **spec-auditor** — Adversarial spec review before engineering picks it up
- **feature-roi-forecaster** ← you are here
- **post-launch-retro** — Closes the loop between hypotheses and reality
- **pmf-signal-analyzer** — Multi-signal product-market fit assessment
- **dependency-risk-mapper** — Cross-team dependency graph and delivery risk
- **competitive-intel-synthesizer** — Competitive signals to roadmap implications
- **pricing-packaging-intel** — Pricing and packaging recommendation engine
- **stakeholder-comm-translator** — Audience-specific message translation
