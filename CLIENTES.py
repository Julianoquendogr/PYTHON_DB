import xlrd
import pyodbc
from datetime import date
from datetime import datetime
import re

#Libro excel + hoja de trabajo
book = xlrd.open_workbook(r'C:\\Users\\Julian\\Downloads\\TABLAS_PRUEBA_ING_DATOS.xlsx')
sheet = book.sheet_by_name('clientes')

#Conexión con la bd
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                      'Database=DB_PYTHON;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

Nombre = ""
Apellido = ""

for i in range(1, sheet.nrows):

    Id               = sheet.cell(i, 0).value
    Cod_Tip_Doc      = sheet.cell(i, 1).value
    Cod_Genero       = sheet.cell(i, 2).value
    Nombre_Completo  = sheet.cell(i, 4).value
    Fecha_Nacimiento = sheet.cell(i, 5).value
    Fecha_Nacimiento = str(Fecha_Nacimiento)
    Ingresos         = sheet.cell(i, 6).value
    Cod_Sucursal     = sheet.cell(i, 7).value
    
    #Manejo  de fecha de nacimiento para calcular edad
    Edad = sheet.cell(i, 5).value
    Edad = re.sub('[^0-9]', '', str(Edad))
    año  = Edad[0:4]
    mes  = Edad[4:6]
    dia  = Edad[6:8]
    if mes == '02' and dia == '29':
        dia = '28'
    elif mes == '00':
         mes = '01'

    Fecha = año + '-' + mes + '-' + dia
    #print(Fecha)

    #Día actual
    today = date.today()
    datetime_object = datetime.strptime(Fecha, '%Y-%m-%d').date()
    años = ((today - datetime_object) / 365.25)
    años = re.sub('[^0-9]', '', str(años))
    Edad = int(años[0:2])
     #Fin manejo  de fecha de nacimiento para calcular edad

    #Separando nombres y apellidos según len
    lista = Nombre_Completo.split()
    if len(lista) == 1:
        Nombre = lista[0]
    elif len(lista) == 2:
        Nombre = lista[0]
        Apellido = lista[1]
    elif len(lista) == 3:
        Nombre = lista[0]
        Apellido = lista[1] + ' ' + lista[2]
    elif len(lista) == 4:
        Nombre = lista[0] + ' ' + lista[1]
        Apellido = lista[2] + ' ' + lista[3]
    elif len(lista) >= 5:
        Nombre = lista[0] + ' ' + lista[1] + ' ' + lista[2]
        Apellido = lista[3] + ' ' + lista[4]
    #fin separando nombres y apellidos según len

    query = '''INSERT INTO CLIENTES 
            (Id, Cod_Tip_Doc, Cod_Genero, Nombre_Completo, Nombre, Apellido, Fecha_Nacimiento, Ingresos, Cod_Sucursal,Edad) 
             VALUES (?,?,?,?,?,?,?,?,?,?)'''
    values = (Id, Cod_Tip_Doc, Cod_Genero, Nombre_Completo, Nombre,
              Apellido, Fecha_Nacimiento, Ingresos, Cod_Sucursal, Edad)
    cursor.execute(query, values)
    conn.commit()

print("Se insertaron : " + str(sheet.nrows - 1) +
      " registros en la tabla CLIENTES")
cursor.close()
conn.close()