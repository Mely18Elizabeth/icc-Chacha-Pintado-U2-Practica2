from benchmarking import Benchmarking
from metodosOrdenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt

if __name__ == "__main__":

    metodos = MetodosOrdenamiento()
    benchmarking = Benchmarking()

    tamanios = [5000, 10000, 30000, 50000, 100000]
    arreglo_general = benchmarking.build_arreglo(100000)

    resultados = []

    metodosD = {
        "bubbleMejorado": metodos.sortByBubbleMejorado,
        "seleccion": metodos.sortBySeleccion,
        "insercion": metodos.sortByInsercion,
        "shell": metodos.sortByShell
    }

    for tam in tamanios:
        arreglo_base = arreglo_general[:tam]

        for nombre, metodo in metodosD.items():
            tiempo = benchmarking.medir_tiempo(metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo))
            print(f"Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} seg")

    tiempos_por_metodo = {nombre: [] for nombre in metodosD}

    for tam, nombre, tiempo in resultados:
        tiempos_por_metodo[nombre].append((tam, tiempo))

    plt.figure(figsize=(12, 7))
    for nombre, datos in tiempos_por_metodo.items():
        tamX = [t for t, _ in datos]
        timpY = [tiempo for _, tiempo in datos]
        plt.plot(tamX, timpY, label=nombre, marker='o')

    plt.title(f"Comparación de métodos de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()
    plt.show()
