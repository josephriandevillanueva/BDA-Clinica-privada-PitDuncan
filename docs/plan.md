# Plan de Implementación (Cambios de Base de Datos)

Este plan abarca las tareas mencionadas en `overhaul.md` que requieren modificaciones en la estructura de la Base de Datos (MongoDB) y en la lógica del backend profundo.

## 1. GESTIÓN DE RECETAS

### 1.1 Vincular medicamentos con recetas
**Problema:** Actualmente las recetas son probablemente texto libre o no están estructuradas para referenciar los IDs de los medicamentos en inventario.
**Solución en BD:** 
- Modificar el modelo/colección de `Recetas`.
- Agregar un arreglo de objetos `medicamentos` que contengan el `medicamento_id` (referencia a la colección `inventario`), `cantidad` y `dosis`.

### 1.2 Validar recetas y firma digital
**Problema:** No hay forma de validar la autenticidad de una receta.
**Solución en BD:**
- Agregar un campo `estado_validacion` (ej. 'pendiente', 'validada', 'rechazada') a `Recetas`.
- Agregar campos `firma_digital` y `hash_receta` para almacenar la firma criptográfica generada en la emisión.
- Crear una nueva colección `SecretosFirma` o añadir atributos protegidos a los Doctores en la colección `personal` para guardar sus llaves privadas/públicas con encriptación simétrica.

### 1.3 Medicina con receta obligatoria
**Problema:** La tienda no sabe qué medicinas exigen receta para su compra.
**Solución en BD:**
- Agregar un campo booleano `requiere_receta` (true/false) en la colección `inventario`.
- Al realizar el pago, si la orden contiene un producto con `requiere_receta = true`, el sistema debe exigir subir el archivo o relacionar el ID de la receta en la orden.

## Pasos para la implementación posterior:
1. Actualizar esquemas de validación de inserción si se están usando validadores de MongoDB, o bien los modelos Pydantic/Diccionarios en Python.
2. Migrar o actualizar los documentos existentes (ej. agregar `requiere_receta = False` a todo el inventario actual para mantener retrocompatibilidad temporalmente).
3. Implementar la librería de encriptación (ej. `cryptography` o `PyJWT`) para la generación y validación de las firmas digitales.
