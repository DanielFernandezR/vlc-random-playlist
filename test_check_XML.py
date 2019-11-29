from acceso_a_datos.check_XML import check_XML

def test_XML_nombre_equivocado():
    assert check_XML("lebrary.xml") == FileNotFoundError

def test_XML_bueno()
    assert check_XML("library.xml") == 