from rapidfuzz import fuzz
from .core import _DATA
from .utils import in_range

supported_countries = ["us", "world"]
def search(
    query=None,
    country=None,
    start=None,
    end=None,
    month=None,
    fuzz_threshold=70,
    return_types=None,
    flat=False,
    limit=None,
    exact=False,
):
    """
    Search days, birthdays, and part_of entries by text, country, date range, or month.

    Parameters:
    - query: str (fuzzy or exact match, case-insensitive)
    - country: "us", "world", or None (search both)
    - start: "MM-DD" (optional)
    - end: "MM-DD" (optional)
    - month: "MM" (optional)
    - fuzz_threshold: int (0–100), fuzzy match threshold (ignored if exact=True)
    - return_types: list of ["days", "birthdays", "part_of"]
        Which data categories to search in. Default: all.
    - flat: bool
        If True, returns a flat list instead of grouping by date.
    - limit: int (optional)
        Maximum number of results to return (after filtering).
    - exact: bool
        If True, requires exact (case-insensitive) string matches.

    Returns:
    dict or list depending on flat flag
    """

    if return_types is None:
        return_types = ["days", "part_of", "birthdays"]

    results = [] if flat else {}

    def matches_query(entry: str) -> bool:
        """Decide whether an entry matches the query."""
        if not query:
            return True
        q = query.strip().lower()
        e = entry.strip().lower()
        if exact:
            return q == e
        return fuzz.partial_ratio(q, e) >= fuzz_threshold

    def add_result(date, section, country, text):
        if flat:
            results.append({
                "date": date,
                "type": section,
                "country": country,
                "text": text
            })
        else:
            results.setdefault(date, {}).setdefault(section, {}).setdefault(country, [])
            results[date][section][country].append(text)

    for date, info in _DATA.items():
        # --- Filter by month and range ---
        if month and not date.startswith(month):
            continue
        if not in_range(date, start, end):
            continue

        # --- DAYS and PART_OF ---
        for section in ("days", "part_of"):
            if section not in return_types:
                continue

            for c in (supported_countries if country not in supported_countries else [country]):
                entries = info.get(section, {}).get(c, [])
                for e in entries:
                    if matches_query(e):
                        add_result(date, section, c, e)
                        if limit and len(results) >= limit:
                            return results

        # --- BIRTHDAYS ---
        if "birthdays" in return_types:
            for e in info.get("birthdays", []):
                if matches_query(e):
                    add_result(date, "birthdays", None, e)
                    if limit and len(results) >= limit:
                        return results

    # Deduplicate & sort if not flat
    if not flat:
        for date_data in results.values():
            for section_data in date_data.values():
                for c, lst in section_data.items():
                    section_data[c] = sorted(set(lst))

    # Apply limit if flat and not hit early exit
    if flat and limit:
        results = results[:limit]

    return results
