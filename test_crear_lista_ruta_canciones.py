from logica_proyecto.crear_lista_ruta_canciones import crear_lista_ruta_canciones


def test_diccionario_y_num_canciones():
    assert crear_lista_ruta_canciones(
        {"e_One_X": "canciones\\e_One_X", "m_Fire_Storm": "canciones\\m_Fire_Storm"}, 2) == "canciones\\e_One_X canciones\\m_FireStorm" or "canciones\\e_One_X canciones\\m_FireStorm"


def test_canciones_no_se_repiten():
    assert crear_lista_ruta_canciones(
        {"e_One_X": "canciones\\e_One_X", "m_Fire_Storm": "canciones\\e_One_X"}, 2) == "canciones\\e_One_X"
