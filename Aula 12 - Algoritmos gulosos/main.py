### Algoritmos gulosos
## Problema: troco de moedas com o menor número de moedas possíveis

import sys
import random

def selecionarMoedas(config):
    ## declarar as moedas disponíveis
    # Configuração 1: Moedas de 1, 2, 5, 10, 25, 50 e 100 centavos
    # Configuração 2: Moedas de 1, 5, 10, 20, 50 e 100 centavos
    # Configuração 3: Moedas de 1, 2, 5, 10, 20, 50 e 100 centavos
    # Configuração 4: Moedas de 1, 5, 12, 24, 50 e 100 centavos
    if (config == 1):
        moedas = [0.01, 0.02, 0.05, 0.10, 0.25, 0.50, 1]
    elif (config == 2):
        moedas = [0.01, 0.05, 0.10, 0.20, 0.50, 1]
    elif (config == 3):
        moedas = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1]
    elif (config == 4):
        moedas = [0.01, 0.05, 0.012, 0.24, 0.50, 1]
    else:
        print("Configuração inválida")
        return
    
    return moedas


def main(moedasDisponiveis, valorTroco):
    # Ordenar as moedas disponíveis
    moedasDisponiveis.sort(reverse=True)

    moedasParaTroco = []
    trocoRestante = valorTroco

    # Iterar sobre as moedas disponíveis, da maior para a menor
    for m in moedasDisponiveis:
        while (m <= trocoRestante):
            moedasParaTroco.append(m)
            trocoRestante -= m

            if (trocoRestante == 0):
                break

    return moedasParaTroco


if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print("!!! Número de argumentos inválido !!!")
        print("Configurações disponíveis: 1, 2, 3, 4")
        print("\t- Configuração 1: Moedas de 1, 2, 5, 10, 25, 50 e 100 centavos \n"
            "\t- Configuração 2: Moedas de 1, 5, 10, 20, 50 e 100 centavos \n"
            "\t- Configuração 3: Moedas de 1, 2, 5, 10, 20, 50 e 100 centavos \n"
            "\t- Configuração 4: Moedas de 1, 5, 12, 24, 50 e 100 centavos"
        )
        print("Uso: python main.py <configuração 1-4> <valor troco a ser calculado>")
        print("Exemplo: python main.py 1 1.50")
        
        print("\nExecutando com configuração padrão (1) e troco aleatório...\n")

        config = 1
        valorTroco = round(random.uniform(0.01, 10.00), 2)

        print("Troco a ser calculado: R$", valorTroco)
    else:
        config = int(sys.argv[1])
        valorTroco = float(sys.argv[2])

    # 
    moedas = selecionarMoedas(config)
    print("Moedas disponíveis (em R$): ", moedas)
    
    # 
    moedasParaTroco = main(moedas, valorTroco)

    # Imprimir as moedas para o troco
    print("\nRESULTADO: ")
    print("Total de moedas: ", moedasParaTroco.__len__())
    # print("Moedas para o troco: ", moedasParaTroco)

    # Agrupar as moedas para o troco
    moedasAgrupadas = {}
    for m in moedasParaTroco:
        if m in moedasAgrupadas:
            moedasAgrupadas[m] += 1
        else:
            moedasAgrupadas[m] = 1

    print("\nMoedas de troco:")
    for m in moedasAgrupadas:
        print(moedasAgrupadas[m], "moeda(s) de R$", m)

