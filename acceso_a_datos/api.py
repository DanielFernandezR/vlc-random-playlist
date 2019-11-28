from logica_proyecto.comprobar_long_dict import contar_canciones_xml


def get_name_and_path_dict(raiz):
    diccionario = {}
    for canciones in raiz:
        for cancion in canciones:
            nombre_ruta = {}
            nombre_ruta[cancion.find('name').text] = cancion.find("path").text
            diccionario.update(nombre_ruta)
    num_canciones = contar_canciones_xml(raiz)
    assert len(diccionario) == num_canciones
    return diccionario, num_canciones
