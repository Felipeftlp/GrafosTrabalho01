"""
Testes automatizados para a classe Grafo
- Estruturas de dados básicas (lista de adjacência, matriz de adjacência, matriz de incidência)
- Operações com vértices (grau, adjacência, contagem)
- Verificação de grafo bipartido
"""

from grafo import Grafo

def imprimir_cabecalho_teste(titulo):
    """Imprime um cabeçalho formatado para os testes."""
    print("\n" + "="*80)
    print(titulo.center(80))
    print("="*80 + "\n")

def imprimir_separador_teste(titulo):
    """Imprime um separador para testes individuais."""
    print("\n" + "="*60)
    print(titulo.center(60))
    print("="*60 + "\n")

def teste_estruturas_basicas():
    """Testa as estruturas de dados básicas do grafo."""
    imprimir_separador_teste("TESTE - ESTRUTURAS BÁSICAS")
    
    # Grafo de exemplo: triângulo
    vertices = {'A', 'B', 'C'}
    arestas = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    grafo = Grafo(vertices, arestas)
    
    # Testa lista de adjacência
    lista_adj = grafo.criar_lista_adjacencia()
    print("Lista de adjacência:")
    for v in sorted(lista_adj.keys()):
        print(f"  {v}: {sorted(lista_adj[v])}")
    
    # Testa matriz de adjacência
    print("\nMatriz de adjacência:")
    matriz_adj = grafo.criar_matriz_adjacencia()
    print(f"  Vertices: {grafo.vertices_ordenados}")
    for i, linha in enumerate(matriz_adj):
        print(f"  {grafo.vertices_ordenados[i]}: {linha}")
    
    # Testa matriz de incidência
    print("\nMatriz de incidência:")
    matriz_inc = grafo.criar_matriz_incidencia()
    print(f"  Arestas: {arestas}")
    for i, linha in enumerate(matriz_inc):
        print(f"  {grafo.vertices_ordenados[i]}: {linha}")
    
    print("✅ Teste passou!")

def teste_propriedades_basicas():
    """Testa propriedades básicas do grafo."""
    imprimir_separador_teste("TESTE - PROPRIEDADES BÁSICAS")
    
    vertices = {'A', 'B', 'C', 'D'}
    arestas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C')]
    grafo = Grafo(vertices, arestas)
    
    # Testa grau dos vértices
    graus = grafo.get_grau_vertices()
    print("Grau dos vértices:")
    for v, grau in graus.items():
        print(f"  {v}: {grau}")
    
    # Testa adjacência
    print(f"\nA e B são adjacentes: {grafo.is_adjacente('A', 'B')}")
    print(f"A e D são adjacentes: {grafo.is_adjacente('A', 'D')}")
    
    # Testa contagens
    print(f"\nNúmero de vértices: {grafo.get_num_vertices()}")
    print(f"Número de arestas: {grafo.get_num_arestas()}")
    
    print("✅ Teste passou!")

def teste_grafo_bipartido():
    """Testa a verificação de grafo bipartido."""
    imprimir_separador_teste("TESTE - GRAFO BIPARTIDO")
    
    # Teste 1: Grafo bipartido simples (K2,2)
    print("Teste 1: Grafo bipartido K2,2")
    vertices1 = {'A', 'B', 'C', 'D'}
    arestas1 = [('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
    grafo1 = Grafo(vertices1, arestas1)
    
    resultado1 = grafo1.eh_bipartido()
    print(f"É bipartido: {resultado1['eh_bipartido']}")
    if resultado1['eh_bipartido']:
        print(f"Partição 1: {sorted(resultado1['particoes'][0])}")
        print(f"Partição 2: {sorted(resultado1['particoes'][1])}")
    print("✅ Teste 1 passou!")
    
    # Teste 2: Grafo não-bipartido (triângulo)
    print("\nTeste 2: Grafo não-bipartido (triângulo)")
    vertices2 = {'A', 'B', 'C'}
    arestas2 = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    grafo2 = Grafo(vertices2, arestas2)
    
    resultado2 = grafo2.eh_bipartido()
    print(f"É bipartido: {resultado2['eh_bipartido']}")
    if not resultado2['eh_bipartido']:
        print(f"Ciclo ímpar encontrado: {resultado2['ciclo_impar']}")
    print("✅ Teste 2 passou!")
    
    # Teste 3: Grafo bipartido em linha
    print("\nTeste 3: Grafo bipartido (caminho)")
    vertices3 = {'A', 'B', 'C', 'D', 'E'}
    arestas3 = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
    grafo3 = Grafo(vertices3, arestas3)
    
    resultado3 = grafo3.eh_bipartido()
    print(f"É bipartido: {resultado3['eh_bipartido']}")
    if resultado3['eh_bipartido']:
        print(f"Partição 1: {sorted(resultado3['particoes'][0])}")
        print(f"Partição 2: {sorted(resultado3['particoes'][1])}")
    print("✅ Teste 3 passou!")
    
    # Teste 4: Grafo vazio
    print("\nTeste 4: Grafo vazio")
    vertices4 = set()
    arestas4 = []
    grafo4 = Grafo(vertices4, arestas4)
    
    resultado4 = grafo4.eh_bipartido()
    print(f"É bipartido: {resultado4['eh_bipartido']}")
    print("✅ Teste 4 passou!")
    
    # Teste 5: Grafo com vértice isolado
    print("\nTeste 5: Grafo com vértice isolado")
    vertices5 = {'A', 'B', 'C', 'D'}
    arestas5 = [('A', 'B'), ('B', 'C')]  # D fica isolado
    grafo5 = Grafo(vertices5, arestas5)
    
    resultado5 = grafo5.eh_bipartido()
    print(f"É bipartido: {resultado5['eh_bipartido']}")
    if resultado5['eh_bipartido']:
        print(f"Partição 1: {sorted(resultado5['particoes'][0])}")
        print(f"Partição 2: {sorted(resultado5['particoes'][1])}")
    print("✅ Teste 5 passou!")

def teste_casos_especiais():
    """Testa casos especiais e edge cases."""
    imprimir_separador_teste("TESTE - CASOS ESPECIAIS")
    
    # Teste 1: Grafo com um vértice
    print("Teste 1: Grafo com um vértice")
    vertices1 = {'A'}
    arestas1 = []
    grafo1 = Grafo(vertices1, arestas1)
    
    resultado1 = grafo1.eh_bipartido()
    print(f"É bipartido: {resultado1['eh_bipartido']}")
    print("✅ Teste 1 passou!")
    
    # Teste 2: Grafo completo K4 (não-bipartido)
    print("\nTeste 2: Grafo completo K4")
    vertices2 = {'A', 'B', 'C', 'D'}
    arestas2 = [('A', 'B'), ('A', 'C'), ('A', 'D'), 
               ('B', 'C'), ('B', 'D'), ('C', 'D')]
    grafo2 = Grafo(vertices2, arestas2)
    
    resultado2 = grafo2.eh_bipartido()
    print(f"É bipartido: {resultado2['eh_bipartido']}")
    print("✅ Teste 2 passou!")
    
    # Teste 3: Grafo estrela (bipartido)
    print("\nTeste 3: Grafo estrela")
    vertices3 = {'A', 'B', 'C', 'D', 'E'}
    arestas3 = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')]
    grafo3 = Grafo(vertices3, arestas3)
    
    resultado3 = grafo3.eh_bipartido()
    print(f"É bipartido: {resultado3['eh_bipartido']}")
    if resultado3['eh_bipartido']:
        print(f"Partição 1: {sorted(resultado3['particoes'][0])}")
        print(f"Partição 2: {sorted(resultado3['particoes'][1])}")
    print("✅ Teste 3 passou!")

# ==============================================================================
# TESTES ITEM 9 - INCLUSÃO DE VÉRTICE
# ==============================================================================

def teste_item_9_lista_adjacencia_basico():
    imprimir_separador_teste("ITEM 9.1 - Inclusão em Lista de Adjacências (Básico)")
    
    # Grafo: a---b---c
    # Adicionar: d (isolado)
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    print(f"Lista original: {lista_adj}")
    
    nova_lista = grafo.incluir_vertice_lista_adjacencia(lista_adj, 'd')
    print(f"Após adicionar 'd': {nova_lista}")
    
    assert 'd' in nova_lista, "Vértice 'd' não foi adicionado"
    assert nova_lista['d'] == [], "Novo vértice deveria estar sem conexões"
    assert len(nova_lista) == 4, "Deveria ter 4 vértices"
    
    print("✅ Teste passou!")

def teste_item_9_matriz_adjacencia_basico():
    imprimir_separador_teste("ITEM 9.2 - Inclusão em Matriz de Adjacências (Básico)")
    
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    matriz_adj = grafo.criar_matriz_adjacencia()
    print(f"Matriz original (3x3):")
    for i, v in enumerate(grafo.vertices_ordenados):
        print(f"  {v}: {matriz_adj[i]}")
    
    nova_matriz, novos_vertices, novo_mapa = grafo.incluir_vertice_matriz_adjacencia(matriz_adj, 'd')
    
    print(f"\nMatriz após adicionar 'd' (4x4):")
    for i, v in enumerate(novos_vertices):
        print(f"  {v}: {nova_matriz[i]}")
    
    assert len(nova_matriz) == 4, "Matriz deveria ter 4 linhas"
    assert len(nova_matriz[0]) == 4, "Matriz deveria ter 4 colunas"
    assert novos_vertices == ['a', 'b', 'c', 'd'], "Vértices deveriam estar ordenados"
    
    print("✅ Teste passou!")

def teste_item_9_vertice_duplicado():
    imprimir_separador_teste("ITEM 9.3 - Vértice Duplicado (Erro Esperado)")
    
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.incluir_vertice_lista_adjacencia(lista_adj, 'a')
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada: {e}")

def teste_item_9_grafo_vazio():
    imprimir_separador_teste("ITEM 9.4 - Inclusão em Grafo Vazio")
    
    vertices = set()
    arestas = []
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    nova_lista = grafo.incluir_vertice_lista_adjacencia(lista_adj, 'x')
    
    assert len(nova_lista) == 1, "Deveria ter 1 vértice"
    assert 'x' in nova_lista, "Vértice 'x' deveria estar presente"
    
    print("✅ Teste passou!")

def teste_item_9_lista_adjacencia_com_arestas():
    imprimir_separador_teste("ITEM 9.5 - Inclusão com Arestas em Lista")
    
    # Grafo: a---b---c
    # Adicionar: d com arestas para a e c
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    print(f"Lista original: {lista_adj}")
    
    nova_lista = grafo.incluir_vertice_lista_adjacencia(
        lista_adj, 'd', [('d', 'a'), ('d', 'c')]
    )
    print(f"Após adicionar 'd' com arestas: {nova_lista}")
    
    assert 'd' in nova_lista, "Vértice 'd' não foi adicionado"
    assert 'a' in nova_lista['d'], "'a' deveria estar conectado a 'd'"
    assert 'c' in nova_lista['d'], "'c' deveria estar conectado a 'd'"
    assert 'd' in nova_lista['a'], "'d' deveria estar na lista de 'a'"
    assert 'd' in nova_lista['c'], "'d' deveria estar na lista de 'c'"
    
    print("✅ Teste passou!")

def teste_item_9_matriz_adjacencia_com_arestas():
    imprimir_separador_teste("ITEM 9.6 - Inclusão com Arestas em Matriz")
    
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    matriz_adj = grafo.criar_matriz_adjacencia()
    
    nova_matriz, novos_vertices, novo_mapa = grafo.incluir_vertice_matriz_adjacencia(
        matriz_adj, 'd', [('d', 'b')]
    )
    
    print(f"Matriz após adicionar 'd' com aresta para 'b':")
    for i, v in enumerate(novos_vertices):
        print(f"  {v}: {nova_matriz[i]}")
    
    assert len(nova_matriz) == 4, "Matriz deveria ter 4 linhas"
    
    idx_d = novo_mapa['d']
    idx_b = novo_mapa['b']
    assert nova_matriz[idx_d][idx_b] == 1, "'d' deveria estar conectado a 'b'"
    assert nova_matriz[idx_b][idx_d] == 1, "'b' deveria estar conectado a 'd'"
    
    print("✅ Teste passou!")

def teste_item_9_aresta_vertice_inexistente():
    imprimir_separador_teste("ITEM 9.7 - Aresta para Vértice Inexistente (Erro)")
    
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.incluir_vertice_lista_adjacencia(lista_adj, 'c', [('c', 'z')])
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada: {e}")

def teste_item_9_aresta_sem_novo_vertice():
    imprimir_separador_teste("ITEM 9.8 - Aresta Não Envolve Novo Vértice (Erro)")
    
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.incluir_vertice_lista_adjacencia(lista_adj, 'c', [('a', 'b')])
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada: {e}")

def teste_item_9_incluir_vertice_no_grafo():
    imprimir_separador_teste("ITEM 9.9 - Inclusão Direta no Grafo")
    
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    print(f"Grafo original:")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    grafo.incluir_vertice('d', [('d', 'b')])
    
    print(f"\nGrafo após incluir 'd':")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    assert 'd' in grafo.vertices_ordenados, "'d' deveria estar nos vértices"
    assert grafo.num_vertices == 4, "Deveria ter 4 vértices"
    assert ('b', 'd') in grafo.arestas or ('d', 'b') in grafo.arestas, "Aresta (d,b) deveria existir"
    
    print("✅ Teste passou!")

def teste_item_9_incluir_vertice_isolado_no_grafo():
    imprimir_separador_teste("ITEM 9.10 - Inclusão de Vértice Isolado no Grafo")
    
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    grafo.incluir_vertice('d')
    
    assert 'd' in grafo.vertices_ordenados, "'d' deveria estar nos vértices"
    assert grafo.num_vertices == 4, "Deveria ter 4 vértices"
    assert grafo.num_arestas == 2, "Número de arestas não deveria mudar"
    
    print("✅ Teste passou!")

# ==============================================================================
# TESTES ITEM 10 - EXCLUSÃO DE VÉRTICE
# ==============================================================================

def teste_item_10_lista_adjacencia_basico():
    imprimir_separador_teste("ITEM 10.1 - Exclusão em Lista de Adjacências")
    
    # Grafo quadrado: a---b
    #                 |   |
    #                 d---c
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    print(f"Lista original:")
    for v, viz in lista_adj.items():
        print(f"  {v}: {viz}")
    
    nova_lista = grafo.excluir_vertice_lista_adjacencia(lista_adj, 'b')
    
    print(f"\nApós remover 'b':")
    for v, viz in nova_lista.items():
        print(f"  {v}: {viz}")
    
    assert 'b' not in nova_lista, "Vértice 'b' ainda está na lista"
    assert 'b' not in nova_lista['a'], "'b' ainda está na lista de 'a'"
    assert 'b' not in nova_lista['c'], "'b' ainda está na lista de 'c'"
    
    print("✅ Teste passou!")

def teste_item_10_matriz_adjacencia_basico():
    imprimir_separador_teste("ITEM 10.2 - Exclusão em Matriz de Adjacências")
    
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    matriz_adj = grafo.criar_matriz_adjacencia()
    print(f"Matriz original (4x4):")
    for i, v in enumerate(grafo.vertices_ordenados):
        print(f"  {v}: {matriz_adj[i]}")
    
    nova_matriz, novos_vertices, novo_mapa = grafo.excluir_vertice_matriz_adjacencia(matriz_adj, 'b')
    
    print(f"\nMatriz após remover 'b' (3x3):")
    for i, v in enumerate(novos_vertices):
        print(f"  {v}: {nova_matriz[i]}")
    
    assert len(nova_matriz) == 3, "Matriz deveria ter 3 linhas"
    assert 'b' not in novos_vertices, "Vértice 'b' ainda está na lista"
    
    print("✅ Teste passou!")

def teste_item_10_vertice_inexistente():
    imprimir_separador_teste("ITEM 10.3 - Remoção de Vértice Inexistente (Erro)")
    
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.excluir_vertice_lista_adjacencia(lista_adj, 'z')
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada: {e}")

def teste_item_10_vertice_central():
    imprimir_separador_teste("ITEM 10.4 - Exclusão de Vértice Central (Hub)")
    
    # Grafo estrela com 'b' no centro
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('b', 'a'), ('b', 'c'), ('b', 'd'), ('b', 'e')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    nova_lista = grafo.excluir_vertice_lista_adjacencia(lista_adj, 'b')
    
    for v in ['a', 'c', 'd', 'e']:
        assert nova_lista[v] == [], f"Vértice {v} deveria estar isolado"
    
    print("✅ Teste passou!")

def teste_item_10_ultimo_vertice():
    imprimir_separador_teste("ITEM 10.5 - Exclusão do Último Vértice")
    
    vertices = {'a'}
    arestas = []
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    nova_lista = grafo.excluir_vertice_lista_adjacencia(lista_adj, 'a')
    
    assert len(nova_lista) == 0, "Lista deveria estar vazia"
    
    print("✅ Teste passou!")

def teste_item_10_excluir_vertice_do_grafo():
    imprimir_separador_teste("ITEM 10.6 - Exclusão Direta do Grafo")
    
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    print(f"Grafo original:")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    grafo.excluir_vertice('b')
    
    print(f"\nGrafo após excluir 'b':")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    assert 'b' not in grafo.vertices_ordenados, "'b' não deveria estar nos vértices"
    assert grafo.num_vertices == 2, "Deveria ter 2 vértices"
    assert grafo.num_arestas == 0, "Não deveria ter arestas"
    
    print("✅ Teste passou!")

def teste_item_10_excluir_vertice_central_do_grafo():
    imprimir_separador_teste("ITEM 10.7 - Exclusão de Vértice Central do Grafo")
    
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('b', 'a'), ('b', 'c'), ('b', 'd'), ('b', 'e')]
    grafo = Grafo(vertices, arestas)
    
    grafo.excluir_vertice('b')
    
    assert 'b' not in grafo.vertices_ordenados, "'b' não deveria estar nos vértices"
    assert grafo.num_vertices == 4, "Deveria ter 4 vértices"
    assert grafo.num_arestas == 0, "Não deveria ter arestas"
    
    print("✅ Teste passou!")

def teste_item_10_excluir_vertice_com_arestas_parciais():
    imprimir_separador_teste("ITEM 10.8 - Exclusão Mantém Outras Arestas")
    
    # Grafo: a---b---c
    #        |       |
    #        +---d---+
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    grafo.excluir_vertice('c')
    
    assert 'c' not in grafo.vertices_ordenados
    assert grafo.num_vertices == 3
    assert grafo.num_arestas == 2
    
    arestas_normalizadas = [tuple(sorted(a)) for a in grafo.arestas]
    assert ('a', 'b') in arestas_normalizadas
    assert ('a', 'd') in arestas_normalizadas
    
    print("✅ Teste passou!")

def executar_todos_os_testes():
    """Executa toda a bateria de testes para a classe Grafo."""
    imprimir_cabecalho_teste("BATERIA DE TESTES PARA A CLASSE GRAFO")
    
    teste_estruturas_basicas()
    teste_propriedades_basicas()
    teste_grafo_bipartido()
    teste_casos_especiais()
    
    # Testes de Inclusão de Vértices (Item 9)
    imprimir_cabecalho_teste("TESTES ITEM 9 - INCLUSÃO DE VÉRTICE")
    teste_item_9_lista_adjacencia_basico()
    teste_item_9_matriz_adjacencia_basico()
    teste_item_9_vertice_duplicado()
    teste_item_9_grafo_vazio()
    teste_item_9_lista_adjacencia_com_arestas()
    teste_item_9_matriz_adjacencia_com_arestas()
    teste_item_9_aresta_vertice_inexistente()
    teste_item_9_aresta_sem_novo_vertice()
    teste_item_9_incluir_vertice_no_grafo()
    teste_item_9_incluir_vertice_isolado_no_grafo()
    
    # Testes de Exclusão de Vértices (Item 10)
    imprimir_cabecalho_teste("TESTES ITEM 10 - EXCLUSÃO DE VÉRTICE")
    teste_item_10_lista_adjacencia_basico()
    teste_item_10_matriz_adjacencia_basico()
    teste_item_10_vertice_inexistente()
    teste_item_10_vertice_central()
    teste_item_10_ultimo_vertice()
    teste_item_10_excluir_vertice_do_grafo()
    teste_item_10_excluir_vertice_central_do_grafo()
    teste_item_10_excluir_vertice_com_arestas_parciais()
    
    imprimir_cabecalho_teste("TODOS OS TESTES DA CLASSE GRAFO FORAM CONCLUÍDOS")

if __name__ == "__main__":
    executar_todos_os_testes()