# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

"""
=============================================================
  Dever de Casa - Analise de Algoritmos
=============================================================
  1) Merge Sort             → Θ(n log n)
  2) Multiplicação de Matrizes 
  3) Recorrências (simulação empírica):
        T(n) = 2T(n/4) + √n   → Θ(√n · log n)
        T(n) = 2T(n/4) + n    → Θ(n)
        T(n) = 16T(n/4) + n²  → Θ(n² log n)
=============================================================
"""

import time
import math
import random


# ─────────────────────────────────────────────────────────────
#  1) MERGE SORT  —  T(n) = 2T(n/2) + cn  →  Θ(n log n)
# ─────────────────────────────────────────────────────────────

def merge_sort(arr: list) -> list:
    """
    Ordena uma lista usando o algoritmo Merge Sort.

    Complexidade:
      Recorrência:  T(n) = 2T(n/2) + Θ(n)
      Solução:      T(n) = Θ(n log n)   — melhor, médio e pior caso

    Estratégia Dividir e Conquistar:
      1. DIVIDIR:    separa o array ao meio             → O(1)
      2. CONQUISTAR: ordena recursivamente cada metade  → 2T(n/2)
      3. COMBINAR:   intercala as duas metades          → Θ(n)
    """
    n = len(arr)

    # Caso base: array de 0 ou 1 elemento já está ordenado
    if n <= 1:
        return arr

    # --- DIVIDIR ---
    meio = n // 2
    esquerda = arr[:meio]   # primeiros n/2 elementos
    direita   = arr[meio:]  # últimos  n/2 elementos

    # --- CONQUISTAR ---
    esquerda = merge_sort(esquerda)
    direita   = merge_sort(direita)

    # --- COMBINAR ---
    return _merge(esquerda, direita)


def _merge(esq: list, dir: list) -> list:
    """
    Intercala dois sub-arrays ordenados em um único array ordenado.
    Custo: Θ(n) — cada elemento é copiado exatamente uma vez.
    """
    resultado = []
    i = j = 0

    # Compara os menores elementos de cada metade e insere em ordem
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # Acrescenta os elementos restantes (já ordenados)
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


# ─────────────────────────────────────────────────────────────
#  2) MULTIPLICAÇÃO DE MATRIZES
#     Ingênuo:   T(n) = Θ(n³)
#     Strassen:  T(n) = 7T(n/2) + Θ(n²)  →  Θ(n^log₂7) ≈ Θ(n^2.807)
# ─────────────────────────────────────────────────────────────

def multiplicar_matrizes_ingenuo(A: list, B: list) -> list:

    n = len(A)
    # Inicializa a matriz resultado com zeros
    C = [[0] * n for _ in range(n)]

    for i in range(n):          # Percorre cada linha de A
        for j in range(n):      # Percorre cada coluna de B
            for k in range(n):  # Acumula o produto interno
                C[i][j] += A[i][k] * B[k][j]

    return C


def strassen(A: list, B: list) -> list:

    n = len(A)

    # Caso base: matriz 1×1 — simples multiplicação escalar
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # --- DIVIDIR: particiona cada matriz em 4 sub-matrizes de tamanho n/2 ---
    meio = n // 2

    A11 = _submatriz(A, 0,    0,    meio, meio)
    A12 = _submatriz(A, 0,    meio, meio, n)
    A21 = _submatriz(A, meio, 0,    n,    meio)
    A22 = _submatriz(A, meio, meio, n,    n)

    B11 = _submatriz(B, 0,    0,    meio, meio)
    B12 = _submatriz(B, 0,    meio, meio, n)
    B21 = _submatriz(B, meio, 0,    n,    meio)
    B22 = _submatriz(B, meio, meio, n,    n)

    # --- CONQUISTAR: 7 produtos de Strassen (em vez de 8 do algoritmo ingênuo) ---
    M1 = strassen(_somar(A11, A22), _somar(B11, B22))
    M2 = strassen(_somar(A21, A22), B11)
    M3 = strassen(A11,               _subtrair(B12, B22))
    M4 = strassen(A22,               _subtrair(B21, B11))
    M5 = strassen(_somar(A11, A12), B22)
    M6 = strassen(_subtrair(A21, A11), _somar(B11, B12))
    M7 = strassen(_subtrair(A12, A22), _somar(B21, B22))

    # --- COMBINAR: monta a matriz resultado a partir dos 7 produtos ---
    C11 = _somar(_subtrair(_somar(M1, M4), M5), M7)
    C12 = _somar(M3, M5)
    C21 = _somar(M2, M4)
    C22 = _somar(_subtrair(_somar(M1, M3), M2), M6)

    return _juntar(C11, C12, C21, C22, n)


# ── Funções auxiliares de matrizes ──────────────────────────

def _submatriz(M, r1, c1, r2, c2):
    return [linha[c1:c2] for linha in M[r1:r2]]

def _somar(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def _subtrair(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def _juntar(C11, C12, C21, C22, n):
    """Reconstrói a matriz n×n a partir dos quatro quadrantes."""
    meio = n // 2
    C = [[0] * n for _ in range(n)]
    for i in range(meio):
        for j in range(meio):
            C[i][j]           = C11[i][j]
            C[i][j + meio]    = C12[i][j]
            C[i + meio][j]    = C21[i][j]
            C[i + meio][j + meio] = C22[i][j]
    return C

def gerar_matriz(n, max_val=10):
    """Gera uma matriz n×n com valores inteiros aleatórios."""
    return [[random.randint(0, max_val) for _ in range(n)] for _ in range(n)]


# ─────────────────────────────────────────────────────────────
#  3) SIMULAÇÃO EMPÍRICA DAS RECORRÊNCIAS
# ─────────────────────────────────────────────────────────────

def recorrencia_1(n: int) -> int:
    """
    Simula T(n) = 2T(n/4) + √n   →   Θ(√n · log n)

    Teorema Mestre:
      a = 2, b = 4  →  log_b(a) = log₄(2) = 0.5
      f(n) = n^(1/2) = Θ(n^0.5) = Θ(n^(log_b a))  → Caso 2
      Resultado: T(n) = Θ(n^(1/2) · log n)
    """
    if n <= 1:
        return 1

    custo_atual = int(math.isqrt(n))  # trabalho neste nível: √n
    return 2 * recorrencia_1(n // 4) + custo_atual


def recorrencia_2(n: int) -> int:
    """
    Simula T(n) = 2T(n/4) + n   →   Θ(n)

    Teorema Mestre:
      a = 2, b = 4  →  log_b(a) = log₄(2) = 0.5
      f(n) = n^1 = Ω(n^(0.5 + ε)) com ε = 0.5  → Caso 3
      Condição de regularidade: 2·(n/4) = n/2 ≤ c·n para c = 1/2 ✓
      Resultado: T(n) = Θ(n)
    """
    if n <= 1:
        return 1

    custo_atual = n  # trabalho neste nível: n
    return 2 * recorrencia_2(n // 4) + custo_atual


def recorrencia_3(n: int) -> int:
    """
    Simula T(n) = 16T(n/4) + n²   →   Θ(n² log n)

    Teorema Mestre:
      a = 16, b = 4  →  log_b(a) = log₄(16) = 2
      f(n) = n^2 = Θ(n^2) = Θ(n^(log_b a))  → Caso 2
      Resultado: T(n) = Θ(n² · log n)
    """
    if n <= 1:
        return 1

    custo_atual = n * n  # trabalho neste nível: n²
    return 16 * recorrencia_3(n // 4) + custo_atual


# ─────────────────────────────────────────────────────────────
#  TESTES E DEMONSTRAÇÕES
# ─────────────────────────────────────────────────────────────

def separador(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)


def testar_merge_sort():
    separador("1) MERGE SORT  —  Θ(n log n)")

    # Teste de correção
    casos = [
        [5, 3, 8, 1, 9, 2, 7, 4, 6],
        [1],
        [],
        [3, 3, 3, 1, 2],
        list(range(10, 0, -1)),   # já invertido
        list(range(1, 11)),       # já ordenado
    ]

    print("\n  Testes de correção:")
    for entrada in casos:
        saida = merge_sort(entrada[:])
        correto = saida == sorted(entrada)
        print(f"  Entrada: {str(entrada):<35} → {saida} {'✓' if correto else '✗'}")

    # Análise de tempo por tamanho
    print("\n  Análise de tempo (tempo real × complexidade esperada):")
    print(f"  {'n':>8} | {'tempo (ms)':>12} | {'n·log₂n':>12} | {'razão t/(n·log n)':>18}")
    print("  " + "-" * 60)

    for n in [1_000, 5_000, 10_000, 50_000, 100_000]:
        dados = random.sample(range(n * 10), n)
        inicio = time.perf_counter()
        merge_sort(dados)
        duracao = (time.perf_counter() - inicio) * 1000

        nlogn = n * math.log2(n)
        razao = duracao / nlogn * 1e6

        print(f"  {n:>8,} | {duracao:>12.3f} | {nlogn:>12.1f} | {razao:>18.4f}")

    print("\n  → Razão aproximadamente constante confirma Θ(n log n).")


def testar_matrizes():
    separador("2) MULTIPLICAÇÃO DE MATRIZES")

    # Verifica que ingênuo e Strassen produzem o mesmo resultado
    print("\n  Verificação de correção (ingênuo == Strassen):")
    for n in [2, 4, 8]:
        A = gerar_matriz(n)
        B = gerar_matriz(n)
        C_ing = multiplicar_matrizes_ingenuo(A, B)
        C_str = strassen(A, B)
        ok = C_ing == C_str
        print(f"  n={n}: ingênuo == Strassen? {'✓ Sim' if ok else '✗ Não'}")

    # Comparação de tempo
    print("\n  Comparação de tempo: ingênuo Θ(n³) vs Strassen Θ(n^2.807):")
    print(f"  {'n':>6} | {'Ingênuo (ms)':>14} | {'Strassen (ms)':>14} | {'Speedup':>10}")
    print("  " + "-" * 52)

    for n in [2, 4, 8, 16, 32, 64]:
        A = gerar_matriz(n)
        B = gerar_matriz(n)

        t0 = time.perf_counter()
        multiplicar_matrizes_ingenuo(A, B)
        t_ing = (time.perf_counter() - t0) * 1000

        t0 = time.perf_counter()
        strassen(A, B)
        t_str = (time.perf_counter() - t0) * 1000

        speedup = t_ing / t_str if t_str > 0 else float('inf')
        print(f"  {n:>6} | {t_ing:>14.4f} | {t_str:>14.4f} | {speedup:>10.2f}×")

    print("\n  → Para n grande, Strassen supera o ingênuo.")
    print(f"  → Expoentes: ingênuo = 3.000, Strassen = log₂(7) ≈ {math.log2(7):.3f}")


def testar_recorrencias():
    separador("3) RECORRÊNCIAS — SIMULAÇÃO EMPÍRICA")

    recorrencias = [
        ("T(n) = 2T(n/4) + √n",   recorrencia_1, "Θ(√n · log n)", lambda n: math.sqrt(n) * math.log2(n) if n > 1 else 1),
        ("T(n) = 2T(n/4) + n",    recorrencia_2, "Θ(n)",          lambda n: n),
        ("T(n) = 16T(n/4) + n²",  recorrencia_3, "Θ(n² · log n)", lambda n: n**2 * math.log2(n) if n > 1 else 1),
    ]

    tamanhos = [4, 16, 64, 256, 1024, 4096]

    for nome, func, complexidade, teorica in recorrencias:
        print(f"\n  Recorrência: {nome}")
        print(f"  Resultado esperado (Teorema Mestre): {complexidade}")
        print(f"  {'n':>6} | {'T(n) simulado':>16} | {'f(n) teórica':>14} | {'razão T/f(n)':>14}")
        print("  " + "-" * 58)

        for n in tamanhos:
            tn  = func(n)
            fn  = teorica(n)
            razao = tn / fn if fn > 0 else 0
            print(f"  {n:>6} | {tn:>16,} | {fn:>14.1f} | {razao:>14.4f}")

        print(f"  → Razão convergindo para constante confirma {complexidade}.")


# ─────────────────────────────────────────────────────────────
#  PONTO DE ENTRADA
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("   Dever de Casa - Analise de Algoritmos")
    print("   Implementacoes e verificacoes empiricas")
    print("=" * 60)

    random.seed(42)

    testar_merge_sort()
    testar_matrizes()
    testar_recorrencias()

    print("\n" + "=" * 60)
    print("  Execucao concluida.")
    print("=" * 60)
