# Bare Laser & Skin Studio — Google Ads Optimization Workspace

This repo is the working system for ongoing Google Ads strategy, keyword research,
and campaign optimization for **Bare Laser & Skin Studio** (Edmonton, AB).

**Scope: laser hair removal only** — not IPL, facials, skin rejuvenation, or
other services. See `business-profile/overview.md`.

**Status: pre-launch.** No campaigns are running yet. See
`campaign-structure/proposed-structure.md` for the launch checklist —
conversion tracking has to be working before spend starts.

## Important: what this system can and can't do

There is currently no Google Ads connector/API access wired into this session, so
nothing here can read your live account or push changes into Google Ads directly.
What this workspace *does* do:

- Keeps researched keyword lists, negative keywords, ad copy, and competitor
  intel up to date based on web research and whatever performance data you share.
- Turns your periodic Google Ads exports (Search Terms report, Keyword
  performance, Campaign performance) into a dated optimization report with
  specific, ready-to-apply recommendations.
- Reminds you weekly to review open recommendations.

**To close the loop, drop your Google Ads exports into
`data/search-term-reports/` (CSV, weekly is enough) and I'll turn them into
a report under `reports/`.** Recommendations get applied by you (or whoever
manages the account) in the Google Ads UI, then check them off in the report.

You have a Google Ads API developer token, which can automate that export
step — see `scripts/google-ads-api/README.md` for setup (it also covers
where the token actually goes, since it's not a website tag).

## Structure

- `business-profile/` — business details, positioning, service area, scope
- `keyword-research/` — keyword list, organized by ad group (laser hair removal only)
- `negative-keywords/` — running negative keyword list with rationale
- `ad-copy/` — RSA headline/description drafts by ad group
- `campaign-structure/` — campaign/ad group architecture + pre-launch checklist
- `scripts/google-ads-api/` — API scripts to pull reports automatically once set up
- `data/search-term-reports/` — Google Ads CSV exports land here (manual or via script)
- `reports/` — dated optimization reports + `optimization-framework.md`
  (the decision rules every recommendation follows)

## Weekly review

A recurring reminder fires weekly to review any open recommendations in
`reports/`. See `reports/README.md` for the review workflow.
