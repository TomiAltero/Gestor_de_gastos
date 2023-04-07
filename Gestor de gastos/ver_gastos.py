import mysql.connector
import json
from datetime import date
from tabulate import tabulate

def obtener_datos():
    try:
        bd = mysql.connector.connect(host="localhost", 
                                    user="root", 
                                    password="", 
                                    database="bd_gastos")
        
        cursor = bd.cursor()
        cursor.execute("SELECT * FROM Gastos")
        filas = cursor.fetchall()
        return filas
    except Exception as e:
        print("Error al obtener los datos:", e)
        return []

def convertir_fecha(fecha):
    return fecha.strftime('%y-%m-%d')

def imprimir_datos(filas):
    print(tabulate(filas, headers=["Monto", "Fecha", "Nombre"], tablefmt="grid", numalign="center"))
    lista_datos = []
    for i in filas:
        dato = { 
            "Monto": i[0], 
            "Fecha": convertir_fecha(i[1]), 
            "Nombre": i[2] 
        } 
        lista_datos.append(dato)
    for i in lista_datos: 
        print(i)

def guardar_datos(lista_datos):
    with open("bd_python/Proyecto/Gestor de gastos/datos.txt", "w") as archivo_txt: 
        for i in lista_datos: 
            archivo_txt.write(json.dumps(i) + "\n")

filas = obtener_datos()
imprimir_datos(filas)
lista_datos = []
for i in filas:
    dato = { 
        "Monto": i[0], 
        "Fecha": convertir_fecha(i[1]), 
        "Nombre": i[2] 
    } 
    lista_datos.append(dato)
guardar_datos(lista_datos)