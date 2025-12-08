from conectar_clinica import conectar, connmongop
from inventario import inventario
from pacientes import pacientes
import bcrypt
import stdiomask
class users:

    def generar_usuario(self,usuario,password):

        try:
            cliente, colecciones = conectar(**connmongop)
            #usuario = input("inserte el nuevo nombre de ususario: ")
            #password = input("cree una contraseña: ")

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
        

   
        
    def dar_de_baja(self,usuario):
        try:
            cliente,colecciones = conectar(**connmongop)
            #usuario = input("ingrese el nombre del  usuario a dar de baja: ")
            us = colecciones['usuarios'].find_one({"user": usuario})

            if not us:
                print("Usuario no encontrado")
                return None
            
            else:
                filtro = {"user": usuario}
                act = {"$set": {"activo": False}}
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
                return []
                
            else:
                return res


        except Exception as e:
            print(f"ERROR: {e}")
            return []

    def login(self,usuario,password):
        try:
            cliente,colecciones = conectar(**connmongop)
            #usuario = input("ingrese su nombre de ususario: ")
            us = colecciones['usuarios'].find_one({"user": usuario})
            
            if not us:
                print("usuario no encontrado")
                return False
            if us.get('activo') == "False":
                print("usted ya no tiene acceso")
                return False
            

           #password = stdiomask.getpass(prompt="ingrese su contraseña: ", mask="*")
           
            
            if bcrypt.checkpw(password.encode('utf-8'), us['contraseña']):
                print(f"bienvenido {usuario}")
                return us

              
                         
               
                    
            else:
                print("Contraseña equivocada!")
                return False
        

        except Exception as e:
            print(f"ERROR: {e}")
            return False