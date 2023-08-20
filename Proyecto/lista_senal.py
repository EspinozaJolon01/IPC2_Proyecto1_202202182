from nodo_senal import nodo_senal


class lista_senal:

    def __init__(self) :
        self.primero = None


    def insertar_dato(self,Senal):
        if self.primero is None:
            self.primero=nodo_senal(Senal)
            return
        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo_senal(Senal)

    def verificar_nombre(self,nombre):
        aux = self.primero

        while aux:
            if aux.Senal.nombre == nombre:
                print("se repite la lista")
            else:
                print("No se encontro el nombre")


    def recorrer_e_imprimir_listas(self):
        print("")
        print("")

        
        nombre_ultima_matriz = None 
        
        aux = self.primero
        while aux != None:
            if aux.Senal.nombre != nombre_ultima_matriz:
                print("-------------------------------------")
                print("Nombre:", aux.Senal.nombre, ", tiempo:", aux.Senal.tiempo, ", Amplitud:", aux.Senal.amplitud)
                print("-------------------------------------")
                nombre_ultima_matriz = aux.Senal.nombre  
                
            aux.Senal.lista_datos.recorrer_e_imprimir_listas()
            aux = aux.siguiente    
        print("-------------------------------------")
        print("")

    def grafica_mi_lista_original(self):
        actual=self.primero
        while actual != None:
            actual.Senal.lista_datos.generar_grafica(actual.Senal.nombre,
                                                    str(actual.Senal.amplitud),
                                                    str(actual.Senal.tiempo))
            #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente
            




            