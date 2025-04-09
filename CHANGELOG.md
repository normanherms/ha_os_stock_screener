# 📄 Changelog – ha_os_stock_screener

Alle relevanten Änderungen an diesem Projekt werden in diesem Dokument dokumentiert.

---

## [v0.3.2-alpha] – 2025-04-09

### ✨ Hinzugefügt
- de_stocks und us_stocks erweitert
- kleine Bugfixes

---

## [v0.3.1-alpha] – 2025-04-09

### ✨ Hinzugefügt
- Updates werden jetzt in Home Assistant angezeigt

---

## [v0.3.0-alpha] – 2025-04-09

### ✨ Hinzugefügt
- Vollständiges Home Assistant **Add-on** (Docker-basiert)
- `run.py` mit automatisierter Ausgabe in `output/message.txt` und zusätzlicher Datei in `config/miniscreener.txt`
- Add-on erzeugt bei Start eine Ausgabe und beendet sich kontrolliert
- Ausgabeformat mit Emoji + kompakten Börsendaten
- Konfiguration des Add-ons via `run.sh` integriert

### ⚙️ Geändert
- Pfad-Handling über `pathlib` zur besseren OS-Kompatibilität
- `message.txt` wird jetzt doppelt geschrieben (für HA und Klartext)
- Screener schreibt strukturierte JSON-Dateien in `data/`
- `build_message()` überprüft jetzt Nachrichtenlänge (`max_length`)
- Add-on-Struktur aufgeteilt in `miniscreener/` und `addon/`
- Projektstruktur überarbeitet (für Docker-Build & Deployment optimiert)
- `Dockerfile` schlanker und gezielter aufgebaut (Python 3.11-slim)

### 🧰 Entwickler-Setup
- Neues GitHub-Branch-Konzept mit `feature/*` und PR-only Merge
- `.github/`-Struktur mit Issue- & PR-Vorlagen
- `CONTRIBUTING.md` und `CODE_OF_CONDUCT.md` ergänzt
- Branch Protection Rules empfohlen & dokumentiert

### 🐛 Fixes
- Zeilenumbruch-Problem bei langen Nachrichten erkannt und ToDo angelegt
- Pfadkonflikte beim Docker-Build durch neue Build-Kontextstruktur gelöst

---

## [v0.2.0] - 2025-04-08

### Hinzugefügt
- Neue README mit vollständiger Anleitung zur Home Assistant-Integration
- Beispiel für `configuration.yaml`, `secrets.yaml` und `rest_command` (CallMeBot)
- WhatsApp-Benachrichtigung via `rest_command.whatsapp_notify`
- `us_stocks.json` als eigene Datei integriert
- `STOCK_SOURCES` in `config.py` für dynamische Datenquellen

### Geändert
- `fetch_and_filter()` fokussiert nur noch auf gefilterte Daten (kein `all_stocks.json`)
- `load_tickers()` liest Quellen aus `config.py`
- `message.txt` ist auf 254 Zeichen begrenzt
- Imports und Pfade im Projekt neu organisiert
- `install.sh` überarbeitet und bereinigt

### Entfernt
- Alte `generate_all_stocks.py` wird nicht mehr genutzt

### Sonstiges
- Projektziel im README ergänzt: Community-getriebenes Lernprojekt mit ChatGPT-Unterstützung

---

## [v0.1.0-alpha] - 2025-04-06

### Erste Alpha-Version
- Basisfunktionalität mit `yfinance`
- Manuelles Filtern von Ticker-Daten aus `all_stocks.json`
- Ausgabe in `message.txt`
- Erste Home Assistant Shell-Integration
