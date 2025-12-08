from conectar_clinica import conectar, connmongop
from datetime import datetime
from receta import crear_pdf
#1. consultar datos medicos, 2. dar de alta un paciente 3. consultar ultima estadia 



class pacientes:

    def consultar_datos_medicos(self,nombre,ap,am):
        try:
            cliente, collecciones = conectar(**connmongop)
            #print("ingrese el paciente a buscar")
            #nombre = input("Nombre: " )
            #ap = input("apellido Paterno: ")
            #am = input("apellido materno: ")
             # para algo especifico dentro del objeto datos_medicos: "tipo_sangre": "$datos_medicos.tipo_sangre"
            cursor = collecciones['Pacientes'].aggregate([{"$match": {"nombre": nombre,"ap_paterno": ap,
                                    "ap_materno": am}}, {"$project": {"_id":0,"nombre":1,"ap_paterno":1, 
                                                                    "ap_materno":1, "datos_medicos":1}}])
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
            """print("Datos del paciente")
            nombre = input("Nombre: " )
            ap = input("apellido Paterno: ")
            am = input("apellido materno: ")
            DOB = input("Fecha de nacimiento YY-MM-DD: ")

            tel = input("Telefono: ")
            email = input("correo electronico del paciente: ")
            print("direccion del paciente: ")
            calle = input("calle: ")
            nint = input("numero interior: ")
            next = input("numero exterior: ")
            col = input("colonia: ")
            cp = input("codigo postal: ")
            cd = input("ciudad: ")
            print("contactos de emergencia: ")
            nombrec = input("nombre del contacto: ")
            parentesco = input("parentesco: ")#aqui podrias poner en la interfaz las opciones y que seleccione una haciendo click
            telc = input("telefono del contacto: ")
            print("datos medicos: ")
            ts = input("tipo de sangre: ")
            alergias = input("alergias, si no tiene, deje este espacio en blanco: ")"""
            
            
            #DOB_Mongo = datetime.strptime(DOB,"%Y-%m-%d")#aqui deberia hacer un parseo de string a formato fecha.  //UPDATE: FUNCIONA!!
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

            colecciones['Pacientes'].insert_one(paciente)  

        except Exception as e:
            print(f"ERROR al tratar de insertar paciente {e}")
            return str(e)

    def dar_de_baja_paciente(self,nombre,ap,am):
        try:
            cliente,colecciones = conectar(**connmongop)
            #print("Datos del paciente que quiere eliminar")
            #nombre = input("Nombre: " )
            #ap = input("apellido Paterno: ")
            #am = input("apellido materno: ")

            paciente = colecciones['Pacientes'].find_one({"nombre": nombre,"ap_paterno": ap,"ap_materno": am})

            if not paciente:
                print("Paciente no encontrado")
                return None
            else:
                filtro = {"nombre": nombre,"ap_paterno": ap,"ap_materno": am}
                act = {"$set": {"activo": False}}
                res = colecciones['Pacientes'].update_one(filtro,act)
                if res.matched_count == 0:
                    print("record invalido")
                else:
                    print(f"El Paciente {nombre} {ap} {am} ha sido dabo de baja")


        except Exception as e:
            print("No se pudo eliminar al paciente {e}")
            return None
        






    def menu(self):

        
        while True:
            print("1.Ingresar a un nuevo paciente")
            print("2. eliminar a un paciente del sistema")
            print("3. Consultar datos medicos del paciente")
            print("4. Prescribir una receta")
            print("5. Solicitar prueba")
            print("6. salir")
            opm = input("elija una opcion: ")

            if opm == '1':
                self.dar_de_alta_paciente()

            elif opm == '2':
                self.dar_de_baja_paciente()

            elif opm == '3':
                self.consultar_datos_medicos()
                
            elif opm == '4':
                crear_pdf()

            elif opm == '6':
                print("Saliendo")
                break


