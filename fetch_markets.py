import requests
import json
import os

os.makedirs("data", exist_ok=True)

# -------- KALSHI --------
kalshi_url = "https://api.elections.kalshi.com/trade-api/v2/markets"

params = {"limit": 500}
kalshi_markets = []

for _ in range(10):  # hard stop after 10 pages
    r = requests.get(kalshi_url, params=params, timeout=20)
    data = r.json()

    kalshi_markets.extend(data.get("markets", []))

    cursor = data.get("cursor")
    if not cursor:
        break

    params["cursor"] = cursor

with open("data/kalshi.json", "w") as f:
    json.dump(kalshi_markets, f)

# -------- POLYMARKET --------
poly_url = "https://gamma-api.polymarket.com/markets"

r = requests.get(poly_url, timeout=20)
poly = r.json()

with open("data/polymarket.json", "w") as f:
    json.dump(poly, f)

print("done")
