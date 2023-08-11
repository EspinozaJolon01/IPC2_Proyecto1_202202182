from nodo import nodo

class lista_datos():

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

    def recorrdio(self):
        aux = self.primero
        while aux != None:
            print("tiempo:", aux.datos.amplitud,"Amplitud: ", aux.datos.frecuencia, "Valor: ", aux.datos.valor)
            aux = aux.siguiente

    def binario(self):
        aux = self.primero
        while aux != None:
            valor_actual = int(aux.datos.valor)
            if valor_actual != 0:
                nuevo_valor = valor_actual
                nuevo_valor == 1
                print("Valor: ", str(nuevo_valor))
                aux = aux.siguiente
            else:
                print("Valor: ",  str(valor_actual))
                aux = aux.siguiente
            
            