def minutos():
    minutos = int(input("Ingrese la cantidad de minutos: "))
    horas = minutos / 60
    print(f"{minutos} minutos equivalen a {horas} horas.")

def horas():
    horas = int(input("Ingrese la cantidad de horas: "))
    segundos = horas * 3600
    print(f"{horas} horas equivalen a {segundos} segundos.")

while True:
    print("Seleccione la conversión que desea realizar:")
    print("1. Segundos a minutos")
    print("2. Minutos a horas")
    print("3. Horas a segundos")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        segundos()
    elif opcion == '2':
        minutos()
    elif opcion == '3':
        horas()