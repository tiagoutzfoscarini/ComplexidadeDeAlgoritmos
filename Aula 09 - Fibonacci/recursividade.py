###

import time

import auxiliar as aux


# função para cálculo número n da sequência de Fibonacci, recursivo
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# MAIN
def main(n_min, n_max, tempoMilisegundos):
    for n in range(n_min, n_max + 1):
        # horário de início de execução
        startTime = time.time_ns()

        # chamada da função
        result = fib(n)

        # horário de término de execução
        endTime = time.time_ns()

        # registrar tempo de execução
        aux.exportarTempo("fib-recursivo", n, (endTime - startTime), tempoMilisegundos)

        # imprimir em tela
        print(f"fib({n}) = {result}")