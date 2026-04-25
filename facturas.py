#Aqui llamamos a otros archivos y sus funciones y otras librerias
from conectar_clinica import conectar, connmongop
from datetime import datetime

class facturas:
    #Funcion para guardar facturas
    def guardar_factura(self, paciente_nombre, doctor_nombre, concepto, costo, archivo_pdf):
        try:
            #conectamos a la BD
            cliente, colecciones = conectar(**connmongop)
            
            #hacemos un diccionario para poder insertar mas facil en la BD
            nueva_factura = {
                "fecha_emision": datetime.now(), #.now() sirve para poder guardar la fecha de hoy
                "paciente": paciente_nombre,
                "doctor": doctor_nombre,
                "concepto": concepto,
                "monto_total": float(costo), 
                "archivo_pdf": archivo_pdf,  
                "estado": "Pagada"            
            }
            #Insertamos la factura
            res = colecciones['facturas'].insert_one(nueva_factura)
            
            #dependiendo si se inserto bien regresa true en caso de que algo falle retorna false, esto sirve para mandar mensajes a la interfaz
            if res:
                return True

        except Exception as e:
            print(f"Error al guardar factura: {e}")
            return False