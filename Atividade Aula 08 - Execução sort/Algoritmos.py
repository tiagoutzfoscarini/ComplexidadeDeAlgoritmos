###

import os
import sys
import Auxiliar as aux


## Quick Sort
def quickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


## Merge Sort
def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mid = len(lista) // 2
        left = mergeSort(lista[:mid])
        right = mergeSort(lista[mid:])
        return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


## Heap Sort
def heapSort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

    return lista

def heapify(lista, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lista[i] < lista[l]:
        largest = l

    if r < n and lista[largest] < lista[r]:
        largest = r

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        heapify(lista, n, largest)


## Counting Sort
def countingSort(lista):
    max_val = max(lista)
    count = [0] * (max_val + 1)

    while len(lista) > 0:
        num = lista.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            lista.append(i)
            count[i] -= 1

    return lista


## Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        
    return arr


## Bubble Sort (auxiliar para Radix Sort e Bucket Sort)
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


## Radix Sort
def radixSortWithInsertionSort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]
        
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        
        for bucket in radixArray:
            insertionSort(bucket)
        
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10

    return arr


## Bucket Sort
def bucketSortWithInsertionSort(arr):
    n = len(arr)
    max_val = max(arr)
    size = max_val // n

    buckets = [[] for _ in range(n)]

    for i in range(n):
        j = min(arr[i] // size, n - 1)
        buckets[j].append(arr[i])

    for i in range(n):
        insertionSort(buckets[i])

    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr