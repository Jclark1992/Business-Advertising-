#!/usr/bin/env python3
"""One-time helper to generate a Google Ads API refresh token.

Run this on YOUR OWN computer (it opens a browser window for you to sign
in and approve access) — not inside a cloud/CI environment. You need an
OAuth Client ID of type "Desktop app" first; see ../README.md step 1.

Usage:
    pip install google-auth-oauthlib
    python get_refresh_token.py <client_id> <client_secret>

Prints a refresh token. Paste it into .env as GOOGLE_ADS_REFRESH_TOKEN.
Treat it like a password: never commit it, never paste it into a chat
or anywhere else public.
"""
import sys

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/adwords"]


def main(client_id: str, client_secret: str) -> None:
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["http://localhost"],
            }
        },
        scopes=SCOPES,
    )
    credentials = flow.run_local_server(port=0)
    print("\nAdd this to scripts/google-ads-api/.env as GOOGLE_ADS_REFRESH_TOKEN:\n")
    print(credentials.refresh_token)
    print("\nDo not commit .env or share this value.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python get_refresh_token.py <client_id> <client_secret>")
    main(sys.argv[1], sys.argv[2])
