###
import random
import time
import Algoritmos
import Auxiliar as aux


def gerarLista(n):
    # int list
    lista = [0 for x in range(n)]

    for i in range(n):
        lista[i] = random.randint(0, 50000)
    return lista


# main
if __name__ == "__main__":

    # Parâmetros
    global repeat, n_min, n_max

    n_min = 10
    n_max = 12

    repeat = 20

    # Inicialização
    n = n_min

    # Loop principal
    while n <= n_max:
        print("n = ", n)

        # Gerar lista de items com valores e pesos aleatórios e ordenar por valor
        listaDesordenada = gerarLista(n)

        # Exportar lista inicial para um txt
        aux.exportarLista(listaDesordenada, './execlog/desordenadas/', 'n_' + str(n) + '.txt')

        ## Ordenar lista com cada algoritmo

        ## Quick Sort
        start_time = time.time()
        listaOrdenada = Algoritmos.quickSort(listaDesordenada)
        elapsed_time = time.time() - start_time

        # Save execution time to a csv file
        aux.exportarTempo('quickSort', n, elapsed_time)

        # Exportar lista ordenada para um txt
        # aux.exportarLista(listaOrdenada, './execlog/ordenadas/quickSort/', 'n_' + str(n) + '.txt')
        listaOrdenada.clear()

        ## Merge Sort
        start_time = time.time()
        listaOrdenada = Algoritmos.mergeSort(listaDesordenada)
        elapsed_time = time.time() - start_time

        # Save execution time to a csv file
        aux.exportarTempo('quickSort', n, elapsed_time)

        # Exportar lista ordenada para um txt
        # aux.exportarLista(listaOrdenada, './execlog/ordenadas/mergeSort/', 'n_' + str(n) + '.txt')
        listaOrdenada.clear()

        ## Heap Sort
        start_time = time.time()
        listaOrdenada = Algoritmos.heapSort(listaDesordenada)
        elapsed_time = time.time() - start_time

        # Save execution time to a csv file
        aux.exportarTempo('quickSort', n, elapsed_time)

        # Exportar lista ordenada para um txt
        # aux.exportarLista(listaOrdenada, './execlog/ordenadas/heapSort/', 'n_' + str(n) + '.txt')
        listaOrdenada.clear()

        ## Counting Sort
        start_time = time.time()
        listaOrdenada = Algoritmos.countingSort(listaDesordenada)
        elapsed_time = time.time() - start_time

        # Save execution time to a csv file
        aux.exportarTempo('quickSort', n, elapsed_time)

        # Exportar lista ordenada para um txt
        aux.exportarLista(listaOrdenada, './execlog/ordenadas/countingSort/', 'n_' + str(n) + '.txt')
        listaOrdenada.clear()

        # ## Radix Sort
        # start_time = time.time()
        # listaOrdenada = Algoritmos.radixSort(listaDesordenada)
        # elapsed_time = time.time() - start_time

        # # Save execution time to a csv file
        # aux.exportarTempo('quickSort', n, elapsed_time)

        # # Exportar lista ordenada para um txt
        # aux.exportarLista(listaOrdenada, './execlog/ordenadas/radixSort/', 'n_' + str(n) + '.txt')
        # listaOrdenada.clear()

        # ## Bucket Sort
        # start_time = time.time()
        # listaOrdenada = Algoritmos.bucketSort(listaDesordenada)
        # elapsed_time = time.time() - start_time

        # # Save execution time to a csv file
        # aux.exportarTempo('quickSort', n, elapsed_time)

        # # Exportar lista ordenada para um txt
        # aux.exportarLista(listaOrdenada, './execlog/ordenadas/bucketSort/', 'n_' + str(n) + '.txt')
        # listaOrdenada.clear()

        n = n + 1