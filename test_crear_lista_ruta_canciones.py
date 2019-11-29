from logica_proyecto.crear_lista_ruta_canciones import crear_lista_ruta_canciones


def test_generar_string_ruta_canciones():
    assert crear_lista_ruta_canciones(
        {"e_One_X": "canciones\\e_One_X.mp3",
         "m_Fire_Storm": "canciones\\m_Fire_Storm.mp3",
         "rt_Con_Calma": "canciones\\rt_Con_Calma.mp3"}, 3) == "canciones\\e_One_X.mp3 canciones\\rt_Con_Calma.mp3 canciones\\m_Fire_Storm.mp3" or "canciones\\e_One_X.mp3 canciones\\m_Fire_Storm.mp3 canciones\\rt_Con_Calma.mp3" or "canciones\\m_Fire_Storm.mp3 canciones\\rt_Con_Calma.mp3 canciones\\e_One_X.mp3" or "canciones\\m_Fire_Storm.mp3 canciones\\e_One_X.mp3 canciones\\rt_Con_Calma.mp3" or "canciones\\rt_Con_Calma.mp3 canciones\\m_Fire_Storm.mp3 canciones\\e_One_X.mp3" or "canciones\\rt_Con_Calma.mp3 canciones\\e_One_X.mp3 canciones\\m_Fire_Storm.mp3"


def test_canciones_no_se_repitan():
    assert crear_lista_ruta_canciones({"e_One_X": "canciones\\e_One_X.mp3",
                                       "m_Fire_Storm": "canciones\\e_One_X.mp3",
                                       "rt_rumba": "canciones\\rt_rumba.mp3",
                                       "m_awaken": "canciones\\e_find_you.mp3",
                                       "e_find_you": "canciones\\e_find_you.mp3"}, 5) == "canciones\\e_One_X canciones\\e_find_you.mp3 canciones\\rt_rumba.mp3" or "canciones\\e_One_X canciones\\rt_rumba.mp3 canciones\\e_find_you.mp3 " or "canciones\\e_find_you.mp3 canciones\\e_One_X canciones\\rt_rumba.mp3" or "canciones\\e_find_you.mp3 canciones\\rt_rumba.mp3 canciones\\e_One_X" or "canciones\\rt_rumba.mp3 canciones\\e_find_you.mp3 canciones\\e_One_X" or "canciones\\rt_rumba.mp3 canciones\\e_One_X canciones\\e_find_you.mp3"
