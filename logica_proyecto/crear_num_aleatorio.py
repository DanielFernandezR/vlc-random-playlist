from random import randrange
from logica_proyecto.comprobar_long_dict import contar_canciones_xml


def crear_num_aleatorio(RUTA_XML):
    longitud_diccionario = contar_canciones_xml(RUTA_XML)
    num_aleatorio = randrange(1, longitud_diccionario + 1)

    return num_aleatorio
