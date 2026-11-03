#!/usr/bin/env python3
"""
Download Morocco World Bank indicator observations for 2000–2025.
Output:
data/worldbank_data.csv
Run: python fetch_worldbank_data.py
Dependency: requests (pip install requests)
"""
import csv
import time
from pathlib import Path
import requests

START_YEAR, END_YEAR = 2000, 2025
COUNTRY = "MA"
OUTPUT = Path("data/worldbank_data.csv")

INDICATORS = {
    "ER.H2O.FWTL.K3": "Annual freshwater withdrawals (billion cubic meters)",
    "AG.LND.IRIG.AG.ZS": "Agricultural land irrigated (%)",
    "SP.POP.GROW": "Population growth (annual %)",
    "AG.YLD.CREL.KG": "Cereal yield (kg per hectare)",
    "AG.LND.ARBL.ZS": "Arable land (% of land area)",
}

BASE_URL = "https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
FIELDS = [
    "country_code", "country_name", "year", "indicator_code",
    "indicator_name", "value", "unit", "obs_status", "decimal",
    "source_note", "source_organization",
]

def fetch_indicator(session, code, name):
    url = BASE_URL.format(country=COUNTRY, indicator=code)
    params = {
        "date": f"{START_YEAR}:{END_YEAR}",
        "format": "json",
        "per_page": 100,
        "page": 1,
    }
    rows = []
    while True:
        response = session.get(url, params=params, timeout=60)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, list) or len(payload) < 2:
            raise RuntimeError(f"Unexpected API response for {code}: {payload!r}")
        page_meta, observations = payload[0], payload[1] or []
        for obs in observations:
            rows.append({
                "country_code": COUNTRY,
                "country_name": (obs.get("country") or {}).get("value"),
                "year": int(obs["date"]),
                "indicator_code": code,
                "indicator_name": name,
                "value": obs.get("value"),
                "unit": obs.get("unit"),
                "obs_status": obs.get("obs_status"),
                "decimal": obs.get("decimal"),
                "source_note": (obs.get("indicator") or {}).get("value"),
                "source_organization": None,
            })
        if params["page"] >= int(page_meta.get("pages", 1)):
            break
        params["page"] += 1
    return rows

def main():
    session = requests.Session()
    session.headers.update({"User-Agent": "Morocco-Water-Scarcity-Research/1.0"})
    all_rows = []
    for code, name in INDICATORS.items():
        rows = fetch_indicator(session, code, name)
        print(f"{code}: {len(rows)} annual observations returned")
        all_rows.extend(rows)
        time.sleep(0.15)

    all_rows.sort(key=lambda r: (r["year"], r["indicator_code"]))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\nSaved: {OUTPUT.resolve()}")
    print(f"Rows: {len(all_rows)}")
    print(f"Year range requested: {START_YEAR}–{END_YEAR}")
    print("Note: World Bank missing observations are retained as blank values; they are not interpolated.")
    print("Use only complete observations for each analysis and report the effective sample size.")

if __name__ == "__main__":
    main()
