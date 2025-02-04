# Usa una versión más reciente de Python
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del backend al contenedor
COPY backend/ /app

# Actualizar pip antes de instalar dependencias
RUN pip install --upgrade pip

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Django
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
