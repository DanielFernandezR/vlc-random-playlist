from presentacion.execute_vlc import ejecuta_vlc
from acceso_a_datos.check_XML import check_XML
from acceso_a_datos.api import get_name_and_path_dict
from logica_proyecto.crear_lista_path_canciones import crear_lista_path_canciones

RUTA_XML = "library.xml"
RUTA_VLC = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"


def main(RUTA_XML, RUTA_VLC):
    raiz = check_XML(RUTA_XML)
    diccionario_canciones, num_canciones = get_name_and_path_dict(raiz)
    lista_canciones = crear_lista_path_canciones(diccionario_canciones, num_canciones)
    ejecuta_vlc(lista_canciones, RUTA_VLC)


if __name__ == "__main__":
    main(RUTA_XML, RUTA_VLC)
