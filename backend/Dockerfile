FROM python:3.11

WORKDIR /app

COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar manualmente cada archivo para evitar errores de directorios
COPY backend/manage.py /app/manage.py
COPY backend/backend /app/backend
COPY backend/api /app/api
COPY backend/populate_db.py /app/populate_db.py
COPY backend/db.sqlite3 /app/db.sqlite3
COPY backend/backend/settings.py /app/settings.py
COPY backend/backend/urls.py /app/urls.py
COPY backend/backend/wsgi.py /app/wsgi.py


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
