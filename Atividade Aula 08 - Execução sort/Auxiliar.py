###
import os
import sys

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
   
# Exportar tempo de execução para um csv
def exportarTempo(algoritmo, n, tempo):
    with open('./tempos/tempos.csv', 'a') as f:
        f.write("%s;%d;%f\n" % (algoritmo, n, tempo))
    f.close()