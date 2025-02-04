# Imagen base
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del backend al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Django
EXPOSE 8000

# Ejecutar el backend
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
