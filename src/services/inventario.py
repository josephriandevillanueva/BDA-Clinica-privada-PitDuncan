from src.config.database import conectar, connmongop
from datetime import datetime
class inventario:

    def agregar_medicamento(self,nombre,sustancia,descripcion,presentacion,marca,cod_b,recet,recetado_fin,stock_t,unidad,precio,cod_lot,fecha_cad,cnt_dis,prov,em_prov):

        try:
            cliente,colecciones = conectar(**connmongop)
            fecha_bien = datetime.combine(fecha_cad, datetime.min.time())
            medicamento_doc = {
                "nombre comercial":nombre,
                "sustancias_activas":sustancia,
                "descripcion":descripcion,
                "categoria":"Medicamento",
                "presentacion":presentacion,
                "marca":marca,
                "codigo_barras":cod_b,
                "recetado":recetado_fin,
                "stock_total":stock_t,
                "unidad_medida":unidad,
                "precio_por_unidad":precio,
                "proveedor":{
                    "nombre":prov,
                    "contacto":em_prov
                },
                "lotes":{
                    "codigo_lote":cod_lot,
                    "fecha_caducidad":fecha_bien,
                    "cantidad_disponible":cnt_dis   
                }
            }

            res = colecciones['inventario'].insert_one(medicamento_doc)
            
            if res.inserted_id:
                return True
            else:
                return False

        except Exception as e:
            print(f"ERROR al tratar de insertar paciente {e}")
            return str(e)

    def consultar_stock(self,aux):
        if aux == True:
            try:
                cliente,colecciones = conectar(**connmongop)
                cursor = colecciones['inventario'].aggregate([{"$project": {"_id":0,"nombre": "$nombre comercial","stock_total":1,"descripcion":1,"presentacion":1,
                                                                    "marca":1,"precio por unidad":"$precio_por_unidad"}}])

                res = list(cursor)

                if not res:
                    return []
                else:
                    return res
                
            except Exception as e:
                print(f"ERROR: {e}")
                return[]
        else:
            try:
                cliente,colecciones = conectar(**connmongop)
                cursor = colecciones['inventario'].aggregate([{"$project": {"_id":0,"nombre":"$nombre comercial","descripcion":1,"presentacion":1,"marca":1,
                                                                                "precio por unidad":"$precio_por_unidad"}}])

                res = list(cursor)

                if not res:
                    return []
                else:
                    return res
                
            except Exception as e:
                print(f"ERROR: {e}")
                return[]

    def consultar_producto(self,medicamento,aux):
        if aux == True:
            try:
                cliente, colecciones = conectar(**connmongop)
                cursor = colecciones['inventario'].aggregate([{"$match":{"nombre comercial":{"$regex":f"^{medicamento}","$options":"i"}}},
                    {"$project":{"_id":0,"nombre":"$nombre comercial","stock_total":1,"descripcion":1,"presentacion":1,"marca":1,"precio por unidad":"$precio_por_unidad"}}])

                res = list(cursor)

                if not res:
                    return []
                else:
                    return res

            except Exception as e:
                print(f"ERROR: {e}")
                return[]
        else:
            try:
                cliente, colecciones = conectar(**connmongop)
                cursor = colecciones['inventario'].aggregate([{"$match":{"nombre comercial":{"$regex":f"^{medicamento}","$options":"i"}}},
                    {"$project":{"_id":0,"nombre":"$nombre comercial","descripcion":1,"presentacion":1,"marca":1,"precio por unidad":"$precio_por_unidad"}}])

                res = list(cursor)

                if not res:
                    return []
                else:
                    return res

            except Exception as e:
                print(f"ERROR: {e}")
                return[]

    def stock_mayor(self,stok):
        try:
            cliente, colecciones = conectar(**connmongop)
            cursor = colecciones['inventario'].aggregate([{"$match":{"stock_total":{"$gte":stok}}},
                                                        {"$project":{"_id":0,"nombre":"$nombre comercial","stock_total":1,"descripcion":1,
                                                        "presentacion":1,"marca":1,"precio por unidad":"precio_por_unidad"}}])

            res = list(cursor)

            if not res:
                return []
            else:
                return res

        except Exception as e:
            print(f"ERROR: {e}")
            return[]

    def stock_menor(self,stok):
        try:
            cliente, colecciones = conectar(**connmongop)
            cursor = colecciones['inventario'].aggregate([{"$match":{"stock_total":{"$lte":stok}}},
                                                        {"$project":{"_id":0,"nombre":"$nombre comercial","stock_total":1,"descripcion":1,
                                                        "presentacion":1,"marca":1,"precio por unidad":"precio_por_unidad"}}])

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
            {"$project": {"_id": 0,"nombre_equipo": 1,"ultima_certificacion":1,"vencimiento_certificacion": 1}}])
            
            res = list(cursor)

            if not res:
                return []
            else:
                return res
        

        except Exception as e:
            print(f"ERROR: {e}")
            return []

    def min_stock(self,nombre,cantidad):
        try:
            cliente,colecciones = conectar(**connmongop)

            cursor = colecciones['inventario'].update_one({"nombre comercial":nombre},{"$inc":{"stock_total":-cantidad}})

            return True

        except Exception as e:
            print(f"ERROR: {e}")
            return False