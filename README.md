# Clínica Pit Duncan - Pharmacy & Clinic Management System

## Arquitectura del Proyecto (Architecture Style)
El proyecto utiliza una arquitectura de **Cliente-Servidor (Frontend/Backend separados)** bajo el patrón **RESTful API** en un enfoque **Modular**.
Al desacoplar el Frontend del Backend, la aplicación es más segura, altamente escalable y permite un desarrollo concurrente.
Se utiliza una utilidad personalizada (`run.py`) en la raíz para iniciar ambos servidores de manera simultánea en entornos de desarrollo local.

---

## 💻 Tech Stack & Frameworks

### Frontend (El "Cliente")
- **Framework**: Angular 17+ (Utilizando *Standalone Components* y la nueva sintaxis de Control Flow `@if` / `@for` para máximo rendimiento y menos código boilerplate).
- **Lenguaje**: TypeScript
- **Estilos**: Tailwind CSS (Actualmente cargado para prototipado rápido; se encarga del esquema de diseño "Rich Aesthetics").
- **Gestión de Estado**: Servicios inyectables en Angular (`@Injectable`) apoyados por `localStorage` temporal (Ej: `CartService` para persistencia efímera a través de las pestañas sin abusar de llamadas a la base de datos).
- **Comunicación HTTP**: `HttpClient` de Angular para consumo de API REST.

### Backend (El "Servidor")
- **Framework**: FastAPI (Elegido por su altísimo rendimiento asíncrono y generación automática de documentación Swagger UI).
- **Lenguaje**: Python 3.x
- **Validación de Datos**: Pydantic v2 (Fuerza esquemas estrictos de validación en las entradas/salidas de los endpoints).
- **Autenticación y Seguridad**: `python-jose` (para tokens JWT), `passlib` con `bcrypt` (para el hasheo criptográfico de contraseñas de usuarios). *En preparación para la Fase 3*.

### Base de Datos & Persistencia
- **Motor de Base de Datos**: MongoDB (Base de datos NoSQL alojada en **MongoDB Atlas**).
- **Driver de Conexión**: `motor` (El driver oficial asíncrono de MongoDB para Python, lo cual evita que la base de datos bloquee las demás peticiones web).
- **Lógica de Conexión**: Administrada mediante el sistema de eventos `lifespan` de FastAPI (se conecta al iniciar el servidor, y destruye la conexión limpiamente al apagarlo).

---

## 📂 Estructura de Directorios

```text
PitDuncan/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/      # Endpoints (inventory.py, etc)
│   │   ├── models/          # Modelos estrictos de Pydantic (inventory.py, patient.py, etc)
│   │   ├── db.py            # Singleton de conexión a MongoDB
│   │   └── main.py          # Entrypoint de FastAPI y configuración de CORS
│   └── .env                 # Variables de entorno y Connection Strings
│
├── frontend/
│   ├── src/app/
│   │   ├── components/      # Componentes Standalone de Angular (store, cart, home, etc)
│   │   ├── models/          # Interfaces TypeScript
│   │   ├── services/        # Lógica de negocio (api.service.ts, cart.service.ts)
│   │   ├── app.component.*  # Shell principal y Navbar
│   │   └── app.routes.ts    # Enrutador
│
└── run.py                   # Script de orquestación de desarrollo (Inicia Uvicorn + NG Serve)
```