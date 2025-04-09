from pathlib import Path
from .screener import run_screener
from .message_builder import build_message

# 1. Basisverzeichnis innerhalb des Add-ons
base = Path(__file__).resolve().parent.parent
output_dir = base / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# 2. Pfad im HA-Config-Verzeichnis (wird vom Add-on nach /config gemountet)
ha_shared_path = Path("/config/miniscreener.txt")

# Schreibe erste Testmeldung
(output_dir / "message.txt").write_text("Erfolg!", encoding="utf-8")
ha_shared_path.write_text("Erfolg!", encoding="utf-8")

def main():
    filtered = run_screener(limit=50)
    message = build_message(filtered)

    # Lokaler Output für Debug
    (output_dir / "message.txt").write_text(message, encoding="utf-8")

    # Shared Output für Home Assistant
    ha_shared_path.write_text(message, encoding="utf-8")

    print("📨 Nachricht vorbereitet:")
    print(message)

if __name__ == "__main__":
    main()
