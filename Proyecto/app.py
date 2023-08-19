
from lectura import lectura
import os.path as path

lecturas = lectura()

class app:

    def __init__(self):
        self.ruta = ""


    def datos_personales(self):

        print("")
        print(">Jose Luis Espinoza Jolon")
        print(">202202182")
        print(">Introduccion a la Programacion y computacion 2 seccion D")
        print(">Ingeniere en ciencias y sistemas")
        print(">4to semestre")

    def nombre_archivo_xml(self):
        print("")
        print("--------------------------------------")
        self.ruta = input("Ingrese el nombre: ")
        if path.exists(self.ruta+".xml") == False: #verifica que la ruta esta exista
            print("No encontrado")

        print("--------------------------------------")
        print("")
    
    def lectura_archivo(self):
        print("")
        print("--------------------------------------")
        print("iniciando proceso")
        lecturas.lectura_xml(self.ruta)
        print("--------------------------------------")
        print("")
            
    def matriz_recorrer(self):
        print("")
        print("--------------------------------------")
        lecturas.listados()


        

    def menu_princial(self):
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
            self.nombre_archivo_xml()
            self.menu_princial()
        elif opcion == 2:
            self.lectura_archivo()
            self.menu_princial()
        elif opcion == 3:
            self.matriz_recorrer()
            self.menu_princial()
        elif opcion == 4:
            self.datos_personales()
            self.menu_princial()
        elif opcion == 5:
            print("opcion5")
            self.menu_princial()
        elif opcion == 6:
            print("opcion6")
            self.menu_princial()
        elif opcion == 7:
            print("Saliendo del programa, vuelva pronto")
        else:
            print("Opcion invalidad, vuelve a intentarlo...")
            self.menu_princial()
    
app_llamar = app()

app_llamar.menu_princial()