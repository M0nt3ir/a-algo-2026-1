def busca_padrao_ia(dataset, padrao_alvo):
    """

    Analisa a complexidade de tempo T(n) baseada na posição do alvo.
    n = len(dataset)

    """
    n = len(dataset)

    for i in range(n):
        # Operação primitiva: Comparação (if)
        if dataset[i] == padrao_alvo:
            return f"Padrão encontrado na posição {i}" # Melhor caso se i=0
        

    return "Padrão não encontrado" # Pior caso (percorreu tudo)

# --- Cenários ---
base_dados = [10, 20, 30, 40, 50] # n = 5

# MELHOR CASO: O alvo é  primeiro elemento (1 operação)
# T(n) = Omega(1)
print(busca_padrao_ia(base_dados, 10))

# PIOR CASO: O alvo não existe ou é último (n operações)
# T(n) = O(n)
print(busca_padrao_ia(base_dados, 99))