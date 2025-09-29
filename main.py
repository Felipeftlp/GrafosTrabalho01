from grafo import Grafo
# Importa as funções do novo módulo de utilidades
from utils import converter_matriz_para_lista, converter_lista_para_matriz

# A função coletar_dados_grafo() permanece exatamente a mesma...
def coletar_dados_grafo():
    # ... (código inalterado)
    print("--- Configuração do Grafo ---")
    input("Digite a quantidade de vértices (informativo, pressione Enter para continuar): ")
    print("\nInsira as arestas no formato 'vertice1,vertice2'.")
    print("Pressione Enter em uma linha vazia para finalizar.")
    arestas = []
    vertices_set = set()
    while True:
        entrada_aresta = input("Aresta: ")
        if not entrada_aresta:
            break
        try:
            v1, v2 = [v.strip() for v in entrada_aresta.split(',')]
            if v1 and v2:
                arestas.append((v1, v2))
                vertices_set.add(v1)
                vertices_set.add(v2)
            else:
                print("Aresta inválida ignorada.")
        except ValueError:
            print(f"Formato inválido na entrada '{entrada_aresta}'. Aresta ignorada.")
    return vertices_set, arestas

def imprimir_resultados(meu_grafo):
    lista_adj_original = meu_grafo.criar_lista_adjacencia()
    matriz_adj_original = meu_grafo.criar_matriz_adjacencia()
    matriz_inc_original = meu_grafo.criar_matriz_incidencia()
    vertices = meu_grafo.vertices_ordenados

    # ... (a impressão das estruturas originais continua a mesma) ...
    print("\n" + "="*50)
    print("      ESTRUTURAS DE DADOS ORIGINAIS DO GRAFO")
    print("="*50)
    
    # 1. Imprime Lista de Adjacência
    print("\n1. Lista de Adjacência:")
    for v, vizinhos in lista_adj_original.items():
        print(f"   {v}: [{', '.join(vizinhos)}]")

    # 2. Imprime Matriz de Adjacência
    print("\n\n2. Matriz de Adjacência:")
    print("     " + "  ".join(vertices))
    print("    " + "---" * len(vertices))
    for i, linha in enumerate(matriz_adj_original):
        print(f" {vertices[i]} | " + "  ".join(map(str, linha)))
        
    # 3. Imprime Matriz de Incidência (opcional, mantido do original)
    print("\n\n3. Matriz de Incidência:")
    rotulos_arestas = [f"e{i}" for i in range(meu_grafo.num_arestas)]
    print("     " + "  ".join(rotulos_arestas))
    print("    " + "---" * meu_grafo.num_arestas)
    for i, linha in enumerate(matriz_inc_original):
        print(f" {vertices[i]} | " + "  ".join(map(str, linha)))

    # --- Demonstração das Conversões usando as funções de utils.py ---
    print("\n\n" + "="*50)
    print("            DEMONSTRAÇÃO DAS CONVERSÕES")
    print("="*50)

    # 1. Converte Matriz -> Lista
    print("\n1. Conversão: Matriz de Adjacência -> Lista de Adjacência")
    # Chama a função importada de utils
    lista_convertida = converter_matriz_para_lista(matriz_adj_original, vertices)
    for v, vizinhos in lista_convertida.items():
        print(f"   {v}: [{', '.join(vizinhos)}]")

    # 2. Converte Lista -> Matriz
    print("\n\n2. Conversão: Lista de Adjacência -> Matriz de Adjacência")
    # Chama a função importada de utils
    matriz_convertida = converter_lista_para_matriz(lista_adj_original, vertices)
    print("     " + "  ".join(vertices))
    print("    " + "---" * len(vertices))
    for i, linha in enumerate(matriz_convertida):
        print(f" {vertices[i]} | " + "  ".join(map(str, linha)))
    
    print("\n" + "="*50)

def main():
    vertices, arestas = coletar_dados_grafo()
    
    if not vertices or not arestas:
        print("\nNenhuma aresta foi fornecida. O grafo está vazio.")
        return
        
    meu_grafo = Grafo(vertices, arestas)
    imprimir_resultados(meu_grafo)

if __name__ == "__main__":
    main()