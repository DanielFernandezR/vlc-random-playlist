from acceso_a_datos.api import crear_dicc_nombre_ruta
import xml.etree.ElementTree as ET


def test_XML_correcto():
    assert crear_dicc_nombre_ruta("prueba.xml") == ({'e_01_Betty_Boop.mp3': 'canciones\\e_01_Betty_Boop.mp3', 'e_02_Waiting_For_Love.mp3': 'canciones\\e_02_Waiting_For_Love.mp3', 'e_03_Animals.mp3': 'canciones\\e_03_Animals.mp3'}, 3)


# def test_XML_nombre_equivocado():
#    assert crear_dicc_nombre_ruta("librar.xml") == exit()


#def test_dict_canciones_no_se_repiten():
#    assert crear_dicc_nombre_ruta("prueba2.xml") == ({'e_01_Betty_Boop.mp3': 'canciones\\e_01_Betty_Boop.mp3'}, 2)
