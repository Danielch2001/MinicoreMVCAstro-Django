
# Imagen base
FROM python:3.8

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del backend al contenedor
COPY backend/ /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Django
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
