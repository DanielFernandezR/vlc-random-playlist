from check_XML import check_XML


def get_name_and_path_dict():
    diccionario = {}
    raiz = check_XML()
    for canciones in raiz:
        for cancion in canciones:
            nombre_ruta = {}
            nombre_ruta[cancion.find('name').text] = cancion.find("path").text
            diccionario.update(nombre_ruta)
    assert len(diccionario) == 20
    return diccionario
