from conectar_clinica import conectar, connmongop

class inventario:
    def consultar_stock(self):
        try:
            cliente,colecciones = conectar(**connmongop)
            cursor = colecciones['inventario'].aggregate([{"$project": {"_id":0,"nombre": {
                        "$ifNull": ["$nombre comercial","$nombre_equipo"]
                    }, 
            "stock_total":1}}])

            res = list(cursor)

            if not res:
                return []
            else:
                return res
            


        except Exception as e:
            print(f"ERROR: {e}")
            return[]
    

    def consultar_certificaciones(self):
        try:
            cliente,colecciones = conectar(**connmongop)
            cursor = colecciones['inventario'].aggregate([{
                "$match": {"nombre_equipo": {"$exists": True},"$expr": {"$lt": [
                            "$vencimiento_certificacion",{
                                "$dateFromString": {"dateString": "2026-03-01"}}]
                    }}
                },
            {"$project": {"_id": 0,"nombre_equipo": 1,"vencimiento_certificacion": 1}}])
            
            res = list(cursor)

            if not res:
                return []
            else:
                return res
        

        except Exception as e:
            print(f"ERROR: {e}")
            return []


    def menu_inventario(self):
        try:
            
            while True:
                    print("1.consultar Stock")
                    print("2.consultar certificaciones")
                    print("3.salir del menu de inventario")
                    op = input("Elija una opcion: ")
                    if op == '1':
                     
                     self.consultar_stock()
                    
                    elif op == '2':
                        self.consultar_certificaciones()
                                 
                    elif op == '3':
                        print("saliendo del menu de inventario")
                        break




        except Exception as e:
            print(f"ERROR: {e}")