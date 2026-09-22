# Launch Setup Guide — Exact Steps

Do these in order. Part 2 (conversion tracking) must be done and verified
*before* Part 3 (turning campaigns on) — launching first and tracking later
means burning budget with no way to tell what worked.

---

## Part 1: Create the Google Ads account

1. Go to [ads.google.com](https://ads.google.com) and sign in with the
   Google account you'll manage this with (ideally the same one tied to
   your Google Business Profile).
2. If prompted with the "Smart campaign" quick-setup flow, look for
   **"Switch to Expert Mode"** (small link, easy to miss) — Smart Campaigns
   hide the controls this plan depends on (manual keywords, ad groups,
   negative keywords).
3. Business info: name **Bare Laser & Skin Studio**, currency **CAD**,
   time zone **Edmonton (Mountain Time)**. Currency/time zone can't be
   changed later without creating a new account, so double-check both.
4. Add a billing method (Settings > Billing).
5. **Tools & Settings > Setup > Linked accounts > Google Business Profile**
   — link it now if it isn't already. This enables location extensions
   later and is a one-time step.

---

## Part 2: Conversion tracking (the blocker — do this before Part 3)

You have three booking channels: website Book Now button, phone calls, and
texts. Track what's realistic to track well rather than forcing all three.

### 2a. Install Google Tag Manager on the website (do this once)

Using Google Tag Manager (GTM) instead of pasting the Ads tag straight into
the site means every future tag (Ads conversion, Analytics, anything else)
gets added from one dashboard without touching site code again.

1. Go to [tagmanager.google.com](https://tagmanager.google.com), create an
   account, then a container for `barelaserandskinstudio.ca` (type: Web).
2. You'll get a container ID like `GTM-XXXXXXX` and two code snippets (one
   for `<head>`, one right after `<body>`).
3. **Where to paste them depends on what the website is built on** — tell
   me the platform (Wix / Squarespace / WordPress / Shopify / custom-coded)
   and I'll give you the exact click path. General locations:
   - **Wix:** Settings > Custom Code (or Marketing Integrations > Google
     Tag Manager, if that panel exists on your plan)
   - **Squarespace:** Settings > Advanced > Code Injection (Header/Footer)
   - **WordPress:** a tag-manager plugin (e.g. "GTM4WP"), or paste directly
     into the theme's header.php / footer.php if no page builder is in use
   - **Shopify:** Online Store > Themes > Edit code > `theme.liquid`, or
     Settings > Customer events (custom pixel)
   - **Custom-coded site:** directly in the HTML template, head/body as
     GTM instructs
4. Publish the site and confirm GTM is firing: install the
   [Tag Assistant](https://tagassistant.google.com) Chrome extension,
   visit the live site, and check it detects the container.

### 2b. Set up the "Book Now" conversion

1. In Google Ads: **Tools & Settings > Conversions > + New conversion
   action > Website**.
2. Category: **Book an appointment** (or "Submit lead form" if that fits
   better once you see the category list). Name it something clear like
   `Book Now Click`. Value: leave as "Don't use a value" unless you want to
   assign a dollar figure per booking. Count: **One** (one conversion per
   click, not every click on the page).
3. Google Ads generates a **Conversion ID + Conversion Label** — copy
   these, you'll need them in GTM next.
4. In GTM: **Tags > New > Google Ads Conversion Tracking**. Paste the
   Conversion ID/Label in.
5. **Trigger:** depends on how "Book Now" behaves on the site:
   - If clicking Book Now takes visitors to a separate booking
     confirmation/thank-you page (common with Vagaro-style embedded
     booking), use a **Page View trigger** on that confirmation URL.
   - If it's a button/modal with no distinct confirmation URL, use a
     **Click trigger** targeting that button (GTM's "Click Element"
     variables, matched by button text/ID/class — Preview mode in GTM
     will show you the button's actual attributes when you click it).
6. Save, then use **GTM Preview mode** to click Book Now on the live
   preview and confirm the tag fires. Publish the container.
7. Back in Google Ads, place a real test booking (or as close as you can
   get) and check **Tools & Settings > Conversions** — it should show a
   recent conversion within 24 hours.

### 2c. Set up call tracking (simpler, lower-effort option)

Full dynamic number tracking (swapping your displayed number automatically
to detect calls from the website) is more setup than a solo home-based
studio needs right now. Start with the simpler option:

1. When you add the **call extension** in Part 3, Google Ads
   automatically offers a **"Calls from ads"** conversion action — turn
   this on (Tools & Settings > Conversions, it may already appear as
   "Calls from ads extensions or call-only ads"). This counts when someone
   taps the phone number shown on a mobile ad. No extra code needed.
2. This won't capture calls from someone who found your number on the
   website itself (not the ad) — that's fine for now. Note it as a known
   gap in `reports/optimization-framework.md`'s data if it matters later.

### 2d. Texts

No reliable native tracking for texts to a regular business line without
a much bigger setup (Google Business Messages). Don't try to force this —
just ask new clients how they found you / whether they texted, and factor
that anecdotally. Revisit only if texts become a major booking channel.

### 2e. Verify before moving on

Confirm at least the Book Now conversion (2b) is firing correctly. This is
the one non-negotiable prerequisite — don't proceed to Part 3 without it.

---

## Part 3: Build the campaign

Reference while building: `keyword-research/keyword-list.md`,
`negative-keywords/negative-keyword-list.md`, `ad-copy/rsa-drafts.md`.

1. **Campaigns > + New campaign.**
2. Objective: **Leads**. Conversion goals: select the Book Now action (and
   Calls from ads, once available). Campaign type: **Search**.
3. Name: `Laser Hair Removal`.
4. Networks: **uncheck** "Search Network partners" and **uncheck** "Display
   Network" if either is auto-checked — stay on Google Search only, budget
   is too tight to dilute into partner/display inventory.
5. **Locations:** choose "Enter another location" > drop a pin at 17003 67
   Ave NW, Edmonton > set a radius (start ~8km, covering the neighbourhoods
   in `business-profile/overview.md`). Under location options, set
   **"Presence: People in or regularly in your targeted locations"** —
   not "Presence or interest."
6. **Languages:** English.
7. **Budget:** $8.00/day.
8. **Bidding:** Manual CPC (select "or, you can select a bid strategy
   directly" to skip the Smart Bidding recommendation prompt initially) —
   or Maximize Clicks with a max CPC cap. See
   `campaign-structure/proposed-structure.md` Bidding section for when to
   graduate off this.
9. **Ad schedule:** leave running all hours/days (don't restrict here —
   see the "why" in `proposed-structure.md`).
10. Create **3 ad groups** for Phase 1 (skip the other 2 for now):
    - `General Laser Hair Removal — Edmonton`
    - `West Edmonton / Near Me`
    - `Brazilian Laser Hair Removal`
11. For each ad group, paste its keyword list from
    `keyword-research/keyword-list.md` (use the bracketed match type —
    Phrase `"..."` as shown).
12. Add the **account-level negative keywords** from
    `negative-keywords/negative-keyword-list.md` at
    **Tools & Settings > Negative keyword lists** (create one list, apply
    it to the campaign) — plus the ad-group-level cross-negatives noted
    there once all 5 groups exist.
13. For each ad group, create one **Responsive Search Ad** using the
    matching section of `ad-copy/rsa-drafts.md` (headlines + descriptions),
    and set the **final URL** to the laser-hair-removal-specific landing
    page (confirm this page exists and isn't the generic homepage).
14. Add **extensions** (now under "Assets"): call extension (with hours
    restricted to your business hours table), sitelinks, callouts,
    location extension — all per the Extensions section of
    `proposed-structure.md`.

---

## Part 4: Final check before enabling

- [ ] Book Now conversion verified firing (Part 2b, step 7)
- [ ] Landing page URL is laser-hair-removal-specific
- [ ] Only 3 ad groups active (Phase 1); Phase 2 ad groups built but left
      **paused** if you created them early
- [ ] Negative keyword list applied
- [ ] Call extension hours match actual business hours
- [ ] Budget shows $8.00/day, bidding is Manual CPC or capped Maximize Clicks
- [ ] Campaign status set to **Enabled** (last step — it stays paused/draft
      until you flip this)

Once live, the weekly review picks up from here — see
`reports/optimization-framework.md`.
