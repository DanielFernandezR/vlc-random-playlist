import xml.etree.ElementTree as ET
from acceso_a_datos.comprobar_long_dict import contar_canciones_xml


def crear_dicc_nombre_ruta(RUTA_XML):
    try:
        arbol = ET.parse(RUTA_XML)
    except FileNotFoundError:
        exit("El nombre del archivo XML no es correcto.")
    except ET.ParseError:
        exit("El archivo XML está mal formado.")
    else:
        raiz = arbol.getroot()
        diccionario = {}
        for canciones in raiz:
            for cancion in canciones:
                nombre_y_ruta = {}
                nombre_y_ruta[cancion.find('name').text] = cancion.find("path").text
                diccionario.update(nombre_y_ruta)
        num_canciones = contar_canciones_xml(raiz)
        assert len(diccionario) == num_canciones
        return diccionario, num_canciones
