def menu():
    print("=========BIBLIOTECA========")
    print("1.Agregar libro")
    print("2.Ver libros")
    print("3.Buscar libro")
    print("4.Prestar libro")
    print("5.Devolver libro")
    print("6.Eliminar libro")
    print("7.Salir")

def agregarlibro():
    nombre_libro = input("Nombre del libro a agregar: ")
    try: 
        año = int(input("Año del libro a agregar: "))
    except:
        print("Año no valido")
        return
    autor = input("Autor del libro a agregar: ")
    
    if nombre_libro =="" :
        print("Libro no valido")
        return
    elif año > 2028 or año <= 0:
        print("Año no valido")
        return
    elif not autor:
        print("Autor no valido")
        return

    for libro in libros:
        if libro["Libro"] == nombre_libro:
            print("El libro ya existe")
            return

    libro = {
        "Libro":nombre_libro,
        "Año":año,
        "Autor":autor,
        "Disponible": True
    }
    libros.append(libro)

def verlibros():
    if len(libros) == 0:
        print("No hay libros registrados")
    else:
        for libro in libros:
            print("Libro: ", libro["Libro"])
            print("Autor: ", libro["Autor"])
            print("Año: ", libro["Año"])
            print("Disponible: ", libro["Disponible"])
            print()

def buscarlibro():
    buscar = input("Escribe el libro a buscar: ")
    encontrado = False
    if buscar == "":
        print("No se puede buscar un libro vacio")
    else:
        for libro in libros:
            if libro["Libro"] == buscar:
                print(libro)
                encontrado = True
        if encontrado == False:
            print("El libro no esta registrado")

def prestarlibro():
    buscar = input("Escribe el libro a prestar: ")
    encontrado = False
    if buscar == "":
        print("No se puede prestar un libro vacio")
    else:

        for libro in libros:
            if libro["Libro"] == buscar:
                encontrado = True
                if libro["Disponible"] == True:
                    libro["Disponible"] = False
                    print("Toma tu libro")
                else:
                    print("El libro ya esta prestado")
        if encontrado == False:
                print("El libro no esta registrado ")


def devolverlibro():
    buscar = input("Escribe el libro a devolver: ")
    encontrado = False
    if buscar == "":
            print("No se puede devolver un libro vacio")
    else:

        for libro in libros:
            if libro["Libro"] == buscar:
                encontrado = True
                if libro["Disponible"] == False:
                    libro["Disponible"] = True
                    print("Gracias por devolver el libro")
                else:
                    print("El libro no se ha prestado")
        if encontrado == False:
            print("El libro no esta registrado")

def eliminarlibro():
    buscar = input("Escribe el libro a eliminar: ")
    encontrado = False 
    if buscar == "":
            print("No se puede eliminar un libro vacio")
    else:

        for libro in libros:
            if libro["Libro"] == buscar:
                libros.remove(libro)
                print("Libro eliminado correctamente")
                encontrado = True
        if encontrado == False:
            print("No se puede borrar el libro, porque no esta registrado")

libros = []
opcion = 0

while opcion != 7:
    menu()
    try:
        opcion = int(input("¿Qué deseas hacer?: "))
    except:
        print("Opcion no valida, verifica la opción")
        continue
    if opcion == 1:
        agregarlibro()
    elif opcion == 2:
        verlibros()
    elif opcion == 3:
        buscarlibro()
    elif opcion == 4:
        prestarlibro()
    elif opcion == 5:
        devolverlibro()
    elif opcion == 6:
        eliminarlibro()
    elif opcion == 7:
        print("Vuelva pronto a su libreria favorita")
        break
