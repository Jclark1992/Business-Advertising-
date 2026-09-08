# Negative Keyword List — Laser Hair Removal Only

Scope is laser hair removal only, so everything adjacent — IPL, facials,
skin rejuvenation, pigmentation, other beauty services — gets negatived
even though a generic "laser and skin studio" search might otherwise seem
relevant.

## Account-level negatives (apply everywhere)

**Out-of-scope services (the business's own other services, kept out of
these campaigns on purpose)**
- ipl, "ipl treatment", photofacial, "skin rejuvenation", pigmentation,
  "chemical peel", microdermabrasion, facial, facials, botox, filler,
  microneedling, "laser skin resurfacing"

**Wrong service entirely**
- tattoo removal, "laser tattoo removal", hair transplant, "hair loss
  treatment", laser eye surgery, lasik, laser printer, laser pointer,
  laser cutting, laser engraving, veterinary, pet, dog, cat

**Job/career seekers**
- job, jobs, career, careers, hiring, resume, salary, "how to become",
  "laser technician course", training, certification, school

**DIY / at-home devices**
- diy, "at home", "home kit", "home use", walmart, amazon, "for sale",
  "laser hair removal machine", "ipl machine", "buy laser device"

**Free / mismatched price intent**
- free, "free trial", groupon (unless a Groupon-style promo is intentionally
  running)

**Other cities (confirm before excluding — see note)**
- calgary, toronto, vancouver, ontario, "bc" — holding these as negatives
  since the business is a single home-based Edmonton studio; remove if
  you're willing to serve clients travelling from other Alberta cities.

## Ad-group-level negatives

**General Laser Hair Removal — Edmonton**
- No group-specific negatives beyond account-level; this group intentionally
  catches broader "laser hair removal edmonton"-type queries.

**Brazilian / Brazilian+Underarms / Underarms-Legs-Bikini groups**
- Cross-negative each specific-area group against the others so a
  "brazilian" search doesn't also trigger the "legs" ad group, e.g. add
  "leg"/"legs" as a negative on the Brazilian group, "brazilian" as a
  negative on the Legs/Bikini group, etc. Keeps reporting and ad relevance
  clean by area.

**West Edmonton / Near Me**
- Negative the specific body-area terms (brazilian, underarm, leg, bikini)
  here too if those already have dedicated ad groups, so this group only
  catches generic/location queries that don't specify an area.

## Comparison / competing-modality searches — do not blanket-negative

Terms like "laser hair removal vs waxing" or "laser vs threading" are
comparison shoppers actively deciding between hair removal methods — high
intent. Don't negative "waxing," "threading," "sugaring," or "epilator" as
broad terms; only negative the specific search term if it shows real spend
with zero conversion signal over a meaningful sample (see
`reports/optimization-framework.md`).

## Process

1. This list is the pre-launch baseline — apply before campaigns go live.
2. Once search term data exists, new negative candidates get proposed in
   the weekly report with the evidence (clicks, cost, conversions) behind
   each one — never negative a term just because it looks odd or hasn't
   converted from a handful of clicks.
3. Never negative a term that is actually converting.
