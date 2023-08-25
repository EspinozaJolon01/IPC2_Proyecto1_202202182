from nodo_patron import nodo_patron

class lista_patron:

    def __init__(self):
        self.primero = None
        self.contador_patron=0


    def insertar_dato(self,patron):
        if self.primero is None:
            self.primero = nodo_patron(patron=patron)
            self.contador_patron+=1
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_patron(patron=patron)
        self.contador_patron+=1

    def recorrer_e_imprimir_lista(self):
        print("--------------------------------------")
        actual = self.primero
        while actual != None:
            print(" Grupo: ",actual.patron.grupo_patron,"Cadena-grupo: ",actual.patron.cadena_patron)
            actual = actual.siguiente
        print("--------------------------------------")