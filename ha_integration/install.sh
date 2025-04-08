#!/bin/bash

echo ""
echo "📦 Starte Installation von ha_os_stock_screener in Home Assistant..."
echo "------------------------------------------------------------"

TARGET_DIR="/config/custom_components/ha_os_stock_screener"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

# 1. Sicherstellen, dass wir auf HA OS sind
if [ ! -d "/config" ]; then
  echo "❌ Dieses Skript muss in einer Home Assistant OS Umgebung ausgeführt werden!"
  exit 1
fi

# 2. Alte Version löschen (wenn vorhanden)
if [ -d "$TARGET_DIR" ]; then
  echo "🧹 Entferne alte Installation..."
  rm -rf "$TARGET_DIR"
fi

# 3. Zielverzeichnis erstellen
mkdir -p "$TARGET_DIR"

# 4. Kopiere komplette Projektstruktur
echo "📁 Kopiere Dateien nach $TARGET_DIR ..."
cp -r "$SCRIPT_DIR/core" "$TARGET_DIR/"
cp -r "$SCRIPT_DIR/data" "$TARGET_DIR/"
cp -r "$SCRIPT_DIR/output" "$TARGET_DIR/"
cp -r "$SCRIPT_DIR/shared" "$TARGET_DIR/"
cp "$SCRIPT_DIR/run.py" "$TARGET_DIR/"
cp "$SCRIPT_DIR/requirements.txt" "$TARGET_DIR/"
cp "$SCRIPT_DIR/LICENSE" "$TARGET_DIR/"
cp "$SCRIPT_DIR/ha_integration/install.sh" "$TARGET_DIR/" 2>/dev/null
cp "$SCRIPT_DIR/README.md" "$TARGET_DIR/" 2>/dev/null
cp "$SCRIPT_DIR/CHANGELOG.md" "$TARGET_DIR/" 2>/dev/null
cp "$SCRIPT_DIR/ideas.md" "$TARGET_DIR/" 2>/dev/null

# 5. Setze Berechtigungen
chmod -R 755 "$TARGET_DIR"

# 6. Abschlussmeldung
echo ""
echo "✅ ha_os_stock_screener wurde erfolgreich installiert nach:"
echo "   $TARGET_DIR"
echo ""
echo "👉 Jetzt bitte in Home Assistant:"
echo ""
echo "1. Füge folgenden Sensor in deine configuration.yaml ein:"
echo ""
echo "sensor:"
echo "  - platform: command_line"
echo "    name: Aktien Screener"
echo "    command: 'cat /config/custom_components/ha_os_stock_screener/output/message.txt'"
echo "    scan_interval: 7200"
echo ""
echo "2. Optional: shell_command hinzufügen:"
echo ""
echo "shell_command:"
echo "  run_stock_screener: 'python3 /config/custom_components/ha_os_stock_screener/run.py'"
echo ""
echo "3. Danach kannst du Automationen erstellen, um den Screener regelmäßig laufen zu lassen."
echo ""
