from random_playlist_generator import generate_random_list_name_song


def test_longitud_lista_igual_num_canciones_dict():
    assert generate_random_list_name_song()

def test_todas_las_canciones_dict_en_lista():
    assert generate_random_list_name_song()

def test_canciones_no_se_repitan():
    assert generate_random_list_name_song()
