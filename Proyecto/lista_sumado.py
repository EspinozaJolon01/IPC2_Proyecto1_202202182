from nodo_sumado import nodo_sumado

class lista_sumando:

    def __init__(self):
        self.primero = None
        
    def insertar_dato(self,dato_sumado):
        if self.primero is None:
            self.primero = nodo_sumado(dato_sumado=dato_sumado)
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_sumado(dato_sumado=dato_sumado)

    def recorrer(self):
        print("--------------------------------------")
        actual = self.primero
        while actual != None:
            print(" amplitud: ",actual.dato_sumado.amplitud,"tiempo: ",actual.dato_sumado.tiempo,
                "valor: ", actual.dato_sumado.valor_resultado, "Grupo: ", actual.dato_sumado.num_grupo)
            actual = actual.siguiente
        print("--------------------------------------")


    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration

        
    




