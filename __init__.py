"""
days_of_the_year
----------------
A searchable dataset of holidays, observances, and awareness days worldwide.

Example:
    from days_of_the_year import search, get_day

    search("blood", country="us")
    get_day("01-01")
"""

from .core import get_day, all_dates
from .search import search

__all__ = ["search", "get_day", "all_dates"]

__version__ = "0.2.0"
