import os
import subprocess


def ejecuta_vlc():
    ruta_vlc = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
    ruta_cancion = r"C:\Users\Dual\Desktop\Trabajos\proyectovlc\ScriptProyectoSistemas\Canciones\e_05_Find_You.mp3"
    subprocess.Popen([ruta_vlc, ruta_cancion])


ejecuta_vlc()