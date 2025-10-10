"""
Este programa permite ao usuário escolher entre trabalhar com:
- Grafo (não-direcionado) - Opção 0
- Dígrafo (direcionado) - Opção 1

Executa todas as funcionalidades implementadas nas classes Grafo e Digrafo.

"""

from grafo import Grafo
from digrafo import Digrafo
from utils import converter_matriz_para_lista, converter_lista_para_matriz

def imprimir_cabecalho():
    """Imprime o cabeçalho do programa."""
    print("\n" + "="*80)
    print("SISTEMA DE ANÁLISE DE GRAFOS E DÍGRAFOS".center(80))
    print("="*80)
    print("Escolha o tipo de estrutura que deseja analisar:")
    print("  [0] - Grafo (não-direcionado)")
    print("  [1] - Dígrafo (direcionado)")
    print("="*80)

def escolher_tipo_grafo():
    """Permite ao usuário escolher entre grafo e dígrafo."""
    while True:
        try:
            opcao = input("\nDigite sua opção (0 ou 1): ").strip()
            if opcao == '0':
                return 'grafo'
            elif opcao == '1':
                return 'digrafo'
            else:
                print("❌ Opção inválida! Digite 0 para Grafo ou 1 para Dígrafo.")
        except (ValueError, KeyboardInterrupt):
            print("❌ Entrada inválida! Digite 0 ou 1.")

def coletar_dados_grafo():
    """Coleta dados para um grafo não-direcionado."""
    print("\n" + "-"*60)
    print("CONFIGURAÇÃO DO GRAFO (NÃO-DIRECIONADO)".center(60))
    print("-"*60)
    print("Insira as arestas no formato 'vertice1,vertice2'.")
    print("Exemplo: A,B representa uma aresta entre A e B")
    print("Pressione Enter em uma linha vazia para finalizar.")
    print("-"*60)
    
    arestas = []
    vertices_set = set()
    
    while True:
        entrada = input("Aresta: ").strip()
        if not entrada:
            break
        try:
            v1, v2 = [v.strip() for v in entrada.split(',')]
            if v1 and v2:
                arestas.append((v1, v2))
                vertices_set.add(v1)
                vertices_set.add(v2)
                print(f"  ✅ Aresta {v1} ↔ {v2} adicionada")
            else:
                print("  ❌ Aresta inválida ignorada.")
        except ValueError:
            print(f"  ❌ Formato inválido na entrada '{entrada}'. Use: vertice1,vertice2")
    
    return vertices_set, arestas

def coletar_dados_digrafo():
    """Coleta dados para um dígrafo (direcionado)."""
    print("\n" + "-"*60)
    print("CONFIGURAÇÃO DO DÍGRAFO (DIRECIONADO)".center(60))
    print("-"*60)
    print("Insira os arcos no formato 'origem,destino'.")
    print("Exemplo: A,B representa um arco de A para B (A → B)")
    print("Pressione Enter em uma linha vazia para finalizar.")
    print("-"*60)
    
    arcos = []
    vertices_set = set()
    
    while True:
        entrada = input("Arco: ").strip()
        if not entrada:
            break
        try:
            origem, destino = [v.strip() for v in entrada.split(',')]
            if origem and destino:
                arcos.append((origem, destino))
                vertices_set.add(origem)
                vertices_set.add(destino)
                print(f"  ✅ Arco {origem} → {destino} adicionado")
            else:
                print("  ❌ Arco inválido ignorado.")
        except ValueError:
            print(f"  ❌ Formato inválido na entrada '{entrada}'. Use: origem,destino")
    
    return vertices_set, arcos

def executar_analise_completa_grafo(grafo):
    """Executa todas as funcionalidades disponíveis para grafos não-direcionados."""
    
    print("\n" + "="*80)
    print("ANÁLISE COMPLETA DO GRAFO (NÃO-DIRECIONADO)".center(80))
    print("="*80)
    
    # =========================================================================
    # 1. ESTRUTURAS DE DADOS BÁSICAS
    # =========================================================================
    print("\n📊 1. ESTRUTURAS DE DADOS BÁSICAS")
    print("-" * 50)
    
    lista_adj = grafo.criar_lista_adjacencia()
    matriz_adj = grafo.criar_matriz_adjacencia()
    matriz_inc = grafo.criar_matriz_incidencia()
    vertices = grafo.vertices_ordenados
    
    print("📋 Lista de Adjacência:")
    for v in sorted(lista_adj.keys()):
        print(f"   {v}: {sorted(lista_adj[v])}")
    
    print("\n📋 Matriz de Adjacência:")
    print("     " + "  ".join(f"{v:>2}" for v in vertices))
    print("    " + "----" * len(vertices))
    for i, linha in enumerate(matriz_adj):
        print(f" {vertices[i]:>2} | " + "  ".join(f"{val:>2}" for val in linha))
    
    print("\n📋 Matriz de Incidência:")
    rotulos_arestas = [f"e{i}" for i in range(grafo.num_arestas)]
    if rotulos_arestas:
        print("     " + "  ".join(f"{e:>2}" for e in rotulos_arestas))
        print("    " + "----" * len(rotulos_arestas))
        for i, linha in enumerate(matriz_inc):
            print(f" {vertices[i]:>2} | " + "  ".join(f"{val:>2}" for val in linha))
    else:
        print("   (Sem arestas)")
    
    # =========================================================================
    # 2. PROPRIEDADES BÁSICAS
    # =========================================================================
    print("\n📈 2. PROPRIEDADES BÁSICAS")
    print("-" * 50)
    
    graus = grafo.get_grau_vertices()
    print("🔢 Grau dos vértices:")
    for v, grau in graus.items():
        print(f"   {v}: {grau}")
    
    print(f"\n📊 Total de vértices: {grafo.get_num_vertices()}")
    print(f"📊 Total de arestas: {grafo.get_num_arestas()}")
    
    # Testa adjacência entre os primeiros dois vértices (se existirem)
    if len(vertices) >= 2:
        v1, v2 = vertices[0], vertices[1]
        adjacente = grafo.is_adjacente(v1, v2)
        print(f"🔗 {v1} e {v2} são adjacentes: {adjacente}")
    
    # =========================================================================
    # 3. ANÁLISE DE BIPARTIÇÃO
    # =========================================================================
    print("\n🎨 3. ANÁLISE DE BIPARTIÇÃO")
    print("-" * 50)
    
    resultado_bip = grafo.eh_bipartido()
    print(f"🎯 O grafo é bipartido: {resultado_bip['eh_bipartido']}")
    
    if resultado_bip['eh_bipartido']:
        print(f"   📦 Partição 1: {sorted(resultado_bip['particoes'][0])}")
        print(f"   📦 Partição 2: {sorted(resultado_bip['particoes'][1])}")
        print("   ✅ Pode ser colorido com apenas 2 cores!")
    else:
        print(f"   ❌ Contém ciclo ímpar (conflito detectado)")
        if resultado_bip['ciclo_impar']:
            print(f"   🔄 Ciclo problemático envolve: {resultado_bip['ciclo_impar']}")
    
    # =========================================================================
    # 4. CONVERSÕES ENTRE REPRESENTAÇÕES
    # =========================================================================
    print("\n🔄 4. CONVERSÕES ENTRE REPRESENTAÇÕES")
    print("-" * 50)
    
    print("🔀 Matriz → Lista de Adjacência:")
    lista_convertida = converter_matriz_para_lista(matriz_adj, vertices)
    for v in sorted(lista_convertida.keys()):
        print(f"   {v}: {sorted(lista_convertida[v])}")
    
    print("\n🔀 Lista → Matriz de Adjacência:")
    matriz_convertida = converter_lista_para_matriz(lista_adj, vertices)
    print("     " + "  ".join(f"{v:>2}" for v in vertices))
    print("    " + "----" * len(vertices))
    for i, linha in enumerate(matriz_convertida):
        print(f" {vertices[i]:>2} | " + "  ".join(f"{val:>2}" for val in linha))
    
    print("\n✅ Análise do grafo concluída!")

def executar_analise_completa_digrafo(digrafo):
    """Executa todas as funcionalidades disponíveis para dígrafos."""
    
    print("\n" + "="*80)
    print("ANÁLISE COMPLETA DO DÍGRAFO (DIRECIONADO)".center(80))
    print("="*80)
    
    # =========================================================================
    # 1. ESTRUTURAS DE DADOS BÁSICAS
    # =========================================================================
    print("\n📊 1. ESTRUTURAS DE DADOS BÁSICAS")
    print("-" * 50)
    
    lista_adj = digrafo.criar_lista_adjacencia()
    matriz_adj = digrafo.criar_matriz_adjacencia()
    matriz_inc = digrafo.criar_matriz_incidencia()
    vertices = digrafo.vertices_ordenados
    
    print("📋 Lista de Adjacência (Saídas):")
    for v in sorted(lista_adj.keys()):
        print(f"   {v} → {sorted(lista_adj[v])}")
    
    print("\n📋 Matriz de Adjacência:")
    print("     " + "  ".join(f"{v:>2}" for v in vertices))
    print("    " + "----" * len(vertices))
    for i, linha in enumerate(matriz_adj):
        print(f" {vertices[i]:>2} | " + "  ".join(f"{val:>2}" for val in linha))
    
    print("\n📋 Matriz de Incidência (+ saída, - entrada):")
    rotulos_arcos = [f"a{i}" for i in range(digrafo.num_arcos)]
    if rotulos_arcos:
        print("     " + "  ".join(f"{a:>3}" for a in rotulos_arcos))
        print("    " + "-----" * len(rotulos_arcos))
        for i, linha in enumerate(matriz_inc):
            print(f" {vertices[i]:>2} | " + "  ".join(f"{val:>3}" for val in linha))
    else:
        print("   (Sem arcos)")
    
    # =========================================================================
    # 2. ALGORITMOS DE BUSCA
    # =========================================================================
    print("\n🔍 2. ALGORITMOS DE BUSCA")
    print("-" * 50)
    
    if vertices:
        vertice_inicial = vertices[0]
        
        # BFS
        resultado_bfs = digrafo.busca_em_largura(vertice_inicial)
        print(f"🌊 BFS a partir de '{vertice_inicial}':")
        print(f"   📋 Ordem de visitação: {resultado_bfs['ordem_visitacao']}")
        print(f"   📏 Distâncias: {resultado_bfs['distancias']}")
        print(f"   🌳 Pais: {resultado_bfs['pais']}")
        print(f"   🎯 Alcançáveis: {sorted(resultado_bfs['alcancaveis'])}")
        
        # DFS
        resultado_dfs = digrafo.busca_em_profundidade_completa()
        print(f"\n🏃 DFS Completo:")
        print(f"   ⏰ Tempos entrada: {resultado_dfs['tempo_entrada']}")
        print(f"   ⏰ Tempos saída: {resultado_dfs['tempo_saida']}")
        print(f"   🌳 Arcos de árvore: {resultado_dfs['tipos_arcos']['arvore']}")
        print(f"   🔄 Arcos de retorno: {resultado_dfs['tipos_arcos']['retorno']}")
        print(f"   ⏭️  Arcos de avanço: {resultado_dfs['tipos_arcos']['avanco']}")
        print(f"   ✂️  Arcos de cruzamento: {resultado_dfs['tipos_arcos']['cruzamento']}")
    
    # =========================================================================
    # 3. GRAFO SUBJACENTE E BIPARTIÇÃO
    # =========================================================================
    print("\n🔗 3. GRAFO SUBJACENTE E ANÁLISE DE BIPARTIÇÃO")
    print("-" * 50)
    
    grafo_subjacente = digrafo.obter_grafo_subjacente()
    
    print("📋 Grafo Subjacente (ignorando direções):")
    lista_adj_subj = grafo_subjacente.criar_lista_adjacencia()
    for v in sorted(lista_adj_subj.keys()):
        print(f"   {v}: {sorted(lista_adj_subj[v])}")
    
    resultado_bip = digrafo.eh_bipartido()
    print(f"\n🎯 O dígrafo é bipartido: {resultado_bip['eh_bipartido']}")
    
    if resultado_bip['eh_bipartido']:
        print(f"   📦 Partição 1: {sorted(resultado_bip['particoes'][0])}")
        print(f"   📦 Partição 2: {sorted(resultado_bip['particoes'][1])}")
        print("   ✅ O grafo subjacente pode ser colorido com apenas 2 cores!")
    else:
        print(f"   ❌ O grafo subjacente contém ciclo ímpar")
    
    # =========================================================================
    # 4. INFORMAÇÕES ESTATÍSTICAS
    # =========================================================================
    print("\n📊 4. INFORMAÇÕES ESTATÍSTICAS")
    print("-" * 50)
    
    print(f"📊 Total de vértices: {digrafo.num_vertices}")
    print(f"📊 Total de arcos: {digrafo.num_arcos}")
    print(f"📊 Arestas no grafo subjacente: {grafo_subjacente.get_num_arestas()}")
    
    # Densidade do dígrafo (arcos / máximo possível)
    max_arcos = digrafo.num_vertices * (digrafo.num_vertices - 1)
    densidade = (digrafo.num_arcos / max_arcos * 100) if max_arcos > 0 else 0
    print(f"📊 Densidade do dígrafo: {densidade:.2f}%")
    
    print("\n✅ Análise do dígrafo concluída!")

def main():
    """Função principal do programa."""
    try:
        # Exibe cabeçalho e coleta escolha do usuário
        imprimir_cabecalho()
        tipo_escolhido = escolher_tipo_grafo()
        
        if tipo_escolhido == 'grafo':
            # ========== MODO GRAFO (NÃO-DIRECIONADO) ==========
            vertices, arestas = coletar_dados_grafo()
            
            if not vertices:
                print("\n❌ Nenhum vértice foi fornecido. Encerrando programa.")
                return
            
            if not arestas:
                print("\n⚠️  Grafo sem arestas (vértices isolados).")
                # Cria grafo apenas com vértices, sem arestas
                
            # Cria o grafo e executa análise completa
            meu_grafo = Grafo(vertices, arestas)
            executar_analise_completa_grafo(meu_grafo)
            
        elif tipo_escolhido == 'digrafo':
            # ========== MODO DÍGRAFO (DIRECIONADO) ==========
            vertices, arcos = coletar_dados_digrafo()
            
            if not vertices:
                print("\n❌ Nenhum vértice foi fornecido. Encerrando programa.")
                return
            
            if not arcos:
                print("\n⚠️  Dígrafo sem arcos (vértices isolados).")
                # Cria dígrafo apenas com vértices, sem arcos
                
            # Cria o dígrafo e executa análise completa
            meu_digrafo = Digrafo(vertices, arcos)
            executar_analise_completa_digrafo(meu_digrafo)
        
        # Mensagem final
        print("\n" + "="*80)
        print("🎉 ANÁLISE CONCLUÍDA COM SUCESSO!".center(80))
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("Por favor, verifique sua entrada e tente novamente.")

if __name__ == "__main__":
    main()