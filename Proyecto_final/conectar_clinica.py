import pymongo
from pymongo import MongoClient

connmongop = {

    "URI" : "mongodb+srv://lonehesh:lonehesh@cluster0.tlhh8z6.mongodb.net/Clinica?appName=Cluster0",
    "bd" : "Clinica",
    "colec" : ["personal","Pacientes", "inventario","usuarios","Citas","facturas"]
   #mongodb+srv://lonehesh:lonehesh@cluster0.tlhh8z6.mongodb.net/?appName=Cluster0
}


def conectar(**connmongop):

    URI = connmongop["URI"]#aqui accedo a los elementos de mi diccionario
    db = connmongop["bd"]
    cols = connmongop.get("colec",[])
  
    try:
     
     cliente = MongoClient(URI)

     db = cliente[db] # aqui igual uso mi diccionario
     colecciones = {col: db[col] for col in cols}#aqui la base accede al diccionario y usa la colleccion "col" que es mi llavecita
      # y de ahi usa el valor de "col" osea "herencia" entonces le decimos que queremos acceder a la coleccion herencia de mi db osea mi base de datos
     print(f"se ha conectado con la BD: '{db.name}' ")

     return cliente,colecciones
     



    except Exception as e:
     print(f"Ocurrió un error: {e}")
     return None, None