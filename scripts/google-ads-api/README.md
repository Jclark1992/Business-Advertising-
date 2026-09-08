# Google Ads API setup — where the developer token actually goes

You have a **Google Ads API developer token (Basic access)**. It's a
private, server-side credential for pulling data/making changes via code —
it does not go on your website, and it does not go into Google Tag Manager.
It also must never be pasted into this chat or committed to git in
plaintext (this repo's `.gitignore` already excludes `.env`).

A developer token alone can't authenticate anything — you also need an
OAuth Client ID/Secret and a refresh token, one time, from your own Google
account. Here's the full path, in order.

## 1. Create an OAuth Client ID (one-time, ~5 minutes)

1. Go to [Google Cloud Console](https://console.cloud.google.com/) and
   create a project (or use an existing one).
2. **APIs & Services > Library** — search for "Google Ads API" and enable it.
3. **APIs & Services > OAuth consent screen** — set it up for "External"
   (or "Internal" if you're on Google Workspace), add your own email as a
   test user if prompted.
4. **APIs & Services > Credentials > Create Credentials > OAuth client ID**
   — Application type: **Desktop app**. Save it; you'll get a Client ID and
   Client Secret.

## 2. Generate a refresh token (one-time, run on your own computer)

This has to run on a machine with a browser, not in a cloud session —
it opens a Google sign-in window for you to approve access to your own
Ads account.

```bash
cd scripts/google-ads-api
pip install google-auth-oauthlib
python get_refresh_token.py <your_client_id> <your_client_secret>
```

Sign in with the Google account that has access to the Ads account, approve
access, and the script prints a refresh token in your terminal.

## 3. Find your Customer ID

Top-right of the Google Ads UI when logged into the account — a 10-digit
number like `123-456-7890`. Use it without the dashes.

## 4. Fill in `.env`

```bash
cp .env.example .env
```

Then open `.env` and fill in the five values you now have: developer
token, client ID, client secret, refresh token, customer ID. Leave
`GOOGLE_ADS_LOGIN_CUSTOMER_ID` blank unless the account sits under a
manager (MCC) account. **`.env` stays on your machine — never commit it,
never share it, never paste its contents into a chat.**

## 5. Install dependencies and test

```bash
pip install -r requirements.txt
python fetch_search_terms.py 7
```

This writes a CSV into `data/search-term-reports/`. Pre-launch (no
campaigns running yet), it'll succeed with 0 rows — that's expected and
confirms the credentials work. Once campaigns are live, run it weekly (or
schedule it) and the weekly review process picks up the export
automatically — see `reports/optimization-framework.md`.

## Security notes

- Developer token, client secret, and refresh token are all equivalent to
  passwords for your Ads account — store them only in `.env`, never in
  code, commit messages, or chat.
- If any of these ever leak (accidentally committed, pasted somewhere
  public), revoke and regenerate them immediately: refresh token via
  Google Account > Security > Third-party access; client secret by
  resetting it in Cloud Console; developer token by contacting Google Ads
  API support if you suspect real compromise.
