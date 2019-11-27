from acceso_a_datos.api import get_name_and_path_dict
from logica_proyecto.crear_num_aleatorio import crear_num_aleatorio


def crear_lista_path_canciones(RUTA_XML):
    diccionario = get_name_and_path_dict(RUTA_XML)
    assert isinstance(diccionario, dict)

    lista_numeros_random = []
    lista_ruta_canciones = []
    nombre_ruta_canciones = list(diccionario.values())

    for cancion in nombre_ruta_canciones:
        while cancion not in lista_ruta_canciones:
            num_aleatorio = crear_num_aleatorio(RUTA_XML)
            if num_aleatorio not in lista_numeros_random:
                lista_numeros_random.append(num_aleatorio)
                lista_ruta_canciones.append(cancion)

    return lista_numeros_random, lista_ruta_canciones
