from src.config.database import conectar, connmongop
from datetime import datetime
#1. consultar datos medicos, 2. dar de alta un paciente 3. consultar ultima estadia 



class pacientes:

    def consultar_datos_medicos(self,nombre,ap,am):
        try:
            cliente, collecciones = conectar(**connmongop)
            
            cursor = collecciones['Pacientes'].aggregate([{"$match": {"nombre":{"$regex":f"^{nombre}","$options":"i"} ,"ap_paterno":{"$regex":f"^{ap}","$options":"i"} ,
                                    "ap_materno":{"$regex":f"^{am}","$options":"i"} }}, {"$project": {"_id":0,"nombre":1,"apellido paterno":"$ap_paterno", 
                                                                    "apellido materno":"$ap_materno", "tipo de sangre":"$datos_medicos.tipo_sangre",
                                                                    "alergias":"$datos_medicos.alergias"}}])
            res = list(cursor)

            if not res:
                
                return []
            else:
                return res

        except Exception as e:
            print(f"ERROR: {e}")
            return []

    def consultar_tdsDts(self):
        try:
            cliente, collecciones = conectar(**connmongop)

            cursor = collecciones['Pacientes'].aggregate([{"$project": {"_id":0,"nombre":1,"apellido paterno":"$ap_paterno", 
                                                                    "apellido materno":"$ap_materno", "tipo de sangre":"$datos_medicos.tipo_sangre",
                                                                    "alergias":"$datos_medicos.alergias"}}])
            res = list(cursor)

            if not res:
                
                return []
            else:
                return res

        except Exception as e:
            print(f"ERROR: {e}")
            return []
    
    def dar_de_alta_paciente(self,nombre,ap,am,DOB,tel,email,calle,nint,next,col,cp,cd,nombrec,parentesco,telc,ts,alergias):
        try:
            clientes, colecciones = conectar(**connmongop)
           
            DOB_Mongo = datetime.combine(DOB, datetime.min.time())
            if alergias == "":
                print("sin alergias")
                alergiasLista =[]
            else:
                alergiasLista = (alergias.split(','))
            #fr = input("fecha registro: ")

            paciente ={
                "nombre": nombre,
                "ap_paterno": ap,
                "ap_materno": am,
                "fecha_nacimiento":  DOB_Mongo,
                "telefono": tel,
                "email": email,
                "direccion":{"calle": calle, "numero_interior": nint, "numero_exterior": next,"colonia": col,
                             "codigo_postal": cp, "ciudad": cd},
                "contacto_de_emergencia":{"nombre": nombrec, "parentesco": parentesco, "telefono": telc},
                "datos_medicos":{"tipo_sangre": ts, "alergias": alergiasLista},
                "fecha_registro": datetime.now(),
                "activo": True
            }

            res = colecciones['Pacientes'].insert_one(paciente)  

            if res:
                return True

        except Exception as e:
            print(f"ERROR al tratar de insertar paciente {e}")
            return False

    def dar_de_baja_paciente(self,nombre,ap,am):
        try:
            cliente,colecciones = conectar(**connmongop)

            paciente = colecciones['Pacientes'].find_one({"nombre": nombre,"ap_paterno": ap,"ap_materno": am})

            if not paciente:
                print("Paciente no encontrado")
                return None
            else:
                filtro = {"nombre": nombre,"ap_paterno": ap,"ap_materno": am}
                act = {"$set": {"activo": "False"}}
                res = colecciones['Pacientes'].update_one(filtro,act)
                if res.matched_count == 0:
                    print("record invalido")
                else:
                    print(f"El Paciente {nombre} {ap} {am} ha sido dabo de baja")


        except Exception as e:
            print("No se pudo eliminar al paciente {e}")
            return None
        
    def mostrar_pacientes(self):
        try:
            cliente, collecciones = conectar(**connmongop)
            cursor = collecciones['Pacientes'].aggregate([{"$project":{"_id":0,"nombre":1,"apellido paterno":"$ap_paterno","apellido materno":"$ap_materno",
                                                            "fecha de nacimiento":{"$dateToString":{"format":"%d-%m-%Y","date":"$fecha_nacimiento"}}
                                                                      ,"telefono":1,"email":1,
                                                                       "Direccion":{
                                                                         "$concat":[
                                                                           "$direccion.calle",
                                                                           ", NumI: ",
                                                                           {"$ifNull":[{"$toString":"$direccion.numero_interior"},"Sin Numero"]},
                                                                           ", NumE: ",
                                                                           {"$toString":"$direccion.numero_exterior"},
                                                                           ", Col. ",
                                                                           "$direccion.colonia",
                                                                           ", ",
                                                                           "$direccion.ciudad"
                                                                         ]
                                                                       },
                                                                      "Contacto de emergencia":{
                                                                        "$concat":[
                                                                          "nom: ",
                                                                          "$contacto_de_emergencia.nombre",
                                                                          ", parent: ",
                                                                          "$contacto_de_emergencia.parentesco",
                                                                          ", tel: ",
                                                                          "$contacto_de_emergencia.telefono"
                                                                        ]
                                                                      },
                                                                      "fecha de registro":{"$dateToString":{"format":"%d-%m-%Y","date":"$fecha_registro"}},
                                                                      "activo":1}}])
            res = list(cursor)

            if not res:
                
                return []
            else:
                return res

        except Exception as e:
            print(f"ERROR: {e}")
            return []

    def mostrar_un_paciente(self,nombre,app,apm):
        try:
            cliente, collecciones = conectar(**connmongop)
            cursor = collecciones['Pacientes'].aggregate([{"$match":{"nombre":{"$regex":f"^{nombre}","$options":"i"} ,"ap_paterno":{"$regex":f"^{app}","$options":"i"} ,"ap_materno":{"$regex":f"^{apm}","$options":"i"} }},
                                                            {"$project":{"_id":0,"nombre":1,"apellido paterno":"$ap_paterno","apellido materno":"$ap_materno",
                                                            "fecha de nacimiento":{"$dateToString":{"format":"%d-%m-%Y","date":"$fecha_nacimiento"}}
                                                                      ,"telefono":1,"email":1,
                                                                       "Direccion":{
                                                                         "$concat":[
                                                                           "$direccion.calle",
                                                                           ", NumI: ",
                                                                           {"$ifNull":[{"$toString":"$direccion.numero_interior"},"Sin Numero"]},
                                                                           ", NumE: ",
                                                                           {"$toString":"$direccion.numero_exterior"},
                                                                           ", Col. ",
                                                                           "$direccion.colonia",
                                                                           ", ",
                                                                           "$direccion.ciudad"
                                                                         ]
                                                                       },
                                                                      "Contacto de emergencia":{
                                                                        "$concat":[
                                                                          "nom: ",
                                                                          "$contacto_de_emergencia.nombre",
                                                                          ", parent: ",
                                                                          "$contacto_de_emergencia.parentesco",
                                                                          ", tel: ",
                                                                          "$contacto_de_emergencia.telefono"
                                                                        ]
                                                                      },
                                                                      "fecha de registro":{"$dateToString":{"format":"%d-%m-%Y","date":"$fecha_registro"}},
                                                                      "activo":1}}])
            res = list(cursor)

            if not res:
                
                return []
            else:
                return res

        except Exception as e:
            print(f"ERROR: {e}")
            return []