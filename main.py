import pandas as pd
import pyodbc 

df_cat_zona = pd.read_excel(r'C:\\Users\\Julian\\Downloads\\TABLAS_PRUEBA_ING_DATOS.xlsx', sheet_name='cat_zona')
#print (df_cat_zona[['cod_pais_region_zona','desc_zona','desc_region','desc_pais']])

cont = df_cat_zona.count()

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                      'Database=DB_PYTHON;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute('''
                INSERT INTO ZONA (Cod_Pais_Region_Zona, Desc_Zona, Desc_Region,Desc_Pais) 
                VALUES (3,'Colombia','Montreal','America')
                ''')
conn.commit()

conn.close()