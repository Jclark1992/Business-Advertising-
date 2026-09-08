# Bare Laser & Skin Studio — Google Ads Optimization Workspace

This repo is the working system for ongoing Google Ads strategy, keyword research,
and campaign optimization for **Bare Laser & Skin Studio** (Edmonton, AB).

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
If you'd rather not hand-export weekly, granting a Google Ads API/connector
later would let this become fully automatic — flag it if you want to pursue that.

## Structure

- `business-profile/` — what we know about the business, services, service area
- `keyword-research/` — seed, long-tail, and location-based keyword lists
- `negative-keywords/` — running negative keyword list with rationale
- `ad-copy/` — RSA headline/description drafts by ad group
- `campaign-structure/` — proposed campaign/ad group architecture
- `data/search-term-reports/` — drop your Google Ads CSV exports here
- `reports/` — dated optimization reports (the "update requests" for your review)

## Weekly review

A recurring reminder fires weekly to review any open recommendations in
`reports/`. See `reports/README.md` for the review workflow.
