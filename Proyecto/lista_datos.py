from nodo_datos import nodo_datos
import os

class lista_datos:

    def __init__(self):
        self.primero=None

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



    def generar_grafica(self,nombre,amplitud,tiempo):
        f = open('bb.dot','w')
        # configuraciones del grafo
        text ="""
            digraph G {"tiempo="""+tiempo+"""","CeldasNivel="""+amplitud+""""->" """+nombre+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.Dato.posicion_t #iniciaria en 1
        fila_iniciada=False
        while actual != None:
            # Si mi fila actual es diferente a la que viene
            if  sentinela_de_filas!=actual.Dato.posicion_t:
                #print(sentinela_de_filas,actual.celda.nivel,"hola")
                sentinela_de_filas=actual.Dato.posicion_t
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.Dato.valor)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.Dato.valor)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o 17agosto.png')
        print("terminado")



    
