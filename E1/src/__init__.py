
def subconjuntosLista(lista):
    subconjuntos = []
    n = len(lista)

    #se generan los sunconjuntos posibles
    for x in range(2**n):
        subconjunto = [lista[y] for y in range(n) if (x &(1 << y))]
        subconjuntos.append(subconjunto)
    return subconjuntos