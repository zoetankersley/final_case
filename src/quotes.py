import json
import random
import os
from collections import Counter

QUOTES_FILE = os.path.join(os.path.dirname(__file__), "../assets/quotes.json")
with open(QUOTES_FILE, "r", encoding="utf-8") as f:
    quotes_data = json.load(f)

category_counter = Counter()

def get_random_quote(category=None):
    """
    Return a random quote.
    If category is provided, filter by category.
    """
    filtered = quotes_data
    if category:
        filtered = [q for q in quotes_data if q.get("category", "").lower() == category.lower()]
        if not filtered:
            return {"quote": "No quotes found for this category.", "author": "", "category": category}

    quote = random.choice(filtered)
    cat = quote.get("category", "general")
    category_counter[cat] += 1
    return quote

def get_metrics():
    """Return the number of requests per category."""
    return dict(category_counter)

