from conectar_clinica import conectar, connmongop
from datetime import datetime

class agendar_citas:

    def generar_cita(self, usuario, especialista, fecha_hora_completa):
        try:
            cliente, colecciones = conectar(**connmongop)

            cita = {
                "nombre": usuario,
                "especialista": especialista,
                "fecha_hora": fecha_hora_completa 
            }

            colecciones['Citas'].insert_one(cita) 
            return True

        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def mostrar_cita(self, nombre):
        try:
            cliente, colecciones = conectar(**connmongop)

            dc = [
                {
                    "$match": {"nombre": nombre}
                },
                {
                    "$project": {
                        "_id": 0,
                        "nombre": 1,
                        "especialista": 1,
                        "fecha": {
                            "$dateToString": {"format": "%d-%m-%Y", "date": "$fecha_hora"}
                        },
                        "hora": {
                            "$dateToString": {"format": "%H:%M", "date": "$fecha_hora"}
                        }
                    }
                }
            ]

            cursor_resultados = colecciones['Citas'].aggregate(dc)
            
            res = list(cursor_resultados) 

            return res

        except Exception as e:
            print(f"ERROR EN MOSTRAR_CITA: {e}")
            return []


