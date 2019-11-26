from prueba_acceso_a_datos.api import *
from prueba_logica_proyecto.comprobar_long_dict import *
from prueba_ejecutar_vlc.execute_vlc import *


def test_longitud_dict_igual_num_canciones_xml():
    assert len(get_name_and_path_dict()) == contar_canciones_xml()


def test_todas_las_canciones_dict_en_lista():
    assert 


def test_canciones_no_se_repitan_en_dict():
    assert 
