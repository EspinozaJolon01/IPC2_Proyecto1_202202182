from nodo_agrupado import nodo_agrupado

class lista_agrupada:

    def __init__(self):
        self.primero = None
        self.ultimo = None
    



    def agregar_nodo(self,agrupado):
        if self.primero is None:
            self.primero=nodo_agrupado(agrupado=agrupado)
            return
        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo_agrupado(agrupado=agrupado)
    
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
        


    def verificar_agrupar(self):
        aux = self.primero
        patron_anterior = None
        grupo_num = 0

        while aux:
            patron_actual = aux.agrupado.patron

            if patron_actual == patron_anterior:
                if grupo_num == 0:
                    grupo_num += 1
                    print("Grupo", grupo_num, ":", patron_actual)
                print(patron_actual)
            else:
                grupo_num = 0
            
            patron_anterior = patron_actual
            aux = aux.siguiente

    def recorer(self):
        aux = self.primero

        while aux:
            print("prueba")
            print(aux.agrupado.patron)
            aux = aux.siguiente










