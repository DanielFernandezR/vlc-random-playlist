from random import randrange


def generate_random_playlist(diccionario):
    assert isinstance(diccionario, dict)
    lista_canciones = []
    if len(lista_canciones) != len(diccionario):
        nombre_canciones = list(diccionario.keys())
        num_aleatorio = randrange(1, 3)
        lista_canciones += str(num_aleatorio)
        lista_canciones += str(nombre_canciones(0,-1))
    return lista_canciones


if __name__ == "__main__":

    assert generate_random_playlist({"California_Uber_Alles.mp3":
                                     {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys",
                                         "location": "./biblioteca/California_Uber_Alles.mp3"},
                                     "Seattle_Party":
                                     {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets",
                                      "location": "./biblioteca/Seattle_Party.flac"},
                                     "King_Kunta":
                                     {"track-number": 3, "artist": "Kendrick Lamar",
                                      "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}
                                     }) == True
