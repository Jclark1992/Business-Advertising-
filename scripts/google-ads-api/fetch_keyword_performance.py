#!/usr/bin/env python3
"""Pull keyword-level performance from Google Ads and save as CSV into
data/keyword-reports/.

Usage:
    python fetch_keyword_performance.py [days]   # default 30 days

Reads credentials from a local .env file (see .env.example).
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
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "data" / "keyword-reports"


def main(days: int = 30) -> None:
    if not CUSTOMER_ID:
        sys.exit("Set GOOGLE_ADS_CUSTOMER_ID in scripts/google-ads-api/.env")

    client = GoogleAdsClient.load_from_env()
    ga_service = client.get_service("GoogleAdsService")

    end = datetime.date.today()
    start = end - datetime.timedelta(days=days)

    query = f"""
        SELECT
          campaign.name,
          ad_group.name,
          ad_group_criterion.keyword.text,
          ad_group_criterion.keyword.match_type,
          metrics.impressions,
          metrics.clicks,
          metrics.cost_micros,
          metrics.conversions,
          metrics.conversions_value,
          metrics.ctr,
          metrics.average_cpc
        FROM keyword_view
        WHERE segments.date BETWEEN '{start.isoformat()}' AND '{end.isoformat()}'
        ORDER BY metrics.cost_micros DESC
    """

    rows = []
    try:
        stream = ga_service.search_stream(customer_id=CUSTOMER_ID, query=query)
        for batch in stream:
            for row in batch.results:
                rows.append(
                    [
                        row.campaign.name,
                        row.ad_group.name,
                        row.ad_group_criterion.keyword.text,
                        row.ad_group_criterion.keyword.match_type.name,
                        row.metrics.impressions,
                        row.metrics.clicks,
                        row.metrics.cost_micros / 1_000_000,
                        row.metrics.conversions,
                        row.metrics.conversions_value,
                        row.metrics.ctr,
                        row.metrics.average_cpc / 1_000_000,
                    ]
                )
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Google Ads API error: {error.message}", file=sys.stderr)
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"keywords-{start.isoformat()}_{end.isoformat()}.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "campaign", "ad_group", "keyword", "match_type",
                "impressions", "clicks", "cost", "conversions",
                "conversions_value", "ctr", "avg_cpc",
            ]
        )
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    days_arg = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    main(days_arg)
