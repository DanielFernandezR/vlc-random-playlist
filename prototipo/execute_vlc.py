import subprocess
from random_playlist_generator import generate_random_list_path_song

def ejecuta_vlc():

    ruta_vlc = r"E:\VLC\vlc.exe"
    ruta_cancion = r" ".join(generate_random_list_path_song())
    subprocess.Popen([ruta_vlc, ruta_cancion])


ejecuta_vlc()
