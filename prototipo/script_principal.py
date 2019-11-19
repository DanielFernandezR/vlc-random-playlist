from random_playlist_generator import generate_random_list_path_song


def iniciar_vlc():
    lista_aleatoria = generate_random_list_path_song()
    return lista_aleatoria


print(iniciar_vlc())