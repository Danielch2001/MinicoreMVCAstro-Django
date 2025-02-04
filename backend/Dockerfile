# Imagen base
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del backend
COPY backend /app
COPY backend/requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para correr Django correctamente
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
