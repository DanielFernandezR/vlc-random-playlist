import xml.etree.ElementTree as ET


def check_XML(RUTA_XML):
    try:
        arbol = ET.parse("library.xml")
    except FileNotFoundError:
        print("El nombre del archivo XML no es correcto.")
        raise
    except XML.etree.ElementTree.ParseError:
        print("El archivo XML está mal formado.")
        raise
    else:
        raiz = arbol.getroot()
        return raiz
