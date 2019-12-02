from capas_proyecto.logica_proyecto.crear_num_aleatorio import crear_num_aleatorio


def crear_string_ruta_canciones(diccionario_canciones, num_canciones):
    assert isinstance(diccionario_canciones, dict)
    lista_num_random = []
    lista_ruta_canciones = []
    nombre_ruta_canciones = list(diccionario_canciones.values())
    for ruta in nombre_ruta_canciones:
        while ruta not in lista_ruta_canciones:
            num_aleatorio = crear_num_aleatorio(num_canciones)
            if num_aleatorio not in lista_num_random:
                lista_num_random.append(num_aleatorio)
                lista_ruta_canciones.append(ruta)
    fusion_listas = sorted(zip(lista_num_random, lista_ruta_canciones))
    lista_num_random, lista_ruta_canciones = (zip(*fusion_listas))
    return " ".join(lista_ruta_canciones)
