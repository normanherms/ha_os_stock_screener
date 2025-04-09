#!/bin/bash

echo ""
echo "📦 Starte Erstinstallation von ha_os_stock_screener in Home Assistant..."
echo "------------------------------------------------------------"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

# Sicherstellen, dass das Skript aus dem custom_components-Ordner ausgeführt wird
if [[ "$SCRIPT_DIR" != *"/custom_components/ha_os_stock_screener" ]]; then
  echo "❌ Bitte das Repository direkt nach /config/custom_components/ha_os_stock_screener klonen und von dort aus starten!"
  exit 1
fi

# Setze Berechtigungen (für alle Dateien im Repo)
chmod -R 755 "$SCRIPT_DIR"

echo ""
echo "✅ ha_os_stock_screener wurde korrekt installiert unter:"
echo "   $SCRIPT_DIR"
echo ""
echo "👉 Jetzt bitte in Home Assistant:"
echo ""
echo "1. Füge folgenden Sensor in deine configuration.yaml ein:"
echo ""
echo "command_line:"
echo "  - sensor:"
echo "      name: \"Aktien_Nachricht\""
echo "      command: \"cat /config/custom_components/ha_os_stock_screener/output/message.txt\""
echo "      value_template: \"{{ value }}\""
echo "      scan_interval: 7200"
echo ""
echo "2. Optional: shell_command hinzufügen:"
echo ""
echo "shell_command:"
echo "  run_stock_screener: \"python3 /config/custom_components/ha_os_stock_screener/run.py\""
echo ""
echo "3. Danach kannst du Automationen erstellen, um den Screener regelmäßig laufen zu lassen."
echo ""
