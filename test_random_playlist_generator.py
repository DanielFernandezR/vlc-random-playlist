from acceso_a_datos.api import *
from logica_proyecto.comprobar_long_dict import *
from presentacion.execute_vlc import *


def test_longitud_dict_igual_num_canciones_xml():
    assert len(get_name_and_path_dict()) == contar_canciones_xml()
