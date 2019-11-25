from random import randrange
from prueba_logica_proyecto.comprobar_long_dict import contar_canciones_xml


def crear_num_aleatorio():
    longitud_diccionario = contar_canciones_xml()
    num_aleatorio = randrange(1, longitud_diccionario + 1)

    return num_aleatorio
