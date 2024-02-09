from Conexion import *

#hola emerson
class Alma:
    
    def mostrar_productos():
        
            try:
                
                cone = Conexion.ConexionBaseDatos()
                if cone is None:
                    return []
                cursor = cone.cursor()
                cursor.execute("SELECT * FROM suministros.usuarios;")
                miResultado = cursor.fetchall()
                cone.commit()
                cone.close()
                return miResultado
            
            except mysql.connector.Error as error:
                print("Error de muestra de datos {}".format(error))
                
    def ingresarCantidad(fren,canti,codMat):
        
        try:
            
            cone = Conexion.ConexionBaseDatos()
            cursor = cone.cursor()
            
            if fren == "Ingeniero 1":
                sql = "Update usuarios SET Ing1 = Ing1 + %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                valores = (canti,codMat,)
                
            if fren =="Ingeniero 2":
                sql = "Update usuarios SET Ing2 = Ing2 + %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                valores = (canti,codMat,)
                
            if fren =="Ingeniero 3":
                sql = "Update usuarios SET Ing3 = Ing3 + %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                valores = (canti,codMat,)
                
            if fren =="Almacen":
                sql = "Update usuarios SET Almacen = Almacen + %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                valores = (canti,codMat,)
                

            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount, "registro ingresado")
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))


    def RetirarCantidad(fren,canti,codMat):
        
        try:
            
            cone = Conexion.ConexionBaseDatos()
            cursor = cone.cursor()
            
            if fren == "Ingeniero 1":
                sql2 = "SELECT Ing1 FROM usuarios WHERE Codigo_Mat = %s"
                valor_1 = (codMat,)

                cursor.execute(sql2, valor_1)

                cantidadIng_1 = cursor.fetchone() 

                if cantidadIng_1[0] > int(canti):
                    sql = "Update usuarios SET Ing1 = Ing1 - %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                    valores = (canti,codMat,)
                else:
                    print("no hay cantidades suficientes para este material")    
                
            if fren =="Ingeniero 2":
                sql = "Update usuarios SET Ing2 = Ing2 - %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                valores = (canti,codMat,)
                
            if fren =="Ingeniero 3":
                sql = "Update usuarios SET Ing3 = Ing3 - %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                valores = (canti,codMat,)
                
            if fren =="Almacen":
                sql = "Update usuarios SET Almacen = Almacen - %s, Total = Ing1 + Ing2 + Ing3 + Almacen WHERE Codigo_Mat = %s"
                valores = (canti,codMat,)
                

            cursor.execute(sql,valores)
            
            cone.commit()
            print(cursor.rowcount, "registro ingresado")
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))



    def busca_producto(nombre_producto):
        
        try:
            
            cone = Conexion.ConexionBaseDatos()
            if cone is None:
                    return ["NO"]
            cursor = cone.cursor()
            sql = "SELECT * FROM usuarios WHERE Codigo_Mat LIKE %s OR Material LIKE %s"
            val1=((f"%{nombre_producto}%", f"%{nombre_producto}%"))
            cursor.execute(sql,val1)
            nombreX = cursor.fetchall()
            cone.commit()
            cone.close()
        
            return nombreX 
        
        except mysql.connector.Error as error:
            print("Error de busqueda de datos {}".format(error))
            return []     
    
    def Inventario():
        
        try:
            
            cone = Conexion.ConexionBaseDatos()
            if cone is None:
                    return ["NO"]
            cursor = cone.cursor()
            sql = "SELECT * FROM usuarios WHERE Total > 0"
            cursor.execute(sql)
            nombreX = cursor.fetchall()
            cone.commit()
            cone.close()
            return nombreX 
        
        except mysql.connector.Error as error:
            print("Error de proyeccion del inventario {}".format(error))
            return []     
    
