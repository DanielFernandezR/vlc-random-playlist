from prueba_acceso_a_datos.check_XML import check_XML
from prueba_logica_proyecto.comprobar_long_dict import contar_canciones_diccionario


def get_name_and_path_dict():
    diccionario = {}
    raiz = check_XML()
    for canciones in raiz:
        for cancion in canciones:
            nombre_ruta = {}
            nombre_ruta[cancion.find('name').text] = cancion.find("path").text
            diccionario.update(nombre_ruta)
    assert len(diccionario) == contar_canciones_diccionario()
    return diccionario
