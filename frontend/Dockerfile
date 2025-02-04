# Imagen base
FROM node:18

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos del frontend
COPY . /app

# Instalar dependencias
RUN npm install

# Exponer el puerto de Astro
EXPOSE 4321

# Ejecutar el frontend
CMD ["npm", "run", "dev"]
