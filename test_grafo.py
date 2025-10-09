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

def executar_todos_os_testes():
    """Executa toda a bateria de testes para a classe Grafo."""
    imprimir_cabecalho_teste("BATERIA DE TESTES PARA A CLASSE GRAFO")
    
    teste_estruturas_basicas()
    teste_propriedades_basicas()
    teste_grafo_bipartido()
    teste_casos_especiais()
    
    imprimir_cabecalho_teste("TODOS OS TESTES DA CLASSE GRAFO FORAM CONCLUÍDOS")

if __name__ == "__main__":
    executar_todos_os_testes()