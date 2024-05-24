###
import time
import Algoritmos
import Auxiliar as aux


# main
if __name__ == "__main__":
    # Opcionais
    runQuickSort = False
    runMergeSort = False
    runHeapSort = False
    runCountingSort = False
    runRadixSort = False
    runBucketSort = True

    exportarListaOrdenada = 10000

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
        listaDesordenada = aux.gerarLista(n)

        # Exportar lista inicial para um txt
        aux.exportarLista(listaDesordenada, './execlog/desordenadas/', 'n_' + str(n) + '.txt')

        ## Ordenar lista com cada algoritmo

        ## Quick Sort
        if (runQuickSort == True):
            start_time = time.time()
            listaOrdenada = Algoritmos.quickSort(listaDesordenada)
            elapsed_time = time.time() - start_time

            # Save execution time to a csv file
            aux.exportarTempo('quickSort', n, elapsed_time)

            # Exportar lista ordenada para um txt
            if (n % exportarListaOrdenada == 0):
                aux.exportarLista(listaOrdenada, './execlog/ordenadas/quickSort/', 'n_' + str(n) + '.txt')

            listaOrdenada.clear()

        ## Merge Sort
        if (runMergeSort == True):
            start_time = time.time()
            listaOrdenada = Algoritmos.mergeSort(listaDesordenada)
            elapsed_time = time.time() - start_time

            # Save execution time to a csv file
            aux.exportarTempo('mergeSort', n, elapsed_time)

            # Exportar lista ordenada para um txt
            if (n % exportarListaOrdenada == 0):
                aux.exportarLista(listaOrdenada, './execlog/ordenadas/mergeSort/', 'n_' + str(n) + '.txt')

            listaOrdenada.clear()

        ## Heap Sort
        if (runHeapSort == True):
            start_time = time.time()
            listaOrdenada = Algoritmos.heapSort(listaDesordenada)
            elapsed_time = time.time() - start_time

            # Save execution time to a csv file
            aux.exportarTempo('heapSort', n, elapsed_time)

            # Exportar lista ordenada para um txt
            if (n % exportarListaOrdenada == 0):
                aux.exportarLista(listaOrdenada, './execlog/ordenadas/heapSort/', 'n_' + str(n) + '.txt')
            
            listaOrdenada.clear()

        ## Counting Sort
        if (runCountingSort == True):
            start_time = time.time()
            listaOrdenada = Algoritmos.countingSort(listaDesordenada)
            elapsed_time = time.time() - start_time

            # Save execution time to a csv file
            aux.exportarTempo('countingSort', n, elapsed_time)

            # Exportar lista ordenada para um txt
            if (n % exportarListaOrdenada == 0):
                aux.exportarLista(listaOrdenada, './execlog/ordenadas/countingSort/', 'n_' + str(n) + '.txt')

            listaOrdenada.clear()

        ## Radix Sort
        if (runRadixSort == True):
            start_time = time.time()
            listaOrdenada = Algoritmos.radixSortWithBubbleSort(listaDesordenada)
            elapsed_time = time.time() - start_time

            # Save execution time to a csv file
            aux.exportarTempo('radixSort', n, elapsed_time)

            # Exportar lista ordenada para um txt
            if (n % exportarListaOrdenada == 0):
                aux.exportarLista(listaOrdenada, './execlog/ordenadas/radixSort/', 'n_' + str(n) + '.txt')

            listaOrdenada.clear()

        ## Bucket Sort
        if (runBucketSort == True):
            start_time = time.time()
            listaOrdenada = Algoritmos.bucketSortWithBubbleSort(listaDesordenada)
            elapsed_time = time.time() - start_time

            # Save execution time to a csv file
            aux.exportarTempo('bucketSort', n, elapsed_time)

            # Exportar lista ordenada para um txt
            if (n % exportarListaOrdenada == 0):
                aux.exportarLista(listaOrdenada, './execlog/ordenadas/bucketSort/', 'n_' + str(n) + '.txt')
                
            listaOrdenada.clear()

        n = n + 1