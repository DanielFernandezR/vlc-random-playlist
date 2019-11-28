from random import randrange
from logica_proyecto.comprobar_long_dict import contar_canciones_xml


def crear_num_aleatorio(num_canciones):
    num_aleatorio = randrange(1, num_canciones + 1)
    return num_aleatorio
