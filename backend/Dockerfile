# Imagen base
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el código fuente de la app
COPY backend/ /app/

# Copiar y instalar dependencias
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Ejecutar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
