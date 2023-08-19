from nodo import nodo

class lista_datos:

    def __init__(self) :
        self.primero = None


    def insertar_dato(self,datos):
        if self.primero is None:
            self.primero=nodo(datos=datos)
            return
        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo(datos=datos)

    def verificar_nombre(self,nombre):
        aux = self.primero

        while aux:
            if aux.datos.nombre == nombre:
                print("se repite la lista")
            else:
                print("")


    def recorrer_e_imprimir_listas(self):
        print("")
        print("")

        
        nombre_ultima_matriz = None 
        
        aux = self.primero
        while aux != None:
            if aux.datos.nombre != nombre_ultima_matriz:
                print("-------------------------------------")
                print("Nombre:", aux.datos.nombre, ", tiempo:", aux.datos.tiempo, ", Amplitud:", aux.datos.amplitud)
                print("-------------------------------------")
                nombre_ultima_matriz = aux.datos.nombre  
                
            aux.datos.lista_valor.recorrer_e_imprimir_listas()
            aux = aux.siguiente    
        print("-------------------------------------")
        print("")





            