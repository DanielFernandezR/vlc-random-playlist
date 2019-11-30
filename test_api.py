from acceso_a_datos.api import crear_dicc_nombre_ruta
import xml.etree.ElementTree as ET


def test_XML_correcto():
    assert crear_dicc_nombre_ruta("library.xml") == (dict, int)


def test_XML_nombre_equivocado():
    assert crear_raiz_XML("librar.xml") == True