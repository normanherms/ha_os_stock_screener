import yfinance as yf
from datetime import datetime
import json
import os

from core.config import STOCK_SOURCES

def load_tickers(limit=None):
    combined = {}

    for filepath in STOCK_SOURCES:
        if not os.path.exists(filepath):
            print(f"⚠️ Datei nicht gefunden: {filepath} – wird übersprungen.")
            continue

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    combined.update(data)
                else:
                    print(f"⚠️ Datei {filepath} ist kein Dictionary – wird ignoriert.")
        except Exception as e:
            print(f"⚠️ Fehler beim Laden von {filepath}: {e}")

    if limit:
        combined = dict(list(combined.items())[:limit])

    return combined


from core.config import VOLUME_MIN, MAX_RESULTS, SORT_BY

def fetch_and_filter(tickers: dict, threshold: float, output=True):
    entries = []

    for name, symbol in tickers.items():
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period="1d")

            if data.empty:
                continue

            latest = data.iloc[-1]
            change_pct = round((latest["Close"] - latest["Open"]) / latest["Open"] * 100, 2)
            volume = int(latest["Volume"])

            if abs(change_pct) >= threshold and volume >= VOLUME_MIN:
                impact_score = abs(change_pct) * (volume / 1_000_000)  # eigene Kennzahl
                info = {
                    "name": name,
                    "symbol": symbol,
                    "price": round(latest["Close"], 2),
                    "change_pct": change_pct,
                    "volume": volume,
                    "impact": round(impact_score, 2),
                    "timestamp": datetime.now().isoformat()
                }
                entries.append(info)

        except Exception as e:
            print(f"❌ Fehler bei {name} ({symbol}): {e}")

    # Sortieren nach Konfiguration
    if SORT_BY == "change":
        entries.sort(key=lambda x: abs(x["change_pct"]), reverse=True)
    elif SORT_BY == "volume":
        entries.sort(key=lambda x: x["volume"], reverse=True)
    else:  # Default: impact
        entries.sort(key=lambda x: x["impact"], reverse=True)

    # Begrenzen
    filtered = {entry["name"]: entry for entry in entries[:MAX_RESULTS]}

    # Optional speichern
    if output:
        os.makedirs("data", exist_ok=True)
        with open("data/filtered_stocks.json", "w", encoding="utf-8") as f:
            json.dump(filtered, f, indent=4)

    return filtered
