# Arquitectura del Proyecto Pit Duncan

El proyecto está diseñado usando un patrón de Separación de Responsabilidades enfocado para Streamlit.

## `src/views/`
Contiene la representación gráfica (Frontend). Estos archivos nunca hacen operaciones directas a la BD, solo envían qué mostrar en la ventana.
- `admin_view.py`: Dashboard de administrador.
- `doctor_view.py`: Dashboard para médicos.
- `inventory_view.py`: Interfaz de inventario.
- `login_view.py`: Frontend del Login.
- `appointments_view.py`: Frontend para el agendamiento y visualización de citas.

## `src/services/`
Contiene la "Lógica de Negocio" (Backend). Estos archivos contienen las clases y funciones que procesan datos, calculan precios, validan información, etc.
- `citas.py`: Lógica de reservación.
- `facturas.py`: Lógica de faturación y cálculos de pago.
- `inventario.py`: Lógica del stock.
- `pacientes.py`: Creación y actualización de historiales.
- `users.py`: Verifica sesiones y encripta contraseñas.

## `src/config/`
- `database.py`: Centraliza las credenciales y conectores de Base de Datos, garantizando que el resto de la aplicación no exponga claves directamente.

## `src/static/`
- `css/styles.css`: Centraliza todo el estilo global, haciéndolo mantenible en un solo archivo en lugar de mezclado dentro de python.
- `img/`: Los logos e imágenes rasterizadas.

## Archivos de Raíz
- `main.py`: Punto de entrada universal (`streamlit run main.py`). Lee el estado interactivo (`st.session_state`) y pinta en pantalla la vista ("view") correspondiente, leyendo también los estilos de `styles.css`.
