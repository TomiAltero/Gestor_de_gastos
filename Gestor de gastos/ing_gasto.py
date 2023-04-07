import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bd_gastos"
)


def ingresar_datos():
    monto = int(input("Ingrese el monto del gasto: "))

    fecha = input("Ingrese la fecha del gasto (AÑO/MES/DÍA): ")

    nombre = input("Ingrese el nombre del gasto: ")

    cursor = bd.cursor()

    sql = "INSERT INTO Gastos (Monto, Fecha, Nombre) VALUES (%s,%s,%s)"
    valores = (monto, fecha, nombre)

    cursor.execute(sql, valores)

    bd.commit()


ingresar_datos()
