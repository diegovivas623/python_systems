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
    while True:
        nombre_libro = input("Nombre del libro a agregar: ")
        if nombre_libro == "" or len(nombre_libro) < 4:
            print("Nombre no valido, ingresa uno valido")
        else:
            break

    while True:
        try: 
            año = int(input("Año del libro a agregar: "))
        except:
            print("Año no valido")
            continue
        if 0 < año <= 2028:
            break
        else:
            print("Año no valido, ingresa uno valido")

    while True:
        autor = input("Autor del libro a agregar: ")
        if autor == "" or len(autor) < 7:
            print("Autor no valido, ingresa uno valido")
        else:
            break
        

    for libro in libros:
        if libro["Libro"].lower() == nombre_libro.lower():
            print("El libro ya existe")
            return

    libro = {
        "Libro":nombre_libro,
        "Año":año,
        "Autor":autor,
        "Disponible": True
    }
    print("Libro agregado correctamente")
    libros.append(libro)

def verlibros():
    if len(libros) == 0:
        print("No hay libros registrados")
    else:
        for libro in libros:
            print("Libro: ", libro["Libro"])
            print("Autor: ", libro["Autor"])
            print("Año: ", libro["Año"])
            if libro["Disponible"] == True:
                print("Disponible: Si")
            else:
                print("Disponible: No")
            print()

def buscarlibro():
    buscar = input("Escribe el libro a buscar: ").lower()
    encontrado = False
    if buscar == "":
        print("No se puede buscar un libro vacio")
    else:
        for libro in libros:
            if libro["Libro"].lower() == buscar:
                print("Libro: ", libro["Libro"])
                print("Autor: ", libro["Autor"])
                print("Año: ", libro["Año"])
                if libro["Disponible"] == True:
                    print("Disponible: Si")
                else:
                    print("Disponible: No")
                print()
                encontrado = True
        if encontrado == False:
            print("El libro no esta registrado")

def prestarlibro():
    buscar = input("Escribe el libro a prestar: ").lower()
    encontrado = False
    if buscar == "":
        print("No se puede prestar un libro vacio")
    else:

        for libro in libros:
            if libro["Libro"].lower() == buscar:
                encontrado = True
                if libro["Disponible"] == True:
                    libro["Disponible"] = False
                    print("Toma tu libro")
                else:
                    print("El libro ya esta prestado")
        if encontrado == False:
                print("El libro no esta registrado ")


def devolverlibro():
    buscar = input("Escribe el libro a devolver: ").lower()
    encontrado = False
    if buscar == "":
            print("No se puede devolver un libro vacio")
    else:

        for libro in libros:
            if libro["Libro"].lower() == buscar:
                encontrado = True
                if libro["Disponible"] == False:
                    libro["Disponible"] = True
                    print("Gracias por devolver el libro")
                else:
                    print("El libro no se ha prestado")
        if encontrado == False:
            print("El libro no esta registrado")

def eliminarlibro():
    buscar = input("Escribe el libro a eliminar: ").lower()
    encontrado = False 
    if buscar == "":
            print("No se puede eliminar un libro vacio")
    else:

        for libro in libros:
            if libro["Libro"].lower() == buscar:
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
    if opcion <= 0 or opcion > 7:
        print("Opcion no valida, solo entre 1 y 7")
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
