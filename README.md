# 📈 ha_os_stock_screener

> **⚠️ Wichtiger Hinweis:**
> Dieses Projekt stellt **keine Anlageberatung** dar und ist **keine Handlungsempfehlung** für Investitionen.
> Alle Kursdaten stammen von **[yfinance](https://pypi.org/project/yfinance/)** und sind ohne Gewähr.

---

🤖 Mit Unterstützung durch ChatGPT (OpenAI) – vielen Dank für den Code-Support!

---

## 🤝 Community-Projekt aus Neugier

Was als einfaches Lern-Skript begann, ist heute ein Home Assistant Add-on, das automatisch den Aktienmarkt scannt, Kursschwankungen erkennt und kompakte Nachrichten für die Weiterverarbeitung (z. B. WhatsApp) erstellt. Modular, offen und erweiterbar gebaut.

---

## 🔧 Funktionen

- ✅ Scan von deutschen & US-Aktien per Ticker-Listen (`data/*.json`)
- ✅ Filterung nach Kursveränderung & Volumen
- ✅ Ausgabe kompaktes Nachrichtenformat (`miniscreener.txt` für Home Assistant)
- ✅ Automatische Ausführung per Automation
- ✅ WhatsApp-Versand über CallMeBot (optional)
- ✅ Add-on-basiert, mit eigener Abhängigkeitserklärung

---

## 📂 Projektstruktur

```text
addon/              -> Add-on Integration, Dockerfile, run.sh
miniscreener/       -> Screener-Logik (core/, data/, tools/, ...)
  └─ output/         -> message.txt für interne Logs
/config/miniscreener.txt -> Datei für Home Assistant Sensor (wird automatisch erzeugt)
```

---

## 🚀 Installation als Add-on (Home Assistant OS)

1. **Repository als Add-on hinterlegen:**
   - Add-on Store → Drei-Punkte-Menü → Repositories → `https://github.com/normanherms/ha_os_stock_screener`

2. **Add-on installieren** ("Stock Screener")
3. **Starten** → Log zeigt Ergebnisse

---

## ⚙️ Konfiguration in Home Assistant

### Sensor (liest Nachricht):

```yaml
sensor:
  - platform: file
    name: Aktiennachricht
    file_path: /config/miniscreener.txt
    encoding: utf-8
    scan_interval: 1800
```

### WhatsApp REST Command:

```yaml
rest_command:
  whatsapp_notify:
    url: "https://api.callmebot.com/whatsapp.php?phone={{ phone }}&text={{ message }}&apikey={{ apikey }}"
    method: get
    content_type: "application/x-www-form-urlencoded"
```

### Beispiel-Automation

```yaml
- id: "aktien_screener_timer"
  alias: "Aktien Screener automatisch tagsüber"
  trigger:
    - platform: time_pattern
      minutes: "/30"
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
    - service: hassio.addon_start
      data:
        addon: "ad4302bf_stock_screener"

    - delay: "00:00:03"

    - condition: template
      value_template: "{{ states('sensor.aktiennachricht') | length > 5 }}"

    - service: rest_command.whatsapp_notify
      data:
        phone: !secret whatsapp_phone
        message: "{{ states('sensor.aktiennachricht') }}"
        apikey: !secret callmebot_api
  mode: single
```

### secrets.yaml
```yaml
callmebot_api: "DEINAPIKEY"
whatsapp_phone: "+49DEINENUMMER"
```

---

## ⚖️ Anpassen

- **Ticker bearbeiten:** `miniscreener/data/de_stocks.json`, `us_stocks.json`
- **Filterregeln:** `miniscreener/core/config.py` z. B. `THRESHOLD`, `VOLUME_MIN`
- **Ausgabe begrenzen:** `message_builder.py` nutzt `max_length = 254`

---

## 📦 Abhängigkeiten (werden beim Add-on-Build installiert)

```txt
yfinance
beautifulsoup4
requests
pandas
```

---

## 🔮 Lokal testen (außerhalb Home Assistant)

```bash
cd miniscreener
python3 run.py
```

---

## 📌 Lizenz

MIT (siehe LICENSE)

---

## 🚀 Noch in Arbeit / Ideen für die Zukunft

- [ ] Reddit-Integration (Trend-Analyse)
- [ ] VIX-Auswertung als Zusatzfilter
- [ ] Automatische Chart-Screenshots via headless browser
- [ ] GUI zur Konfiguration der Schwellenwerte
- [ ] Tickerlisten automatisch updaten (per cron)

> Du hast Lust mitzuentwickeln? Feedback? Fork gerne oder melde dich – wir freuen uns! 🚀

Mit ❤️ gebaut von [Norman Herms] – und einem ordentlichen Schuss KI-Assistenz 🤖
