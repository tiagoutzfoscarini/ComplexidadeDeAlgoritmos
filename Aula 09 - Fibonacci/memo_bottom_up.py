###

import time

import auxiliar as aux


# função para cálculo número n da sequência de Fibonacci, memoização bottom-up
# bottom-up: calcular os valores menores primeiro até chegar em n
def bottomup_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # inicializar memoização
    memo = [-1] * (n + 1)
    memo[0] = 0 # fib(0) = 0
    memo[1] = 1 # fib(1) = 1

    # Calcular o valor de todos os números da sequência de Fibonacci até n, armazenando na lista de memoização
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]
    

# MAIN
def main(n_min, n_max, tempoMilisegundos):
    for n in range(n_min, n_max):
        # horário de início de execução
        startTime = time.time_ns()

        # chamada da função
        result = bottomup_fib(n)

        # horário de término de execução
        endTime = time.time_ns()

        # registrar tempo de execução
        aux.exportarTempo("fib-bottom-up", n, (endTime - startTime), tempoMilisegundos)

        # imprimir em tela
        print(f"fib({n}) = {result}")