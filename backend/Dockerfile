FROM python:3.11

WORKDIR /app

COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app

# Si el archivo está en /app/backend/manage.py, lo movemos a /app/
RUN if [ -f /app/backend/manage.py ]; then mv /app/backend/manage.py /app/manage.py; fi

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
