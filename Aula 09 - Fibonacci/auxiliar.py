###

import os


# Checar se pasta existe
def mkdir(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


# Exportar tempo de execução (em milisegundos) para um csv
def exportarTempo(algoritmo, n, tempo, tempoMilisegundos):
    # check path
    mkdir(os.path.dirname('./execlog/'))

    with open('./execlog/tempos.csv', 'a') as f:
        if (tempoMilisegundos):
            tempo = tempo / 1000000 # converter nanosegundos para milisegundos

        f.write("%s;%d;%d\n" % (algoritmo, n, tempo))

    f.close()