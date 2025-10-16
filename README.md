# 🗓️ Days of the Year

A lightweight, searchable Python dataset of **holidays**, **awareness days**, and **birthdays** around the world — with fuzzy search, date range filters, country filters, and more.

---

## 📦 Installation

```bash
pip install days-of-the-year
```

## 🚀 Quick Start
```python
from days_of_the_year import all_dates, get_day, search
```

Get all dates
```
print(all_dates())
```

Get everything for a specific date
```
print(get_day("02-01"))
```

## 🔍 Search Examples
Search by keyword
```
search("peace")
```

US-only results
```
search("peace", country="us")
```

Filter by date range
```
search(query="peace", start="01-01", end="01-10")
```

Filter by month
```
search(query="food", month="10")
```

Fuzzy match (partial similarity)
```
search("pea", fuzz_threshold=60)
```

Search birthdays only (exact match)
```
search("Billy Joel", return_types=["birthdays"], exact=True)
```

Limit results
```
search("health", flat=True, limit=10)
```

Flat results (great for APIs or exports)
```
flat_results = search("health", country="us", flat=True)
for item in flat_results:
    print(f"{item['date']} | {item['country']} | {item['type']} | {item['text']}")
```
## ⚙️ Function Reference
```get_day(date: str)```

Returns all info for a given date ("MM-DD").

```all_dates()```

Returns a list of all available date keys.

```search(...)```

Powerful search function to explore days, observances, and birthdays.

|Parameter|Type|Default|Description|
|---|---|---|---|
|`query`|`str`|`None`|Text to search (fuzzy or exact).|
|`country`|a [supported country code](#supported-countries) or `None`|None|Filter by country|.
|`start / end`|`"MM-DD"`|None|Filter by date range.|
|`month`|`"MM"`|`None`|Filter by month only.|
|`fuzz_threshold`|`int`|`70`|Fuzzy match sensitivity (0–100).|
|`return_types`|`list`|`["days", "part_of", "birthdays"]`|Which categories to include.|
|`flat`|`bool`|`False`|Return a flat list instead of a nested dict.|
|`limit`|`int`|`None`|Limit number of results returned.|
|`exact`|`bool`|`False`|Require exact (case-insensitive) match instead of fuzzy search.|

## Supported countries
Country|Code|
|---|---|
|USA|`us`|
|World|`world`|

## 📋 Example Output
Nested (default)
```
{
  "01-01": {
    "days": {
      "us": ["National Bloody Mary Day"],
      "world": ["Global Family Day"]
    },
    "part_of": {
      "world": ["Veganuary"]
    },
    "birthdays": ["J. Edgar Hoover"]
  }
}
```
Flat (flat=True)
```
[
  {
    "date": "01-01",
    "type": "days",
    "country": "us",
    "text": "National Bloody Mary Day"
  },
  {
    "date": "01-01",
    "type": "part_of",
    "country": "world",
    "text": "Veganuary"
  },
  {
    "date": "05-09",
    "type": "birthdays",
    "country": null,
    "text": "Billy Joel"
  }
]
```
## 🧠 Usage Examples
```from days_of_the_year import all_dates, get_day, search

# Print all dates
print("All available dates:")
print(all_dates())```

# Get everything on Feb 1
print("\nGet all info for February 1st:")
print(get_day("02-01"))

# Search by keyword
print("\nSearch for 'peace' related days:")
print(search("peace"))

# US-only results
print("\nSearch for 'peace' related days in the US:")
print(search("peace", country="us"))

# Between Jan 1 and Jan 10
print("\nSearch for 'peace' related days between Jan 1 and Jan 10:")
print(search(query="peace", start="01-01", end="01-10"))

# By month
print("\nSearch for 'food' related days in October:")
print(search(query="food", month="10"))

# Fuzzy match (pea vs peace)
print("\nFuzzy search for 'pea' related days with lower threshold:")
results = search("pea")
print(results)  # Might include “National Pea Day”, “National Peace Day”

# Restrict to US results
print("\nFuzzy search for 'pea' related days in the US:")
us_results = search("pea", country="us")
print(us_results)  # Might include “National Pea Day” only

# Broader search tolerance
print("\nFuzzy search for 'pea' related days with a more lenient threshold:")
lenient = search("pea", fuzz_threshold=60)
print(lenient)

# Find all US "peace"-related days
print("\nSearch for 'peace' related days in the US only, returning 'days' type:")
us_peace_related = search("peace", country="us", return_types=["days"])
print(us_peace_related)

# Search birthdays only
print("\nSearch for 'Billy Joel' in birthdays only (exact match):")
billy_joel_birthday = search("Billy Joel", return_types=["birthdays"], exact=True)
print(billy_joel_birthday)

# Search in both "part_of" and "days" within January
print("\nSearch for 'tea' in both 'days' and 'part_of' within January:")
tea_part_of_days = search("tea", month="01", return_types=["days", "part_of"])
print(tea_part_of_days)

# World only, May, part_of only
print("\nSearch for 'health' related 'part_of' days in May (worldwide):")
health_part_of_may_worldwide = search("health", country="world", month="05", return_types=["part_of"])
print(health_part_of_may_worldwide)

# Flat results
print("\nFlat results for 'health' related days in the US:")
flat_results = search("health", country="us", flat=True)
for item in flat_results:
    print(f"{item['date']} | {item['country']} | {item['type']} | {item['text']}")

# Limit results
print("\nLimited to 10 results for 'health' related 'part_of' days in May (worldwide, flat format):")
limited_results = search("health", country="world", month="05", return_types=["part_of"], flat=True, limit=10)
print(limited_results)
```

## 🧰 Development

Clone the repo and install locally:
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/days-of-the-year.git
cd days-of-the-year
pip install -e .
```

## 🧾 Requirements

Python 3.8+

rapidfuzz
 ≥ 3.9.0

## ⭐ Contributing

Pull requests welcome! New countries are always welcome
If you want to add new features, open an issue first to discuss your ideas.

## 🪶 Example Project Ideas

Daily “This Day in History” Telegram or Discord bot
Custom Home Assistant or calendar integration

## 📜 License
MIT

