# 1) Basis-Image: schlankes Python 3.11
FROM python:3.11-slim

# 2) Setze Arbeitsverzeichnis im Container
WORKDIR /app

# 3) Kopiere requirements.txt aus dem Repository-Root in /app
COPY requirements.txt /app/requirements.txt

# 4) Installiere alle Python-Abhängigkeiten aus requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 5) Kopiere den gesamten core-Ordner ins Image
COPY core/ /app/core/

# (Optional) Wenn ihr Dateien aus 'output' oder 'shared' braucht, diese ebenfalls kopieren, z. B.:
# COPY output/ /app/output/
# COPY shared/ /app/shared/

# 6) Kopiere das Start-Skript aus dem addon-Ordner
COPY addon/run.sh /app/run.sh
RUN chmod +x /app/run.sh

# 7) Standardbefehl zum Start des Add-ons
CMD [ "/app/run.sh" ]
