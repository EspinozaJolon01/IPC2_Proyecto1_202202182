from nodo_datos import nodo_datos
import os
import sys

class lista_datos:

    def __init__(self):
        self.primero = None
    

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return 


    def insertar_datos(self,Dato):
        if self.primero is None:
            self.primero=nodo_datos(Dato)
            return

        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo_datos(Dato)
    
    def recorrer_e_imprimir_listas(self):
        aux=self.primero
        while aux !=None:
            print("t:",aux.Dato.posicion_t,", A: ",aux.Dato.posicion_A,
                ", valor:",aux.Dato.valor, ", Valor Binario: ", aux.Dato.valor_binario)
            aux=aux.siguiente

    def actualizar_datos(self,t,A,valor,vinario):
        aux = self.primero

        while aux:
            aux.Dato.posicion_t = t
            aux.Dato.posicion_A = A
            aux.Dato.valor = valor
            aux.Dato.valor_binario = vinario
            aux = aux.siguiente
    


    def generar_grafica(self,nombre,amplitud,tiempo,nombre_matriz):
        f = open('bb.dot','w')
        # configuraciones del grafo
        text ="""
            digraph G {"Amplitud="""+amplitud+"""","Tiempo="""+tiempo+""""->" """+nombre+ """" bgcolor="skyblue" style="filled"
            subgraph cluster1 {fillcolor="blue:blue4" style="filled"
            node [ fillcolor="Cyan:Teal" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="navy:darkblue" gradientangle="315">\n"""
        aux = self.primero
        sentinela_de_filas=aux.Dato.posicion_t #iniciaria en 1
        fila_iniciada=False
        while aux != None:
            # Si mi fila actual es diferente a la que viene
            if sentinela_de_filas!=aux.Dato.posicion_t:
                #print(sentinela_de_filas,actual.celda.nivel,"hola")
                sentinela_de_filas=aux.Dato.posicion_t
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+str(aux.Dato.valor)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+str(aux.Dato.valor)+"""</TD>\n"""
            aux = aux.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o {nombre_matriz}.png")
        print("terminado")


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








    
