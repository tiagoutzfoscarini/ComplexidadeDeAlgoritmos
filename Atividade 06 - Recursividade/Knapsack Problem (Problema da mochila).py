###
# Retorna o valor máximo que pode ser colocado em uma mochila de capacidade W

import sys
import random

# Gerar lista de items com valores e pesos aleatórios
def gerarLista(n):
    lista = [dict() for x in range(n)]
    for i in range(n):
        lista[i] = {'id': i, 'valor': random.randint(1, 100), 'peso': random.randint(1, 30)}
    return lista


# Ordenar lista de items por valor
def ordenarListaPorValor(lista):
    lista.sort(key=lambda x: x['valor'], reverse=True)
    return lista


# Imprimir lista de items como tabela
def imprimirLista(lista):
    # Print list as table
    print('ID\tValor\tPeso')
    for item in lista:
        print(f"{item['id']}\t{item['valor']}\t{item['peso']}")


# Função recursiva para o problema da mochila
def knapSack(W, lista, n, bag):
    # Caso base
    if n == 0 or W == 0:
        return 0, bag

    # Se o peso do item é maior que a capacidade da mochila, então não pode ser incluído na solução ótima
    if (lista[n-1]['peso'] > W):
        return knapSack(W, lista, n-1, bag)
    
    # Retorna o máximo entre o valor do item incluído e o valor do item não incluído
    else:
        valor_incluido, bag_incluido = knapSack(W-lista[n-1]['peso'], lista, n-1, bag + [lista[n-1]])
        valor_nao_incluido, bag_nao_incluido = knapSack(W, lista, n-1, bag)
        if valor_incluido + lista[n-1]['valor'] > valor_nao_incluido:
            return valor_incluido + lista[n-1]['valor'], bag_incluido
        else:
            return valor_nao_incluido, bag_nao_incluido


# Main
if __name__ == '__main__':
    # Algoritmo modificado
    # Gerar valores e pesos aleatórios para n itens
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        W = int(sys.argv[2])
    else:
        n = 5
        W = 50
        print("\nValores padrão: n = 5, W = 50")
        print("Sem argumentos, o programa utilizará os valores padrão.")
        print("Utilize 'python3 Knapsack Problem.py <n> <W>' para definir a quantidade de itens e a capacidade da mochila.")

    # Gerar lista de items com valores e pesos aleatórios e ordenar por valor
    lista = gerarLista(n)
    lista = ordenarListaPorValor(lista)

    # # Teste de acordo com valores do original (deve resultar em 220)
    # lista = [{'id': 1, 'valor': 60, 'peso': 10},
    #         {'id': 2, 'valor': 100, 'peso': 20},
    #         {'id': 3, 'valor': 120, 'peso': 30}]    
    # n = len(lista)
    # W = 50
    
    print("\nLista de itens:")
    imprimirLista(lista)

    bag = []

    resultado, bag = knapSack(W, lista, n, bag)

    print("\nO valor máximo que pode ser colocado na mochila é:", resultado)

    print("\nItens na mochila:")
    imprimirLista(bag)