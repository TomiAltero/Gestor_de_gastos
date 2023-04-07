import subprocess

def menu_principal():
    caracter = "-" * 30
    print(f"{caracter} BIENVENIDOS AL GESTOR DE GASTOS A.L.T {caracter}")
    print("1.Ingresar un gasto")
    print("2.Ver mis gastos ")
    print("3.Salir")
    
    while True:
        entrada = input("Ingrese la opción que desee: ")
        if entrada == "1":
            subprocess.run(["/usr/bin/python3", "bd_python/Proyecto/Gestor de gastos/ing_gasto.py"])
            break
        elif entrada == "2":
            subprocess.run(["/usr/bin/python3", "bd_python/Proyecto/Gestor de gastos/ver_gastos.py"])
            break
        elif entrada == "3":
            exit()
        else:
            print("Opción inválida. Por favor, ingrese una opción correcta.")
            continue

menu_principal()
