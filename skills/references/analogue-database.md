# Analogue Database

Industry benchmarks and published reference ranges for common feature categories. Use in Stage 2 to estimate lift and adoption when the user has no internal data.

All ranges are medians with interquartile spread from published research, industry reports, and documented case studies as of 2024. Flag every analogue-derived estimate as Medium confidence in the model.

---

## Table of Contents
1. [Onboarding & Activation](#onboarding--activation)
2. [Search & Discovery](#search--discovery)
3. [Notifications & Re-engagement](#notifications--re-engagement)
4. [Checkout & Conversion Flows](#checkout--conversion-flows)
5. [Collaboration & Sharing](#collaboration--sharing)
6. [Self-Serve & Support Deflection](#self-serve--support-deflection)
7. [Personalization & Recommendations](#personalization--recommendations)
8. [Pricing & Packaging Changes](#pricing--packaging-changes)
9. [Mobile & Performance Improvements](#mobile--performance-improvements)
10. [Feature Adoption Benchmarks](#feature-adoption-benchmarks)

---

## Onboarding & Activation

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Guided checklist added to empty state | +10–25% D7 retention | Medium | Higher end for products with complex setup; lower end for simple products |
| Time-to-value reduced by 50% | +8–18% D30 retention | Medium | Based on SaaS onboarding studies; varies heavily by product type |
| Onboarding tooltips on key friction points | +5–15% activation rate | Medium | Assumes tooltips placed at measured drop-off points |
| Template library added | +15–30% activation rate | Medium | Strong for creative/content tools; weaker for data/analytics tools |
| Single sign-on (SSO) added | +10–20% enterprise signup conversion | Medium | Primarily impacts B2B enterprise segment |
| Email verification friction removed | +5–12% signup completion | Medium | Higher end for consumer; lower end for B2B |
| Progress indicator added to multi-step signup | +8–15% completion rate | Medium | |

**Activation rate benchmarks by product type:**

| Product Type | Median Activation Rate | Top Quartile |
|-------------|----------------------|--------------|
| B2B SaaS (simple) | 40–60% | >70% |
| B2B SaaS (complex setup) | 20–40% | >55% |
| Consumer app | 25–45% | >60% |
| Developer tool | 30–50% | >65% |
| Marketplace (supply side) | 15–30% | >45% |

---

## Search & Discovery

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Autocomplete added | −15–25% search abandonment | Medium | |
| Search result relevance improvement | +10–20% search conversion | Medium | Defined as search → click on result |
| Filters / faceted search added | +8–18% search conversion | Medium | Higher impact for large catalogs (>1,000 items) |
| "No results" handling improved | +5–12% recovery rate | Medium | Recovery = user tries again and finds something |
| Search moved to persistent header | +20–40% search usage | Medium | Not necessarily conversion lift; usage lift |
| Typo tolerance / fuzzy match added | −10–20% "no results" rate | Medium | |

---

## Notifications & Re-engagement

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Push notification (mobile, opted-in) | 5–15% open rate | Medium | Varies heavily by relevance and timing |
| Triggered email (behavior-based) | 15–35% open rate, 3–8% click rate | Medium | vs. 20–25% open / 2–3% click for broadcast |
| In-app notification (unread badge) | +8–15% return visit rate | Medium | For users who haven't visited in 7+ days |
| Weekly digest email | +5–10% WAU for churned users | Low–Medium | High variance; depends on content quality |
| Re-engagement campaign (30-day inactive) | 8–20% reactivation rate | Medium | |
| Notification preference center added | −15–30% unsubscribe rate | Medium | Reduces churn from notification fatigue |

**Important caveat:** Notification features have high variance. The same feature can produce 2× or 0.5× these benchmarks depending on content relevance, user segment, and send timing. Treat all notification estimates as Low–Medium confidence without internal data.

---

## Checkout & Conversion Flows

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Checkout step consolidated (3→1 page) | +15–35% completion rate | Medium | Higher end for mobile |
| Form field removed | +3–8% completion per field removed | Medium | Diminishing returns after first 2–3 removals |
| Guest checkout added | +20–45% checkout completion (consumer) | Medium | Lower impact for B2B where accounts are expected |
| Trust signal / security badge added | +3–10% checkout conversion | Low–Medium | Mostly impacts first-time buyers |
| Credit card autofill / Apple Pay added | +10–20% mobile checkout completion | Medium | |
| Pricing clarity improved | +5–15% plan selection rate | Low–Medium | Depends on whether confusion was the actual barrier |
| Free trial added (no credit card) | +20–50% top-of-funnel signups | Medium | With 15–30% conversion to paid at end of trial |
| Money-back guarantee prominently added | +5–12% conversion | Low–Medium | |

---

## Collaboration & Sharing

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Invite teammates feature added (B2B) | 0.2–0.8 viral coefficient | Medium | Each active user invites 0.2–0.8 additional activating users |
| Real-time collaboration added | +15–30% D30 retention for teams | Medium | Assumes collaboration creates genuine shared work product |
| Shareable links / public sharing | +10–25% organic acquisition from sharing | Low–Medium | High variance; depends on shareability of content |
| Comment / annotation feature added | +8–18% session depth for collaborative users | Medium | |
| @mention notifications | +10–20% return visit rate | Medium | For users who are mentioned |

---

## Self-Serve & Support Deflection

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Help center / knowledge base launched | 10–25% ticket deflection | Medium | First 90 days; deflection grows as content matures |
| In-app contextual help added | 8–20% deflection for tier-1 issues | Medium | |
| Chatbot (FAQ-based) | 15–35% deflection for scripted scenarios | Medium | Falls sharply for complex or emotional issues |
| AI-assisted support (generative) | 20–45% deflection | Low–Medium | High variance; 2024 data still maturing |
| Self-serve account management | 30–60% reduction in account-change tickets | High analogue | Based on documented deployments |
| In-app status page / incident alerts | 40–70% reduction in "is it down?" tickets | High analogue | Very consistent across deployments |

**Cost model:** Average fully-loaded cost per support ticket: $8–25 (tier-1), $25–80 (tier-2), depending on team location and tooling.

---

## Personalization & Recommendations

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Collaborative filtering recommendations | +5–20% content consumption per session | Low–Medium | Requires sufficient data density; weak for new products |
| "Recently viewed" history | +3–8% return engagement | Medium | |
| Personalized homepage / dashboard | +8–18% D30 retention | Low–Medium | High implementation variance |
| Behavioral email (based on in-app actions) | +25–60% open rate vs. broadcast | Medium | |
| Personalized empty states | +5–15% activation | Medium | Works best for products with diverse use cases |

**Important caveat:** Recommendation quality is the dominant variable. Poor recommendations actively hurt engagement. Without model quality validation, treat all recommendation lift estimates as Low confidence.

---

## Pricing & Packaging Changes

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Price increase (10%) | −2–8% new customer volume, +8–10% ARPU | Low–Medium | Net revenue impact typically positive in SaaS |
| New tier added (mid-market) | +15–30% expansion MRR if positioned correctly | Low | Highly dependent on positioning |
| Usage-based pricing introduced | +20–40% expansion MRR for high-usage accounts | Low–Medium | Loss of predictability for low-usage accounts |
| Annual plan discount added | 20–40% of new signups choose annual | Medium | Typical range across SaaS; improves cash flow and retention |
| Free tier introduced | +30–80% top-of-funnel volume | Medium | Conversion to paid: 2–8% for freemium |

---

## Mobile & Performance Improvements

| Improvement Type | Typical Lift | Confidence | Notes |
|-----------------|-------------|------------|-------|
| Page load time −1 second | +2–8% conversion rate (e-commerce) | Medium | Google/Deloitte research; lower for B2B SaaS |
| Core Web Vitals improvement to "Good" | +1–5% organic search ranking improvement | Low–Medium | Indirect effect; content quality dominates |
| Mobile app vs. mobile web | +20–40% session depth on mobile | Medium | App users are higher intent; selection effect present |
| Offline mode added | +10–25% retention for mobile-primary users | Low–Medium | Only relevant when connectivity is actually a problem |
| Dark mode added | Minimal measurable impact on retention | Low | High satisfaction, low retention impact |

---

## Feature Adoption Benchmarks

How many users typically adopt a new feature within 90 days of launch:

| Adoption Type | Typical Range | Notes |
|--------------|--------------|-------|
| Actively promoted (in-app tour + email) | 25–50% of eligible users | |
| Passively discoverable (in nav, no promotion) | 5–20% of eligible users | |
| Power-user feature (advanced, not promoted) | 2–10% of eligible users | |
| Opt-in notification / communication feature | 15–40% opt-in rate | |
| New default behavior (replaces existing) | 60–90% transition within 60 days | |

**Adoption vs. engagement:** First use ≠ habitual use. For features where habit formation matters, reduce adoption estimates by 40–60% to get "habitual adoption" (used 2+ times in 30 days).

---

## Using These Benchmarks

1. **Always flag the source.** When using these numbers, note "based on industry benchmarks" in the confidence column — never present them as internal data.

2. **Adjust for product maturity.** Early-stage products (<$1M ARR, <10K users) tend to show higher variance and often outperform or underperform benchmarks significantly.

3. **Adjust for segment.** Enterprise segments, developer audiences, and highly technical users often respond differently than consumer or SMB benchmarks suggest.

4. **Prefer the conservative end.** When in doubt, use the lower end of the range. Features that outperform a conservative estimate are welcome surprises; features that underperform an optimistic estimate create credibility damage.

5. **One benchmark, one confidence level.** Never average two weak analogues to get a medium-confidence estimate. Two Low confidence inputs combined are still Low confidence.
