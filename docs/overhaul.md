# TAREAS Y MEJORAS PENDIENTES DEL PROYECTO

1. GESTIÓN DE RECETAS
---
* Vincular medicamentos con recetas.
* Validar recetas.
* Aceptar solamente recetas válidas (que contengan una firma digital).
* Pensar en guardar de lado BD los secretos de la firma digital para poder verificar su validez.
* Pedir documento de receta si la medicina lo requiere.
* Analizar funcionamiento actual de todo el sistema y todas las vistas, pensar en mejorar o rediseñar para un uso natural, mientras se respeten los cambios especificos pedidos abajo.

2. MÓDULO DE TIENDA
---
## General
* Crear una tabla de todos los productos con un filtro de búsqueda 
  en la parte superior.
* Abajo del formulario de agregar al carrito, colocar la tabla de 
  medicinas (en vez de mezclar la búsqueda y la vista).
* El input de medicamentos debe ser un datalist con las medicinas 
  disponibles.

## Carrito de Compras
* Cambiar la pestaña "Carrito".
* Permitir cambiar la cantidad agregada o eliminar el producto.
* Agregar botones para quitar medicamentos individuales o modificar 
  cantidades.
* Solicitar una receta (documento PDF) en el proceso de pago si es 
  necesario.


3. PAGOS Y TARJETAS (CARRITO)
---
* Tarjetas: validar que sean 16 dígitos (sin validación real con 
  pasarela).
* Fecha de vencimiento: usar solo Mes y Año en vez de un "date" 
  completo en el form (tal vez usar dos inputs distintos).
* Validar 3 dígitos de CVV.


4. MÓDULO DE MÉDICOS
---
## Recetas
* Agregar Datalist (como en la TIENDA) para vincular medicamentos 
  con cada receta.
* Agregar Datalists de doctores.
* Agregar datos ocultos al PDF generado para verificar que es una 
  receta real.
