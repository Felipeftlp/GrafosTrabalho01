class Digrafo:
    """
    Classe para representar um dígrafo (grafo direcionado) e suas estruturas de dados.
    
    Em um dígrafo, as arestas têm direção: uma aresta (u, v) vai de u para v,
    mas não necessariamente existe a aresta (v, u).
    """
    
    def __init__(self, vertices, arcos):
        """
        Inicializa o dígrafo com uma lista de vértices e uma lista de arcos direcionados.
        
        Args:
            vertices (set ou list): Conjunto de vértices do dígrafo
            arcos (list): Lista de tuplas (origem, destino) representando arcos direcionados
        """
        self.vertices_ordenados = sorted(list(vertices))
        self.arcos = arcos
        self.num_vertices = len(self.vertices_ordenados)
        self.num_arcos = len(self.arcos)
        self.mapa_vertices = {vertice: i for i, vertice in enumerate(self.vertices_ordenados)}

    def criar_lista_adjacencia(self):
        """
        Cria e retorna a lista de adjacência do dígrafo.
        
        Returns:
            dict: Dicionário onde cada chave é um vértice e o valor é uma lista
                  de vértices que são alcançáveis a partir dele (destinos).
        """
        lista_adj = {v: [] for v in self.vertices_ordenados}
        for origem, destino in self.arcos:
            if origem in lista_adj and destino in lista_adj:
                lista_adj[origem].append(destino)
        return lista_adj

    def criar_matriz_adjacencia(self):
        """
        Item 16 - Cria e retorna a matriz de adjacência do dígrafo.
        
        Returns:
            list: Matriz onde matriz[i][j] = 1 se existe arco de i para j, 0 caso contrário
        """
        matriz_adj = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for origem, destino in self.arcos:
            idx_origem = self.mapa_vertices.get(origem)
            idx_destino = self.mapa_vertices.get(destino)
            if idx_origem is not None and idx_destino is not None:
                matriz_adj[idx_origem][idx_destino] = 1
        return matriz_adj

    def criar_matriz_incidencia(self):
        """
        Cria e retorna a matriz de incidência do dígrafo.
        
        Na matriz de incidência de um dígrafo:
        - Valor +1 indica que o vértice é a origem do arco
        - Valor -1 indica que o vértice é o destino do arco
        - Valor 0 indica que o vértice não participa do arco
        
        Returns:
            list: Matriz de incidência do dígrafo
        """
        matriz_inc = [[0] * self.num_arcos for _ in range(self.num_vertices)]
        for i, (origem, destino) in enumerate(self.arcos):
            idx_origem = self.mapa_vertices.get(origem)
            idx_destino = self.mapa_vertices.get(destino)
            if idx_origem is not None:
                matriz_inc[idx_origem][i] = 1
            if idx_destino is not None:
                matriz_inc[idx_destino][i] = -1
        return matriz_inc

    # =========================================================================
    # BUSCA EM LARGURA (BFS) PARA DÍGRAFOS
    # =========================================================================
    
    def busca_em_largura(self, vertice_inicial):
        """
        Realiza uma Busca em Largura (BFS) a partir de um vértice inicial em um dígrafo.
        
        A BFS em dígrafos segue apenas os arcos na direção correta (origem -> destino).
        Explora o dígrafo em camadas: primeiro visita todos os vértices alcançáveis
        diretamente do vértice inicial, depois os alcançáveis a partir desses, e assim por diante.
        
        Args:
            vertice_inicial (str): Vértice de onde a busca deve começar
            
        Returns:
            dict: Dicionário contendo:
                - 'ordem_visitacao': Lista com a ordem em que os vértices foram visitados
                - 'distancias': Dicionário com a distância (em arcos) de cada vértice ao inicial
                - 'pais': Dicionário com o vértice pai de cada vértice na árvore BFS
                - 'alcancaveis': Conjunto de vértices alcançáveis a partir do inicial
                
        Raises:
            ValueError: Se o vértice inicial não existir no dígrafo
        """
        if vertice_inicial not in self.vertices_ordenados:
            raise ValueError(f"O vértice '{vertice_inicial}' não existe no dígrafo.")
        
        lista_adj = self.criar_lista_adjacencia()
        
        visitados = set()
        fila = [vertice_inicial]
        ordem_visitacao = []
        distancias = {vertice_inicial: 0}
        pais = {vertice_inicial: None}
        
        while fila:
            vertice_atual = fila.pop(0)
            
            if vertice_atual in visitados:
                continue
            
            visitados.add(vertice_atual)
            ordem_visitacao.append(vertice_atual)
            
            for vizinho in sorted(lista_adj[vertice_atual]):
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    distancias[vizinho] = distancias[vertice_atual] + 1
                    pais[vizinho] = vertice_atual
        
        return {
            'ordem_visitacao': ordem_visitacao,
            'distancias': distancias,
            'pais': pais,
            'alcancaveis': visitados
        }
