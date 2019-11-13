import xml.etree.ElementTree as ET

def check_XML(archivoXML):
    try:
        arbol = ET.parse('library.xml')
    except FileNotFoundError:
        print("El nombre del archivo XML no es correcto.")
    except XML.etree.ElementTree.ParseError:
        print("El archivo XML está mal formado.")
    else:
        raiz = arbol.getroot()
        return raiz


if __name__ == "__main__":

    assert check_XML('library.xml') == True   

    
