# Usar Python 3.11
FROM python:3.11

WORKDIR /app

# Copiar y actualizar dependencias
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar `manage.py` y dar permisos de ejecución
COPY backend/manage.py /app/manage.py
RUN chmod +x /app/manage.py

# Copiar todo el backend
COPY backend/ /app/

# Asegurar permisos correctos en todos los archivos copiados
RUN chmod -R 755 /app/

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
