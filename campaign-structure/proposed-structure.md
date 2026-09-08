# Proposed Campaign Structure

## Structure

```
Account: Bare Laser & Skin Studio
├── Campaign: Laser Hair Removal (Search)
│   ├── Ad Group: Brand/Location Core
│   ├── Ad Group: Brazilian / Full Body
│   └── Ad Group: Face / Underarm / Small Area
├── Campaign: IPL Treatments (Search)
│   └── Ad Group: IPL Skin Rejuvenation
├── Campaign: Facials & Skin Rejuvenation (Search)
│   └── Ad Group: Facials
├── Campaign: Near Me / Local Catch-all (Search)
│   └── Ad Group: General Local Intent
└── Campaign: Remarketing (Display) — Phase 2, once there's site traffic
```

Split by service (rather than one giant campaign) so budget, bids, and ad
copy can be tuned independently — laser hair removal will likely have far
higher search volume and different economics than facials.

## Targeting

- **Location:** Radius targeting centered on 17003 67 Ave NW, Edmonton
  (see `business-profile/overview.md` for radius assumptions) —
  `[CONFIRM exact radius]`. Use "Presence" targeting (people in/regularly in
  the area), not "Presence or interest," to avoid serving ads to people
  merely searching about Edmonton from elsewhere.
- **Ad schedule:** Align with business hours + a lead-in window (people
  research treatments in the evening even if booking during business hours)
  — `[CONFIRM hours]`.
- **Bidding:** Start with Maximize Conversions (or manual CPC if no
  conversion data yet) with a modest daily budget per campaign; move to
  Target CPA once ~30+ conversions/month of data exist.
- **Conversion tracking:** Confirm what's tracked today — booking completions
  (Vagaro), phone calls, contact form fills. This is the #1 prerequisite for
  any real optimization; without it, "optimization" is guesswork.
  `[CONFIRM — this is a blocker for smart bidding]`.

## Budget

`[CONFIRM monthly/daily budget]` — recommendations above assume a modest
single-location local services budget. Splits should weight toward Laser
Hair Removal first (highest intent + revenue), then IPL/Facials.

## Extensions to enable

- Call extensions (click-to-call, especially on mobile)
- Location extension (linked Google Business Profile)
- Sitelinks, callouts, structured snippets (see `ad-copy/rsa-drafts.md`)
- Price extensions if you want to publish package pricing
