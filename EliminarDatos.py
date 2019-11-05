###############################################################################################
#       FUNCIÓN QUE LLAMA SP EN LA BD PARA BORRAR DATOS DE LAS TABLAS
###############################################################################################

import pyodbc

def InsertarEliminarTablas():

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                          'Database=DB_PYTHON;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('''
                    EXEC sp_EliminarTablas
                    ''')
    conn.commit()

    print("Se borraron los datos de 5 tablas")
    cursor.close()
    conn.close()