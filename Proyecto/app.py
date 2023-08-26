
from lectura import lectura
from lista_datos import lista_datos
#from lista_suma import lista_suma




import os.path as path

lecturas = lectura()
lista = lista_datos()
#sumaa = lista_suma()


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
        
        lecturas.lectura_xml(self.ruta)
        
        print("--------------------------------------")
        print("")
            
    def matriz_recorrer(self):
        print("")
        print("--------------------------------------")
        print("iniciando proceso")
        lecturas.listados()

    def generador_grafi(self):
        print("")
        print("--------------------------------------")
        nombre =  input("ingrese el nombre de la matriz que quiere graficar: ")
        print("--------------------------------------")
        print("1. Grafica normal")
        print("2. Grafica reducida")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            nombre_de_grafica = input("Ingrese el nombre que quiere guarda la matriz: ")
            lecturas.generar_grafica(nombre,nombre_de_grafica)
        elif opcion == 2:
            print("opcion")
        else:
            print("opcion no valida")
        
        print("")

    def verificar_nombre(self):
        nombre = input("ingrese nombre de matriz: ")
        lecturas.porbrar_matriz(nombre)
    
    def inicializar_sistema(self):
        print("")
        print("--------------------------------------")
        self.ruta = ""
        print("Elimando la lista")
        lecturas.eliminar_lista()
        print("")
    
    def prueba_grafica(self):
        lecturas.grafica_sumados()
    
    def prueba_calcular_matriz3(self):
        #lista_sum.recorrer()
        print("----------------------")
        #sumaa.imprimir_resultados()
    def crear_xml(self):
        print("")
        print("--------------------------------------")
        nombre_arhivo = input("ingrese el nombre para su arhivo: ")
        print("Generando archivo...")
        lecturas.crear_xml(nombre_arhivo)
        

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
        print("--------------------------------------")
        opcion = int(input("->Ingrese una opcion: "))
        print("--------------------------------------")

        if opcion == 1:
            self.nombre_archivo_xml()
            self.menu_princial()
        elif opcion == 2:
            if self.ruta != "":
                self.lectura_archivo()
            else:
                print("->Debes cargar el archivo")    
            self.menu_princial()
        elif opcion == 3:
            if self.ruta != "":
                self.crear_xml()
            else:
                print("->Debes cargar el archivo")
            self.menu_princial()
        elif opcion == 4:
            self.matriz_recorrer()
            self.menu_princial()
        elif opcion == 5:
            self.generador_grafi()
            self.menu_princial()
        elif opcion == 6:
            self.inicializar_sistema()
            self.menu_princial()
        elif opcion == 7:
            print("->Saliendo del programa, vuelva pronto")
        else:
            print("->Opcion invalidad, vuelve a intentarlo...")
            self.menu_princial()
    
app_llamar = app()

app_llamar.menu_princial()