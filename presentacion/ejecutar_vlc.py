import subprocess
import shlex


def ejecuta_vlc(lista_canciones, RUTA_VLC):
    try:
        vlc_en_path = subprocess.Popen("vlc " + lista_canciones)
    except FileNotFoundError:
        print("El programa VLC no esta asociado a la variable PATH")
        vlc_ruta_completa = shlex.split(RUTA_VLC + " " + lista_canciones, posix=False)
        vlc_en_path = subprocess.Popen(vlc_ruta_completa)
