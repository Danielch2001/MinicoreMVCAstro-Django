# Imagen base
FROM python:3.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar todos los archivos del backend al contenedor
COPY . /app

# Verificar la estructura de archivos
RUN ls -l /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Django
EXPOSE 8000

# Ejecutar el backend (asegurarse de la ruta correcta de `manage.py`)
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]
