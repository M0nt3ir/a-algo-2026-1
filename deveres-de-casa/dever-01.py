import time
import random

def insert_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

tamanhos = [1000, 5000, 20000, 50000]

print(f"{'n':>10} | {'Insert Sort (s)' :>20} | {'Timsort (s)' :>15}")
print("-" * 52)

for n in tamanhos:
    lista_original = [random.randint(0, 1000000) for _ in range(n)]


    lista_ins = lista_original.copy()
    inicio_ins = time.time()
    insert_sort(lista_ins)
    fim_ins = time.time()
    tempo_ins = fim_ins - inicio_ins

    lista_tim = lista_original.copy()
    inicio_tim = time.time()
    sorted(lista_tim)
    fim_tim = time.time()
    tempo_tim = fim_tim - inicio_tim

    print(f"{n:10d} | {tempo_ins:20.5f} | {tempo_tim:15.5f}")
