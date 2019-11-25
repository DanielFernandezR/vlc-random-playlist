from prueba_logica_proyecto.random_playlist_generator import generate_random_list_path_song


def fusion_listas():
    lista_numeros_random, lista_ruta_canciones = generate_random_list_path_song()
    listas_unidas = sorted(zip(lista_numeros_random, lista_ruta_canciones))
    lista_numeros_random, lista_ruta_canciones = zip(*listas_unidas)
    # Juntamos las 2 listas en una lista con tuplas, las ordenamos
# por el número que tiene asignada cada canción y
# las separamos otra vez en listas.
    return lista_ruta_canciones
