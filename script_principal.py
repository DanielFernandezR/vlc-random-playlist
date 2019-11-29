from presentacion.ejecutar_vlc import ejecuta_vlc
from acceso_a_datos.crear_raiz_XML import crear_raiz_XML
from acceso_a_datos.api import crear_dicc_nombre_ruta
from logica_proyecto.crear_lista_ruta_canciones import crear_lista_ruta_canciones

RUTA_XML = "library.xml"
RUTA_VLC = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"


def main(RUTA_XML, RUTA_VLC):
    raiz = crear_raiz_XML(RUTA_XML)
    diccionario_canciones, num_canciones = crear_dicc_nombre_ruta(raiz)
    lista_canciones = crear_lista_ruta_canciones(diccionario_canciones, num_canciones)
    ejecuta_vlc(lista_canciones, RUTA_VLC)


if __name__ == "__main__":
    main(RUTA_XML, RUTA_VLC)
