from nodo_senal import nodo_senal


class lista_senal:

    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertar_dato(self,Senal):
        if self.primero is None:
            self.primero=nodo_senal(Senal=Senal)
            return
        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo_senal(Senal=Senal)

    def generar_grafia(self,nombre,nombre_matriz):
        aux = self.primero
        verificar = False

        while aux:
            if aux.Senal.nombre == nombre:
                verificar = True
                break
            aux = aux.siguiente

        if verificar:
                aux.Senal.lista_datos.generar_grafica(aux.Senal.nombre,str(aux.Senal.amplitud),str(aux.Senal.tiempo),nombre_matriz)
            #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
                aux=aux.siguiente
        else:
            print("no se encontro en la lista")
    

    def actualizar_matriz(self,nombre):
        dato = None
        aux = self.primero

        while aux:
            if aux.Senal.nombre == nombre:
                if dato is None:
                    self.primero = aux.siguiente
                else:
                    dato.siguiente = aux.siguiente  #realizamos la eliminacion
                    print("Se actualizo....")
                aux = aux.siguiente
            else:
                dato = aux   #acutalizamos los punteros
                aux = aux.siguiente
        


    def recorrer_e_imprimir_listas(self):
        print("")
        print("")

        
        #nombre_ultima_matriz = None 
        
        aux = self.primero
        while aux != None:
            #if aux.Senal.nombre != nombre_ultima_matriz:
            print("-------------------------------------")
            print("Nombre:", aux.Senal.nombre, ", tiempo:", aux.Senal.tiempo, ", Amplitud:", aux.Senal.amplitud)
            print("-------------------------------------")
                #nombre_ultima_matriz = aux.Senal.nombre  
                
            aux.Senal.lista_datos.recorrer_e_imprimir_listas()
            aux = aux.siguiente    
        print("-------------------------------------")
        print("")

    def grafica_mi_lista_original(self):
        actual=self.primero
        while actual != None:
            actual.Senal.lista_datos.generar_grafica(actual.Senal.nombre,str(actual.Senal.amplitud),str(actual.Senal.tiempo))
            #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente

    def eliminar_lista_nodo(self):
        while self.primero:
            aux = self.primero
            self.primero = self.primero.siguiente
            del aux
    
    
            




            