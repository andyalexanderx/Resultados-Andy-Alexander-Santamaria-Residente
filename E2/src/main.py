def encontrar_palabra(matriz, palabra):
    if not matriz or not matriz[0]: return False #comprueba si la matriz esta vacia
    if not palabra: return True #comprueba si la palabra (cadena) esta vacia, aunque si puede contener solo espacios (true)

    #se recorre cada celda de la matriz si encuentra la primera letra de la palabra llama a la funcion dfs
    # para seguir con la busqueda de las letras que conforman la palabra
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if dfs(matriz, palabra, i, j, 0): #si retorna TRUE indica que la palabra si esta contenida en la matriz
                return True
    return False

def dfs(matriz, palabra, i, j, k): #realizar busqueda en profundidad
    #visita la celda actual con cada llamada de la funcion para la letra siguiente de la palabra
    if i < 0 or j < 0 or i >= len(matriz) or j >= len(matriz[0]) or matriz[i][j] != palabra[k]:
        return False
    if k == len(palabra) - 1:
        return True

    tmp, matriz[i][j] = matriz[i][j], 'x' #evitar volver a visitar la misma celda, marcandola con una "x" (remplaza con su valor con "x")
    # las 8 posibles direcciones para moverse en las celdas vecinas
    #                            (arriba, 
    #                             abajo, 
    #                             izquierda, 
    #                             derecha,
    #                             esquina superior izquierda,
    #                             esquina superior derecha,
    #                             esquina inferior izquierda,
    #                             esquina inferior derecha)
    res = dfs(matriz, palabra, i+1, j, k+1) or\
        dfs(matriz, palabra, i-1, j, k+1) or\
        dfs(matriz, palabra, i, j+1, k+1) or\
        dfs(matriz, palabra, i, j-1, k+1) or\
        dfs(matriz, palabra, i+1, j+1, k+1) or\
        dfs(matriz, palabra, i-1, j-1, k+1) or\
        dfs(matriz, palabra, i-1, j+1, k+1) or\
        dfs(matriz, palabra, i+1, j-1, k+1)
    matriz[i][j] = tmp #se restablece el valor de la celda
    return res

# matriz = [
#     ['H', 'O', 'L', 'A'],
#     ['S', 'L', 'C', 'N'],
#     ['Q', 'E', 'L', 'D'],
#     ['S', 'D', 'E', 'Y']
# ]
# palabra = "HLLY"
# print(encontrar_palabra(matriz, palabra))