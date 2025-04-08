> **⚠️ Wichtiger Hinweis:**
> Dieses Projekt stellt **keine Anlageberatung** dar und ist **keine Handlungsempfehlung** für Investitionen.
> Alle Kursdaten stammen von **[yfinance](https://pypi.org/project/yfinance/)** und sind ohne Gewähr.

---

## 🤝 Community-Projekt aus Spaß und Neugier

Eigentlich sollte dieses Projekt mal ein kleines Lern-Skript für den Umgang mit Python, APIs und Home Assistant werden.  
Die Idee war: ein einfacher Aktien-Screener, ein bisschen Datenspielerei, vielleicht mal bei Reddit nach Tipps fragen...

Doch daraus ist (mit ChatGPTs Hilfe 🤖) ein richtiges System geworden – modular, erweiterbar und mit echter Home Assistant-Integration. 🎯

Was als Nebenprojekt für mehr Verständnis über den Aktienmarkt begann, ist inzwischen ein richtig schönes Open-Source-Tool geworden – nicht geplant, aber mit viel Freude gebaut.

Wir entwickeln es Stück für Stück weiter, bauen neue Filter ein, verbessern die Benachrichtigung – und freuen uns, wenn jemand Lust hat mitzumachen oder eigene Ideen einbringt! 🛠️✨

# 📈 ha_os_stock_screener

Ein modularer Aktien-Screener für Home Assistant OS – überwacht deutsche & US-Aktien, erkennt starke Kursbewegungen und erstellt automatisch eine kompakte Zusammenfassung als `message.txt`.

---

## ⚙️ Funktionen

- Analyse beliebiger Aktien aus `data/de_stocks.json` und `data/us_stocks.json`
- Filter nach prozentualer Kursveränderung & Volumen
- Kompakte Ausgabe für Home Assistant (`command_line`-Sensor)
- Optional: VIX-Auswertung (Volatilitätsindikator)
- WhatsApp-Benachrichtigung über CallMeBot (optional)
- Leicht erweiterbar über Module (`core/`)
- Bereit zur Integration in Home Assistant via `shell_command`

---

## 🗂️ Projektstruktur

```plaintext
core/              → Screener-Logik, Filter, Konfiguration, Nachricht
ha_integration/    → Install-Skript & run.py für HA
data/              → Ticker-Listen (z. B. de_stocks, us_stocks)
output/            → message.txt & Logs für HA
shared/            → Suchbegriffe (z. B. für Reddit)
tools/             → Hilfs-Skripte wie Aktien-Scraper
```

---

## 🚀 Installation (Home Assistant OS)

### 1. Terminal-Befehle:

```bash
cd /config/custom_components
git clone https://github.com/normanherms/ha_os_stock_screener.git
cd ha_os_stock_screener
chmod +x ha_integration/install.sh
./ha_integration/install.sh
pip install -r /config/custom_components/ha_os_stock_screener/requirements.txt

```

---

### 2. `configuration.yaml`:

```yaml
command_line:
  - sensor:
      name: "Aktien_Nachricht"
      command: "cat /config/custom_components/ha_os_stock_screener_output/message.txt"
      value_template: "{{ value }}"
      scan_interval: 1800
      unique_id: aktien_nachricht_cmdline

# Shell-Befehle
shell_command:
  run_stock_screener: "python3 /config/custom_components/ha_os_stock_screener/run.py"
```

---

### 3. Automatisierung (Beispiel)

```yaml
- id: "aktien_screener_timer"
  alias: "Aktien Screener automatisch tagsüber"
  trigger:
    - trigger: time_pattern
      minutes: /30
  condition:
    - condition: time
      after: "09:00:00"
      before: "22:00:00"
    - condition: time
      weekday:
        - mon
        - tue
        - wed
        - thu
        - fri
  action:
    - action: shell_command.run_stock_screener

    - delay: "00:00:03" # Warte kurz, bis Sensor die Datei neu liest

    - condition: template
      value_template: "{{ states('sensor.aktien_nachricht') | length > 5 }}"

    - action: rest_command.whatsapp_notify
      data:
        phone: !secret whatsapp_phone
        message: "{{ states('sensor.aktien_nachricht') }}"
        apikey: !secret callmebot_api
  mode: single

```

In deiner `secrets.yaml`:

```yaml
callmebot_api: "DEINAPIKEY"
whatsapp_phone: "+49hierdeineNummerohneNull"
```

### WhatsApp-Integration in der `configuration.yaml`:

```yaml
# WhatsApp REST API (CallMeBot)
rest_command:
  whatsapp_notify:
    url: "https://api.callmebot.com/whatsapp.php?phone={{ phone }}&text={{ message }}&apikey={{ apikey }}"
    method: get
    content_type: "application/x-www-form-urlencoded"
```

---

## 🔧 Anpassbar

- **Beobachtete Aktien** in: `data/de_stocks.json`, `data/us_stocks.json`
- **Filterregeln** in: `core/config.py` (`THRESHOLD`, `VOLUME_MIN`, `MAX_RESULTS`)
- **Nachricht** wird automatisch erstellt in `output/message.txt`

---

## 📦 Abhängigkeiten

```txt
yfinance
beautifulsoup4
requests
```

Installation:

```bash
pip install -r requirements.txt
```

---

## 🧪 Lokal testen

```bash
python run.py
```

---

## 📌 Lizenz

MIT (siehe LICENSE)
