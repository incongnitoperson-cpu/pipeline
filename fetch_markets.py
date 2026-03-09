import requests
import json
import os

os.makedirs("data", exist_ok=True)

# Kalshi markets
kalshi_url = "https://api.elections.kalshi.com/trade-api/v2/markets"
params = {"limit": 1000}

kalshi_markets = []

while True:
    r = requests.get(kalshi_url, params=params)
    data = r.json()

    kalshi_markets.extend(data["markets"])

    cursor = data.get("cursor")
    if not cursor:
        break

    params["cursor"] = cursor

with open("data/kalshi.json", "w") as f:
    json.dump(kalshi_markets, f)

# Polymarket markets
poly_url = "https://gamma-api.polymarket.com/markets"

poly = requests.get(poly_url).json()

with open("data/polymarket.json", "w") as f:
    json.dump(poly, f)

print("done")
