from prueba_acceso_a_datos.api import get_name_and_path_dict
from prueba_logica_proyecto.crear_num_aleatorio import num_aleatorio

def generate_random_list_path_song():
    diccionario = get_name_and_path_dict()
    assert isinstance(diccionario, dict)
    lista_numeros_random = []
    lista_ruta_canciones = []
    nombre_ruta_canciones = list(diccionario.values())
    for cancion in nombre_ruta_canciones:

        while cancion not in lista_ruta_canciones:
            num_aleatorio = num_aleatorio()

            if num_aleatorio not in lista_numeros_random:
                lista_numeros_random.append(num_aleatorio)
                lista_ruta_canciones.append(cancion)

    listas_unidas = sorted(zip(lista_numeros_random, lista_ruta_canciones))
    lista_numeros_random, lista_ruta_canciones = zip(*listas_unidas)
# Juntamos las 2 listas en una lista con tuplas, las ordenamos
# por el número que tiene asignada cada canción y
# las separamos otra vez en listas.
    return lista_ruta_canciones
