import random
import time
from metodosOrdenamiento import MetodosOrdenamiento

class Benchmarking:

    def __init__(self):
        self.mOrdenamiento = MetodosOrdenamiento()

    def build_arreglo(self, size):
        return [random.randint(0, 50000) for _ in range(size)]

    def medir_tiempo(self, metodo, array):
        copia = array.copy()
        inicio = time.perf_counter()
        metodo(copia)
        fin = time.perf_counter()
        return fin - inicio
