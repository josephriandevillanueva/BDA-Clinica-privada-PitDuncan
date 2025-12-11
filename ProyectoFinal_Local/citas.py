#Aqui llamamos a otros archivos y sus funciones y otras librerias
from conectar_clinica import conectar, connmongop
from datetime import datetime

class agendar_citas:
    #Funcion para insertar datos de una cita en la Base de datos.
    def generar_cita(self, usuario, especialista, fecha_hora_completa):
        try:   
            #Conectamos a la BD
            cliente, colecciones = conectar(**connmongop)
            #Hacemos un diccionario para guardar los datos que nos llegan de la interfaz
            cita = {
                "nombre": usuario,
                "especialista": especialista,
                "fecha_hora": fecha_hora_completa 
            }
            #Hacemos la incercion
            colecciones['Citas'].insert_one(cita)
            #En caso de que todo salga bien nos retorna True
            return True

        except Exception as e:
            print(f"ERROR: {e}")
            #En caso de que algo falle nos retorna False
            return False

    #Funcion para mostrar una cita por medio de un nombre.
    def mostrar_cita(self, nombre):
        try:
            #Conectamos a la BD siempre que aparezca esta linea de codigo es para conectar a la BD
            cliente, colecciones = conectar(**connmongop)

            #diccionario para poner insertar mas facil en la BD, aqui se usa un match para filtrar y que solo regrese los datos del paciente que se busca
            dc = [
                {
                    "$match": {"nombre":{"$regex":f"^{nombre}","$options":"i"}}
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
            #Hacemos la consulta
            cursor_resultados = colecciones['Citas'].aggregate(dc)
            
            #Guardamos el valor que nos regreso la consulta como una lista
            res = list(cursor_resultados) 

            #Retornamos hacia la interfaz
            return res

        except Exception as e:
            print(f"ERROR EN MOSTRAR_CITA: {e}")
            return []

    #Esta funcion es parecida a la funcion de mostar cita la diferencia es que no se usa match, nada mas se llaman a todos los datos del catalago de citas.
    def mostrar_todas_citas(self):
        try:
            cliente, colecciones = conectar(**connmongop)

            documento = [
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

            cursor_resultados = colecciones['Citas'].aggregate(documento)
            
            res = list(cursor_resultados) 

            return res

        except Exception as e:
            print(f"ERROR EN MOSTRAR_CITA: {e}")
            return []


