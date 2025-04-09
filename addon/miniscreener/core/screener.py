from core.data_handler import load_tickers, fetch_and_filter
from core.config import THRESHOLD

def run_screener(limit=None):
    tickers = load_tickers(limit=limit)
    filtered = fetch_and_filter(tickers, THRESHOLD)
    return filtered
