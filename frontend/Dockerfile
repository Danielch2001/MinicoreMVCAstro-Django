# Imagen base actualizada a una versión compatible con Astro y Vite
FROM node:20

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del frontend al contenedor
COPY frontend/ /app

# Limpiar la caché de npm para evitar conflictos de versiones
RUN npm cache clean --force

# Instalar dependencias con compatibilidad de versiones
RUN npm install --legacy-peer-deps

# Exponer el puerto de Astro
EXPOSE 4321

# Ejecutar el frontend
CMD ["npm", "run", "dev"]
