from capas_proyecto.presentacion.ejecutar_vlc import ejecuta_vlc
from capas_proyecto.acceso_a_datos.api import crear_dicc_nombre_ruta
from capas_proyecto.logica_proyecto.crear_string_ruta_canciones import crear_string_ruta_canciones

RUTA_XML = "archivos_xml\\library.xml"
RUTA_VLC = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"


def main(RUTA_XML, RUTA_VLC):
    diccionario_canciones, num_canciones = crear_dicc_nombre_ruta(RUTA_XML)
    lista_canciones = crear_string_ruta_canciones(diccionario_canciones, num_canciones)
    ejecuta_vlc(lista_canciones, RUTA_VLC)


if __name__ == "__main__":
    main(RUTA_XML, RUTA_VLC)
