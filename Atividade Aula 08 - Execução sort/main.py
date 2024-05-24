###
import time
import Algoritmos
import Auxiliar as aux


# main
if __name__ == "__main__":
    # Opcionais
    runQuickSort = True
    runMergeSort = True
    runHeapSort = True
    runCountingSort = True
    runRadixSort = True
    runBucketSort = True

    exportarListaOrdenada = 5000 # Exportar lista ordenada a cada n itens, 0 para desativar

    # Parâmetros
    global repeat, n_min, n_max

    n_min = 10
    n_max = 50000

    repeat = 20

    # Inicialização
    n = n_min

    # Loop principal
    while n <= n_max:
        print("n = ", n)

        # Gerar lista de items com valores e pesos aleatórios e ordenar por valor
        listaDesordenada = aux.gerarLista(n)

        # Exportar lista inicial para um txt
        if (n % exportarListaOrdenada == 0):
            aux.exportarLista(listaDesordenada, './execlog/desordenadas/', 'n-' + str(n) + '.txt')

        ## Ordenar lista com cada algoritmo

        ## Quick Sort
        if (runQuickSort == True):
            executionTimeSum = 0
            count = 0
            while count < repeat:
                count += 1

                start_time = time.time()
                listaOrdenada = Algoritmos.quickSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % exportarListaOrdenada == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'quickSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('quickSort', n, executionTimeSum/repeat)


        ## Merge Sort
        if (runMergeSort == True):
            executionTimeSum = 0
            count = 0
            while count < repeat:
                count += 1

                start_time = time.time()
                listaOrdenada = Algoritmos.mergeSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % exportarListaOrdenada == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'mergeSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('mergeSort', n, executionTimeSum/repeat)


        ## Heap Sort
        if (runHeapSort == True):
            executionTimeSum = 0
            count = 0
            while count < repeat:
                count += 1

                start_time = time.time()
                listaOrdenada = Algoritmos.heapSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % exportarListaOrdenada == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'heapSort-n-' + str(n) + '.txt')
                
                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('heapSort', n, elapsed_time/repeat)


        ## Counting Sort
        if (runCountingSort == True):
            executionTimeSum = 0
            count = 0
            while count < repeat:
                count += 1

                start_time = time.time()
                listaOrdenada = Algoritmos.countingSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % exportarListaOrdenada == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'countingSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('countingSort', n, elapsed_time/repeat)


        ## Radix Sort
        if (runRadixSort == True):
            executionTimeSum = 0
            count = 0
            while count < repeat:
                count += 1

                start_time = time.time()
                listaOrdenada = Algoritmos.radixSortWithBubbleSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % exportarListaOrdenada == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'radixSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('radixSort', n, elapsed_time/repeat)


        ## Bucket Sort
        if (runBucketSort == True):
            executionTimeSum = 0
            count = 0
            while count < repeat:
                count += 1

                start_time = time.time()
                listaOrdenada = Algoritmos.bucketSortWithBubbleSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % exportarListaOrdenada == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'bucketSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('bucketSort', n, elapsed_time/repeat)

        # Incremento
        n = n + 1