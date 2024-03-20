###

import sys
from datetime import datetime, timedelta

# Função quick sort
def quickSortPartition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = quickSortPartition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Função bubble sort
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# função para gerar lista de listSize numeros aleatorios inteiros
def generateList(listSize):
    import random
    return [random.randint(0, listSize) for i in range(listSize)]


# Main
def main():
    if len(sys.argv) > 1:
        listSize = int(sys.argv[1])
    else:
        listSize = 1000

    # Gera lista de numeros aleatorios
    lista = generateList(listSize)

    listaOrdenadaBubbleSort = lista.copy()
    listaOrdenadaQuickSort = lista.copy()

    # Bubble Sort
    print ("Executando Bubble Sort para lista de tamanho ", listSize, "...")

    start = datetime.now()
    bubbleSort(listaOrdenadaBubbleSort)
    end = datetime.now()
    executionTime = (end - start).total_seconds() * 1000

    print("Bubble Sort: ", executionTime)
    
    # Quick Sort
    print ("Executando Quick Sort para lista de tamanho ", listSize, "...")

    start = datetime.now()
    quickSort(listaOrdenadaQuickSort, 0, listSize-1)
    end = datetime.now()
    executionTime = (end - start).total_seconds() * 1000

    print("Quick Sort: ", executionTime)

    

## MAIN
if __name__ == "__main__":
    main()