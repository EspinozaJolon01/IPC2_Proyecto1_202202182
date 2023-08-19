from nodo_celda import nodo_celda

class lista_celda:

    def __init__(self):
        self.primero=None

    def insertar_datos(self,celda):
        if self.primero is None:
            self.primero=nodo_celda(celda=celda)
            return

        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo_celda(celda=celda)
    
    def recorrer_e_imprimir_listas(self):
        aux=self.primero
        while aux !=None:
            print("t:",aux.celda.posicion_t,", A: ",aux.celda.posicion_A,
                ", valor:",aux.celda.valor, ", Valor Binario: ", aux.celda.valor_binario)
            aux=aux.siguiente

    
