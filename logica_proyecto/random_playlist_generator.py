from random import randrange
from acceso_a_datos.api import get_name_dict


def generate_random_playlist():
    diccionario = get_name_dict()
    assert isinstance(diccionario, dict)
    lista_canciones = []
    nombre_canciones = list(diccionario.keys())
    for cancion in nombre_canciones:
        while cancion not in lista_canciones:
            num_aleatorio = randrange(1, 4)
            if str(num_aleatorio) not in lista_canciones:
                lista_canciones += str(num_aleatorio)
                lista_canciones.append(cancion)
    return lista_canciones
