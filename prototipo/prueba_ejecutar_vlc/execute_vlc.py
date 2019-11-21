import subprocess
from prueba_logica_proyecto.random_playlist_generator import generate_random_list_path_song


def ejecuta_vlc():
    ruta_vlc = r"‪E:\VLC\vlc.exe"
    ruta_cancion = " ".join(generate_random_list_path_song())
    ejecutar = subprocess.call('"' + ruta_vlc + '"' + ' ' + ruta_cancion, shell=True)
    return ejecutar
