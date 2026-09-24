"""Loads and aggregates the sales data.

Workshop note: this module works, but it is doing a lot by hand.
It is a good target for refactoring, caching and validation exercises.
"""

import csv
import os
from datetime import datetime

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sales.csv")


def load_rows():
    rows = []
    with open(DATA_PATH, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # amount is sometimes blank or contains a thousands separator
            amount = row["amount"].replace(",", "")
            if amount == "":
                amount = 0
            row["amount"] = float(amount)
            row["units"] = int(row["units"])
            rows.append(row)
    return rows


def parse_date(value):
    # only handles one format - other formats in the file silently break sorting
    return datetime.strptime(value, "%Y-%m-%d").date()


def total_revenue(rows):
    total = 0
    for r in rows:
        total = total + r["amount"]
    return total


def revenue_by_region(rows):
    out = {}
    for r in rows:
        region = r["region"]
        if region not in out:
            out[region] = 0
        out[region] = out[region] + r["amount"]
    return out


def revenue_by_product(rows):
    out = {}
    for r in rows:
        key = r["product"]
        if key not in out:
            out[key] = 0
        out[key] = out[key] + r["amount"]
    return out


def revenue_by_month(rows):
    out = {}
    for r in rows:
        month = r["date"][0:7]
        if month not in out:
            out[month] = 0
        out[month] = out[month] + r["amount"]
    return dict(sorted(out.items()))


def top_reps(rows, limit=5):
    out = {}
    for r in rows:
        out[r["rep"]] = out.get(r["rep"], 0) + r["amount"]
    ranked = sorted(out.items(), key=lambda kv: kv[1], reverse=True)
    return ranked[:limit]


def summary():
    rows = load_rows()
    return {
        "order_count": len(rows),
        "total_revenue": total_revenue(rows),
        "average_order": total_revenue(rows) / len(rows),
        "by_region": revenue_by_region(rows),
        "by_product": revenue_by_product(rows),
        "by_month": revenue_by_month(rows),
        "top_reps": top_reps(rows),
    }
