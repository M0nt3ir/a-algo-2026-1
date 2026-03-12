# Importa a biblioteca time para medir o tempo de execução
import time
import sys

sys.setrecursionlimit(2000)

# Função recursiva para calcular o fatorial
def fatorial(n):
    """
    Calcula o fatorial de n utilizando recursão.
    Fatorial de n (n!) = n * (n-1) * (n-2) ... * 1
    """

    # Caso base da recursão
    # Quando n é 0 ou 1, o fatorial é 1
    if n == 0 or n == 1:
        return 1

    # Caso recursivo
    # n! = n * (n-1)!
    return n * fatorial(n - 1)


# Lista de valores de entrada para testar o tempo
valores = [10, 100, 500, 1000]

# Teste de tempo de execução
for n in valores:

    # Marca o tempo inicial
    inicio = time.time()

    # Calcula o fatorial
    resultado = fatorial(n)

    # Marca o tempo final
    fim = time.time()

    # Calcula o tempo total
    tempo_execucao = fim - inicio

    # Exibe o resultado
    print(f"n = {n}")
    print(f"Tempo de execucao: {tempo_execucao:.8f} segundos\n")

"""
A complexidade de tempo do algoritmo de fatorial recursivo é O(n),
pois para calcular o fatorial de um número nm a função realiza
uma chamada recursiva para cada valor até chegar ao caso base.

Portanto, conforme n aumenta, o tempo de execução também cresce proporcionalmente,
caracterizando uma complexidade linear O(n). Além disso, o algoritmo
também utiliza O(n) de espaço.
"""

