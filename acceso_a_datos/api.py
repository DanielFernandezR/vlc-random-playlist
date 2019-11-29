from acceso_a_datos.comprobar_long_dict import contar_canciones_xml


def crear_dicc_nombre_ruta(raiz):
    diccionario = {}
    for canciones in raiz:
        for cancion in canciones:
            nombre_ruta = {}
            nombre_ruta[cancion.find('name').text] = cancion.find("path").text
            diccionario.update(nombre_ruta)
    num_canciones = contar_canciones_xml(raiz)
    assert len(diccionario) == num_canciones
    return diccionario, num_canciones
