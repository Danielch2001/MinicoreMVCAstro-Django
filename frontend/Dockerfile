# Usar Node.js 18
FROM node:18

WORKDIR /app

# Copiar package.json y lockfile antes de instalar dependencias
COPY frontend/package.json frontend/package-lock.json /app/
RUN npm install

# Copiar todo el código fuente
COPY frontend/. /app/

# Asegurar permisos correctos en todos los archivos copiados
RUN chmod -R 755 /app/

CMD ["npm", "run", "dev"]
