FROM python:3.11

WORKDIR /app

COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el backend
COPY backend/ /app/

# Mover `manage.py` a `/app`
RUN mv /app/backend/manage.py /app/manage.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
