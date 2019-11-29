from logica_proyecto.crear_lista_path_canciones import crear_lista_path_canciones


def test_diccionario_y_num_canciones():
    assert crear_lista_path_canciones(
        {"e_One_X": "canciones\\e_One_X", "m_Fire_Storm": "canciones\\m_Fire_Storm"}, 2) == "canciones\\e_One_X canciones\\m_FireStorm" or "canciones\\e_One_X canciones\\m_FireStorm"


def test_num_canciones_error():
    assert crear_lista_path_canciones(
        {"cancion1": "canciones1.mp3", "cancion2": "canciones2.mp3"}, 4) == "canciones1.mp3 canciones2.mp3"


def test_canciones_sin_nombre_error():
    assert crear_lista_path_canciones(
        {" ": "cancion1.mp3", " ": "cancion3.mp3"}, 2) == "cancion3.mp3"
