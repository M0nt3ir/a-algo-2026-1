def bellman_ford(vertices, arestas, vertice_inicial):
    # Inicialização: distância infinita para todos e predecessor como None
    # O vértice inicial começa com distância 0
    distancias = {v: float('inf') for v in vertices}
    predecessores = {v: None for v in vertices}
    distancias[vertice_inicial] = 0

    print("=== TABELA DE ITERACOES ===")
    # Cabeçalho da tabela
    cabecalho = "Iteracao\t" + "\t".join([f"V{v}" for v in vertices])
    print(cabecalho)
    print("-" * (len(cabecalho) * 2))

    # Print do estado inicial (Iteração 0)
    estado_inicial = "Inicial\t\t" + "\t".join([f"{distancias[v]}({predecessores[v]})" for v in vertices])
    print(estado_inicial)

    # Executa as iterações (o enunciado pede explicitamente Iteração 1, 2 e 3)
    # Nota: Para um grafo de 5 vértices, o algoritmo completo corre até V-1 (4) iterações para convergir.
    for iteracao in range(1, 4):
        # Criamos uma cópia para não atualizar e usar o valor na mesma iteração de forma inconsistente
        novas_distancias = distancias.copy()
        novos_predecessores = predecessores.copy()
        
        # Relaxamento de todas as arestas
        for origem, destino, peso in arestas:
            if distancias[origem] != float('inf') and distancias[origem] + peso < novas_distancias[destino]:
                novas_distancias[destino] = distancias[origem] + peso
                novos_predecessores[destino] = origem
                
        distancias = novas_distancias
        predecessores = novos_predecessores

        # Formata a linha da tabela: "distancia(predecessor)"
        linha = f"Iteração {iteracao}\t" + "\t".join([
            f"{distancias[v]}({predecessores[v]})" if distancias[v] != float('inf') else f"inf(None)" 
            for v in vertices
        ])
        print(linha)

    print("\n" + "="*30)
    
    # Verificação de ciclo negativo (Passo extra após as iterações)
    print("=== VERIFICACAO DE CICLO NEGATIVO ===")
    existe_ciclo_negativo = False
    for origem, destino, peso in arestas:
        if distancias[origem] != float('inf') and distancias[origem] + peso < distancias[destino]:
            print(f"Aresta ({origem} -> {destino}) ainda pode ser reduzida! Peso atual: {distancias[destino]}, Novo potencial: {distancias[origem] + peso}")
            existe_ciclo_negativo = True
            
    if existe_ciclo_negativo:
        print("\nResultado: Existe pelo menos um ciclo negativo no grafo!")
    else:
        print("\nResultado: Nao foi detectado nenhum ciclo negativo atingivel a partir do vertice inicial nas iteracoes atuais.")

# --- Definição do Grafo da Imagem ---

# Vértices do grafo
vertices = [0, 1, 2, 3, 4]

# Lista de arestas: (origem, destino, peso)
arestas = [
    (0, 1, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 1),
    (4, 3, -1)
]

# Executa o algoritmo partindo do vértice 0
bellman_ford(vertices, arestas, vertice_inicial=0)