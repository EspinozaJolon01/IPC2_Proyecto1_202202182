

def datos_personales():
    print("")
    print(">Jose Luis Espinoza Jolon")
    print(">202202182")
    print(">Introduccion a la Programacion y computacion 2 seccion D")
    print(">Ingeniere en ciesncas y sistemas")
    print(">4to semestre")


def menu_princial():
    print("")
    print("--------------------------------------")
    print("Menu principal")
    print("--------------------------------------")
    print("")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostar datos del estudiante")
    print("5. Generar grafica")
    print("6. Inicialiar sistema")
    print("7. Salida")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("opcion1")
        menu_princial()
    elif opcion == 2:
        print("opcion2")
        menu_princial()
    elif opcion == 3:
        print("opcion1")
        menu_princial()
    elif opcion == 4:
        datos_personales()
        menu_princial()
    elif opcion == 5:
        print("opcion5")
        menu_princial()
    elif opcion == 6:
        print("opcion6")
        menu_princial()
    elif opcion == 7:
        print("Saliendo del programa, vuelva pronto")
    else:
        print("Opcion invalidad, vuelve a intentarlo...")
        menu_princial()

menu_princial()
        