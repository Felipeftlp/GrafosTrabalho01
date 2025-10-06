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

    def is_adjacente(
            self,
            v1: str,
            v2: str
    ) -> bool:
        """
        Item 6 - Verifica se os vertices são adjacentes.
        """
        for aresta in self.arestas:
            if v1 in aresta and v2 in aresta:
                return True
        return False

    def get_num_vertices(self) -> int:
        """
        Item 7 - Retorna o total de vértices
        """
        return self.num_vertices

    def get_num_arestas(self) -> int:
        """
        Item 8 - Retorna o total de arestas
        """
        return self.num_arestas

    # =========================================================================
    # ITEM 9 - INCLUSÃO DE VÉRTICE
    # =========================================================================
    
    def incluir_vertice_lista_adjacencia(self, lista_adj, novo_vertice):
        """
        Inclui um novo vértice na representação de lista de adjacências.
        
        Args:
            lista_adj (dict): Lista de adjacências atual do grafo
            novo_vertice (str): Identificador do novo vértice a ser adicionado
            
        Returns:
            dict: Nova lista de adjacências com o vértice incluído
            
        Raises:
            ValueError: Se o vértice já existir na lista de adjacências
        """
        if novo_vertice in lista_adj:
            raise ValueError(f"O vértice '{novo_vertice}' já existe no grafo.")
        
        nova_lista = lista_adj.copy()
        nova_lista[novo_vertice] = []
        return nova_lista

    def incluir_vertice_matriz_adjacencia(self, matriz_adj, novo_vertice):
        """
        Inclui um novo vértice na representação de matriz de adjacências.
        
        Args:
            matriz_adj (list): Matriz de adjacências atual do grafo (lista de listas)
            novo_vertice (str): Identificador do novo vértice a ser adicionado
            
        Returns:
            tuple: (nova_matriz, novos_vertices_ordenados, novo_mapa_vertices)
                - nova_matriz: Matriz de adjacências expandida
                - novos_vertices_ordenados: Lista atualizada de vértices
                - novo_mapa_vertices: Dicionário atualizado de mapeamento
                
        Raises:
            ValueError: Se o vértice já existir no grafo
        """
        if novo_vertice in self.mapa_vertices:
            raise ValueError(f"O vértice '{novo_vertice}' já existe no grafo.")
        
        novos_vertices = sorted(self.vertices_ordenados + [novo_vertice])
        novo_mapa = {v: i for i, v in enumerate(novos_vertices)}
        novo_tamanho = len(novos_vertices)
        
        nova_matriz = [[0] * novo_tamanho for _ in range(novo_tamanho)]
        
        for i, v_orig in enumerate(self.vertices_ordenados):
            for j, v_dest in enumerate(self.vertices_ordenados):
                nova_pos_i = novo_mapa[v_orig]
                nova_pos_j = novo_mapa[v_dest]
                nova_matriz[nova_pos_i][nova_pos_j] = matriz_adj[i][j]
        
        return nova_matriz, novos_vertices, novo_mapa

    # =========================================================================
    # ITEM 10 - EXCLUSÃO DE VÉRTICE
    # =========================================================================
    
    def excluir_vertice_lista_adjacencia(self, lista_adj, vertice_remover):
        """
        Exclui um vértice da representação de lista de adjacências.
        
        Args:
            lista_adj (dict): Lista de adjacências atual do grafo
            vertice_remover (str): Identificador do vértice a ser removido
            
        Returns:
            dict: Nova lista de adjacências sem o vértice e suas conexões
            
        Raises:
            ValueError: Se o vértice não existir na lista de adjacências
        """
        if vertice_remover not in lista_adj:
            raise ValueError(f"O vértice '{vertice_remover}' não existe no grafo.")
        
        nova_lista = {}
        for vertice, vizinhos in lista_adj.items():
            if vertice != vertice_remover:
                nova_lista[vertice] = [v for v in vizinhos if v != vertice_remover]
        
        return nova_lista

    def excluir_vertice_matriz_adjacencia(self, matriz_adj, vertice_remover):
        """
        Exclui um vértice da representação de matriz de adjacências.
        
        Args:
            matriz_adj (list): Matriz de adjacências atual do grafo (lista de listas)
            vertice_remover (str): Identificador do vértice a ser removido
            
        Returns:
            tuple: (nova_matriz, novos_vertices_ordenados, novo_mapa_vertices)
                - nova_matriz: Matriz de adjacências reduzida
                - novos_vertices_ordenados: Lista atualizada de vértices
                - novo_mapa_vertices: Dicionário atualizado de mapeamento
                
        Raises:
            ValueError: Se o vértice não existir no grafo
        """
        if vertice_remover not in self.mapa_vertices:
            raise ValueError(f"O vértice '{vertice_remover}' não existe no grafo.")
        
        idx_remover = self.mapa_vertices[vertice_remover]
        novos_vertices = [v for v in self.vertices_ordenados if v != vertice_remover]
        novo_mapa = {v: i for i, v in enumerate(novos_vertices)}
        novo_tamanho = len(novos_vertices)
        
        nova_matriz = [[0] * novo_tamanho for _ in range(novo_tamanho)]
        
        idx_nova_linha = 0
        for i in range(len(self.vertices_ordenados)):
            if i == idx_remover:
                continue
            idx_nova_coluna = 0
            for j in range(len(self.vertices_ordenados)):
                if j == idx_remover:
                    continue
                nova_matriz[idx_nova_linha][idx_nova_coluna] = matriz_adj[i][j]
                idx_nova_coluna += 1
            idx_nova_linha += 1
        
        return nova_matriz, novos_vertices, novo_mapa

    # =========================================================================
    # ITEM 13 - BUSCA EM LARGURA (BFS)
    # =========================================================================
    
    def busca_em_largura(self, vertice_inicial):
        """
        Realiza uma Busca em Largura (BFS) a partir de um vértice inicial.
        
        A BFS explora o grafo em camadas: primeiro visita todos os vizinhos diretos
        do vértice inicial, depois os vizinhos dos vizinhos, e assim por diante.
        
        Args:
            vertice_inicial (str): Vértice de onde a busca deve começar
            
        Returns:
            dict: Dicionário contendo:
                - 'ordem_visitacao': Lista com a ordem em que os vértices foram visitados
                - 'distancias': Dicionário com a distância (em arestas) de cada vértice ao inicial
                - 'pais': Dicionário com o vértice pai de cada vértice na árvore BFS
                - 'alcancaveis': Conjunto de vértices alcançáveis a partir do inicial
                
        Raises:
            ValueError: Se o vértice inicial não existir no grafo
        """
        if vertice_inicial not in self.vertices_ordenados:
            raise ValueError(f"O vértice '{vertice_inicial}' não existe no grafo.")
        
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
