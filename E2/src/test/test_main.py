from src.main import encontrar_palabra

def test_encontrar_palabra():
    matriz = [
    ['H', 'O', 'L', 'A'],
    ['S', 'L', 'C', 'N'],
    ['Q', 'E', 'L', 'D'],
    ['S', 'D', 'E', 'Y']
]
    palabra = "ANDY"
    assert (encontrar_palabra(matriz,palabra)) == True #comprobar si la palabra deseada se puede encuentrar en la matriz
    #para provocar un caso de error se introduce una palabra que no podria contenerse en la matriz dada