import subprocess
from prueba_logica_proyecto.juntar_dos_listas import fusion_listas


def ejecuta_vlc():
    ruta_vlc = r"‪E:\VLC\vlc.exe"
    ruta_cancion = " ".join(fusion_listas())
    ejecutar = subprocess.call('"' + ruta_vlc + '"' + ' ' + ruta_cancion, shell=True)
    return ejecutar
