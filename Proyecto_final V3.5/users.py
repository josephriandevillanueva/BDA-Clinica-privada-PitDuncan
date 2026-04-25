from conectar_clinica import conectar, connmongop
from inventario import inventario
from pacientes import pacientes
import bcrypt
import stdiomask
class usuarios:# este archivo es de cuando solo era el puro back

    def generar_usuario(self):

        try:
            cliente, colecciones = conectar(**connmongop)
            usuario = input("inserte el nuevo nombre de ususario: ")
            password = input("cree una contraseña: ")

            bytes = password.encode('utf-8')#lo convierte en un arreglo de bytes
            salt = bcrypt.gensalt()# esto es una cadena aleatoria que se le agrega al final en caso de que logren atravesar el hasheo
            hash = bcrypt.hashpw(bytes,salt)

            user = {
                "user": usuario,
                "contraseña": hash,
                "activo": True 
            }

            colecciones['usuarios'].insert_one(user)
            print("insertado")



        except Exception as e:
            print(f"ERROR: {e}")
            return None
        

   
        
    def dar_de_baja(self):
        try:
            cliente,colecciones = conectar(**connmongop)
            usuario = input("ingrese el nombre del  usuario a dar de baja: ")
            us = colecciones['usuarios'].find_one({"user": usuario})

            if not us:
                print("Usuario no encontrado")
                return None
            
            else:
                filtro = {"user": usuario}
                act = {"$set": {"activo": "False"}}
                res = colecciones['usuarios'].update_one(filtro,act)
                if res.matched_count == 0:
                    print("record invalido")
                else:
                    print(f"{usuario} ha sido dado de baja")

        except Exception as e:
            print(f"ERROR: {e}")
            return None
    


    def mostrar_usuarios(self):
        try:
            cliente,colecciones = conectar(**connmongop)
            cursor = colecciones['usuarios'].aggregate([{"$project": {"_id":0 ,"user":1,"activo":1}},{"$match": {"activo":True}}])
            
            res = list(cursor)

            if not res:
                print("no hay resultados")
                return None
            else:
                for doc in res:
                    print(doc)


        except Exception as e:
            print(f"ERROR: {e}")
            return None

    def login(self):
        try:
            cliente,colecciones = conectar(**connmongop)
            usuario = input("ingrese su nombre de ususario: ")
            us = colecciones['usuarios'].find_one({"user": usuario})
            
            if not us:
                print("usuario no encontrado")
                return None
            if us.get('activo') == "False":
                print("usted ya no tiene acceso")
                return None
            

            password = stdiomask.getpass(prompt="ingrese su contraseña: ", mask="*")
           
            
            if bcrypt.checkpw(password.encode('utf-8'), us['contraseña']):
                print(f"bienvenido {usuario}")

                #logica menu admin
                if "admin" in usuario.lower():
                    print("Desplegando Menu del administrador")
                    while True:
                         print("1. crear un nuevo usuario")
                         print("2. dar de baja un ususario")
                         print("3.menu de inventario")
                         print("4. salir del menu de administrador")
                         op = input("Elija una opcion: ")

                         if op == '1':
                            self.generar_usuario()
                         elif op == '2':
                             self.dar_de_baja()
                         elif op == '3':
                             print("menu inventario")
                             inv = inventario()
                             inv.menu_inventario()
                             

                         elif op == '4':
                             print("cerrando menu de administrador")
                             break
                         
                else:
                    print("Menu medicos")
                    p = pacientes()
                    p.menu()

                    
            else:
                print("Contraseña equivocada!")
                return None
        

        except Exception as e:
            print(f"ERROR: {e}")
            return None