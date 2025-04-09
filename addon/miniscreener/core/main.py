from pathlib import Path
from .screener import run_screener
from .message_builder import build_message

# Basisverzeichnis: 1x nach oben vom aktuellen Skript
base = Path(__file__).resolve().parent.parent
output_dir = base / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# Erste Testausgabe
(output_dir / "message.txt").write_text("Erfolg!", encoding="utf-8")

def main():
    filtered = run_screener(limit=50)
    message = build_message(filtered)

    (output_dir / "message.txt").write_text(message, encoding="utf-8")

    print("📨 Nachricht vorbereitet:")
    print(message)

if __name__ == "__main__":
    main()
