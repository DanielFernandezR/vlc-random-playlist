def contar_canciones_xml(raiz):
    num_canciones = 0
    for canciones in raiz:
        for cancion in canciones:
            num_canciones += 1
    assert isinstance(num_canciones, int)
    return num_canciones
