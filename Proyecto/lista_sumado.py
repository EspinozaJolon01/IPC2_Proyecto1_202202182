from nodo_sumado import nodo_sumado
import os

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
            print(" amplitud: ",actual.dato_sumado.amplitud,"tiempo: ",actual.dato_sumado.grupos,
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
        
    def generar_grafica(self,nombre,amplitud,tiempo,nombre_matriz):
        f = open('bb.dot','w')

        text ="""
            digraph G {"Amplitud="""+amplitud+""""->" """+nombre+ """" bgcolor="skyblue" style="filled"
            subgraph cluster1 {fillcolor="blue:blue4" style="filled"
            node [ fillcolor="Cyan:Teal" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="navy:darkblue" gradientangle="315">\n"""
        aux = self.primero
        sentinela_de_filas=aux.dato_sumado.num_grupo
        fila_iniciada=False
        
        text+="""<TR><TD border="3"  bgcolor="lavender" gradientangle="315">"""+"Grupo="+str(aux.dato_sumado.num_grupo)+" t="+str(aux.dato_sumado.grupos)+"""</TD>\n"""
        while aux != None:

            
            if sentinela_de_filas!=aux.dato_sumado.num_grupo:
                
                sentinela_de_filas=aux.dato_sumado.num_grupo
                
                fila_iniciada=False

                text+="""</TR>\n""" 
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+"Grupo="+str(aux.dato_sumado.num_grupo)+" t="+str(aux.dato_sumado.grupos)+"""</TD>\n"""
            if fila_iniciada==False:
                fila_iniciada=True

                
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+str(aux.dato_sumado.valor_resultado)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+str(aux.dato_sumado.valor_resultado)+"""</TD>\n"""
            aux = aux.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o {nombre_matriz}.png")
        print("terminado")

        
    




