# Impact Pathway Library

Common feature-to-metric pathways by feature type and product category. Use this reference in Stage 1 to identify the most plausible causal chain and assess pathway quality.

---

## Table of Contents
1. [Retention Features](#retention-features)
2. [Activation & Onboarding Features](#activation--onboarding-features)
3. [Engagement Features](#engagement-features)
4. [Conversion Features](#conversion-features)
5. [Expansion & Upsell Features](#expansion--upsell-features)
6. [Cost Reduction Features](#cost-reduction-features)
7. [Acquisition Features](#acquisition-features)
8. [Platform & Infrastructure Features](#platform--infrastructure-features)
9. [Pathway Quality Patterns](#pathway-quality-patterns)

---

## Retention Features

### Notification / Re-engagement

**Pathway:** Notification delivery → user returns to product → session depth increases → monthly active rate improves → churn rate decreases → retained ARR
**Quality:** Indirect (3–4 steps)
**Key variable:** The notification must trigger a return visit that creates genuine value, not just an open. Notifications that don't lead to value-creating sessions don't move retention.
**Common failure:** Confusing email open rate (leading indicator) with retained users (lagging metric). Opens don't equal retention.

---

### Collaboration / Sharing Features

**Pathway:** User shares content or invites collaborator → second user activates → shared sessions create mutual dependency → both users' switching cost increases → churn decreases for both
**Quality:** Indirect to Direct depending on product
**Key variable:** Multi-user features only drive retention when the collaboration creates genuine work product. Social sharing features in B2B products often have weak pathways.
**Watch for:** Network effects can make this pathway stronger over time — early adopters create the value for later ones.

---

### Progress / Achievement Features

**Pathway:** User earns achievement or sees progress indicator → motivation to continue increases → session frequency increases → habit formation → retained at D30/D90
**Quality:** Indirect (mechanism depends on product category)
**Key variable:** Works best for products where habit formation is the retention driver (fitness, learning, productivity). Less relevant for B2B tools where retention is driven by workflow embedding.

---

### Save / Bookmark / History Features

**Pathway:** User saves content or builds history → accumulated data creates switching cost → user has reason to return to access their saved content → retention improves
**Quality:** Direct
**Key variable:** The value of the saved content must grow over time. If saved items are rarely accessed, the switching cost is theoretical, not real.

---

## Activation & Onboarding Features

### Guided Onboarding / Checklists

**Pathway:** User completes guided setup → reaches the product's "aha moment" faster → activates within first session → D7 retention improves → LTV increases
**Quality:** Direct
**Key variable:** The onboarding must actually lead to the aha moment, not just complete checklist items. Onboarding that generates completions but not activation doesn't move retention.
**Benchmark anchor:** Improving time-to-value by 50% typically moves D7 retention by 5–15 percentage points in B2B SaaS.

---

### Templates / Getting Started Content

**Pathway:** User starts from template → reaches functional state faster → reduces friction-driven abandonment → activation rate improves → D1 retention improves
**Quality:** Direct
**Key variable:** Templates must match the user's actual use case. Generic templates that don't fit real workflows don't reduce abandonment.

---

### In-App Tooltips / Contextual Help

**Pathway:** User encounters friction → contextual help reduces confusion → user completes the action → activation rate improves
**Quality:** Direct
**Key variable:** Only effective if placed at actual friction points. Tooltip coverage of high-traffic, low-completion flows. Adding tooltips to flows users already complete has near-zero impact.

---

## Engagement Features

### Search Improvements

**Pathway:** User finds relevant content faster → search abandonment decreases → session depth increases → engagement metric improves → retention improves
**Quality:** Direct to Indirect depending on how central search is to the product
**Key variable:** Impact scales with how often users search vs. browse. Products where search is the primary navigation have Direct pathways. Products where search is supplemental have Indirect pathways.

---

### Personalization / Recommendations

**Pathway:** Recommendation surfaces relevant content → user engages with recommended content → session depth increases → content consumption per session improves → D30 retention improves
**Quality:** Indirect
**Key variable:** Recommendation quality is the critical variable. Bad recommendations actively hurt engagement by wasting attention. Model accuracy needs to be validated before pathway strength can be assessed.

---

### Filtering / Sorting / Organization

**Pathway:** User finds relevant items faster → task completion time decreases → user perceives product as efficient → repeat usage increases → engagement depth improves
**Quality:** Indirect
**Key variable:** Works when the core problem is findability, not when the content itself is the problem. Adding organization to a product with a weak content catalog doesn't move metrics.

---

## Conversion Features

### Pricing Page / Plan Comparison

**Pathway:** User sees clearer plan differentiation → upgrade intent increases → conversion rate improves → MRR increases
**Quality:** Direct
**Key variable:** Requires that pricing confusion is actually a conversion barrier (validate with session recordings, support tickets). If users aren't confused about pricing, this won't move conversion.

---

### Free Trial / Freemium Feature Gating

**Pathway:** User hits feature limit → upgrade prompt appears → user sees value of paid tier → converts to paid → MRR increases
**Quality:** Direct
**Key variable:** The gated feature must be one users have already experienced value from. Gating features before users understand their value produces abandonment, not upgrades.

---

### Social Proof / Case Studies / Trust Signals

**Pathway:** Prospect encounters trust signal → perceived risk of purchase decreases → conversion rate improves → new ARR increases
**Quality:** Indirect
**Key variable:** Most effective when trust is the primary conversion barrier. If conversion is blocked by price, fit, or timing, trust signals don't move the needle.

---

### Checkout / Signup Flow Simplification

**Pathway:** User encounters fewer friction points in checkout → drop-off rate at each step decreases → overall conversion rate improves → revenue increases
**Quality:** Direct
**Key variable:** Impact depends on where drop-off currently occurs. Simplifying a step where users aren't dropping off has no impact.
**Benchmark anchor:** Removing a field from a checkout form typically reduces drop-off at that step by 5–15%. Reducing checkout from 3 pages to 1 can improve conversion by 20–35%.

---

## Expansion & Upsell Features

### Usage-Based Upgrade Triggers

**Pathway:** User approaches usage limit → upgrade prompt appears in context → user upgrades rather than leaving → expansion MRR increases
**Quality:** Direct
**Key variable:** Must appear at the right moment — when the user is experiencing the limit as a genuine problem, not as an abstract warning.

---

### Team / Collaboration Invites

**Pathway:** User invites teammates → new seats added → seat count grows → expansion MRR increases
**Quality:** Direct
**Key variable:** Invitation conversion rate is the critical unknown. Invited users who don't activate don't generate expansion revenue.
**Benchmark anchor:** In B2B SaaS, viral coefficient for team invites typically ranges 0.2–0.8 (each existing user invites 0.2–0.8 additional users who activate).

---

### Feature Discovery / Upsell Prompts

**Pathway:** User discovers higher-tier feature while using lower tier → perceives incremental value → upgrades to access feature → expansion MRR increases
**Quality:** Indirect
**Key variable:** The discovered feature must solve a real problem the user currently has. Feature discovery for features users don't need doesn't drive upgrades.

---

## Cost Reduction Features

### Automation / Workflow Efficiency

**Pathway:** Manual task is automated → staff hours saved → cost per unit of output decreases → margin improves
**Quality:** Direct
**Key variable:** Automation must actually replace the manual task, not just provide an alternative. If staff continue doing the manual work alongside the automation, savings don't materialize.
**Modeling note:** For cost-reduction features, replace "Revenue per unit" in the model with "Cost saved per unit" and "Expected value" with "Annual cost savings."

---

### Self-Serve / Deflection Features

**Pathway:** User resolves issue through self-serve → support ticket not created → support cost per user decreases → margin improves
**Quality:** Direct
**Key variable:** Self-serve only deflects tickets for issues that self-serve actually solves. Complex or emotional issues escalate regardless of self-serve availability.
**Benchmark anchor:** A well-designed help center or chatbot typically deflects 15–40% of tier-1 support volume.

---

## Acquisition Features

### SEO / Content Features

**Pathway:** New content indexed → organic search visibility increases → organic traffic increases → signups from organic channel increase → new ARR from organic increases
**Quality:** Indirect (long time-to-impact, 3–6 months)
**Key variable:** Content must rank for terms with commercial intent. Traffic without conversion intent doesn't produce signups.
**Time-to-impact note:** SEO features have the longest time-to-impact of any acquisition feature. Models should use 6–12 month windows.

---

### Referral / Word-of-Mouth Features

**Pathway:** Satisfied user shares product → referred prospect signs up → new ARR from referral channel increases
**Quality:** Indirect
**Key variable:** Referral features amplify existing word-of-mouth; they don't create it. If users aren't already recommending the product organically, a referral program won't move acquisition significantly.

---

## Platform & Infrastructure Features

These features have no direct revenue pathway — their value is enabling other features or preventing future costs. Model them differently.

**Framework for platform features:**

1. **Optionality value:** What features become possible that aren't currently?
2. **Speed value:** How much faster can the team ship? (engineering velocity × average feature value)
3. **Risk reduction value:** What failure modes does this prevent? (probability × cost of incident)
4. **Technical debt cost:** What is the compounding cost of not doing this?

**Pathway:** Platform investment → engineering velocity increases or risk decreases → future feature value is captured faster or failure costs are avoided → effective ROI over 12–24 months
**Quality:** Speculative (many dependencies on future decisions)
**Modeling note:** Platform features are often better framed as "cost of inaction" than "expected return." See `references/roi-model-guide.md` for the platform feature modeling approach.

---

## Pathway Quality Patterns

### Signs of a Direct Pathway
- Feature directly enables or prevents the target behavior (no intermediary steps)
- The metric can be measured within 30 days of launch
- There are no significant confounders (other things happening simultaneously that could move the metric)
- A/B testing is feasible

### Signs of an Indirect Pathway
- 2–4 causal steps between feature and metric
- Time-to-impact is 30–90 days
- Multiple things need to go right simultaneously
- Attribution is clear but not perfect

### Signs of a Speculative Pathway
- 5+ causal steps
- Time-to-impact is 90+ days
- Depends on behavioral changes outside the product's control (user mindset shifts, market changes)
- The metric is a lagging indicator with many drivers (NPS, brand perception, long-term LTV)
- Cannot be A/B tested directly

### The "Correlation Trap"
Features that correlate with good outcomes aren't necessarily causing them. Power users tend to use more features — but adding more features doesn't necessarily create power users. Check whether the pathway runs in the right direction before assuming causality.
