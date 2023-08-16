from nodo import nodo

class lista_datos:

    def __init__(self) :
        self.primero = None
        self.ultimo = None

    def estado_lista(self):
        return self.primero == None

    def agregar_lista_de_xml(self,dato):
        if self.estado_lista() == True:
            self.primero = self.ultimo = nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(dato)

    def verificar_nombre(self,nombre):
        aux = self.primero

        while aux:
            if aux.datos.nombre == nombre:
                print("se repite la lista")
            else:
                print("")


    def recorrdio(self):
        aux = self.primero
        while aux != None:
            print("tiempo:", aux.datos.tiempo,"Amplitud: ", aux.datos.amplitud, "Valor: ", aux.datos.valor)
            aux = aux.siguiente 
    
    def recorrdio_binario(self):
        aux = self.primero
        while aux != None:
            print("tiempo:", aux.datos.tiempo,"Amplitud: ", aux.datos.amplitud, "Valor: ", aux.datos.cambio_dato)
            aux = aux.siguiente 
            


            