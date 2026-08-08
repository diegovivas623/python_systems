#sistema bancario 
def menu():
    print("=======BANCO=======")
    print("1.Crear cuenta")
    print("2.Consultar saldo")
    print("3.Depositar dinero")
    print("4.Retirar dinero")
    print("5.Ver informacion de la cuenta")
    print("6.Salir")

def crearcuenta():
    while True:
        nombre = input("Agrega tu nombre: ")
        if nombre == "" or len(nombre) <= 3:
            print("Nombre no valido")
        else:
            break 
    while True:
        try:
            edad = int(input("Agrega tu edad: "))
        except:
            print("Edad no valida")
            continue
        if edad >= 18:
            break
        else:
            print("No puedes crear una cuenta")

    while True:
        try:
            cuenta = int(input("Agrega tu numero de cuenta: "))
        except:
            print("Cuenta no valida")
            continue
        if cuenta >= 1000:
            break
        else:
            print("Cuenta no valida, añade mas caracteres")

    while True:
        try:
            saldo_inicial = int(input("Agrega saldo inicial en tu cuenta: "))
        except: 
            print("Saldo no valido")
            continue
        if saldo_inicial >= 0:
            break
        else:
            print("Cuenta no valida, no valores invalidos")

    cuenta = {
        "Nombre": nombre,
        "Edad" : edad,
        "Cuenta": cuenta,
        "Saldo_Inicial" : saldo_inicial
    }
    print("Cuenta registrada exitosamente")
    cuentas.append(cuenta)


def consultasaldo():
    buscar = int(input("Ingresa tu numero de cuenta para ver saldo: "))
    

def depositardinero():
    buscar = int(input("Ingresa tu numero de cuenta para depositar dinero: "))

def retirardinero():
    buscar = int(input("Ingresa tu numero de cuenta para retirar dinero"))

def vercuenta():
    buscar = int(input("Ingresa numero de cuenta para ver tus datos: "))

cuentas = []
opcion = 0

while opcion != 6:
    menu()
    try:
        opcion = int(input("Agrega lo que quieres hacer: "))
    except:
        print("Escoje una opcion valida")
        continue
    if opcion == 1:
        crearcuenta()
    elif opcion == 2:
        consultasaldo()
    elif opcion == 3:
        depositardinero()
    elif opcion == 4:
        retirardinero()
    elif opcion == 5:
        vercuenta()
    elif opcion == 6:
        print("Vuelve a visitar tu banco favorito")
        break

