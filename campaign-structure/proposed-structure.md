# Campaign Structure & Launch Checklist — Laser Hair Removal Only

Status: **pre-launch.** No campaigns are running yet. This is the plan to
launch with, plus the prerequisites that need to be true before spend starts.

## Structure

```
Account: Bare Laser & Skin Studio
└── Campaign: Laser Hair Removal (Search)
    ├── Ad Group: General Laser Hair Removal — Edmonton   [Phase 1]
    ├── Ad Group: West Edmonton / Near Me                  [Phase 1]
    ├── Ad Group: Brazilian Laser Hair Removal             [Phase 1]
    ├── Ad Group: Brazilian + Underarms                    [Phase 2]
    └── Ad Group: Underarms / Legs / Bikini                [Phase 2]
```

One campaign, five ad groups — matches `keyword-research/keyword-list.md`
and `ad-copy/rsa-drafts.md` exactly. Do not add IPL/facial/skin-rejuvenation
campaigns here; that's explicitly out of scope for this account.

## Budget reality check ($8/day)

$8/day (~$240/month) is a real constraint on a single-location home studio
— worth being upfront about what it actually buys. Edmonton "laser hair
removal" terms commonly run several dollars per click, so $8/day likely
means somewhere in the range of **1–4 clicks/day** to start. That's not
enough to run all 5 ad groups at once and still get a meaningful read on
any of them within weeks — the budget would get split so thin that no
single ad group accumulates enough clicks/conversions to judge.

**Phasing plan:**

- **Phase 1 (launch with this):** General Laser Hair Removal — Edmonton +
  West Edmonton / Near Me (broadest reach, lowest-friction entry points)
  + Brazilian Laser Hair Removal (explicitly the highest-emphasis service).
  All the campaign budget concentrates on these three.
- **Phase 2 (enable once there's a real signal):** Brazilian + Underarms,
  and Underarms / Legs / Bikini — turn these on once Phase 1 has run long
  enough to show what's converting (or once budget increases), not on a
  fixed calendar date.

This is a recommendation, not a rule — say the word if you'd rather launch
all five thin and see what happens, but the honest expectation at $8/day is
slower, noisier data that way.

## Pre-launch checklist (blockers, in order)

1. **Conversion tracking working end-to-end.** Booking completions and/or
   phone calls and/or contact form fills must fire a trackable conversion
   before any spend starts — otherwise "optimization" has no signal to work
   from and every later recommendation is a guess. This is the single
   biggest prerequisite.
2. **Google Ads conversion tag placed on the website** (or Google Tag
   Manager container installed) — see the setup notes you're working
   through separately for token placement.
3. Landing page confirmed relevant to laser hair removal specifically
   (not a generic homepage covering every service) — Google's Quality Score
   and ad relevance both depend on this, and it stops IPL/facial visitors
   from clicking a laser hair removal ad.
4. Google Business Profile linked for location extensions.
5. ~~Budget and daily cap decided~~ — done, $8/day (see Budget below).

## Targeting

- **Location:** Radius/location targeting centered on 17003 67 Ave NW,
  Edmonton, prioritizing West Edmonton/Callingwood and the neighbourhoods
  listed in `business-profile/overview.md`. Use **Presence** targeting
  (people in or regularly in the area) rather than "Presence or interest,"
  since a home-based studio needs people who can realistically show up.
- **Ad schedule:** Run search ads **continuously (24/7)**, not restricted
  to the hours below. Website booking via the "Book Now" button works any
  time, and people research/decide on personal care services in the
  evening even when they'll book or come in later — cutting ads off
  outside business hours would lose exactly that research-then-book
  behavior. Restrict live phone availability instead, at the extension
  level (see Extensions below), not the ad schedule.
- **Business hours (for call extension scheduling, not ad scheduling):**

  | Day | Hours |
  |---|---|
  | Monday | 4:30pm – 8:30pm |
  | Tuesday | 5:30pm – 8:30pm |
  | Wednesday | 4:30pm – 8:30pm |
  | Thursday | 5:30pm – 8:30pm |
  | Friday | 3:00pm – 8:00pm |
  | Saturday | 9:00am – 3:00pm |
  | Sunday | 9:00am – 3:00pm |

- **Devices:** Watch mobile vs. desktop performance separately once data
  exists (see `reports/optimization-framework.md`); don't assume evenly.

## Bidding

- **Start:** Manual CPC (or Maximize Clicks with the $8 daily cap as a hard
  ceiling) while there's no conversion history — at this budget the goal
  in week 1-4 is clean, affordable data, not volume. Keep max CPC modest
  enough that the account isn't spending its whole day's budget on one or
  two clicks — check actual Edmonton CPC ranges (Keyword Planner, or the
  `scripts/google-ads-api/` tooling) before setting a number.
- **Move to Maximize Conversions** once conversion tracking is verified
  and a small amount of data exists — note that at $8/day this will likely
  take longer than it would on a bigger budget, and that's expected, not
  a sign something's wrong.
- **Move to Target CPA** only once there's a statistically meaningful
  number of conversions (roughly 30+/month) — not before, since Smart
  Bidding with too little data optimizes toward noise. At $8/day this
  threshold may take several months; don't force it early.

## Budget

**$8/day (~$240/month).** See "Budget reality check" above for what that
actually buys and the phasing plan it implies. The optimization-framework
rule applies from day one regardless: reduce wasted spend (irrelevant
search terms, underperforming ad groups) before increasing budget — don't
chase volume at the expense of lead quality. At this budget size, every
wasted click is a meaningfully larger share of the day's spend than it
would be on a bigger account, so the weekly search-term review matters more
here, not less.

## Extensions to enable at launch

- **Call extensions** (click-to-call) — use the "Advanced options" call
  scheduling in Google Ads to only show the clickable number during actual
  business hours (table above), so mobile users aren't prompted to call
  when no one can pick up. The ad itself still runs 24/7; only the call
  button is time-gated.
- **Location extension** (linked Google Business Profile)
- **Sitelinks, callouts** (see `ad-copy/rsa-drafts.md`) — add a "Book
  Online" sitelink pointing straight at the website's Book Now flow, since
  that channel works regardless of hours.
- **Text/SMS:** Google Ads doesn't have a simple native click-to-text
  extension for a standard business phone line (that requires Business
  Messages setup, likely overkill here) — keep texting as something
  mentioned in ad copy/sitelinks rather than a dedicated extension for now.
- **Price extensions**, only once real package pricing is confirmed.
