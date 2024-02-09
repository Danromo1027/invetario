import pandas as pd

from Conexion import *


cone = Conexion.ConexionBaseDatos()
query = "SELECT * FROM usuario;"
df = pd.read_sql(cone,query)
df.to_excel('C:/Users/diosc/OneDrive/Documentos/PROYECTOS_DE_PROGRAMACION/Forma.xlsx', index=False)
cone.commit()
cone.close()
        
    
