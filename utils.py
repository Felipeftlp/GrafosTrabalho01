def converter_matriz_para_lista(matriz_adj, vertices_ordenados):
    """
    Converte uma matriz de adjacência para uma lista de adjacência.
    """
    lista_adj = {v: [] for v in vertices_ordenados}
    for i, vertice_origem in enumerate(vertices_ordenados):
        for j, vertice_destino in enumerate(vertices_ordenados):
            if matriz_adj[i][j] == 1:
                lista_adj[vertice_origem].append(vertice_destino)
    return lista_adj

def converter_lista_para_matriz(lista_adj, vertices_ordenados):
    """
    Converte uma lista de adjacência para uma matriz de adjacência.
    """
    num_vertices = len(vertices_ordenados)
    mapa_vertices = {vertice: i for i, vertice in enumerate(vertices_ordenados)}
    matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]

    for vertice, vizinhos in lista_adj.items():
        idx_origem = mapa_vertices.get(vertice)
        if idx_origem is not None:
            for vizinho in vizinhos:
                idx_destino = mapa_vertices.get(vizinho)
                if idx_destino is not None:
                    matriz_adj[idx_origem][idx_destino] = 1
    return matriz_adj