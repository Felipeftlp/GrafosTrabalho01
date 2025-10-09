"""
Trabalho 01 - Grafos

Testes para validar as implementações de
- Item 13: Busca em Largura (BFS) em grafos
- Item 19: Busca em Largura (BFS) em dígrafos
"""

from grafo import Grafo
from digrafo import Digrafo

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
    print("INICIANDO BATERIA DE TESTES DE BFS")
    print("Item: 13")
    print("="*80)
    
    # Testes Item 13 - BFS em grafos
    teste_item_13_bfs_arvore()
    teste_item_13_bfs_caminho_mais_curto()
    teste_item_13_bfs_grafo_desconexo()
    teste_item_13_bfs_grafo_completo()
    teste_item_13_bfs_ciclo()
    teste_item_13_bfs_vertice_isolado()
    teste_item_13_bfs_vertice_inexistente()
    
    print("\n" + "="*80)
    print("INICIANDO BATERIA DE TESTES DE BFS EM DIGRAFOS")
    print("Item: 19")
    print("="*80)
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
