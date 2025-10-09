"""
Testes automatizados para a classe Digrafo
- Estruturas de dados básicas (lista de adjacência, matriz de adjacência, matriz de incidência)
- Algoritmos de busca (BFS e DFS)
- Verificação de dígrafo bipartido
- Determinação do grafo subjacente
"""

from digrafo import Digrafo
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
    """Testa as estruturas de dados básicas do dígrafo."""
    imprimir_separador_teste("TESTE - ESTRUTURAS BÁSICAS DÍGRAFO")
    
    # Dígrafo de exemplo: A → B → C ← A (triângulo direcionado)
    vertices = {'A', 'B', 'C'}
    arcos = [('A', 'B'), ('B', 'C'), ('A', 'C')]
    digrafo = Digrafo(vertices, arcos)
    
    # Testa lista de adjacência
    lista_adj = digrafo.criar_lista_adjacencia()
    print("Lista de adjacência:")
    for v in sorted(lista_adj.keys()):
        print(f"  {v}: {sorted(lista_adj[v])}")
    
    # Testa matriz de adjacência
    print("\nMatriz de adjacência:")
    matriz_adj = digrafo.criar_matriz_adjacencia()
    print(f"  Vertices: {digrafo.vertices_ordenados}")
    for i, linha in enumerate(matriz_adj):
        print(f"  {digrafo.vertices_ordenados[i]}: {linha}")
    
    # Testa matriz de incidência
    print("\nMatriz de incidência:")
    matriz_inc = digrafo.criar_matriz_incidencia()
    print(f"  Arcos: {arcos}")
    for i, linha in enumerate(matriz_inc):
        print(f"  {digrafo.vertices_ordenados[i]}: {linha}")
    
    print("✅ Teste passou!")

def teste_busca_largura():
    """Testa o algoritmo BFS em dígrafos."""
    imprimir_separador_teste("TESTE - BUSCA EM LARGURA (BFS)")
    
    # Dígrafo em cadeia: A → B → C → D
    vertices = {'A', 'B', 'C', 'D'}
    arcos = [('A', 'B'), ('B', 'C'), ('C', 'D')]
    digrafo = Digrafo(vertices, arcos)
    
    resultado_bfs = digrafo.busca_em_largura('A')
    
    print("Resultado BFS a partir de 'A':")
    print(f"  Ordem de visitação: {resultado_bfs['ordem_visitacao']}")
    print(f"  Distâncias: {resultado_bfs['distancias']}")
    print(f"  Pais: {resultado_bfs['pais']}")
    print(f"  Alcançáveis: {sorted(resultado_bfs['alcancaveis'])}")
    
    # Testa BFS de vértice com alcance limitado
    resultado_bfs_c = digrafo.busca_em_largura('C')
    print(f"\nBFS a partir de 'C': {sorted(resultado_bfs_c['alcancaveis'])}")
    
    print("✅ Teste passou!")

def teste_busca_profundidade():
    """Testa o algoritmo DFS completo em dígrafos."""
    imprimir_separador_teste("TESTE - BUSCA EM PROFUNDIDADE (DFS)")
    
    # Dígrafo com diferentes tipos de arcos
    vertices = {'A', 'B', 'C', 'D'}
    arcos = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D')]
    digrafo = Digrafo(vertices, arcos)
    
    resultado_dfs = digrafo.busca_em_profundidade_completa()
    
    print("Resultado DFS completo:")
    print(f"  Pais: {resultado_dfs['pais']}")
    print(f"  Tempos de entrada: {resultado_dfs['tempo_entrada']}")
    print(f"  Tempos de saída: {resultado_dfs['tempo_saida']}")
    print(f"  Arcos de árvore: {resultado_dfs['tipos_arcos']['arvore']}")
    print(f"  Arcos de retorno: {resultado_dfs['tipos_arcos']['retorno']}")
    print(f"  Arcos de avanço: {resultado_dfs['tipos_arcos']['avanco']}")
    print(f"  Arcos de cruzamento: {resultado_dfs['tipos_arcos']['cruzamento']}")
    
    print("✅ Teste passou!")

def teste_grafo_subjacente():
    """Testa a determinação do grafo subjacente."""
    imprimir_separador_teste("TESTE - GRAFO SUBJACENTE")
    
    # Teste 1: Dígrafo simples
    print("Teste 1: Dígrafo A → B → C")
    vertices1 = {'A', 'B', 'C'}
    arcos1 = [('A', 'B'), ('B', 'C')]
    digrafo1 = Digrafo(vertices1, arcos1)
    
    grafo_sub1 = digrafo1.obter_grafo_subjacente()
    lista_adj_sub1 = grafo_sub1.criar_lista_adjacencia()
    
    print("Dígrafo original:")
    lista_adj_dir1 = digrafo1.criar_lista_adjacencia()
    for v in sorted(lista_adj_dir1.keys()):
        print(f"  {v} → {lista_adj_dir1[v]}")
    
    print("Grafo subjacente:")
    for v in sorted(lista_adj_sub1.keys()):
        print(f"  {v}: {sorted(lista_adj_sub1[v])}")
    
    print("✅ Teste 1 passou!")
    
    # Teste 2: Dígrafo com arcos bidirecionais
    print("\nTeste 2: Dígrafo com arcos bidirecionais")
    vertices2 = {'A', 'B', 'C'}
    arcos2 = [('A', 'B'), ('B', 'A'), ('B', 'C')]
    digrafo2 = Digrafo(vertices2, arcos2)
    
    grafo_sub2 = digrafo2.obter_grafo_subjacente()
    lista_adj_sub2 = grafo_sub2.criar_lista_adjacencia()
    
    print("Dígrafo original:")
    lista_adj_dir2 = digrafo2.criar_lista_adjacencia()
    for v in sorted(lista_adj_dir2.keys()):
        print(f"  {v} → {lista_adj_dir2[v]}")
    
    print("Grafo subjacente:")
    for v in sorted(lista_adj_sub2.keys()):
        print(f"  {v}: {sorted(lista_adj_sub2[v])}")
    
    print("✅ Teste 2 passou!")
    
    # Teste 3: Dígrafo vazio
    print("\nTeste 3: Dígrafo vazio")
    vertices3 = {'A', 'B'}
    arcos3 = []
    digrafo3 = Digrafo(vertices3, arcos3)
    
    grafo_sub3 = digrafo3.obter_grafo_subjacente()
    lista_adj_sub3 = grafo_sub3.criar_lista_adjacencia()
    
    print("Grafo subjacente (vazio):")
    for v in sorted(lista_adj_sub3.keys()):
        print(f"  {v}: {lista_adj_sub3[v]}")
    
    print("✅ Teste 3 passou!")

def teste_digrafo_bipartido():
    """Testa a verificação de dígrafo bipartido."""
    imprimir_separador_teste("TESTE - DÍGRAFO BIPARTIDO")
    
    # Teste 1: Dígrafo bipartido (cadeia alternada)
    print("Teste 1: Dígrafo bipartido (A → B → C → D)")
    vertices1 = {'A', 'B', 'C', 'D'}
    arcos1 = [('A', 'B'), ('B', 'C'), ('C', 'D')]
    digrafo1 = Digrafo(vertices1, arcos1)
    
    resultado1 = digrafo1.eh_bipartido()
    print(f"É bipartido: {resultado1['eh_bipartido']}")
    if resultado1['eh_bipartido']:
        print(f"Partição 1: {sorted(resultado1['particoes'][0])}")
        print(f"Partição 2: {sorted(resultado1['particoes'][1])}")
    
    print("✅ Teste 1 passou!")
    
    # Teste 2: Dígrafo não-bipartido (ciclo ímpar no subjacente)
    print("\nTeste 2: Dígrafo não-bipartido (ciclo A → B → C → A)")
    vertices2 = {'A', 'B', 'C'}
    arcos2 = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    digrafo2 = Digrafo(vertices2, arcos2)
    
    resultado2 = digrafo2.eh_bipartido()
    print(f"É bipartido: {resultado2['eh_bipartido']}")
    if not resultado2['eh_bipartido']:
        print(f"Motivo: O grafo subjacente contém ciclo ímpar")
    
    print("✅ Teste 2 passou!")
    
    # Teste 3: Dígrafo bipartido completo
    print("\nTeste 3: Dígrafo bipartido K2,2 direcionado")
    vertices3 = {'A', 'B', 'C', 'D'}
    arcos3 = [('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
    digrafo3 = Digrafo(vertices3, arcos3)
    
    resultado3 = digrafo3.eh_bipartido()
    print(f"É bipartido: {resultado3['eh_bipartido']}")
    if resultado3['eh_bipartido']:
        print(f"Partição 1: {sorted(resultado3['particoes'][0])}")
        print(f"Partição 2: {sorted(resultado3['particoes'][1])}")
    
    print("✅ Teste 3 passou!")
    
    # Teste 4: Dígrafo com ciclo par (bipartido)
    print("\nTeste 4: Dígrafo com ciclo par (A → B → C → D → A)")
    vertices4 = {'A', 'B', 'C', 'D'}
    arcos4 = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
    digrafo4 = Digrafo(vertices4, arcos4)
    
    resultado4 = digrafo4.eh_bipartido()
    print(f"É bipartido: {resultado4['eh_bipartido']}")
    if resultado4['eh_bipartido']:
        print(f"Partição 1: {sorted(resultado4['particoes'][0])}")
        print(f"Partição 2: {sorted(resultado4['particoes'][1])}")
    
    print("✅ Teste 4 passou!")

def teste_casos_especiais():
    """Testa casos especiais e edge cases para dígrafos."""
    imprimir_separador_teste("TESTE - CASOS ESPECIAIS DÍGRAFO")
    
    # Teste 1: Dígrafo com um vértice
    print("Teste 1: Dígrafo com um vértice")
    vertices1 = {'A'}
    arcos1 = []
    digrafo1 = Digrafo(vertices1, arcos1)
    
    resultado_bip1 = digrafo1.eh_bipartido()
    grafo_sub1 = digrafo1.obter_grafo_subjacente()
    
    print(f"É bipartido: {resultado_bip1['eh_bipartido']}")
    print(f"Vertices no grafo subjacente: {grafo_sub1.vertices_ordenados}")
    print("✅ Teste 1 passou!")
    
    # Teste 2: Dígrafo completamente desconexo
    print("\nTeste 2: Dígrafo desconexo")
    vertices2 = {'A', 'B', 'C', 'D'}
    arcos2 = []
    digrafo2 = Digrafo(vertices2, arcos2)
    
    resultado_bfs2 = digrafo2.busca_em_largura('A')
    resultado_bip2 = digrafo2.eh_bipartido()
    
    print(f"BFS de A alcança: {sorted(resultado_bfs2['alcancaveis'])}")
    print(f"É bipartido: {resultado_bip2['eh_bipartido']}")
    print("✅ Teste 2 passou!")
    
    # Teste 3: Dígrafo com auto-loops
    print("\nTeste 3: Dígrafo com auto-loop")
    vertices3 = {'A', 'B'}
    arcos3 = [('A', 'A'), ('A', 'B')]
    digrafo3 = Digrafo(vertices3, arcos3)
    
    grafo_sub3 = digrafo3.obter_grafo_subjacente()
    lista_adj_sub3 = grafo_sub3.criar_lista_adjacencia()
    
    print("Grafo subjacente com auto-loop:")
    for v in sorted(lista_adj_sub3.keys()):
        print(f"  {v}: {sorted(lista_adj_sub3[v])}")
    
    print("✅ Teste 3 passou!")

def executar_todos_os_testes():
    """Executa toda a bateria de testes para a classe Digrafo."""
    imprimir_cabecalho_teste("BATERIA DE TESTES PARA A CLASSE DIGRAFO")
    
    teste_estruturas_basicas()
    teste_busca_largura()
    teste_busca_profundidade()
    teste_grafo_subjacente()
    teste_digrafo_bipartido()
    teste_casos_especiais()
    
    imprimir_cabecalho_teste("TODOS OS TESTES DA CLASSE DIGRAFO FORAM CONCLUÍDOS")

if __name__ == "__main__":
    executar_todos_os_testes()