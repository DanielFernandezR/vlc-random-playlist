from checkXML import check_XML

def get_name_dict(archivoxml):
    assert isinstance(dict, dict)
    tree = ET.parse('library.xml')
    root = tree.getroot()
    diccionario = {}
    for canciones in root:
        for cancion in canciones:
            nombre_ruta = {}
            nombre_ruta[cancion.find('name').text] = cancion.find("path").text
            diccionario.update(nombre_ruta)
    return diccionario
