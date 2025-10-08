
import matplotlib
matplotlib.use('TkAgg')
# Importa suas classes dos arquivos correspondentes
from grafo import Grafo
from digrafo import Digrafo
import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(
    classe_grafo,
    titulo="Visualização de Grafo",
    resultado_busca=None
):
    """
    Desenha um grafo ou dígrafo a partir das suas classes, usando NetworkX e Matplotlib.
    Pode destacar os resultados de uma busca (BFS ou DFS).
    """
    # Determina se é um grafo ou dígrafo para criar o objeto NetworkX correto
    if hasattr(classe_grafo, 'arcos'): # Verifica se é uma instância de Digrafo
        G = nx.DiGraph()
        G.add_edges_from(classe_grafo.arcos)
        G.add_nodes_from(classe_grafo.vertices_ordenados)
    else: # Senão, é uma instância de Grafo
        G = nx.Graph()
        G.add_edges_from(classe_grafo.arestas)
        G.add_nodes_from(classe_grafo.vertices_ordenados)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    plt.title(titulo, size=15)
    
    if resultado_busca:
        ordem = resultado_busca.get('ordem_visitacao', [])
        pais = resultado_busca.get('pais', {})
        
        # Define as cores dos nós
        cores_nos = []
        for no in G.nodes():
            if no not in ordem:
                cores_nos.append('lightgray') # Não visitado
            elif ordem.index(no) == 0:
                cores_nos.append('green') # Nó inicial
            else:
                cores_nos.append('skyblue') # Visitado
        
        # Destaca as arestas da árvore de busca
        arestas_busca = [(pai, filho) for filho, pai in pais.items() if pai is not None]
        
        nx.draw_networkx_edges(G, pos, edgelist=set(G.edges()) - set(arestas_busca), edge_color='gray', style='dashed')
        nx.draw_networkx_edges(G, pos, edgelist=arestas_busca, edge_color='black', width=2.0)
        nx.draw_networkx_nodes(G, pos, node_color=cores_nos, node_size=700)
    else:
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
        nx.draw_networkx_edges(G, pos, edge_color='gray')

    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    plt.axis('off')
    plt.show()


def visualizar_digrafo_dfs(digrafo, resultado_dfs_completa):
    """
    Função especializada para visualizar os resultados da DFS em dígrafos,
    colorindo os arcos de acordo com sua classificação.
    """
    G = nx.DiGraph()
    G.add_edges_from(digrafo.arcos)
    G.add_nodes_from(digrafo.vertices_ordenados)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 9))
    plt.title("Visualização DFS em Dígrafo com Classificação de Arcos", size=15)

    tipos_arcos = resultado_dfs_completa['tipos_arcos']
    cores = {'arvore': 'black', 'retorno': 'red', 'avanco': 'green', 'cruzamento': 'orange'}

    nx.draw_networkx_edges(G, pos, edgelist=tipos_arcos['arvore'], edge_color=cores['arvore'], width=2.0)
    nx.draw_networkx_edges(G, pos, edgelist=tipos_arcos['retorno'], edge_color=cores['retorno'], width=1.5, style='dashed', connectionstyle='arc3,rad=0.1')
    nx.draw_networkx_edges(G, pos, edgelist=tipos_arcos['avanco'], edge_color=cores['avanco'], width=1.5, style='dotted')
    nx.draw_networkx_edges(G, pos, edgelist=tipos_arcos['cruzamento'], edge_color=cores['cruzamento'], width=1.5, style='dashdot')

    tempos_d = resultado_dfs_completa['tempo_entrada']
    tempos_f = resultado_dfs_completa['tempo_saida']
    rotulos_nos = {no: f"{no}\n({tempos_d.get(no, ' ')}/{tempos_f.get(no, ' ')})" for no in G.nodes()}

    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1200)
    nx.draw_networkx_labels(G, pos, labels=rotulos_nos, font_size=10)

    handles = [plt.Line2D([0], [0], color=cor, lw=2, label=tipo.capitalize()) for tipo, cor in cores.items()]
    plt.legend(handles=handles, title="Tipos de Arco")
    plt.axis('off')
    plt.show()

def executar_demonstracoes():
    """
    Função principal que executa as demonstrações de visualização.
    """
    # =================================================================
    # Exemplo 1: Visualização de Grafo e Busca em Largura (BFS)
    # =================================================================
    print("--- Exemplo 1: Grafo e Busca em Largura ---")
    vertices_g = {'a', 'b', 'c', 'd', 'e', 'f'}
    arestas_g = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'f')]
    # Utiliza a sua classe Grafo completa
    grafo_exemplo = Grafo(vertices_g, arestas_g)

    # Visualiza o grafo original
    visualizar_grafo(grafo_exemplo, titulo="Grafo Original (Exemplo 1)")

    # Executa a BFS a partir de 'a' usando o método da sua classe
    resultado_bfs = grafo_exemplo.busca_em_largura('a')
    print(f"Ordem de visitação da BFS: {resultado_bfs['ordem_visitacao']}")

    # Visualiza o resultado da BFS
    visualizar_grafo(
        grafo_exemplo,
        titulo="Resultado da Busca em Largura (BFS) a partir de 'a'",
        resultado_busca=resultado_bfs
    )

    # =================================================================
    # Exemplo 2: Visualização de Dígrafo e Busca em Profundidade (DFS)
    # =================================================================
    print("\n--- Exemplo 2: Dígrafo e Busca em Profundidade ---")
    vertices_d = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    arcos_d = [
        ('A', 'B'), ('B', 'C'), ('C', 'A'), ('B', 'D'), ('A', 'D'),
        ('E', 'F'), ('F', 'G'), ('A', 'F')
    ]
    # Utiliza a sua classe Digrafo completa
    digrafo_exemplo = Digrafo(vertices_d, arcos_d)

    # Visualiza o dígrafo original
    visualizar_grafo(digrafo_exemplo, titulo="Dígrafo Original (Exemplo 2)")

    # Executa a DFS completa no dígrafo usando o método da sua classe
    resultado_dfs_d = digrafo_exemplo.busca_em_profundidade_completa()
    print("Arcos de Retorno (indicam ciclo):", resultado_dfs_d['tipos_arcos']['retorno'])
    
    # Usa a função de visualização especializada para DFS em dígrafos
    visualizar_digrafo_dfs(digrafo_exemplo, resultado_dfs_d)


if __name__ == "__main__":
    executar_demonstracoes()