import os
import subprocess
from logica_proyecto.juntar_dos_listas import fusion_listas


def ejecuta_vlc(RUTA_XML):
    ruta_cancion = " ".join(fusion_listas(RUTA_XML))
    try:
        ejecutar = subprocess.Popen("vlc" + ruta_cancion)
    except FileNotFoundError:
        print("El programa VLC no esta asociado a la variable PATH")
    finally:
        ejecutar = subprocess.Popen(r"E:\VLC\vlc.exe" + " " + ruta_cancion)
# añadir_path = subprocess.Popen("set PATH=" + os.environ["PATH"] + ";C:\Program Files (x86)\VideoLAN\VLC\;")
    return ejecutar
