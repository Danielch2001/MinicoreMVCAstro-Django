FROM python:3.11

WORKDIR /app

COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar `manage.py` explícitamente antes de copiar el resto
COPY backend/manage.py /app/manage.py

# Copiar todo el backend
COPY backend/ /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
