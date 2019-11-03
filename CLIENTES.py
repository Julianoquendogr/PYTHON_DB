import xlrd
import pyodbc

book = xlrd.open_workbook(r'C:\\Users\\Julian\\Downloads\\TABLAS_PRUEBA_ING_DATOS.xlsx')
sheet = book.sheet_by_name('clientes')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                      'Database=DB_PYTHON;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

Nombre = ""
Apellido = ""

for i in range(1, sheet.nrows):

    Id                    = sheet.cell(i, 0).value
    Cod_Tip_Doc           = sheet.cell(i, 1).value
    Cod_Genero            = sheet.cell(i, 2).value
    Nombre_Completo       = sheet.cell(i, 4).value
    Fecha_Nacimiento      = "2019/03/07" #sheet.cell(i, 6).value 
    Ingresos              = sheet.cell(i,6).value
    Cod_Sucursal          = sheet.cell(i,7).value
    lista                 = Nombre_Completo.split()

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

    query = '''INSERT INTO CLIENTES 
            (Id, Cod_Tip_Doc, Cod_Genero, Nombre_Completo, Nombre, Apellido, Fecha_Nacimiento, Ingresos, Cod_Sucursal) 
             VALUES (?,?,?,?,?,?,?,?,?)'''
    values = (Id, Cod_Tip_Doc, Cod_Genero, Nombre_Completo, Nombre, Apellido,Fecha_Nacimiento, Ingresos,Cod_Sucursal)
    cursor.execute(query, values)
    conn.commit()

print("Se insertaron : " + str(sheet.nrows - 1) + " registros en la tabla CLIENTES")
cursor.close()
conn.close()
