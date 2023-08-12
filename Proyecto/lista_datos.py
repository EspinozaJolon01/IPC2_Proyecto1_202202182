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
            print("Matriz: ", aux.datos.nombre)
            print("tiempo:", aux.datos.tiempo,"Amplitud: ", aux.datos.amplitud, "Valor: ", aux.datos.valor)
            aux = aux.siguiente

    def binario(self):
        valor = 0
        aux = self.primero
        while aux != None:
            valor_actual = aux.datos.valor
            if valor_actual != 0:
                nuevo_valor = valor_actual
                nuevo_valor == valor
                print("Valor: ", nuevo_valor)
                aux = aux.siguiente
            else:
                print("Valor: ",  valor_actual)
                aux = aux.siguiente
            
    def verificar_nombre(self,nombre):
        pass


    def actualizar_datos(self, nombre, nuevo_tiempo, nuevo_amplitud, nuevo_valor):
        aux = self.primero
        while aux:
            if nombre == aux.datos.nombre:
                aux.datos.tiempo = nuevo_tiempo
                aux.datos.amplitud = nuevo_amplitud
                aux.datos.valor = nuevo_valor
                print("Actualizar matriz")
                return
            aux = aux.siguiente
        
        print("Sin ninguna modificación")

            


            