import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "days_of_the_year.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    _DATA = json.load(f)

def all_dates():
    """Return all available date keys (MM-DD)."""
    return list(_DATA.keys())

def get_day(date: str):
    """Return all info for a given date (MM-DD)."""
    return _DATA.get(date)
