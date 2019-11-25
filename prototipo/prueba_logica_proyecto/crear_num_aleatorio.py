from random import randrange
from prueba_acceso_a_datos.api import get_name_and_path_dict


def num_aleatorio():
    num_aleatorio = randrange(1, len(get_name_and_path_dict()) + 1)
    return num_aleatorio
