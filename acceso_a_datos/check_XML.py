import xml.etree.ElementTree as ET


def check_XML(RUTA_XML):
    try:
        arbol = ET.parse(RUTA_XML)
    except FileNotFoundError:
        print("El nombre del archivo XML no es correcto.")
        exit()
    except NameError:
        print("El archivo XML está mal formado.")
        exit()
    else:
        raiz = arbol.getroot()
        return raiz
