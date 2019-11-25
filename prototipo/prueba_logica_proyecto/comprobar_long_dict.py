from prueba_acceso_a_datos.check_XML import check_XML


def contar_canciones_diccionario():
    raiz = check_XML()
    num_canciones = 0
    for canciones in raiz:
        for cancion in canciones:
            num_canciones += 1
    assert isinstance(num_canciones, int)
    return num_canciones
