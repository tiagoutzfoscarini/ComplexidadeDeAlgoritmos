###
import os
import random
import time

#
def gerarLista(n):
    # int list
    lista = [-1 for x in range(n)]

    for i in range(n):
        lista[i] = random.randint(0, 50000)
    return lista


# Checar se pasta existe
def mkdir(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


# Exportar lista para um txt
def exportarLista(lista, folderpath, filename):
    # check path
    mkdir(os.path.dirname(folderpath))

    with open(folderpath + filename, 'w') as f:
        for item in lista:
            f.write("%s\n" % item)
    f.close()


# transforma o tempo em milisegundos
def current_milli_time(tempo):
    return round(tempo * 1000)


# Exportar tempo de execução (em milisegundos) para um csv
def exportarTempo(algoritmo, n, tempo):
    # check path
    mkdir(os.path.dirname('./execlog/'))

    with open('./execlog/tempos.csv', 'a') as f:
        # tempo = current_milli_time(tempo)
        f.write("%s;%d;%f\n" % (algoritmo, n, tempo))

    f.close()
