from src.main import comprimir_cadena

def test_comprimir_cadena():
    cadena = "hhhoollaaaaa"
    assert (comprimir_cadena(cadena)) == "h3o2l2a5" #comparar cadena comprimida esperada
    #para provocar error de intruduce una cadena comprimida esperada incorrecta