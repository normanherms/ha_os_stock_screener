# 1) Verwende schlankes Python-Image
FROM python:3.11-slim

# 2) Setze Arbeitsverzeichnis
WORKDIR /app

# 3) Kopiere requirements.txt und installiere Abhängigkeiten
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 4) Kopiere den gesamten miniscreener-Ordner ins Image
COPY miniscreener/ /app/miniscreener/

# 5) Kopiere das Startskript
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# 6) Starte das Add-on
CMD ["/app/run.sh"]
