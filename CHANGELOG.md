# 📄 Changelog – ha_os_stock_screener

Alle relevanten Änderungen an diesem Projekt werden in diesem Dokument dokumentiert.

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
