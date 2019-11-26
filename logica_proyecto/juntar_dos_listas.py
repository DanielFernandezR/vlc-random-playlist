from logica_proyecto.crear_lista_path_canciones import crear_lista_path_canciones


def fusion_listas():
    lista_numeros_random, lista_ruta_canciones = crear_lista_path_canciones()

    listas_unidas = sorted(zip(lista_numeros_random, lista_ruta_canciones))
    lista_numeros_random, lista_ruta_canciones = zip(*listas_unidas)
# Juntamos las 2 listas en una lista con tuplas, las ordenamos
# por el número que tiene asignada cada canción y
# las separamos otra vez en listas.
    return lista_ruta_canciones
