from nodo_senal import nodo_senal
from patron import patron
from lista_sumado import lista_sumando
from dato_sumado import dato_sumado
import xml.etree.ElementTree as ET
import os


class lista_senal:

    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertar_dato(self,Senal):
        if self.primero is None:
            self.primero=nodo_senal(Senal=Senal)
            return
        aux=self.primero
        while aux.siguiente:
            aux=aux.siguiente
        aux.siguiente=nodo_senal(Senal=Senal)

    def generar_grafia(self,nombre,nombre_matriz):
        aux = self.primero
        verificar = False

        while aux:
            if aux.Senal.nombre == nombre:
                verificar = True
                break
            aux = aux.siguiente

        if verificar:
                aux.Senal.lista_datos.generar_grafica(aux.Senal.nombre,str(aux.Senal.amplitud),str(aux.Senal.tiempo),nombre_matriz)
                #aux.Senal.lista_sumando.generar_grafica(aux.Senal.nombre,str(aux.Senal.amplitud),str(aux.Senal.tiempo),nombre_matriz)
                aux=aux.siguiente
        else:
            print("no se encontro en la lista")


    def generar_grafia_pratones(self,nombre,nombre_matriz):
        aux = self.primero
        verificar = False

        while aux:
            if aux.Senal.nombre == nombre:
                verificar = True
                break
            aux = aux.siguiente

        if verificar:
                aux.Senal.lista_datos.generar_grafica_praton(aux.Senal.nombre,str(aux.Senal.amplitud),str(aux.Senal.tiempo),nombre_matriz)
                #aux.Senal.lista_sumando.generar_grafica(aux.Senal.nombre,str(aux.Senal.amplitud),str(aux.Senal.tiempo),nombre_matriz)
                aux=aux.siguiente
        else:
            print("no se encontro en la lista")

    def generar_grafia_reducida(self,nombre,nombre_matriz):
        aux = self.primero
        verificar = False

        while aux:
            if aux.Senal.nombre == nombre:
                verificar = True
                break
            aux = aux.siguiente

        if verificar:
                #aux.Senal.lista_datos.generar_grafica(aux.Senal.nombre,str(aux.Senal.amplitud),str(aux.Senal.tiempo),nombre_matriz)
                aux.Senal.lista_sumando.generar_grafica(aux.Senal.nombre,str(aux.Senal.amplitud),str(aux.Senal.tiempo),nombre_matriz)
                aux=aux.siguiente
        else:
            print("no se encontro en la lista")
    

    def actualizar_matriz(self,nombre):
        dato = None
        aux = self.primero

        while aux:
            if aux.Senal.nombre == nombre:
                if dato is None:
                    self.primero = aux.siguiente
                    print("Se actualizo....")
                else:
                    dato.siguiente = aux.siguiente  #realizamos la eliminacion
                    print("Se actualizo....")
                aux = aux.siguiente
            else:
                dato = aux   #acutalizamos los punteros
                aux = aux.siguiente
        


    def recorrer_e_imprimir_listas(self):
        print("")
        print("")
        #nombre_ultima_matriz = None 
        
        aux = self.primero
        while aux != None:
            #if aux.Senal.nombre != nombre_ultima_matriz:
            print("-------------------------------------")
            print("Nombre:", aux.Senal.nombre, ", tiempo:", aux.Senal.tiempo, ", Amplitud:", aux.Senal.amplitud)
            print("-------------------------------------")
                #nombre_ultima_matriz = aux.Senal.nombre  
                
            aux.Senal.lista_datos.recorrer_e_imprimir_listas()
            aux = aux.siguiente    
        print("-------------------------------------")
        print("")

    def grafica_mi_lista_original(self):
        actual=self.primero
        while actual != None:
            actual.Senal.lista_datos.generar_grafica(actual.Senal.nombre,str(actual.Senal.amplitud),str(actual.Senal.tiempo))
            #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente

    # def grafica_mi_lista_reducida(self):
    #     actual=self.primero
    #     while actual != None:
    #         actual.Senal.lista_sumando.generar_grafica(actual.Senal.nombre,str(actual.Senal.amplitud),str(actual.Senal.tiempo))
    #         #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
    #         actual=actual.siguiente

    def eliminar_lista_nodo(self):
        while self.primero:
            aux = self.primero
            self.primero = self.primero.siguiente
            del aux

    def calcular_los_patrones(self,nombre,lista_suma):

        actual = self.primero
        while actual != None:
            if actual.Senal.nombre==nombre:
                actual.Senal.lista_grupo=actual.Senal.lista_datos.devolver_patrones_por_nivel(actual.Senal.lista_grupo)

                listra_grup_temp=actual.Senal.lista_grupo
                grupos_sin_analizar=listra_grup_temp.encontrar_coincidencias()
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.Senal.lista_datos.devolver_cadena_del_grupo(buffer)
                        actual.Senal.listra_patrones.insertar_dato(patron=patron(buffer,cadena_grupo,actual.Senal.listra_patrones.get_tam()))
                        
                        self.realizar_suma(actual.Senal.lista_datos,actual.Senal.amplitud,buffer,actual.Senal.listra_patrones.get_tamanio(),lista_suma)
                        
                        buffer=""
                    else:
                        buffer=""
                
                #actual.Senal.listra_patrones.recorrer_e_imprimir_lista()
                return
            actual=actual.siguiente
        print ("No se encontró la carcel")

    def realizar_suma(self, lista_datos, amplitud, grupo,num_grupo,lista_suma):
        suma = 0
        contador = 0
        string_resultado = ""
        
        tiempo_sin_comas = grupo.replace(",","")
        
        contador_comas = grupo.count(',')
        for i in range(1, int(amplitud)+1):
            for datos_lista in lista_datos:
                if self.analizar(str(datos_lista.Dato.posicion_t),grupo) and int(datos_lista.Dato.posicion_A) == i:
                    #print(int(datos_lista.Dato.posicion_A),"=", i)
                    suma = suma + int(datos_lista.Dato.valor)
                    
                    contador += 1
                    if contador == contador_comas:
                        string_resultado+=str(suma)+","
                        lista_suma.insertar_dato(dato_sumado(datos_lista.Dato.posicion_A,grupo,suma,num_grupo))    
            contador = 0
            suma = 0
        #lista_suma.recorrer()

    def actualizar_tem(self,lista_temporal_suma,nombre):
        aux = self.primero
        while aux:
            if aux.Senal.nombre ==  nombre:
                aux.Senal.lista_sumando = lista_temporal_suma
                return
            aux = aux.siguiente

    def analizar(self,analizar_tiempo,tiempos):
        ini = 0
        stop = 0
        while stop <= len(tiempos):
            if stop == len(tiempos) or tiempos[stop] == ',':
                tiempo_actual = tiempos[ini:stop]
                if tiempo_actual == analizar_tiempo:
                    return True
                ini = stop + 1
            stop += 1
        return False



    def generar_archivo_xml(self,nombre):
        # Crear el elemento raíz
        senales_reducidas = ET.Element("senalesReducidas")
        aux = self.primero

        while aux:
        # Crear el elemento senal con atributos nombre y A
            
            senal = ET.SubElement(senales_reducidas, "senal", nombre=f"{aux.Senal.nombre}", A=f"{aux.Senal.amplitud}")
            num_gruposv = aux.Senal.listra_patrones
            # Crear grupos dentro de la sena
            for g in num_gruposv:
                grupo = ET.SubElement(senal, "grupo",g=f"{g.patron.num_grupos}" )
                tiempos = ET.SubElement(grupo, "tiempos"  )
                tiempos.text = g.patron.grupo_patron

                datos_gru = ET.SubElement(grupo, "datosGrupo")
                dato_grupos = aux.Senal.lista_sumando
                for d in dato_grupos:
                    if d.dato_sumado.num_grupo == g.patron.num_grupos:

                        dato = ET.SubElement(datos_gru, "dato", A=f"{d.dato_sumado.amplitud}")
                        dato.text = str(d.dato_sumado.valor_resultado)
                    #dato.text = str((g + d) % 10)

            aux = aux.siguiente
            
        # Crear el árbol XML
        self.prettify_xml(senales_reducidas)
        tree = ET.ElementTree(senales_reducidas)
        print("-> Proceso terminado correcto...")
        tree.write(f"{nombre}.xml", encoding="utf-8", xml_declaration=True)

    
    def prettify_xml(self,element, indent='    '):
        queue = [(0, element)]  # (level, element)
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level+1) 
            if queue:
                element.tail = '\n' + indent * queue[0][0]  
            else:
                element.tail = '\n' + indent * (level-1)  
            queue[0:0] = children


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
    
    
        
