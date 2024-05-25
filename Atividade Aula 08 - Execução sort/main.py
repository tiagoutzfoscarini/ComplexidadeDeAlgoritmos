###
import time
from datetime import datetime
import Algoritmos
import Auxiliar as aux


def main(runAlgorithm, executionParams):
    # Inicialização
    n = executionParams['n_min']

    # Loop principal
    while n <= executionParams['n_max']:
        currentDatetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print("[%s] n = %d" % (currentDatetime, n))

        aux.registrarUltimaIteracao(currentDatetime, n)

        # Gerar lista de items com valores e pesos aleatórios e ordenar por valor
        listaDesordenada = aux.gerarLista(n)

        # Exportar lista inicial para um txt
        if (n % executionParams['exportarListaOrdenada'] == 0):
            aux.exportarLista(listaDesordenada, './execlog/desordenadas/', 'n-' + str(n) + '.txt')

        ## Ordenar lista com cada algoritmo

        ## Quick Sort
        if (runAlgorithm['quickSort'] == True):
            executionTimeSum = 0
            count = 0
            while count < executionParams['repeat']:
                count += 1

                start_time = time.time_ns()
                listaOrdenada = Algoritmos.quickSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time_ns() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % executionParams['exportarListaOrdenada'] == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'quickSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('quickSort', n, executionTimeSum/executionParams['repeat'])


        ## Merge Sort
        if (runAlgorithm['mergeSort'] == True):
            executionTimeSum = 0
            count = 0
            while count < executionParams['repeat']:
                count += 1

                start_time = time.time_ns()
                listaOrdenada = Algoritmos.mergeSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time_ns() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % executionParams['exportarListaOrdenada'] == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'mergeSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('mergeSort', n, executionTimeSum/executionParams['repeat'])


        ## Heap Sort
        if (runAlgorithm['heapSort'] == True):
            executionTimeSum = 0
            count = 0
            while count < executionParams['repeat']:
                count += 1

                start_time = time.time_ns()
                listaOrdenada = Algoritmos.heapSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time_ns() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % executionParams['exportarListaOrdenada'] == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'heapSort-n-' + str(n) + '.txt')
                
                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('heapSort', n, executionTimeSum/executionParams['repeat'])


        ## Counting Sort
        if (runAlgorithm['countingSort'] == True):
            executionTimeSum = 0
            count = 0
            while count < executionParams['repeat']:
                count += 1

                start_time = time.time_ns()
                listaOrdenada = Algoritmos.countingSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time_ns() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % executionParams['exportarListaOrdenada'] == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'countingSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('countingSort', n, executionTimeSum/executionParams['repeat'])


        ## Radix Sort
        if (runAlgorithm['radixSort'] == True):
            executionTimeSum = 0
            count = 0
            while count < executionParams['repeat']:
                count += 1

                start_time = time.time_ns()
                listaOrdenada = Algoritmos.radixSortWithInsertionSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time_ns() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % executionParams['exportarListaOrdenada'] == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'radixSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('radixSort', n, executionTimeSum/executionParams['repeat'])


        ## Bucket Sort
        if (runAlgorithm['bucketSort'] == True):
            executionTimeSum = 0
            count = 0
            while count < executionParams['repeat']:
                count += 1

                start_time = time.time_ns()
                listaOrdenada = Algoritmos.bucketSortWithInsertionSort(listaDesordenada[:]) # [:] para passar uma cópia da lista
                elapsed_time = time.time_ns() - start_time
                executionTimeSum += elapsed_time

                # Exportar lista ordenada a cada n itens para um txt
                if (n % executionParams['exportarListaOrdenada'] == 0):
                    aux.exportarLista(listaOrdenada, './execlog/ordenadas/', 'bucketSort-n-' + str(n) + '.txt')

                listaOrdenada.clear() # Limpar lista ordenada para próxima execução

            # Salvar média (tempo de execução total dividido pelo número de repetições) em um arquivo csv
            aux.exportarTempo('bucketSort', n, executionTimeSum/executionParams['repeat'])


        # Incremento
        n = n + 1

# main
if __name__ == "__main__":
    # Opcionais
    global runAlgorithm

    runAlgorithm = {
        'quickSort': True,
        'mergeSort': True,
        'heapSort': True,
        'countingSort': True,
        'radixSort': False,
        'bucketSort': True
    }

    # Parâmetros
    global executionParams

    executionParams = {
        'n_min': 10,
        'n_max': 50000,
        'repeat': 20,
        'exportarListaOrdenada': 5000 # Exportar lista ordenada a cada n itens, 0 para desativar
    }

    main(runAlgorithm, executionParams)

