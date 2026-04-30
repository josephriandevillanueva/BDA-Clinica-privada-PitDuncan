Database Migration Report
Summary

All data has been successfully migrated from the source database (local) to the target database (MongoDB Atlas).

Source Database (Local)

Database: pitduncan
Collections: personal, Pacientes, inventario, usuarios, Citas, facturas
Target Database (Atlas)

Cluster: cluster0.ngkrl.mongodb.net
Database: pitduncan
Collections: personal, Pacientes, inventario, usuarios, Citas, facturas
Field Analysis
Connection url: uri = "mongodb+srv://emiliocastillon8:b1bV10jueIac55QE@cluster0.ngkrl.mongodb.net/?appName=Cluster0"

Below is the detailed analysis of all collections, their fields, and whether each field is obligatory (used in all records).

Collection: personal (31 documents)
| Field | Count | Obligatory |
|---|---|---|
| `_id` | 31 | Yes |
| `nombre` | 31 | Yes |
| `apellido_paterno` | 31 | Yes |
| `apellido_materno` | 31 | Yes |
| `rol` | 31 | Yes |
| `fecha_contratacion` | 30 | No |
| `direccion` | 30 | No |
| `especialidad` | 15 | No |

## Collection: `Pacientes` (83 documents)
| Field | Count | Obligatory |
|---|---|---|
| `_id` | 83 | Yes |
| `nombre` | 83 | Yes |
| `ap_paterno` | 83 | Yes |
| `ap_materno` | 83 | Yes |
| `fecha_nacimiento` | 83 | Yes |
| `telefono` | 83 | Yes |
| `email` | 83 | Yes |
| `direccion` | 83 | Yes |
| `contacto_de_emergencia` | 83 | Yes |
| `datos_medicos` | 83 | Yes |
| `fecha_registro` | 83 | Yes |
| `activo` | 83 | Yes |

## Collection: `inventario` (87 documents)
| Field | Count | Obligatory |
|---|---|---|
| `_id` | 87 | Yes |
| `categoria` | 87 | Yes |
| `marca` | 87 | Yes |
| `stock_total` | 87 | Yes |
| `nombre comercial` | 72 | No |
| `descripcion` | 72 | No |
| `unidad_medida` | 72 | No |
| `precio_por_unidad` | 72 | No |
| `lotes` | 72 | No |
| `proveedor` | 66 | No |
| `sustancia_activa` | 51 | No |
| `presentacion` | 51 | No |
| `codigo_barras` | 51 | No |
| `recetado` | 51 | No |
| `sku_interno` | 21 | No |
| `nombre_equipo` | 15 | No |
| `modelo` | 15 | No |
| `numero_serie` | 15 | No |
| `codigo_activo_fijo` | 15 | No |
| `ultima_certificacion` | 15 | No |
| `vencimiento_certificacion` | 15 | No |

## Collection: `usuarios` (40 documents)
| Field | Count | Obligatory |
|---|---|---|
| `_id` | 40 | Yes |
| `user` | 40 | Yes |
| `contraseña` | 40 | Yes |
| `activo` | 40 | Yes |

## Collection: `Citas` (4 documents)
| Field | Count | Obligatory |
|---|---|---|
| `_id` | 4 | Yes |
| `nombre` | 4 | Yes |
| `especialista` | 4 | Yes |
| `fecha_hora` | 4 | Yes |

## Collection: `facturas` (5 documents)
| Field | Count | Obligatory |
|---|---|---|
| `_id` | 5 | Yes |
| `fecha_emision` | 5 | Yes |
| `paciente` | 5 | Yes |
| `doctor` | 5 | Yes |
| `concepto` | 5 | Yes |
| `monto_total` | 5 | Yes |
| `archivo_pdf` | 5 | Yes |
| `estado` | 5 | Yes |
