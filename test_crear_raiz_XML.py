from acceso_a_datos.crear_raiz_XML import crear_raiz_XML
import xml.etree.ElementTree as ET


def test_XML_correcto():
    raiz = crear_raiz_XML("library.xml")
    assert isinstance(raiz, ET.Element)


def test_XML_nombre_equivocado():
    assert crear_raiz_XML("librar.xml") == exit()
    continue