# Campaign Structure & Launch Checklist — Laser Hair Removal Only

Status: **pre-launch.** No campaigns are running yet. This is the plan to
launch with, plus the prerequisites that need to be true before spend starts.

## Structure

```
Account: Bare Laser & Skin Studio
└── Campaign: Laser Hair Removal (Search)
    ├── Ad Group: General Laser Hair Removal — Edmonton
    ├── Ad Group: Brazilian Laser Hair Removal
    ├── Ad Group: Brazilian + Underarms
    ├── Ad Group: Underarms / Legs / Bikini
    └── Ad Group: West Edmonton / Near Me
```

One campaign, five ad groups — matches `keyword-research/keyword-list.md`
and `ad-copy/rsa-drafts.md` exactly. Do not add IPL/facial/skin-rejuvenation
campaigns here; that's explicitly out of scope for this account.

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
5. Budget and daily cap decided (see Budget below).

## Targeting

- **Location:** Radius/location targeting centered on 17003 67 Ave NW,
  Edmonton, prioritizing West Edmonton/Callingwood and the neighbourhoods
  listed in `business-profile/overview.md`. Use **Presence** targeting
  (people in or regularly in the area) rather than "Presence or interest,"
  since a home-based studio needs people who can realistically show up.
- **Ad schedule:** Align with actual appointment availability — no point
  serving ads for times you can't book. `[CONFIRM hours/availability]`.
- **Devices:** Watch mobile vs. desktop performance separately once data
  exists (see `reports/optimization-framework.md`); don't assume evenly.

## Bidding

- **Start:** Manual CPC or Maximize Clicks with a firm daily cap while
  there's no conversion history — the goal in week 1-2 is clean data, not
  volume.
- **Move to Maximize Conversions** once conversion tracking is verified
  and a small amount of data exists.
- **Move to Target CPA** only once there's a statistically meaningful
  number of conversions (roughly 30+/month) — not before, since Smart
  Bidding with too little data optimizes toward noise.

## Budget

`[CONFIRM monthly/daily budget]`. Whatever the number, the rule from the
optimization framework applies from day one: reduce wasted spend (irrelevant
search terms, underperforming ad groups) before increasing budget — don't
chase volume at the expense of lead quality.

## Extensions to enable at launch

- Call extensions (click-to-call — especially valuable on mobile for a
  service business)
- Location extension (linked Google Business Profile)
- Sitelinks, callouts (see `ad-copy/rsa-drafts.md`)
- Price extensions, only once real package pricing is confirmed
