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
    n = len(lista)
    output = [0] * n
    count = [0] * 256
    for i in lista:
        count[i] += 1
    for i in range(256):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        output[count[lista[i]] - 1] = lista[i]
        count[lista[i]] -= 1
        i -= 1
    for i in range(n):
        lista[i] = output[i]
    return lista


## Radix Sort


## Bucket Sort
