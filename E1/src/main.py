import psutil
import time
import os


def subconjuntosLista(lista):
    subconjuntos = []
    n = len(lista)

    #se generan los sunconjuntos posibles
    for x in range(2**n):
        subconjunto = [lista[y] for y in range(n) if (x &(1 << y))] # se recorre cada elemento de la lista y añade al subconjunto
        # si el bit es 1 en la representacion binaria, en el mismo recorrido
        subconjuntos.append(subconjunto) #agrega el subconjunto a la lista subconjuntos
    return subconjuntos

print((subconjuntosLista(['y','x','z'])))




def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

def test_subconjuntosLista():
    tiempo_inicio = time.time()

    # Ejecuta la función y guarda el resultado
    assert type(subconjuntosLista(['y','x','z'])) == list

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicio

    print("Tiempo de ejecución: ", tiempo_ejecucion, "s")
    print("Memoria usada: ", memory_usage_psutil(),"mb")


memory_usage_psutil()
test_subconjuntosLista()