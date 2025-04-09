import yfinance as yf
from datetime import datetime
import json
from pathlib import Path

from core.config import STOCK_SOURCES, VOLUME_MIN, MAX_RESULTS, SORT_BY

# Basisverzeichnis des Add-ons bestimmen
BASE = Path(__file__).resolve().parent.parent


def load_tickers(limit=None):
    combined = {}

    for filepath in STOCK_SOURCES:
        full_path = BASE / filepath
        if not full_path.exists():
            print(f"⚠️ Datei nicht gefunden: {full_path} – wird übersprungen.")
            continue

        try:
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    combined.update(data)
                else:
                    print(f"⚠️ Datei {full_path} ist kein Dictionary – wird ignoriert.")
        except Exception as e:
            print(f"⚠️ Fehler beim Laden von {full_path}: {e}")

    if limit:
        combined = dict(list(combined.items())[:limit])

    return combined


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
        output_dir = BASE / "data"
        output_dir.mkdir(parents=True, exist_ok=True)

        out_file = output_dir / "filtered_stocks.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(filtered, f, indent=4)

    return filtered
