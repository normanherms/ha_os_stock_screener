# 1) Verwende schlankes Python-Image
FROM python:3.11-slim

# 2) Setze Arbeitsverzeichnis
WORKDIR /app

# 3) Kopiere requirements.txt ins Image und installiere Abhängigkeiten
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 4) Kopiere alle notwendigen Python-Dateien (Module, Daten, Tools, etc.)
COPY core/ /app/core/
COPY data/ /app/data/
COPY ha_integration/ /app/ha_integration/
COPY output/ /app/output/
COPY shared/ /app/shared/
COPY tools/ /app/tools/

# 5) Kopiere Startskript
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# 6) Startbefehl für das Add-on
CMD ["/app/run.sh"]
