# Proyecto Web: Consulta de Gastos por Departamento

Este es un proyecto web desarrollado con **Django** para el backend y **Astro** para el frontend. El objetivo del programa es permitir a los usuarios consultar los gastos totales por departamento dentro de un rango de fechas específico. Incluye una interfaz amigable para seleccionar las fechas y visualizar los datos en una tabla dinámica.

## **Funcionalidades Principales**
- Selección de rango de fechas para consultar gastos.
- Visualización de los totales de gastos agrupados por departamento.
- Inclusión de departamentos sin gastos (con total igual a `0.0`).
- Diseño limpio y responsivo.

---

## **Requisitos Previos**

Para ejecutar este proyecto en tu entorno local, necesitas tener instaladas las siguientes herramientas:

1. **Python 3.8 o superior**
2. **Node.js 16 o superior**
3. **npm (incluido con Node.js)**
4. **Git**
5. **Un entorno virtual para Python** (opcional pero recomendado).

---

## **Pasos para Configurar y Ejecutar el Proyecto**

### **1. Clonar el Repositorio**
Clona el proyecto en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd minicoreAstroDjango
```

---

### **2. Configurar el Backend (Django)**

#### **a) Crear un entorno virtual** (opcional):
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

#### **b) Instalar las dependencias de Python:**
```bash
cd backend
pip install -r requirements.txt
```

#### **c) Realizar las migraciones:**
Configura la base de datos y aplica las migraciones necesarias:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### **d) Crear un superusuario (opcional):**
Si deseas acceder al panel de administración de Django:
```bash
python manage.py createsuperuser
```

#### **e) Ejecutar el servidor de desarrollo:**
```bash
python manage.py runserver
```
El backend estará disponible en: `http://127.0.0.1:8000`

---

### **3. Configurar el Frontend (Astro)**

#### **a) Instalar las dependencias de Node.js:**
```bash
cd ../frontend
npm install
```

#### **b) Ejecutar el servidor de desarrollo:**
```bash
npm run dev
```
El frontend estará disponible en: `http://localhost:4321`

---

### **4. Configurar CORS (Cross-Origin Resource Sharing)**
Para permitir que el frontend se comunique con el backend, asegúrate de que CORS esté configurado correctamente en el archivo `backend/settings.py`:

```python
INSTALLED_APPS += ['corsheaders']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    *MIDDLEWARE,
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:4321',  # Dirección del frontend
]
```

---

## **Cómo Usar el Proyecto**

1. Abre el frontend en tu navegador: `http://localhost:4321`
2. Selecciona una fecha de inicio y una fecha de fin en el formulario.
3. Haz clic en el botón **"Buscar"**.
4. Visualiza los totales de gastos por departamento en la tabla.

---

## **Estructura del Proyecto**

```
minicoreAstroDjango/
├── backend/           # Código fuente del backend (Django)
│   ├── api/           # Aplicación principal de Django
│   ├── manage.py      # Script de administración de Django
│   └── requirements.txt  # Dependencias del backend
├── frontend/          # Código fuente del frontend (Astro)
│   ├── src/           # Componentes y páginas del frontend
│   ├── package.json   # Dependencias del frontend
│   └── astro.config.mjs  # Configuración de Astro
└── README.md          # Documentación del proyecto
```

---

## **Créditos**
Desarrollado por Daniel Chicaiza
Contacto: daniel.chicaiza@udla.edu.ec

