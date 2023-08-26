import xml.etree.ElementTree as ET
from Senal import Senal
from Dato import Dato
from lista_senal import lista_senal
from Dato import Dato
from lista_datos import lista_datos
from lista_agrupada import lista_agrupada
from lista_patron import lista_patron
from lista_sumado import lista_sumando






class lectura:

    def __init__(self) :
        self.lista_senal_temp = lista_senal()
        self.lista_datos_temp = lista_datos()
        

    def lectura_xml(self, ruta):

        
        try:
            xml_file = open(f"{ruta}.xml")
            if xml_file.readable():
                xml_data = ET.fromstring(xml_file.read())
                lst_doc = xml_data.findall("senal")
                self.lista_senal_temp = lista_senal()
                
                for doc in lst_doc:
                    print("-------------------------------------")
                    print(f"Nombre: {doc.get('nombre')}")
                    nombre = doc.get('nombre')
                    tiempo = int(doc.get('t'))
                    amplitud = int(doc.get('A'))

                    print("-------------------------------------")
                    print("")

                    self.lista_datos_temp = lista_datos()
                    lista_temporal_grupos = lista_agrupada()
                    lista_temporal_patrones = lista_patron()
                    lista_temporal_suma = lista_sumando()
                    
                    

                    if 0 < tiempo <= 3600 and 0 < amplitud <= 130:
                        for t in range(1, tiempo + 1):
                            for A in range(1, amplitud + 1):
                                valor_encontrado = False
                                datos_lista = doc.findall("dato")
                                for dato in datos_lista:
                                    dato_t = int(dato.get('t'))
                                    dato_A = int(dato.get('A'))

                                    if dato_t == t and dato_A == A:
                                        valor = dato.text
                                        valor_nulo = 0 if valor is None or valor.strip() == "" else int(valor)
                                        valor_binario = 1 if valor_nulo != 0 else 0
                                        valor_encontrado = True
                                        break
                                if valor_encontrado:
                                    #print(f"Coordenada t={t}, A={A}, Valor={valor_nulo}")
                                    dato_encontrado = Dato(t,A,valor_nulo,valor_binario)
                                    #lista_datos_temp.insertar_datos(dato_encontrado)
                                else:
                                    print(f"Falta valor en coordenada t={t}, A={A}")
                                    dato_encontrado = Dato(t,A,"0","0")
                                    
                                
                                self.lista_datos_temp.insertar_datos(dato_encontrado)
                                
                                
                        self.lista_senal_temp.actualizar_matriz(nombre)
                        self.lista_senal_temp.insertar_dato(Senal(nombre,tiempo,amplitud,self.lista_datos_temp,lista_temporal_grupos,lista_temporal_patrones,lista_temporal_suma))
                        self.lista_senal_temp.calcular_los_patrones(nombre,lista_temporal_suma)
                        self.lista_senal_temp.actualizar_tem(lista_temporal_suma,nombre)
                        #self.lista_senal_temp.recorrer_e_imprimir_listas()
                        #self.agregar_cadena(tiempo,self.lista_datos_temp)
                        
                        
                        
                
                    
                    else:
                        print("El tiempo o la amplitud están fuera de los límites.")            
                                
                    
    
                    print("-------------------------------------")

                    print("Proceso terminado")
                        
                
                xml_file.close()
            else:
                print(False)
        except Exception as rr:
            print("Error por terminal", rr)

    def validar_salto_de_linea(self, t, A):
        tiempos = int(self.tiempo)
        amplitudes = int(self.amplitud)
        encontrado = False  

        for i in range(1, tiempos + 1):
            for j in range(1, amplitudes + 1):
                if int(t) == i and int(A) == j:
                    encontrado = True  
                    break  
            if encontrado:  
                break
        if encontrado:
            print("Todo bien")
        else:
            print(f"Falta un dato en t: {t}, A: {A}")
    
    """
    def agregar_cadena(self, tiempos, lista_dato):
        lista_temp = lista_agrupada()

        for t in range(1, tiempos + 1):
            agrupar = ""
            nodo_actual = lista_dato.primero

            while nodo_actual:
                valor_bi = nodo_actual.Dato.valor_binario
                time = nodo_actual.Dato.posicion_t

                if t == int(time):
                    agrupar += str(valor_bi)

                nodo_actual = nodo_actual.siguiente
            
            lista_d = agrupado(t, agrupar)
            lista_temp.agregar_nodo(lista_d)
        lista_temp.recorer()
    """
        




    def patrones_prueba(self):
        self.lista_senal_temp.calcular_los_patrones("Prueba 1")



    def listados(self):
        self.lista_senal_temp.recorrer_e_imprimir_listas()
        
        

    def generar_grafica(self,nombre,nombre_de_grafica):
        self.lista_senal_temp.generar_grafia(nombre,nombre_de_grafica)

    
    def eliminar_lista(self):
        self.lista_senal_temp.eliminar_lista_nodo()
    
    def grafica_sumados(self):
        self.lista_senal_temp.grafica_mi_sumados()


    def crear_xml(self,nombre):
        self.lista_senal_temp.generar_archivo_xml(nombre)

    