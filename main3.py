# Listas para almacenar taxis y autobuses
from Taxi import Taxi
from Autobus import Autobus
taxis = []
autobuses = []


def registrar_taxi():
    print("Vas a registrar un taxi")
    matricula = input("Ingrese matricula: ")
    modelo = input("Ingrese modelo: ")
    potencia = float(input("Ingrese potencia: "))
    licencia = int(input("Ingrese numero de licencia: "))
    t = Taxi(matricula, modelo, potencia, licencia)
    taxis.append(t)


def mostrar_taxis():
    if not taxis:
        print("No hay taxis registrados.")
    else:
        print("Taxis registrados:")
        for i, taxi in enumerate(taxis, start=1):
            print(f'Taxi #{i}:\n{taxi}')


def registrar_autobus():
    print("Vas a registrar un autobus")
    matricula = input("Ingrese matricula: ")
    modelo = input("Ingrese modelo: ")
    potencia = float(input("Ingrese potencia: "))
    asientos = int(input("Ingrese numero de asientos: "))
    a = Autobus(matricula, modelo, potencia, asientos)
    autobuses.append(a)


def mostrar_autobuses():
    if not autobuses:
        print("No hay autobuses registrados.")
    else:
        print("Autobuses registrados:")
        for i, autobus in enumerate(autobuses, start=1):
            print(f'Autobus #{i}:\n{autobus}')


print("Bienvenido a Huber")
while True:
    print("1.- Registrar taxi")
    print("2.- Mostrar taxis")
    print("3.- Registrar autobus")
    print("4.- Mostrar autobuses")
    print("5.- Salir")
    try:
        opcion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        continue

    if opcion == 1:
        registrar_taxi()
    elif opcion == 2:
        mostrar_taxis()
    elif opcion == 3:
        registrar_autobus()
    elif opcion == 4:
        mostrar_autobuses()
    elif opcion == 5:
        print("Gracias por usar Huber. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")