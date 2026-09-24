"""A deliberately thin test suite - a good starting point for
"Claude, increase coverage" exercises.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.data_loader import load_rows, revenue_by_region, total_revenue


def test_rows_load():
    rows = load_rows()
    assert len(rows) > 0


def test_total_revenue_is_positive():
    rows = load_rows()
    assert total_revenue(rows) > 0


def test_regions_present():
    rows = load_rows()
    by_region = revenue_by_region(rows)
    assert "North" in by_region
