# Imagen base
FROM python:3.11

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del backend
COPY backend/ /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Django
EXPOSE 8000

# Comando para iniciar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
