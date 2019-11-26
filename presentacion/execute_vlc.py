import os
import subprocess
from logica_proyecto.juntar_dos_listas import fusion_listas


def ejecuta_vlc():
    ruta_vlc = "‪‪C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
    ruta_cancion = " ".join(fusion_listas())

    #añadir_path = subprocess.Popen("set PATH=" + os.environ["PATH"] + ";C:\Program Files (x86)\VideoLAN\VLC\;")
    ejecutar = subprocess.Popen(r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe " + ruta_cancion)
    return ejecutar
