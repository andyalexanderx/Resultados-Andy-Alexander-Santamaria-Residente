import time
import psutil
import os
from src.main import subconjuntosLista

def test_subconjuntosLista():
    tiempo_inicio = time.time()
    tiempo_final = time.time()
    # Comprobamos la cantidad de los conjuntos obtenidos, en este caso "8" (2**n, donde n es la longitud de la lista(3))
    # RESULTATO: "8"--> 7 combinaciones posibles + 1 de conjunto vacio son 8combinaciones
    assert len(subconjuntosLista(['y','x','z'])) == 8
    #para provocar un error se fuerza a esperar un numero de subconjuntos incorrectos