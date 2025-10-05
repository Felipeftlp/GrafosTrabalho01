class Grafo:
    """
    Classe para representar um grafo e gerar as suas principais estruturas de dados:
    - Lista de Adjacência
    - Matriz de Adjacência
    - Matriz de Incidência
    """
    def __init__(self, vertices, arestas):
        """
        Inicializa o grafo com uma lista de vértices e uma lista de arestas.
        """
        self.vertices_ordenados = sorted(list(vertices))
        self.arestas = arestas
        self.num_vertices = len(self.vertices_ordenados)
        self.num_arestas = len(self.arestas)
        # Cria um dicionário para mapear cada vértice a um índice (ex: 'A': 0, 'B': 1)
        self.mapa_vertices = {vertice: i for i, vertice in enumerate(self.vertices_ordenados)}

    def criar_lista_adjacencia(self):
        """
        Cria e retorna a lista de adjacência do grafo.
        """
        lista_adj = {v: [] for v in self.vertices_ordenados}
        for v1, v2 in self.arestas:
            # Garante que os vértices existem na lista antes de adicionar
            if v1 in lista_adj and v2 in lista_adj:
                lista_adj[v1].append(v2)
                lista_adj[v2].append(v1)
        return lista_adj

    def criar_matriz_adjacencia(self):
        """
        Cria e retorna a matriz de adjacência do grafo.
        """
        matriz_adj = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for v1, v2 in self.arestas:
            # Usa o mapa de vértices para encontrar os índices corretos
            idx1 = self.mapa_vertices.get(v1)
            idx2 = self.mapa_vertices.get(v2)
            if idx1 is not None and idx2 is not None:
                matriz_adj[idx1][idx2] = 1
                matriz_adj[idx2][idx1] = 1
        return matriz_adj

    def criar_matriz_incidencia(self):
        """
        Cria e retorna a matriz de incidência do grafo.
        """
        matriz_inc = [[0] * self.num_arestas for _ in range(self.num_vertices)]
        for i, (v1, v2) in enumerate(self.arestas):
            idx1 = self.mapa_vertices.get(v1)
            idx2 = self.mapa_vertices.get(v2)
            if idx1 is not None:
                matriz_inc[idx1][i] = 1
            if idx2 is not None:
                matriz_inc[idx2][i] = 1
        return matriz_inc

    """
    Abaixo estão as funções resultantes dos itens 5 a 8 da lista:
    - Grau de cada vértice
    - vertice adjacente
    - total de vertices
    - total de arestas
    """

    def get_grau_vertices(self):
        """
        Item 5 - Retorna o grau dos vértices.
        """
        grau_vertices = {}
        for v in self.vertices_ordenados:
            grau_vertices[f"d({v})"] = sum(v in aresta for aresta in self.arestas)
        return grau_vertices

    def is_adjacente(self, v1, v2):
        """
        Item 6 - Verifica se os vertices são adjacentes.
        """
        for aresta in self.arestas:
            if v1 in aresta and v2 in aresta:
                return True
        return False

    def get_num_vertices(self):
        """
        Item 7 - Retorna o total de vértices
        """
        return self.num_vertices

    def get_num_arestas(self):
        """
        Item 8 - Retorna o total de arestas
        """
        return self.num_arestas
