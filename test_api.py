from acceso_a_datos.api import crear_dicc_nombre_ruta


def test_XML_correcto_y_long_dict_igual_num_canciones_xml():
    assert crear_dicc_nombre_ruta("archivos_xml\\prueba.xml") == ({'e_01_Betty_Boop.mp3': 'canciones\\e_01_Betty_Boop.mp3',
                                                     'e_02_Waiting_For_Love.mp3': 'canciones\\e_02_Waiting_For_Love.mp3',
                                                     'e_03_Animals.mp3': 'canciones\\e_03_Animals.mp3'}, 3)

# Este caso test solo funciona si quitamos la precondición de crear_dicc_nombre_ruta()
# def test_dict_canciones_no_se_repiten():
#    assert crear_dicc_nombre_ruta("archivos_xml\\prueba2.xml") == ({'e_01_Betty_Boop.mp3': 'canciones\\e_01_Betty_Boop.mp3'}, 2)

# Casos test que no hemos sabido elaborar:
# def test_XML_nombre_equivocado():
#    assert crear_dicc_nombre_ruta("fallo.xml") == SystemExit("El nombre del archivo XML no es correcto.")


# def test_XML_mal_formado():
#    assert crear_dicc_nombre_ruta("archivos_xml\\librar.xml") == SystemExit("El archivo XML está mal formado.")
