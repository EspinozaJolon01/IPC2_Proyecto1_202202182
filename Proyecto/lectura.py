import xml.etree.ElementTree as ET
from Datos import Datos
from lista_datos import lista_datos

lista = lista_datos()

class lectura:



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
                    print(f"Amplitud: {doc.get('A')}")
                    print("------------------------")
                    lst_dato = doc.findall("dato")
                    for dato in lst_dato:
                        t = dato.get('t')  
                        A = dato.get('A')  
                        valor = dato.text
                        datos_xml = Datos(nombre,t,A,valor)
                        lista.actualizar_datos(nombre,t,A,valor)
                        lista.agregar_lista_de_xml(datos_xml)
                        #print(f"t: {t}, A: {A}, Valor: {valor}")
                print("proceso terminado")
            else:
                print(False)
        except Exception as rr:
            print("Error por terminal",rr)
        finally:
            pass

    def prueba(self):
        lista.recorrdio()

    def prube_binario(self):
        lista.binario()