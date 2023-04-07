import subprocess

INGRESAR_GASTO = "bd_python/Proyecto/Gestor de gastos/ing_gasto.py"
VER_GASTOS = "bd_python/Proyecto/Gestor de gastos/ver_gastos.py"
OPCIONES_VALIDAS = ["1", "2", "3"]

def ejecutar_comando(archivo):
    subprocess.run(["/usr/bin/python3", archivo])

def menu_principal():
    caracter = "-" * 30
    print(f"{caracter} BIENVENIDOS AL GESTOR DE GASTOS A.L.T {caracter}")
    print("1.Ingresar un gasto")
    print("2.Ver mis gastos ")
    print("3.Salir")
    
    while True:
        entrada = input("Ingrese la opción que desee: ")
        if entrada in OPCIONES_VALIDAS:
            if entrada == "1":
                ejecutar_comando(INGRESAR_GASTO)
            elif entrada == "2":
                ejecutar_comando(VER_GASTOS)
            elif entrada == "3":
                exit()
        else:
            print("Opción inválida. Por favor, ingrese una opción correcta.")
            continue

menu_principal()