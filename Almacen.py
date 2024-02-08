from Conexion import *

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
                
    def ingresarCantidad(canti):
        
        try:
            
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            
            if canti.get()=="Ingeniero 1":
                sql = "insert into usuarios values(null,null,null,%s,%s,%s,%s,%s,null);"
                valores = (canti,)
            if canti.get()=="Ingeniero 2":
                sql = "insert into usuarios values(null,null,null,%s,%s,%s,%s,%s,null);"
                valores = (canti,)
            if canti.get()=="Ingeniero 3":
                sql = "insert into usuarios values(null,null,null,%s,%s,%s,%s,%s,null);"
                valores = (canti,)

            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount, "registro ingresado")
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
    
    def modificarClientes():
        
        try:
            
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.Ing1 = %s, usuarios.Ing2 = %s, usuarios.Ing3 = %s, usuarios.Almacen = %s, usuarios.Total = %s where usuarios.id = %s;"
           
            valores = (nombres, apellidos, sexo, idUsuarios,)
            
            
            cursor.execute(sql,valores)
            
            #Ejecucion de la funcion
            cone.commit()
            print(cursor.rowcount, "registro actualizado")
        
        except mysql.connector.Error as error:
            print("Error al actualizar datos {}".format(error))


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
            print(nombre_producto+"almacen sin codigo")
            return nombreX 
        
        except mysql.connector.Error as error:
            print("Error de busqueda de datos {}".format(error))
            return []     
    
