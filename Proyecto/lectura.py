import xml.etree.ElementTree as ET
from Datos import Datos
from lista_datos import lista_datos

lista = lista_datos()

class lectura:


    def lectura_xml(self, ruta):
        try:
            xml_file = open(f"{ruta}.xml")
            if xml_file.readable():
                xml_data = ET.fromstring(xml_file.read())
                lst_doc = xml_data.findall("senal")
                
                for doc in lst_doc:
                    print(f"Nombre: {doc.get('nombre')}")
                    nombre = doc.get('nombre')
                    tiempo = int(doc.get('t'))
                    amplitud = int(doc.get('A'))

                    print("------------------------")

                    if 0 < tiempo <= 3600 and 0 < amplitud <= 130:
                        for t in range(1, tiempo + 1):
                            for A in range(1, amplitud + 1):
                                valor_encontrado = False
                                for dato in doc.findall("dato"):
                                    dato_t = int(dato.get('t'))
                                    dato_A = int(dato.get('A'))

                                    if dato_t == t and dato_A == A:
                                        valor = dato.text
                                        valor_nulo = 0 if valor is None or valor.strip() == "" else int(valor)
                                        valor_binario = 1 if valor_nulo != 0 else 0
                                        valor_encontrado = True
                                        break

                                if valor_encontrado:
                                    print(f"Coordenada t={t}, A={A}, Valor={valor_nulo}")
                                    dato_encontrado = Datos(t,A,valor_nulo,valor_binario)
                                else:
                                    print(f"Falta valor en coordenada t={t}, A={A}")
                                    dato_encontrado = Datos(t,A,"0","0")
                                
                                nodo_final = dato_encontrado
                                lista.agregar_lista_de_xml(nodo_final)

                        print("Proceso terminado")
                        
                    else:
                        print("El tiempo o la amplitud están fuera de los límites.")
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

    def listado_binario(self):
        lista.recorrdio_binario()

    def lista_matriz(self):
        lista.recorrdio()