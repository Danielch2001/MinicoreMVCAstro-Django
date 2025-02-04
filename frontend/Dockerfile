# Imagen base
FROM node:16

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del frontend al contenedor
COPY frontend/ /app

# Instalar dependencias
RUN npm install

# Exponer el puerto de Astro
EXPOSE 4321

# Ejecutar el frontend
CMD ["npm", "run", "dev"]
