###

import recursividade
import memo_bottom_up
import memo_top_down


def main(runParameters):
    if runParameters["recursividade"]:
        print("RECURSIVIDADE")
        recursividade.main(runParameters["n_min"], runParameters["n_max"], runParameters["tempoMilisegundos"])

    if runParameters["memo_bottom_up"]:
        print("MEMO BOTTOM-UP")
        memo_bottom_up.main(runParameters["n_min"], runParameters["n_max"], runParameters["tempoMilisegundos"])

    if runParameters["memo_top_down"]:
        print("MEMO TOP-DOWN")
        memo_top_down.main(runParameters["n_min"], runParameters["n_max"], runParameters["tempoMilisegundos"])


if __name__ == "__main__":
    # n é a quantidade de elementos da sequência de Fibonacci a serem calculados
    # executar de 0 a 40
    runParameters = {
        "n_min": 0,
        "n_max": 40,
        "recursividade": True,
        "memo_bottom_up": True,
        "memo_top_down": True,
        "tempoMilisegundos": True # True para exportar tempo em milisegundos, False para nanosegundos
    }

    main(runParameters)