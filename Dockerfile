# Utiliser une image officielle Python
FROM python:3.12.9-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers
COPY . .

# Exécuter le programme
CMD ["python", "main.py"]