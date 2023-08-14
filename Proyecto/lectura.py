import xml.etree.ElementTree as ET
from Datos import Datos
from lista_datos import lista_datos

lista = lista_datos()

class lectura:

    def __init__(self) :
        self.tiempo = ""
        self.amplitud = ""

    def lectura_xml(self,ruta):
        try:
            xml_file = open(f"{ruta}.xml")
            if xml_file.readable():
                xml_data = ET.fromstring(xml_file.read())
                lst_doc = xml_data.findall("senal")
                
                for doc in lst_doc:
                    #lista.verificar_nombre(doc.get('nombre'))
                    print(f"Nombre: {doc.get('nombre')}")
                    nombre = doc.get('nombre')
                    print(f"Tiempo: {doc.get('t')}")
                    self.tiempo = doc.get('t')
                    tiempos = int(self.tiempo)
                    print(f"Amplitud: {doc.get('A')}")
                    self.amplitud =doc.get('A')
                    amplitudes = int(self.amplitud)
                    print("------------------------")

                    if int(self.tiempo) > 0 and int(self.tiempo) <=130:
                        if int(self.amplitud) > 0 and int(self.amplitud) <=130:
                            lst_dato = doc.findall("dato")

                            for dato in lst_dato:
                                t = dato.get('t')  
                                A = dato.get('A')  
                                valor = dato.text

                                self.validar_salto_de_linea(t,A)

                                if valor is None or valor.strip() == "":
                                    valor_nulo = 0
                                    agregar = str(valor_nulo)
                                else:
                                    valor_nulo = int(valor)
                                    agregar = str(valor_nulo)

                                valor_binario = 1 if valor_nulo != 0 else 0
                                agrega_nodo = str(valor_binario)

                                datos_xml = Datos(t,A,agregar,agrega_nodo)
                                lista.agregar_lista_de_xml(datos_xml)
                        #print(f"t: {t}, A: {A}, Valor: {valor}")
                            print("proceso terminado")
                        
                        else: 
                            print("amplitud se pasa de su limite de 0 a 130")
                    else:
                        print("tiempo se pasa de su limite de 0 a 130")

                
            else:
                print(False)
        except Exception as rr:
            print("Error por terminal",rr)
        finally:
            pass

    def validar_salto_de_linea(self, t, A):
        tiempos = int(self.tiempo)
        amplitudes = int(self.amplitud)
        encontrado = False  # Usamos esto para saber si se encontró el dato

        for i in range(1, tiempos + 1):
            for j in range(1, amplitudes + 1):
                if int(t) == i and int(A) == j:
                    encontrado = True  # Se encontró el dato, cambiamos el valor
                    break  # Salir del bucle interno
            if encontrado:  # Si se encontró el dato, salir del bucle externo también
                break

        # Verificar si se encontró el dato o no
        if encontrado:
            print("Todo bien")
        else:
            print(f"Falta un dato en t: {t}, A: {A}")


                


    def prueba(self):
        lista.recorrdio_binario()

    def matriz(self):
        lista.recorrdio()