"""
Trabalho 01 - Grafos

Testes para validar as implementações de:
- Item 9: Inclusão de vértice
- Item 10: Exclusão de vértice  
- Item 13: Busca em Largura (BFS) em grafos
- Item 19: Busca em Largura (BFS) em dígrafos
"""

from grafo import Grafo
from digrafo import Digrafo


# ==============================================================================
# TESTES ITEM 9 - INCLUSÃO DE VÉRTICE
# ==============================================================================

def teste_item_9_lista_adjacencia_basico():
    print("\n" + "="*80)
    print("TESTE 9.1 - Inclusão de vértice em lista de adjacências (caso básico)")
    print("="*80)
    
    #   ANTES:               DEPOIS :
    #   a---b---c            a---b---c
    #                        
    #                        d (sozinho)
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    print(f"\nLista original: {lista_adj}")
    
    nova_lista = grafo.incluir_vertice_lista_adjacencia(lista_adj, 'd')
    print(f"Após adicionar 'd': {nova_lista}")
    
    assert 'd' in nova_lista, "Vértice 'd' não foi adicionado"
    assert nova_lista['d'] == [], "Novo vértice deveria estar sem conexões"
    assert len(nova_lista) == 4, "Deveria ter 4 vértices"
    
    print("✅ Teste passou!")


def teste_item_9_matriz_adjacencia_basico():
    print("\n" + "="*80)
    print("TESTE 9.2 - Inclusão de vértice em matriz de adjacências")
    print("="*80)
    
    #     ANTES:              DEPOIS
    #   a---b---c            a---b---c
    #                        
    #                        d (sozinho)
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    matriz_adj = grafo.criar_matriz_adjacencia()
    print(f"\nMatriz original (3x3):")
    for i, v in enumerate(grafo.vertices_ordenados):
        print(f"  {v}: {matriz_adj[i]}")
    
    nova_matriz, novos_vertices, novo_mapa = grafo.incluir_vertice_matriz_adjacencia(matriz_adj, 'd')
    
    print(f"\nMatriz após adicionar 'd' (4x4):")
    for i, v in enumerate(novos_vertices):
        print(f"  {v}: {nova_matriz[i]}")
    
    assert len(nova_matriz) == 4, "Matriz deveria ter 4 linhas"
    assert len(nova_matriz[0]) == 4, "Matriz deveria ter 4 colunas"
    assert novos_vertices == ['a', 'b', 'c', 'd'], "Vértices deveriam estar ordenados"
    
    # Verifica que nova linha e coluna estão zeradas
    for i in range(4):
        assert nova_matriz[3][i] == 0, "Nova linha deveria estar zerada"
        assert nova_matriz[i][3] == 0, "Nova coluna deveria estar zerada"
    
    print("✅ Teste passou!")


def teste_item_9_vertice_duplicado():
    print("\n" + "="*80)
    print("TESTE 9.3 - Tentativa de adicionar vértice duplicado (deve falhar)")
    print("="*80)
    
    # Grafo:
    #   a---b
    # já tem 'a'
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.incluir_vertice_lista_adjacencia(lista_adj, 'a')  # 'a' já existe
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada corretamente: {e}")


def teste_item_9_grafo_vazio():
    print("\n" + "="*80)
    print("TESTE 9.4 - Inclusão em grafo vazio")
    print("="*80)
    
    # Grafo ANTES:        Grafo DEPOIS de incluir 'x':
    #   (vazio)              x (sozinho)
    vertices = set()
    arestas = []
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    nova_lista = grafo.incluir_vertice_lista_adjacencia(lista_adj, 'x')
    
    assert len(nova_lista) == 1, "Deveria ter 1 vértice"
    assert 'x' in nova_lista, "Vértice 'x' deveria estar presente"
    
    print("✅ Teste passou!")


def teste_item_9_lista_adjacencia_com_arestas():
    print("\n" + "="*80)
    print("TESTE 9.5 - Inclusão de vértice com arestas em lista de adjacências")
    print("="*80)
    
    #   ANTES:               DEPOIS:
    #   a---b---c            a---b---c
    #                        |       |
    #                        +---d---+
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    print(f"\nLista original: {lista_adj}")
    
    # Adiciona 'd' com arestas para 'a' e 'c'
    nova_lista = grafo.incluir_vertice_lista_adjacencia(
        lista_adj, 'd', [('d', 'a'), ('d', 'c')]
    )
    print(f"Após adicionar 'd' com arestas: {nova_lista}")
    
    assert 'd' in nova_lista, "Vértice 'd' não foi adicionado"
    assert 'a' in nova_lista['d'], "'a' deveria estar conectado a 'd'"
    assert 'c' in nova_lista['d'], "'c' deveria estar conectado a 'd'"
    assert 'd' in nova_lista['a'], "'d' deveria estar na lista de 'a'"
    assert 'd' in nova_lista['c'], "'d' deveria estar na lista de 'c'"
    assert len(nova_lista) == 4, "Deveria ter 4 vértices"
    
    print("✅ Teste passou!")


def teste_item_9_matriz_adjacencia_com_arestas():
    print("\n" + "="*80)
    print("TESTE 9.6 - Inclusão de vértice com arestas em matriz de adjacências")
    print("="*80)
    
    # Grafo ANTES:        Grafo DEPOIS de incluir 'd' com aresta (d,b):
    #   a---b---c            a---b---c
    #                            |
    #                            d
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    matriz_adj = grafo.criar_matriz_adjacencia()
    
    # Adiciona 'd' com aresta para 'b'
    nova_matriz, novos_vertices, novo_mapa = grafo.incluir_vertice_matriz_adjacencia(
        matriz_adj, 'd', [('d', 'b')]
    )
    
    print(f"\nMatriz após adicionar 'd' com aresta para 'b':")
    for i, v in enumerate(novos_vertices):
        print(f"  {v}: {nova_matriz[i]}")
    
    assert len(nova_matriz) == 4, "Matriz deveria ter 4 linhas"
    assert novos_vertices == ['a', 'b', 'c', 'd'], "Vértices deveriam estar ordenados"
    
    # Verifica conexão entre 'd' e 'b'
    idx_d = novo_mapa['d']
    idx_b = novo_mapa['b']
    assert nova_matriz[idx_d][idx_b] == 1, "'d' deveria estar conectado a 'b'"
    assert nova_matriz[idx_b][idx_d] == 1, "'b' deveria estar conectado a 'd'"
    
    print("✅ Teste passou!")


def teste_item_9_aresta_vertice_inexistente():
    print("\n" + "="*80)
    print("TESTE 9.7 - Tentativa de adicionar aresta para vértice inexistente (deve falhar)")
    print("="*80)
    
    # Grafo:
    #   a---b
    # 
    # Tentativa: incluir 'c' com aresta para 'z' (que não existe)
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.incluir_vertice_lista_adjacencia(lista_adj, 'c', [('c', 'z')])
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada corretamente: {e}")


def teste_item_9_aresta_sem_novo_vertice():
    print("\n" + "="*80)
    print("TESTE 9.8 - Tentativa de adicionar aresta que não envolve o novo vértice (deve falhar)")
    print("="*80)
    
    # Grafo:
    #   a---b
    # 
    # Tentativa: incluir 'c' mas passar aresta (a,b) que não envolve 'c'
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.incluir_vertice_lista_adjacencia(lista_adj, 'c', [('a', 'b')])
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada corretamente: {e}")


def teste_item_9_incluir_vertice_no_grafo():
    print("\n" + "="*80)
    print("TESTE 9.9 - Inclusão de vértice diretamente no grafo")
    print("="*80)
    
    # Grafo ANTES:        Grafo DEPOIS de incluir 'd' com aresta (d,b):
    #   a---b---c            a---b---c
    #                            |
    #                            d
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    print(f"\nGrafo original:")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    # Adiciona 'd' diretamente no grafo
    grafo.incluir_vertice('d', [('d', 'b')])
    
    print(f"\nGrafo após incluir 'd':")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    assert 'd' in grafo.vertices_ordenados, "'d' deveria estar nos vértices"
    assert grafo.num_vertices == 4, "Deveria ter 4 vértices"
    assert ('b', 'd') in grafo.arestas or ('d', 'b') in grafo.arestas, "Aresta (d,b) deveria existir"
    assert grafo.num_arestas == 3, "Deveria ter 3 arestas"
    
    print("✅ Teste passou!")


def teste_item_9_incluir_vertice_isolado_no_grafo():
    print("\n" + "="*80)
    print("TESTE 9.10 - Inclusão de vértice isolado diretamente no grafo")
    print("="*80)
    
    # Grafo ANTES:        Grafo DEPOIS de incluir 'd' isolado:
    #   a---b---c            a---b---c
    #                        
    #                        d (isolado)
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    # Adiciona 'd' sem arestas
    grafo.incluir_vertice('d')
    
    assert 'd' in grafo.vertices_ordenados, "'d' deveria estar nos vértices"
    assert grafo.num_vertices == 4, "Deveria ter 4 vértices"
    assert grafo.num_arestas == 2, "Número de arestas não deveria mudar"
    
    print("✅ Teste passou!")


# ==============================================================================
# TESTES ITEM 10 - EXCLUSÃO DE VÉRTICE
# ==============================================================================

def teste_item_10_lista_adjacencia_basico():
    print("\n" + "="*80)
    print("TESTE 10.1 - Exclusão de vértice em lista de adjacências")
    print("="*80)
    
    #    ANTES (quadrado):          DEPOIS:
    #   a---b                       a       c
    #   |   |                       |       |
    #   d---c                       d-------c
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    print(f"\nLista original:")
    for v, viz in lista_adj.items():
        print(f"  {v}: {viz}")
    
    nova_lista = grafo.excluir_vertice_lista_adjacencia(lista_adj, 'b')
    
    print(f"\nApós remover 'b':")
    for v, viz in nova_lista.items():
        print(f"  {v}: {viz}")
    
    assert 'b' not in nova_lista, "Vértice 'b' ainda está na lista"
    assert 'b' not in nova_lista['a'], "'b' ainda está na lista de 'a'"
    assert 'b' not in nova_lista['c'], "'b' ainda está na lista de 'c'"
    assert len(nova_lista) == 3, "Deveria ter 3 vértices"
    
    print("✅ Teste passou!")


def teste_item_10_matriz_adjacencia_basico():
    print("\n" + "="*80)
    print("TESTE 10.2 - Exclusão de vértice em matriz de adjacências")
    print("="*80)
    
    # ANTES:                        DEPOIS :
    #   a---b                       a       c
    #   |   |                       |       |
    #   d---c                       d-------c
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    matriz_adj = grafo.criar_matriz_adjacencia()
    print(f"\nMatriz original (4x4):")
    for i, v in enumerate(grafo.vertices_ordenados):
        print(f"  {v}: {matriz_adj[i]}")
    
    nova_matriz, novos_vertices, novo_mapa = grafo.excluir_vertice_matriz_adjacencia(matriz_adj, 'b')
    
    print(f"\nMatriz após remover 'b' (3x3):")
    for i, v in enumerate(novos_vertices):
        print(f"  {v}: {nova_matriz[i]}")
    
    assert len(nova_matriz) == 3, "Matriz deveria ter 3 linhas"
    assert len(nova_matriz[0]) == 3, "Matriz deveria ter 3 colunas"
    assert 'b' not in novos_vertices, "Vértice 'b' ainda está na lista"
    
    print("✅ Teste passou!")


def teste_item_10_vertice_inexistente():
    print("\n" + "="*80)
    print("TESTE 10.3 - Tentativa de remover vértice inexistente (deve falhar)")
    print("="*80)
    
    # Grafo:
    #   a---b
    # (não tem 'z')
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    
    try:
        grafo.excluir_vertice_lista_adjacencia(lista_adj, 'z')  # 'z' não existe
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada corretamente: {e}")


def teste_item_10_vertice_central():
    print("\n" + "="*80)
    print("TESTE 10.4 - Exclusão de vértice central (hub)")
    print("="*80)
    
    #   ANTES (estrela):           DEPOIS (ilhas)
    #       a                        a  c  d  e
    #       |                        (todos isolados)
    #   e---b---c
    #       |
    #       d
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('b', 'a'), ('b', 'c'), ('b', 'd'), ('b', 'e')]
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    nova_lista = grafo.excluir_vertice_lista_adjacencia(lista_adj, 'b')
    
    # Após remover 'b', todos os vértices ficam isolados
    for v in ['a', 'c', 'd', 'e']:
        assert nova_lista[v] == [], f"Vértice {v} deveria estar isolado"
    
    print("✅ Teste passou!")


def teste_item_10_ultimo_vertice():
    print("\n" + "="*80)
    print("TESTE 10.5 - Exclusão do último vértice")
    print("="*80)
    
    #   ANTES:               DEPOIS:
    #   a (sozinho)          (vazio)
    vertices = {'a'}
    arestas = []
    grafo = Grafo(vertices, arestas)
    
    lista_adj = grafo.criar_lista_adjacencia()
    nova_lista = grafo.excluir_vertice_lista_adjacencia(lista_adj, 'a')
    
    assert len(nova_lista) == 0, "Lista deveria estar vazia"
    
    print("✅ Teste passou!")


def teste_item_10_excluir_vertice_do_grafo():
    print("\n" + "="*80)
    print("TESTE 10.6 - Exclusão de vértice diretamente do grafo")
    print("="*80)
    
    # Grafo ANTES:        Grafo DEPOIS de excluir 'b':
    #   a---b---c            a       c
    #                        (isolados)
    vertices = {'a', 'b', 'c'}
    arestas = [('a', 'b'), ('b', 'c')]
    grafo = Grafo(vertices, arestas)
    
    print(f"\nGrafo original:")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    # Remove 'b' diretamente do grafo
    grafo.excluir_vertice('b')
    
    print(f"\nGrafo após excluir 'b':")
    print(f"  Vértices: {grafo.vertices_ordenados}")
    print(f"  Arestas: {grafo.arestas}")
    
    assert 'b' not in grafo.vertices_ordenados, "'b' não deveria estar nos vértices"
    assert grafo.num_vertices == 2, "Deveria ter 2 vértices"
    assert grafo.num_arestas == 0, "Não deveria ter arestas (b conectava a e c)"
    
    print("✅ Teste passou!")


def teste_item_10_excluir_vertice_central_do_grafo():
    print("\n" + "="*80)
    print("TESTE 10.7 - Exclusão de vértice central diretamente do grafo")
    print("="*80)
    
    # Grafo ANTES (estrela):     Grafo DEPOIS de excluir 'b':
    #       a                        a  c  d  e
    #       |                        (todos isolados)
    #   e---b---c
    #       |
    #       d
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('b', 'a'), ('b', 'c'), ('b', 'd'), ('b', 'e')]
    grafo = Grafo(vertices, arestas)
    
    grafo.excluir_vertice('b')
    
    assert 'b' not in grafo.vertices_ordenados, "'b' não deveria estar nos vértices"
    assert grafo.num_vertices == 4, "Deveria ter 4 vértices"
    assert grafo.num_arestas == 0, "Não deveria ter arestas (todas conectavam a b)"
    
    # Verifica que os vértices restantes estão isolados
    lista_adj = grafo.criar_lista_adjacencia()
    for v in ['a', 'c', 'd', 'e']:
        assert lista_adj[v] == [], f"Vértice {v} deveria estar isolado"
    
    print("✅ Teste passou!")


def teste_item_10_excluir_vertice_com_arestas_parciais():
    print("\n" + "="*80)
    print("TESTE 10.8 - Exclusão de vértice mantém outras arestas")
    print("="*80)
    
    # Grafo ANTES:        Grafo DEPOIS de excluir 'c':
    #   a---b---c            a---b
    #   |       |            |
    #   +---d---+            +---d
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    grafo.excluir_vertice('c')
    
    assert 'c' not in grafo.vertices_ordenados
    assert grafo.num_vertices == 3
    # Apenas as arestas que conectavam a 'c' foram removidas
    # Restam: (a,b) e (d,a)
    assert grafo.num_arestas == 2
    
    # Verifica que as arestas corretas foram mantidas
    arestas_normalizadas = [tuple(sorted(a)) for a in grafo.arestas]
    assert ('a', 'b') in arestas_normalizadas
    assert ('a', 'd') in arestas_normalizadas
    assert ('b', 'c') not in arestas_normalizadas
    assert ('c', 'd') not in arestas_normalizadas
    
    print("✅ Teste passou!")


# ==============================================================================
# TESTES ITEM 13 - BUSCA EM LARGURA (BFS) EM GRAFOS
# ==============================================================================

def teste_item_13_bfs_arvore():
    print("\n" + "="*80)
    print("TESTE 13.1 - BFS em árvore")
    print("="*80)
    
    #       a
    #      / \
    #     b   c
    #    / \
    #   d   e
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_largura('a')
    
    print(f"\nOrdem de visitação: {resultado['ordem_visitacao']}")
    print(f"Distâncias: {resultado['distancias']}")
    print(f"Pais: {resultado['pais']}")
    
    # BFS deve visitar por níveis: a (nível 0), b e c (nível 1), d e e (nível 2)
    assert resultado['ordem_visitacao'][0] == 'a', "Primeiro deve ser 'a'"
    assert resultado['distancias']['a'] == 0, "Distância de 'a' deve ser 0"
    assert resultado['distancias']['b'] == 1, "Distância de 'b' deve ser 1"
    assert resultado['distancias']['c'] == 1, "Distância de 'c' deve ser 1"
    assert resultado['distancias']['d'] == 2, "Distância de 'd' deve ser 2"
    assert resultado['distancias']['e'] == 2, "Distância de 'e' deve ser 2"
    assert resultado['pais']['a'] is None, "'a' não tem pai"
    assert resultado['pais']['b'] == 'a', "Pai de 'b' deve ser 'a'"
    
    print("✅ Teste passou!")


def teste_item_13_bfs_caminho_mais_curto():
    print("\n" + "="*80)
    print("TESTE 13.2 - BFS encontra caminho mais curto")
    print("="*80)
    
    # Grafo com dois caminhos de 'a' até 'd':
    #   a---b---c---d
    #   |           |
    #   +-----------+
    # 
    # BFS de 'a': Caminho 1: a->b->c->d (3 arestas)
    #             Caminho 2: a->d (1 aresta) ← BFS escolhe este!
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_largura('a')
    
    # BFS deve encontrar caminho direto a -> d
    assert resultado['distancias']['d'] == 1, "Distância até 'd' deve ser 1 (caminho direto)"
    assert resultado['pais']['d'] == 'a', "Pai de 'd' deve ser 'a' (caminho direto)"
    
    print("✅ Teste passou!")


def teste_item_13_bfs_grafo_desconexo():
    print("\n" + "="*80)
    print("TESTE 13.3 - BFS em grafo desconexo")
    print("="*80)
    
    # Grafo com 2 componentes desconexas:
    #   Componente 1: a---b---c
    #   
    #   Componente 2: d---e  (separada, sem ligação)
    # 
    # BFS de 'a': alcança apenas {a, b, c}
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('a', 'b'), ('b', 'c'), ('d', 'e')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_largura('a')
    
    print(f"\nAlcançáveis de 'a': {resultado['alcancaveis']}")
    
    # De 'a', só alcançamos a, b, c
    assert 'a' in resultado['alcancaveis']
    assert 'b' in resultado['alcancaveis']
    assert 'c' in resultado['alcancaveis']
    assert 'd' not in resultado['alcancaveis'], "'d' não deveria ser alcançável"
    assert 'e' not in resultado['alcancaveis'], "'e' não deveria ser alcançável"
    
    print("✅ Teste passou!")


def teste_item_13_bfs_grafo_completo():
    print("\n" + "="*80)
    print("TESTE 13.4 - BFS em grafo completo")
    print("="*80)
    
    # Grafo completo K4:
    #   a---b
    #   |\ /|
    #   | X |
    #   |/ \|
    #   d---c
    # 
    # BFS de 'a': todos os outros vértices estão a distância 1
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [
        ('a', 'b'), ('a', 'c'), ('a', 'd'),
        ('b', 'c'), ('b', 'd'),
        ('c', 'd')
    ]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_largura('a')
    
    # Em grafo completo, todos os outros vértices estão a distância 1
    for v in ['b', 'c', 'd']:
        assert resultado['distancias'][v] == 1, f"Distância até '{v}' deve ser 1"
    
    print("✅ Teste passou!")


def teste_item_13_bfs_ciclo():
    print("\n" + "="*80)
    print("TESTE 13.5 - BFS em grafo com ciclo")
    print("="*80)
    
    # Grafo cíclico:
    #   a---b
    #   |   |
    #   d---c
    # 
    # BFS de 'a': visita cada vértice exatamente uma vez
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_largura('a')
    
    # Cada vértice deve aparecer exatamente uma vez
    assert len(resultado['ordem_visitacao']) == 4, "Deve visitar 4 vértices"
    assert len(set(resultado['ordem_visitacao'])) == 4, "Nenhum vértice deve ser visitado duas vezes"
    
    print("✅ Teste passou!")


def teste_item_13_bfs_vertice_isolado():
    print("\n" + "="*80)
    print("TESTE 13.6 - BFS de vértice isolado")
    print("="*80)
    
    # Grafo:
    #   a  (isolado)
    #   
    #   b---c
    # 
    # BFS de 'a': alcança apenas {a}
    vertices = {'a', 'b', 'c'}
    arestas = [('b', 'c')]  # 'a' está isolado
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_largura('a')
    
    assert len(resultado['alcancaveis']) == 1, "Só deve alcançar 'a'"
    assert 'a' in resultado['alcancaveis'], "Deve alcançar 'a'"
    
    print("✅ Teste passou!")


def teste_item_13_bfs_vertice_inexistente():
    print("\n" + "="*80)
    print("TESTE 13.7 - BFS de vértice inexistente (deve falhar)")
    print("="*80)
    
    # Grafo:
    #   a---b
    # 
    # Tentativa: BFS de 'z' (não existe - deve gerar erro)
    vertices = {'a', 'b'}
    arestas = [('a', 'b')]
    grafo = Grafo(vertices, arestas)
    
    try:
        grafo.busca_em_largura('z')  # 'z' não existe
        assert False, "Deveria ter lançado ValueError"
    except ValueError as e:
        print(f"✅ Exceção capturada corretamente: {e}")


# ==============================================================================
# TESTES ITEM 19 - BUSCA EM LARGURA (BFS) EM DÍGRAFOS
# ==============================================================================

def teste_item_19_bfs_digrafo_simples():
    print("\n" + "="*80)
    print("TESTE 19.1 - BFS em dígrafo simples")
    print("="*80)
    
    # Dígrafo (arcos direcionados):
    #   a → b → c
    # 
    # BFS de 'a': alcança {a, b, c}
    # BFS de 'c': alcança apenas {c} (sem arcos saindo)
    vertices = {'a', 'b', 'c'}
    arcos = [('a', 'b'), ('b', 'c')]
    digrafo = Digrafo(vertices, arcos)
    
    resultado = digrafo.busca_em_largura('a')
    
    print(f"\nOrdem de visitação: {resultado['ordem_visitacao']}")
    
    # De 'a', alcançamos todos seguindo os arcos
    assert 'a' in resultado['alcancaveis']
    assert 'b' in resultado['alcancaveis']
    assert 'c' in resultado['alcancaveis']
    
    # Agora de 'c', não alcançamos ninguém (arcos vão para 'c', não saem dele)
    resultado_c = digrafo.busca_em_largura('c')
    assert len(resultado_c['alcancaveis']) == 1, "De 'c' só alcançamos 'c'"
    
    print("✅ Teste passou!")


def teste_item_19_bfs_digrafo_ciclo():
    print("\n" + "="*80)
    print("TESTE 19.2 - BFS em dígrafo com ciclo")
    print("="*80)
    
    # Dígrafo cíclico:
    #   a → b
    #   ↑   ↓
    #   c ←-+
    # 
    # BFS de qualquer vértice: alcança todos {a, b, c}
    vertices = {'a', 'b', 'c'}
    arcos = [('a', 'b'), ('b', 'c'), ('c', 'a')]
    digrafo = Digrafo(vertices, arcos)
    
    resultado = digrafo.busca_em_largura('a')
    
    # De qualquer vértice do ciclo, alcançamos todos
    assert len(resultado['alcancaveis']) == 3, "Deve alcançar todos os 3 vértices"
    
    print("✅ Teste passou!")


def teste_item_19_bfs_digrafo_nao_fortemente_conexo():
    print("\n" + "="*80)
    print("TESTE 19.3 - BFS em dígrafo não fortemente conexo")
    print("="*80)
    
    # Dígrafo:
    #   a → b → c
    #   ↑
    #   d
    # 
    # BFS de 'a': alcança {a, b, c} (não alcança 'd')
    # BFS de 'd': alcança {d, a, b, c} (todos)
    vertices = {'a', 'b', 'c', 'd'}
    arcos = [('a', 'b'), ('b', 'c'), ('d', 'a')]
    digrafo = Digrafo(vertices, arcos)
    
    # De 'a', não alcançamos 'd' (arco vai de d para a, não de a para d)
    resultado_a = digrafo.busca_em_largura('a')
    assert 'd' not in resultado_a['alcancaveis'], "De 'a' não alcançamos 'd'"
    
    # De 'd', alcançamos todos (d → a → b → c)
    resultado_d = digrafo.busca_em_largura('d')
    assert len(resultado_d['alcancaveis']) == 4, "De 'd' alcançamos todos"
    
    print("✅ Teste passou!")


def teste_item_19_bfs_digrafo_fonte_e_sumidouro():
    print("\n" + "="*80)
    print("TESTE 19.4 - BFS com fonte e sumidouro")
    print("="*80)
    
    # Dígrafo:
    #   a (fonte) → b → c (sumidouro)
    # 
    # BFS de 'a' (fonte): alcança {a, b, c}
    # BFS de 'c' (sumidouro): alcança apenas {c}
    vertices = {'a', 'b', 'c'}
    arcos = [('a', 'b'), ('b', 'c')]
    digrafo = Digrafo(vertices, arcos)
    
    # De 'a' (fonte), alcançamos todos
    resultado_fonte = digrafo.busca_em_largura('a')
    assert len(resultado_fonte['alcancaveis']) == 3, "De fonte alcançamos todos"
    
    # De 'c' (sumidouro), só alcançamos 'c'
    resultado_sumidouro = digrafo.busca_em_largura('c')
    assert len(resultado_sumidouro['alcancaveis']) == 1, "De sumidouro só alcançamos ele mesmo"
    
    print("✅ Teste passou!")


def teste_item_19_bfs_digrafo_componentes_separadas():
    print("\n" + "="*80)
    print("TESTE 19.5 - BFS em dígrafo com componentes separadas")
    print("="*80)
    
    # Dígrafo com 2 componentes desconexas:
    #   Componente 1: a → b
    #   
    #   Componente 2: c → d  (desconectada)
    # 
    # BFS de 'a': alcança apenas {a, b}
    vertices = {'a', 'b', 'c', 'd'}
    arcos = [('a', 'b'), ('c', 'd')]
    digrafo = Digrafo(vertices, arcos)
    
    resultado = digrafo.busca_em_largura('a')
    
    # De 'a', só alcançamos componente 1
    assert 'a' in resultado['alcancaveis']
    assert 'b' in resultado['alcancaveis']
    assert 'c' not in resultado['alcancaveis']
    assert 'd' not in resultado['alcancaveis']
    
    print("✅ Teste passou!")


def teste_item_19_comparacao_grafo_vs_digrafo():
    print("\n" + "="*80)
    print("TESTE 19.6 - Comparação: Grafo vs Dígrafo")
    print("="*80)
    
    # GRAFO (não-direcionado):    DÍGRAFO (direcionado):
    #   a---b---c                    a → b → c
    # 
    # BFS de 'c' no GRAFO: alcança {a, b, c} (arestas bidirecionais)
    # BFS de 'c' no DÍGRAFO: alcança apenas {c} (sem arcos saindo de 'c')
    vertices = {'a', 'b', 'c'}
    conexoes = [('a', 'b'), ('b', 'c')]
    
    # Grafo não-direcionado
    grafo = Grafo(vertices, conexoes)
    resultado_grafo = grafo.busca_em_largura('c')
    
    # Dígrafo direcionado
    digrafo = Digrafo(vertices, conexoes)
    resultado_digrafo = digrafo.busca_em_largura('c')
    
    print(f"\nGrafo - Alcançáveis de 'c': {resultado_grafo['alcancaveis']}")
    print(f"Dígrafo - Alcançáveis de 'c': {resultado_digrafo['alcancaveis']}")
    
    # Em grafo, de 'c' alcançamos todos (arestas bidirecionais)
    assert len(resultado_grafo['alcancaveis']) == 3, "Grafo: de 'c' alcançamos todos"
    
    # Em dígrafo, de 'c' só alcançamos 'c' (não há arcos saindo de 'c')
    assert len(resultado_digrafo['alcancaveis']) == 1, "Dígrafo: de 'c' só alcançamos 'c'"
    
    print("✅ Teste passou!")


# ==============================================================================
# FUNÇÃO PRINCIPAL - EXECUTA TODOS OS TESTES
# ==============================================================================

def executar_todos_os_testes():
    """
    Executa todos os testes implementados.
    """
    print("\n" + "="*80)
    print("INICIANDO BATERIA DE TESTES DE BFS E INCLUSÃO/EXCLUSÃO DE VÉRTICES")
    print("Itens: 9, 10, 13, 19")
    print("="*80)
    
    # Testes Item 9 - Inclusão de vértice
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
    
    # Testes Item 10 - Exclusão de vértice
    teste_item_10_lista_adjacencia_basico()
    teste_item_10_matriz_adjacencia_basico()
    teste_item_10_vertice_inexistente()
    teste_item_10_vertice_central()
    teste_item_10_ultimo_vertice()
    teste_item_10_excluir_vertice_do_grafo()
    teste_item_10_excluir_vertice_central_do_grafo()
    teste_item_10_excluir_vertice_com_arestas_parciais()
    
    # Testes Item 13 - BFS em grafos
    teste_item_13_bfs_arvore()
    teste_item_13_bfs_caminho_mais_curto()
    teste_item_13_bfs_grafo_desconexo()
    teste_item_13_bfs_grafo_completo()
    teste_item_13_bfs_ciclo()
    teste_item_13_bfs_vertice_isolado()
    teste_item_13_bfs_vertice_inexistente()
    
    # Testes Item 19 - BFS em dígrafos
    teste_item_19_bfs_digrafo_simples()
    teste_item_19_bfs_digrafo_ciclo()
    teste_item_19_bfs_digrafo_nao_fortemente_conexo()
    teste_item_19_bfs_digrafo_fonte_e_sumidouro()
    teste_item_19_bfs_digrafo_componentes_separadas()
    teste_item_19_comparacao_grafo_vs_digrafo()
    
    print("\n" + "="*80)
    print("FIM DA BATERIA DE TESTES DE BFS E INCLUSÃO/EXCLUSÃO DE VÉRTICES")
    print("="*80)


if __name__ == "__main__":
    executar_todos_os_testes()
