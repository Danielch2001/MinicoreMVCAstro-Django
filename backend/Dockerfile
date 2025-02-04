# Usar Python 3.11
FROM python:3.11

WORKDIR /app

# Copiar todo el backend primero
COPY backend/ /app/

# Copiar y actualizar dependencias
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Verificar si `manage.py` realmente existe y dar permisos
RUN ls -lah /app && chmod -R 755 /app/

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
