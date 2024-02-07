from Conexion import *

class Alma:
    def mostrar_productos():
            try:
                cone = Conexion.ConexionBaseDatos()
                if cone is None:
                    return []
                cursor = cone.cursor()
                cursor.execute("SELECT * FROM suministros.almacen;")
                miResultado = cursor.fetchall()
                cone.commit()
                cone.close()
                return miResultado
            except mysql.connector.Error as error:
                print("Error de muestra de datos {}".format(error))

    def busca_producto(nombre_producto,nombre_material):
        
        try:
            cone = Conexion.ConexionBaseDatos()
            if cone is None:
                    return ["NO"]
            cursor = cone.cursor()
            
            sql = "SELECT * FROM almacen WHERE Codigo_Mat LIKE %s OR Material LIKE %s"
            val1=((f"%{nombre_producto}%", f"%{nombre_producto}%"))
            val2=((f"%{nombre_material}%", f"%{nombre_material}%"))
            cursor.execute(sql,val1)
            
            #cursor2.execute(sql2, (f"%{nombre_material}%", f"%{nombre_material}%"))
            nombreX = cursor.fetchall()
            #nombref = cursor.fetchall()
            cone.commit()
            cone.close()
            print(nombre_producto+"almacen sin codigo")
            print(nombre_material+"almacen sin nombre")
            return nombreX 
        except mysql.connector.Error as error:
            print("Error de busqueda de datos {}".format(error))
            return []     
        
