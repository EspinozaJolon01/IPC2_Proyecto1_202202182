from nodo_patron import nodo_patron

class lista_patron:

    def __init__(self):
        self.primero = None
        self.contador_patron=0
        self.contador_patrones=1


    def insertar_dato(self,patron):
        if self.primero is None:
            self.primero = nodo_patron(patron=patron)
            self.contador_patron+=1
            self.contador_patrones+=1
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_patron(patron=patron)
        self.contador_patron+=1
        self.contador_patrones+=1

    def recorrer_e_imprimir_lista(self):
        print("--------------------------------------")
        actual = self.primero
        while actual != None:
            print(" Grupo: ",actual.patron.grupo_patron,"Cadena-grupo: ",actual.patron.cadena_patron)
            actual = actual.siguiente
        print("--------------------------------------")
    
    def get_tamanio(self):
        return self.contador_patron
    
    def get_tam(self):
        return self.contador_patrones
    

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