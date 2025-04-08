import yfinance as yf
from datetime import datetime
import json
import os

def load_tickers(filepath="data/all_stocks.json", limit=None):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        if limit:
            data = dict(list(data.items())[:limit])
        return data

def fetch_and_filter(tickers: dict, threshold: float, output=True):
    results = {}
    filtered = {}

    for name, symbol in tickers.items():
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period="1d")
            if data.empty:
                results[name] = {"error": "Keine Daten gefunden"}
                continue

            latest = data.iloc[-1]
            change_pct = round((latest["Close"] - latest["Open"]) / latest["Open"] * 100, 2)
            info = {
                "symbol": symbol,
                "price": round(latest["Close"], 2),
                "change_pct": change_pct,
                "volume": int(latest["Volume"]),
                "timestamp": datetime.now().isoformat()
            }
            results[name] = info

            if abs(change_pct) >= threshold:
                filtered[name] = info

        except Exception as e:
            results[name] = {"error": str(e)}

    if output:
        os.makedirs("data", exist_ok=True)
        with open("data/all_stocks.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        with open("data/filtered_stocks.json", "w", encoding="utf-8") as f:
            json.dump(filtered, f, indent=4)

    return filtered
