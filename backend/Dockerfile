# Usa Python 3.11 como base
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia primero el archivo de dependencias y lo instala
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos de backend dentro del contenedor
COPY backend /app

# Lista los archivos para verificar que `manage.py` existe
RUN ls -lah /app

# Comando para correr el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
