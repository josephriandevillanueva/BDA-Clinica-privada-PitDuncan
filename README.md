# BDA-Clinica-privada-PitDuncan
Proyecto de Base de Datos Avanzadas (BDA) desarrollado por Joseph Riande Villanueva y Jonathan Garcia Lopez.

## Objetivo del Proyecto
El sistema es una **Plataforma de Gestión Integrada de Clínica Privada** (Clínica Pit Duncan) construida con Python y la librería Streamlit. Su objetivo es gestionar eficientemente todas las operaciones del negocio y agilizar el control administrativo/médico integrándose a una base de datos centralizada. Permite desde la atención al público en general (reservar citas y comprar medicinas) hasta la gestión interna a través de una sólida división de roles (Administrador y Médico).

## Estructura Avanzada del Proyecto

- **🎛️ Punto de Entrada y Ruteo (`test.py`)**
  Archivo principal que orquesta toda la aplicación Streamlit, establece los estilos gráficos globales (CSS custom) y maneja el estado de la sesión (`st.session_state`) para la navegación dinámica entre menús interactivos.

- **🔐 Autenticación y Seguridad (`interfaz_login.py`, `user_streamlit.py`)**
  Gestión de inicio de sesión seguro, validación de perfiles y habilitación de los permisos correspondientes (Admin vs Médicos).

- **👥 Paneles de Control por Roles:**
  - `interfaces_menu_admin.py`: Dashboard de administración con altos privilegios (gestión de usuarios e inventarios globales).
  - `interfaces_menu_doc.py`: Portal de trabajo de los médicos para acceder a los módulos de pacientes, recetarios y facturación.
  - `interfaces_menu_inv.py`: Vistas exclusivas para operaciones logísticas y de inventario.

- **📅 Gestión de Atención Clínica (`citas.py`, `interfaz_citas.py`, `pacientes.py`)**
  Manejo completo del ciclo de vida del paciente: captación de un visitante, conversión a paciente, registro hospitalario y agendamiento de su consulta médica.

- **💊 Inventario y Farmacia (`inventario.py`)**
  Control total sobre el stock, insumos médicos y punto de venta del catálogo en línea de medicinas.

- **🧾 Facturación y Prescripciones (`facturas.py`, enrutado de recetas)**
  Automatización en la emisión de cobros por servicios médicos otorgados y de recetas.

- **⚙️ Conexión de Base de Datos (`conectar_clinica.py`)**
  Lógica de conectores, cursores y ejecución de querys responsables de comunicar al backend con el sistema gestor de bases de datos avanzadas.