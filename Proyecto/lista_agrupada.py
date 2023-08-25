from nodo_agrupado import nodo_agrupado

class lista_agrupada:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 1
    
    def agregar_nodo(self,agrupado):
        if self.primero is None:
            self.primero=nodo_agrupado(agrupado=agrupado)
            self.tamanio += 1
            return
        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo_agrupado(agrupado=agrupado)
        self.tamanio += 1
    
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
        



    def recorer(self):
        aux = self.primero
        while aux:
            print()
            print("Nivel: ",aux.agrupado.tiempo,"caneda-patron",aux.agrupado.patron)
            aux = aux.siguiente

    def eliminar(self,tiempo):
        actual = self.primero
        anterior = None
        while actual and actual.agrupado.tiempo != tiempo:
            anterior=actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def encontrar_coincidencias(self):
        print("")
        resultado = ""  # Inicializa un string vacío para almacenar el resultado final  
        # Bucle principal que se ejecuta mientras haya nodos en la lista
        while self.primero:
            actual = self.primero  # Comienza desde el primer nodo en la lista
            temp_string = ""  # String temporal para almacenar niveles coincidentes
            temp_niveles = ""  # Lista temporal para almacenar niveles      
        # Bucle interno para recorrer la lista de nodos y buscar coincidencias
        
            while actual:
                if actual.agrupado.patron == self.primero.agrupado.patron:
                    temp_niveles+=(str(actual.agrupado.tiempo))+","  # Agrega el nivel a la lista temporal
                # Si no hay nodo siguiente, elimina el primer nodo
                actual=actual.siguiente
            # Terminamos la iteración, quiere decir que ya tenemos la coincidencias:
            buffer=""
            #print(temp_niveles)
            for digito in temp_niveles:
                if digito.isdigit():
                    buffer+=digito
                #Quiere decir que viene una coma
                else:
                    if buffer!="":
                        self.eliminar(int(buffer))
                        buffer=""
                    else:
                        buffer=""
            resultado+=temp_niveles+"--"
        return resultado  # Devuelve el resultado final con la agrupación de niveles

    
        











