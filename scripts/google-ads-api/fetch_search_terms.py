#!/usr/bin/env python3
"""Pull the Search Terms report from Google Ads and save it as CSV into
data/search-term-reports/, in the format the weekly review already expects.

Usage:
    python fetch_search_terms.py [days]   # default 7 days

Reads credentials from a local .env file (see .env.example) — create that
file first with your real values. Returns 0 rows with no error if there's
no campaign traffic yet (expected pre-launch).
"""
import csv
import datetime
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

load_dotenv(Path(__file__).parent / ".env")

CUSTOMER_ID = os.environ.get("GOOGLE_ADS_CUSTOMER_ID", "").replace("-", "")
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "data" / "search-term-reports"


def main(days: int = 7) -> None:
    if not CUSTOMER_ID:
        sys.exit("Set GOOGLE_ADS_CUSTOMER_ID in scripts/google-ads-api/.env")

    client = GoogleAdsClient.load_from_env()
    ga_service = client.get_service("GoogleAdsService")

    end = datetime.date.today()
    start = end - datetime.timedelta(days=days)

    query = f"""
        SELECT
          search_term_view.search_term,
          campaign.name,
          ad_group.name,
          metrics.impressions,
          metrics.clicks,
          metrics.cost_micros,
          metrics.conversions,
          metrics.conversions_value
        FROM search_term_view
        WHERE segments.date BETWEEN '{start.isoformat()}' AND '{end.isoformat()}'
        ORDER BY metrics.clicks DESC
    """

    rows = []
    try:
        stream = ga_service.search_stream(customer_id=CUSTOMER_ID, query=query)
        for batch in stream:
            for row in batch.results:
                rows.append(
                    [
                        row.search_term_view.search_term,
                        row.campaign.name,
                        row.ad_group.name,
                        row.metrics.impressions,
                        row.metrics.clicks,
                        row.metrics.cost_micros / 1_000_000,
                        row.metrics.conversions,
                        row.metrics.conversions_value,
                    ]
                )
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Google Ads API error: {error.message}", file=sys.stderr)
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"search-terms-{start.isoformat()}_{end.isoformat()}.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "search_term",
                "campaign",
                "ad_group",
                "impressions",
                "clicks",
                "cost",
                "conversions",
                "conversions_value",
            ]
        )
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    days_arg = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    main(days_arg)
