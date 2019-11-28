import os
import subprocess
import shlex


def ejecuta_vlc(lista_canciones, RUTA_VLC):
    try:
        ejecutar = subprocess.Popen("vlc " + lista_canciones)
    except FileNotFoundError:
        print("El programa VLC no esta asociado a la variable PATH")
    finally:
        ejecución = shlex.split(RUTA_VLC + " " + lista_canciones, posix=False)
        ejecutar = subprocess.Popen(ejecución)
    return ejecutar
