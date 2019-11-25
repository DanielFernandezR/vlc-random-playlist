from prueba_acceso_a_datos.api import get_name_and_path_dict
from prueba_logica_proyecto.crear_num_aleatorio import crear_num_aleatorio


def generate_random_list_path_song():
    diccionario = get_name_and_path_dict()
    assert isinstance(diccionario, dict)
    lista_numeros_random = []
    lista_ruta_canciones = []
    nombre_ruta_canciones = list(diccionario.values())
    for cancion in nombre_ruta_canciones:
        while cancion not in lista_ruta_canciones:
            num_aleatorio = crear_num_aleatorio()
            if num_aleatorio not in lista_numeros_random:
                lista_numeros_random.append(num_aleatorio)
                lista_ruta_canciones.append(cancion)
    return lista_numeros_random, lista_ruta_canciones
