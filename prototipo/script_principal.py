from random_playlist_generator import generate_random_playlist


def iniciar_vlc():
    lista_aleatoria = generate_random_playlist()
    return lista_aleatoria


print(iniciar_vlc())