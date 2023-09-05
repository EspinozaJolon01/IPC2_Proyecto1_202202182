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
        resultado = ""  
        
        while self.primero:
            actual = self.primero  
            temp_string = ""  
            temp_niveles = ""  
        
        
            while actual:
                if actual.agrupado.patron == self.primero.agrupado.patron:
                    temp_niveles+=(str(actual.agrupado.tiempo))+","  
                
                actual=actual.siguiente
            
            buffer=""
            
            for digito in temp_niveles:
                if digito.isdigit():
                    buffer+=digito
                
                else:
                    if buffer!="":
                        self.eliminar(int(buffer))
                        buffer=""
                    else:
                        buffer=""
            resultado+=temp_niveles+"--"
        return resultado  

    
        











