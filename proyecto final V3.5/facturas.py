from conectar_clinica import conectar, connmongop
from datetime import datetime

class facturas:
    def guardar_factura(self, paciente_nombre, doctor_nombre, concepto, costo, archivo_pdf):
        try:
            cliente, colecciones = conectar(**connmongop)
            
            nueva_factura = {
                "fecha_emision": datetime.now(),
                "paciente": paciente_nombre,
                "doctor": doctor_nombre,
                "concepto": concepto,
                "monto_total": float(costo), 
                "archivo_pdf": archivo_pdf,  
                "estado": "Pagada"            
            }

            res = colecciones['facturas'].insert_one(nueva_factura)
            
            if res.inserted_id:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error al guardar factura: {e}")
            return False

    def consultar_facturas_paciente(self, nombre_paciente):
        try:
            cliente, colecciones = conectar(**connmongop)
            cursor = colecciones['facturas'].find({"paciente": nombre_paciente})
            return list(cursor)
        except:
            return []