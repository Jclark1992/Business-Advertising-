# Historical Campaign Analysis — October 7, 2026

First real-data report. Pulled directly from the Google Ads API (search
terms, keyword performance, campaign performance — all in
`data/*-reports/`), covering the previous campaigns that ran and were
paused. This explains what actually happened and what to carry forward
into the relaunch.

## What was found

**Two campaigns ran, not one, plus a third dormant one:**

| Campaign | Type | Ran | Spend | Clicks | Conversions |
|---|---|---|---|---|---|
| March 10, 2026 - Leads, Performance Max | Performance Max | 77 days | $377.55 | 2,953 | 2,153.6 (reported) |
| May 5, Leads-Search-2 | Search | 56 days | $289.99 | 251 | 3.0 |
| Website traffic-Search-1 | Search | — | $0 (never ran/no impressions) | 0 | 0 |

1. **The Performance Max campaign's reported conversion count (2,153.6) is not
   real.** $377.55 cannot plausibly buy 2,153 real bookings for a
   single-operator home studio. You've since confirmed conversion tracking
   wasn't hooked up correctly on that campaign at the time — so that
   number is noise, not signal, and nothing from that campaign's history
   should be trusted for decision-making. Separately, Performance Max runs
   across Search, Display, YouTube, Gmail, Discover, and Maps with Google
   controlling most of the targeting — the opposite of the tightly
   controlled, laser-hair-removal-only, local-radius approach this project
   is built around. Not recommending it be part of the relaunch.

2. **The real Search campaign ("May 5, Leads-Search-2") is usable data:**
   56 days, $289.99, 3 conversions ≈ **$96.66 cost per conversion**
   blended across the whole campaign.

3. **It ran almost entirely on Broad Match, with no ad-group segmentation
   by service area.** 320 keywords existed, but 194 of them (generic
   beauty-industry terms like "epilators," "beauty," "electrolysis,"
   "facial," "beauty salon," "brazilian waxing," "esthetician," "body
   sugaring") got **zero impressions** — not useful targeting, just
   clutter. All real spend ($261.22) and all clicks (206) came from the
   126 Broad Match keywords. Everything sat in one single ad group
   ("Ad group 1") instead of being split by Brazilian/underarms/legs/
   bikini/near-me the way this project's plan calls for.

4. **Broad Match caused real, quantifiable waste.** Looking at the actual
   search queries that triggered the ads (not just the keywords typed
   in): **42.6% of search-term spend ($75.60 of $177.38 trackable spend)
   went to queries unrelated to laser hair removal** — competitor/business
   names (`rejuvenation dermatology windermere edmonton`, `the vanity lab
   edmonton`, `serena clinic`, `lucere south`, `bellavera`, `off the hook
   st albert`, `laser sheer wem`), competing modalities (`brazilian wax
   near me`, `electrolysis edmonton`, `chemical peels edmonton`), and
   off-topic queries (`lip wrinkles removal`, `what age should i shave my
   arms`, `underarm whitening edmonton`, `laser hair removal groupon`).

5. **One single phrase drove all the real bookings.** The keyword
   `permanent facial hair removal near me` (Broad Match) — 305
   impressions, 17 clicks, $50.26, **3 conversions** — accounts for every
   tracked conversion in the Search campaign. Cost per conversion on just
   this keyword: **~$16.75**, dramatically better than the campaign's
   blended $96.66. By contrast, the single highest-spend keyword,
   `edmonton laser hair removal` (Broad), got 47 clicks for $55.30 and
   **zero conversions**.

6. **The dormant "Website traffic-Search-1" campaign** has 361 keywords
   including completely unrelated services (`pedicure`, `waxing`,
   `chemical peel`, `dermatologist`, `wax`) and even `laser hair removal`
   itself duplicated. It never spent anything, but it's account clutter
   that should be deleted before relaunch so it can't accidentally
   activate.

## What's recommended

- [ ] **Delete the "Website traffic-Search-1" campaign entirely** — unused, off-topic keyword list, no reason to keep it.
- [ ] **Do not resume the Performance Max campaign.** Its data is untrustworthy (broken tracking) and its automated, cross-network targeting conflicts with the controlled local-service strategy already planned.
- [ ] **Relaunch using Phrase/Exact match only, never Broad**, per the original campaign-structure plan — this is the single biggest fix. Broad Match is what let 42.6% of spend leak to irrelevant queries.
- [x] **Add `facial hair removal near me` / `permanent facial hair removal near me` style phrasing** to `keyword-research/keyword-list.md` — this is the one phrase with proven real-world conversion evidence, and the current list is weighted toward "laser hair removal edmonton" phrasing which, per this data, got real clicks but zero bookings. — *Done.*
- [x] **Add the following to `negative-keywords/negative-keyword-list.md`**, backed by real wasted spend:
  - Competitor/business names: `rejuvenation dermatology`, `windermere`, `vanity lab`, `serena clinic`, `lucere`, `bellavera`, `off the hook`, `laser sheer wem`
  - Off-topic/informational: `whitening`, `wrinkle`, `shave my arms`, `groupon`
  - (Electrolysis, chemical peel, waxing-as-standalone-term are already partially covered by the existing list — this confirms that coverage was the right call.)
- [ ] **Rebuild the ad group structure** on relaunch to match the plan (General / Brazilian / Brazilian+Underarms / Underarms-Legs-Bikini / Near-Me) instead of one flat ad group.

## Why

The account wasn't failing because laser hair removal isn't a viable
search category here — `permanent facial hair removal near me` proves
real demand exists and converts well. It was failing because Broad Match
let the budget leak to irrelevant and competitor traffic, and a lack of
ad group structure meant there was no way to see or control where the
money was actually going until now.

## Expected benefit

Relaunching with Phrase/Exact match only, informed by the one proven
converting phrase, and with the off-topic queries pre-negatived, should
meaningfully cut the ~43% wasted-spend rate seen here — meaning the same
$8-10/day budget should produce more real bookings, not just more clicks.

## Potential risk

Phrase/Exact match reduces reach compared to Broad, so expect fewer total
clicks per day than before — that's intentional (quality over volume) but
worth knowing going in, especially given the already-small daily budget.
There's also real uncertainty here from small sample size: 3 conversions
total is not a large enough number to be fully confident "facial hair
removal" phrasing will keep converting at the same rate — it's the
strongest signal available, not a guarantee.

## Open question

The search-term-level report shows a different converting query
(`rejuvenation dermatology windermere edmonton`, 2.0 conversions) than the
keyword-level report's converting keyword. This is likely just Google
withholding some very low-volume individual search queries from the
Search Terms report for privacy — not a data error — but flagging it since
it means the true "winning" query may differ slightly from what's shown
here.
