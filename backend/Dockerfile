# Imagen base
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar todos los archivos del backend al contenedor
COPY backend /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Ejecutar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
