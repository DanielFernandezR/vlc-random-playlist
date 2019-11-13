from check_XML import check_XML

def get_name_dict(archivo_XML):
    raiz = check_XML(archivo_XML)
    diccionario = {}
    for canciones in raiz:
        for cancion in canciones:
            nombre_ruta = {}
            nombre_ruta[cancion.find('name').text] = cancion.find("path").text
            diccionario.update(nombre_ruta)
    assert len(diccionario) == 20
    return diccionario
    


if __name__ == "__main__":

    assert get_name_dict("library.xml") == dict