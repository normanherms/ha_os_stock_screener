THRESHOLD = 1.5  # Prozent
VOLUME_MIN = 1_000_000  # Mindestvolumen
MAX_RESULTS = 5  # Nur Top 5 auffällige Aktien
SORT_BY = "impact"  # Oder: "change", "volume"

STOCK_SOURCES = [
    "data/de_stocks.json",
    "data/us_stocks.json"
    # später z. B.: "data/etf_stocks.json", "data/cn_stocks.json"
]
