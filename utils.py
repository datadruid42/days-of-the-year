from datetime import datetime

def parse_date(date_str: str):
    """Convert MM-DD to datetime using a leap-safe year (2000)."""
    return datetime.strptime(f"2000-{date_str}", "%Y-%m-%d")

def in_range(date_str: str, start=None, end=None):
    """Check if date_str (MM-DD) is within start/end (inclusive)."""
    if not start or not end:
        return True
    d = parse_date(date_str)
    return parse_date(start) <= d <= parse_date(end)
