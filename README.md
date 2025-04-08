Aufbau des Programms mit kleiner Beschreibung

ha_os_stock_screener/
├── core/
│   ├── __init__.py
│   ├── main.py              # Einstiegspunkt (für Home Assistant)
│   ├── screener.py          # Hauptlogik (Filter, Analyse)
│   ├── notifier.py          # WhatsApp / Logik für Notifications
│   ├── data_handler.py      # Datenzugriff (CSV, ggf. API)
│   ├── config.py            # Einstellungen & Defaults
│   └── vix_checker.py       # VIX-Abfrage (wenn aktiviert)
├── data/
│   ├── stocks.csv           # ggf. vorbereitete Aktienliste
│   └── vix_cache.json       # optionaler VIX-Cache
├── output/
│   ├── message.txt          # wird von HA ausgelesen
│   └── log.txt              # Ablauf-Log
├── shared/
│   └── keywords.json        # Suchbegriffe
├── .gitignore
├── README.md
├── ideas.md
├── CHANGELOG.md
├── requirements.txt
└── run.py                  # zum manuellen Starten außerhalb von HA

Ablauf
## 📦 Installation (Home Assistant Terminal)

```bash
cd /config
git clone https://github.com/<deinname>/ha_os_stock_screener.git
cd ha_os_stock_screener
chmod +x install.sh
./install.sh
