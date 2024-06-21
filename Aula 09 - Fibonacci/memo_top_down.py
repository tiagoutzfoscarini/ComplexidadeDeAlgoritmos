###

import time

import auxiliar as aux


# função para cálculo número n da sequência de Fibonacci, memoização top-down
# top-down: calcular o valor de n, partindo de n, através de chamadas recursivas
def topdown_fib(n, memo):
    # Se o valor já foi calculado, retornar o valor armazenado
    if memo[n] != -1:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        # Calcular o valor de n através de chamadas recursivas e armazenar na lista de memoização
        memo[n] = topdown_fib(n - 1, memo) + topdown_fib(n - 2, memo)

    return memo[n]


# MAIN
def main(n_min, n_max, tempoMilisegundos):
    for n in range(n_min, n_max + 1):
        # inicializar memoização
        memo = [-1] * (n + 1)

        # horário de início de execução
        startTime = time.time_ns()

        # chamada da função
        result = topdown_fib(n, memo)

        # horário de término de execução
        endTime = time.time_ns()

        # registrar tempo de execução
        aux.exportarTempo("fib-top-down", n, (endTime - startTime), tempoMilisegundos)

        # imprimir em tela
        print(f"fib({n}) = {result}")