import pandas as pd

from Conexion import *

class Formato:
    
    def formatoExcel():
        
        cone = Conexion.ConexionBaseDatos()
        query = "SELECT * FROM usuario;"
        df = pd.read_sql(cone,query)
        fri = pd.DataFrame(df)
        fri.to_CSV('C:/Documentos/PROYECTOS DE PROGRAMACION/Forma.csv')
        cone.commit()
        cone.close()
        
    
