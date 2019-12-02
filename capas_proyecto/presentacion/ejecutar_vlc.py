import subprocess
import shlex


def ejecuta_vlc(lista_canciones, RUTA_VLC):
    try:
        subprocess.Popen("vlc " + lista_canciones)
    except FileNotFoundError:
        print("El programa VLC no esta asociado a la variable PATH")
    else:
        exit()

    try:
        vlc_ruta_completa = shlex.split(RUTA_VLC + " " + lista_canciones, posix=False)
        subprocess.Popen(vlc_ruta_completa)
    except FileNotFoundError:
        print("El programa VLC no esta en la ruta C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
        exit()
    else:
        exit()
