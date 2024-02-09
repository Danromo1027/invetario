import pandas as pd

from Conexion import *

class Formato:
    
    def formatoExcel():
        
        cone = Conexion.ConexionBaseDatos()
        query = "SELECT * FROM usuario;"
        df = pd.read_sql(query, cone)
        df.to_excel('C:\Documentos\PROYECTOS DE PROGRAMACION\Forma.xlsx', index=False)
        cone.commit()
        cone.close()
        
    
