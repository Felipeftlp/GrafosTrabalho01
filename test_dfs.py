"""

Testes para validar as implementações de:
- Item 11: Verificação de conectividade em grafos
- Item 14: Busca em Profundidade (DFS) em grafos
- Item 15: Determinação de Articulações e Blocos em grafos
- Item 20: Busca em Profundidade (DFS) em dígrafos
"""

from grafo import Grafo
from digrafo import Digrafo


# ==============================================================================
# TESTES ITEM 11 - VERIFICAÇÃO DE CONECTIVIDADE
# ==============================================================================

def teste_item_11_grafo_conexo():
    print("\n" + "="*80)
    print("TESTE 11.1 - Verificação de grafo conexo")
    print("="*80)
    
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.is_conexo()
    print(f"O grafo é conexo? {resultado}")
    
    assert resultado is True, "Grafo caminho deveria ser conexo"
    print("✅ Teste passou!")

def teste_item_11_grafo_desconexo():
    print("\n" + "="*80)
    print("TESTE 11.2 - Verificação de grafo desconexo")
    print("="*80)
    
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('c', 'd')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.is_conexo()
    print(f"O grafo é conexo? {resultado}")
    
    assert resultado is False, "Grafo com duas componentes deveria ser desconexo"
    print("✅ Teste passou!")
    
def teste_item_11_grafo_vazio_e_unitario():
    print("\n" + "="*80)
    print("TESTE 11.3 - Verificação de grafo vazio e unitário")
    print("="*80)

    grafo_vazio = Grafo(set(), [])
    assert grafo_vazio.is_conexo() is True, "Grafo vazio é conexo"
    print("Grafo vazio é conexo? True")

    grafo_unitario = Grafo({'a'}, [])
    assert grafo_unitario.is_conexo() is True, "Grafo com um vértice é conexo"
    print("Grafo com um vértice é conexo? True")
    
    print("✅ Teste passou!")

# ==============================================================================
# TESTES ITEM 14 - BUSCA EM PROFUNDIDADE (DFS) EM GRAFOS
# ==============================================================================

def teste_item_14_dfs_arvore():
    print("\n" + "="*80)
    print("TESTE 14.1 - DFS em árvore")
    print("="*80)
    
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_profundidade()
    
    print(f"Ordem de visitação: {resultado['ordem_visitacao']}")
    print(f"Arestas de retorno: {resultado['arestas_retorno']}")
    
    # Ordem depende da implementação, mas o comprimento deve ser 5
    assert len(resultado['ordem_visitacao']) == 5, "Deve visitar todos os 5 vértices"
    assert len(resultado['arestas_retorno']) == 0, "Árvore não deve ter arestas de retorno"
    assert resultado['pais']['b'] == 'a', "Pai de 'b' deve ser 'a'"
    assert resultado['pais']['d'] == 'b', "Pai de 'd' deve ser 'b'"
    
    print("✅ Teste passou!")

def teste_item_14_dfs_ciclo():
    print("\n" + "="*80)
    print("TESTE 14.2 - DFS em grafo com ciclo")
    print("="*80)
    
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_profundidade()
    
    print(f"Ordem de visitação: {resultado['ordem_visitacao']}")
    print(f"Arestas de retorno: {resultado['arestas_retorno']}")
    
    assert len(resultado['arestas_retorno']) == 1, "Deveria encontrar 1 aresta de retorno"
    # A aresta de retorno será entre o último e o primeiro vértice na ordem de visitação
    assert tuple(sorted((resultado['ordem_visitacao'][-1], resultado['ordem_visitacao'][0]))) in resultado['arestas_retorno']
    
    print("✅ Teste passou!")

def teste_item_14_dfs_desconexo():
    print("\n" + "="*80)
    print("TESTE 14.3 - DFS em grafo desconexo")
    print("="*80)
    
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('a', 'b'), ('d', 'e')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.busca_em_profundidade()
    
    print(f"Ordem de visitação: {resultado['ordem_visitacao']}")
    print(f"Pais: {resultado['pais']}")

    assert len(resultado['ordem_visitacao']) == 5, "Deve visitar todos os 5 vértices"
    # Raízes das árvores da floresta DFS não têm pai
    # A verificação exata depende da ordem de self.vertices_ordenados
    pais_raizes = {v for v, p in resultado['pais'].items() if p is None}
    assert len(pais_raizes) >= 3 # {'a', 'c', 'd'} devem ser raízes de suas componentes
    
    print("✅ Teste passou!")

# ==============================================================================
# TESTES ITEM 15 - ARTICULAÇÕES E BLOCOS
# ==============================================================================

def teste_item_15_ponte_e_articulacao():
    print("\n" + "="*80)
    print("TESTE 15.1 - Grafo com ponte e articulação")
    print("="*80)
    
    # Grafo "gravata borboleta": dois triângulos conectados pelo vértice 'c'
    vertices = {'a', 'b', 'c', 'd', 'e'}
    arestas = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'd'), ('d', 'e'), ('e', 'c')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.determinar_articulacoes_blocos()
    
    print(f"Articulações: {resultado['articulacoes']}")
    print(f"Blocos: {resultado['blocos']}")
    
    assert resultado['articulacoes'] == {'c'}, "'c' deve ser a única articulação"
    assert len(resultado['blocos']) == 2, "Devem existir 2 blocos"
    
    # Normaliza os blocos para teste (converte set para tuple de itens ordenados)
    blocos_normalizados = {tuple(sorted(list(b))) for b in resultado['blocos']}
    blocos_esperados = {('a', 'b', 'c'), ('c', 'd', 'e')}
    assert blocos_normalizados == blocos_esperados
    
    print("✅ Teste passou!")

def teste_item_15_sem_articulacoes():
    print("\n" + "="*80)
    print("TESTE 15.2 - Grafo biconexo (sem articulações)")
    print("="*80)
    
    # Grafo completo K4
    vertices = {'a', 'b', 'c', 'd'}
    arestas = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.determinar_articulacoes_blocos()

    print(f"Articulações: {resultado['articulacoes']}")
    
    assert len(resultado['articulacoes']) == 0, "Grafo completo não tem articulações"
    assert len(resultado['blocos']) == 1, "Grafo completo deve ter apenas 1 bloco"
    assert set(vertices) in resultado['blocos']
    
    print("✅ Teste passou!")

def teste_item_15_grafo_complexo():
    print("\n" + "="*80)
    print("TESTE 15.3 - Grafo com múltiplas articulações e blocos")
    print("="*80)
    
    vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}
    arestas = [
        ('A', 'B'), ('A', 'C'), ('B', 'C'),  # Bloco 1
        ('C', 'D'),                         # Ponte (Bloco 2)
        ('D', 'E'), ('D', 'F'), ('E', 'F'),  # Bloco 3
        ('D', 'G'),                         # Ponte (Bloco 4)
        ('G', 'H'), ('G', 'I'), ('H', 'I')   # Bloco 5
    ]
    grafo = Grafo(vertices, arestas)
    
    resultado = grafo.determinar_articulacoes_blocos()

    print(f"Articulações: {resultado['articulacoes']}")
    print(f"Blocos: {resultado['blocos']}")
    
    assert resultado['articulacoes'] == {'C', 'D', 'G'}, "As articulações devem ser C, D, G"
    assert len(resultado['blocos']) == 5, "Devem existir 5 blocos (3 ciclos + 2 pontes)"

    # Verificação robusta do conteúdo dos blocos
    blocos_encontrados_normalizados = {tuple(sorted(list(b))) for b in resultado['blocos']}
    blocos_esperados = {
        ('A', 'B', 'C'),
        ('C', 'D'),
        ('D', 'E', 'F'),
        ('D', 'G'),
        ('G', 'H', 'I')
    }
    assert blocos_encontrados_normalizados == blocos_esperados, "O conteúdo dos blocos não corresponde ao esperado"

    print("✅ Teste passou!")
    

# ==============================================================================
# TESTES ITEM 20 - BUSCA EM PROFUNDIDADE (DFS) EM DÍGRAFOS
# ==============================================================================

def teste_item_20_dfs_digrafo_cadeia():
    print("\n" + "="*80)
    print("TESTE 20.1 - DFS em dígrafo em cadeia (a → b → c)")
    print("="*80)
    
    vertices = {'a', 'b', 'c'}
    arcos = [('a', 'b'), ('b', 'c')]
    digrafo = Digrafo(vertices, arcos)
    
    resultado = digrafo.busca_em_profundidade_completa()

    print(f"Tempos de entrada: {resultado['tempo_entrada']}")
    print(f"Tempos de saída: {resultado['tempo_saida']}")
    print(f"Arcos de árvore: {resultado['tipos_arcos']['arvore']}")
    
    # Propriedade do parêntese: [d(u), f(u)] contém [d(v), f(v)] se v é descendente de u
    assert resultado['tempo_entrada']['a'] < resultado['tempo_entrada']['b'] < resultado['tempo_entrada']['c']
    assert resultado['tempo_saida']['c'] < resultado['tempo_saida']['b'] < resultado['tempo_saida']['a']
    assert len(resultado['tipos_arcos']['arvore']) == 2
    assert len(resultado['tipos_arcos']['retorno']) == 0
    
    print("✅ Teste passou!")

def teste_item_20_dfs_digrafo_classificacao_arcos():
    print("\n" + "="*80)
    print("TESTE 20.2 - DFS em dígrafo com todos os tipos de arcos")
    print("="*80)
    
    vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    arcos = [
        ('A', 'B'),  # Árvore
        ('B', 'C'),  # Árvore
        ('C', 'A'),  # Retorno (ciclo A-B-C)
        ('B', 'D'),  # Árvore
        ('A', 'D'),  # Avanço (A é ancestral de D)
        ('E', 'F'),  # Cruzamento (se A->F não existisse)
        ('F', 'G'),  # Árvore
        ('A', 'F')   # Árvore (porque A vem antes de E na ordem de travessia)
    ]
    digrafo = Digrafo(vertices, arcos)
    
    resultado = digrafo.busca_em_profundidade_completa()

    arcos_classificados = resultado['tipos_arcos']
    print("Arcos classificados:")
    for tipo, lista in arcos_classificados.items():
        print(f"  - {tipo.capitalize()}: {lista}")

    # CORREÇÃO: Ajustando as assertivas para o comportamento real do código
    assert ('C', 'A') in arcos_classificados['retorno']
    assert ('A', 'D') in arcos_classificados['avanco']
    assert ('A', 'F') in arcos_classificados['arvore']    # << CORRIGIDO
    assert ('E', 'F') in arcos_classificados['cruzamento']  # << CORRIGIDO
    assert ('A', 'B') in arcos_classificados['arvore']
    
    print("✅ Teste passou!")

def teste_item_20_dfs_digrafo_desconexo():
    print("\n" + "="*80)
    print("TESTE 20.3 - DFS em dígrafo desconexo")
    print("="*80)
    
    vertices = {'a', 'b', 'c', 'd'}
    arcos = [('a', 'b'), ('c', 'd')]
    digrafo = Digrafo(vertices, arcos)
    
    resultado = digrafo.busca_em_profundidade_completa()

    print(f"Pais: {resultado['pais']}")
    print(f"Tempos de entrada: {resultado['tempo_entrada']}")

    # As raízes das árvores da floresta não têm pai
    assert resultado['pais']['a'] is None
    assert resultado['pais']['c'] is None
    # O tempo continua de uma componente para outra
    assert resultado['tempo_entrada']['c'] > resultado['tempo_saida']['a']
    
    print("✅ Teste passou!")


# ==============================================================================
# FUNÇÃO PRINCIPAL - EXECUTA TODOS OS TESTES DE DFS
# ==============================================================================

def executar_todos_os_testes_dfs():
    """
    Executa todos os testes implementados neste arquivo.
    """
    print("\n" + "="*80)
    print("INICIANDO BATERIA DE TESTES DE DFS E ALGORITMOS RELACIONADOS")
    print("Itens: 11, 14, 15, 20")
    print("="*80)
    
    # Testes Item 11
    teste_item_11_grafo_conexo()
    teste_item_11_grafo_desconexo()
    teste_item_11_grafo_vazio_e_unitario()
    
    # Testes Item 14
    teste_item_14_dfs_arvore()
    teste_item_14_dfs_ciclo()
    teste_item_14_dfs_desconexo()
    
    # Testes Item 15
    teste_item_15_ponte_e_articulacao()
    teste_item_15_sem_articulacoes()
    teste_item_15_grafo_complexo()
    
    # Testes Item 20
    teste_item_20_dfs_digrafo_cadeia()
    teste_item_20_dfs_digrafo_classificacao_arcos()
    teste_item_20_dfs_digrafo_desconexo()

    print("\n" + "="*80)
    print("FIM DA BATERIA DE TESTES DE DFS E ALGORITMOS RELACIONADOS")
    print("="*80)

if __name__ == "__main__":
    executar_todos_os_testes_dfs()