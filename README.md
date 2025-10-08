# Estruturas de Dados e Algoritmos em Grafos
![Status](https://img.shields.io/badge/Status-Em%20Andamento-yellow)

Trabalho prático da disciplina de Teoria dos Grafos, focado na implementação em Python de diversas estruturas de dados e algoritmos para manipulação e análise de grafos, tanto não-direcionados (Grafos) quanto direcionados (Dígrafos).

---

## 🛠️ Tecnologias Utilizadas
* **Python 3**

---

## 📂 Estrutura do Projeto
O projeto está organizado de forma modular para separar responsabilidades e facilitar a manutenção:

- **`main.py`**: Ponto de entrada do programa. Responsável pela interação com o usuário (coleta de dados do grafo) e pela exibição dos resultados.
- **`grafo.py`**: Contém a classe `Grafo`, que modela o grafo e seus métodos para gerar as representações básicas (lista/matriz de adjacência, matriz de incidência).
- **`digrafo.py`**: Contém a classe `Digrafo`, que modela grafos direcionados e implementa BFS.
- **`utils.py`**: Módulo com funções auxiliares e de conversão, como `matriz -> lista` e `lista -> matriz`.
- **`test_bfs.py`**: Testes automatizados para validar as implementações de BFS e operações com vértices.
- **`test_dfs.py`**: Testes automatizados para validar as implementações de DFS e operações.
- **`visualizacao_demo.py`**: Contém uma parte gráfica simples para representar os grafos e buscas.
- **`.gitignore`**: Define os arquivos e pastas que devem ser ignorados pelo Git (ex: `__pycache__`, ambientes virtuais).
- **`README.md`**: Documentação do projeto (este arquivo).

---

## 🚀 Como Executar
1. Clone o repositório para a sua máquina local:
   ```sh
   git clone [URL_DO_SEU_REPOSITORIO]
   ```
2. Navegue até a pasta do projeto:
   ```sh
   cd GRAFOSTRABALHO01
   ```
3. (Opcional, mas recomendado) Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
4. Execute o programa principal:
   ```sh
   python main.py
   ```
5. Siga as instruções no terminal para inserir os vértices e as arestas do grafo desejado.

---

## ✅ Funcionalidades

Esta seção detalha o que já foi implementado e o que está planejado para o projeto, com base nos requisitos do trabalho.

### Implementado ✔️
-   Representação de grafos por **Lista de Adjacências**.
-   Representação de grafos por **Matriz de Adjacências**.
-   Representação de grafos por **Matriz de Incidência**.
-   Conversão de **Matriz de Adjacências para Lista de Adjacências**.
-   Conversão de **Lista de Adjacências para Matriz de Adjacências**.
-   **(9)** Inclusão de um novo vértice usando Lista de Adjacências e Matriz de Adjacências.
-   **(10)** Exclusão de um vértice existente usando Lista de Adjacências e Matriz de Adjacências.
-   **(13)** Busca em Largura (BFS) em grafos não-direcionados.
-   **(19)** Busca em Largura (BFS) em dígrafos.
-   **(11)** Função que determina se um grafo é conexo ou não
-   **(14)** Busca em Profundidade (DFS), com determinação de arestas de retorno
-   **(15)** Determinação de articulações e blocos (biconectividade), utilizando obrigatoriamente a função lowpt
-   **(20)** Busca em profundidade (DFS) para DIGRAFOS, com determinação de profundidade de entrada/saída e tipos de arestas



### A Implementar 🚧

#### A. Para GRAFOS (Não-Direcionados)
-   (5) Função que calcula o grau de cada vértice.
-   (6) Função que determina se dois vértices são adjacentes.
-   (7) Função que determina o número total de vértices.
-   (8) Função que determina o número total de arestas.
<!-- -   (9) Inclusão de um novo vértice usando Lista de Adjacências e Matriz de Adjacências. -->
<!-- -   (10) Exclusão de um vértice existente usando Lista de Adjacências e Matriz de Adjacências. -->
-   (12) **Determinar se um grafo é bipartido (OPC = 1,0 ponto)**
<!-- -   (13) Busca em Largura, a partir de um vértice específico. -->

#### B. Para DÍGRAFOS (Direcionados)
-   (16) Representação do Dígrafo a partir da Matriz de Adjacências.
-   (17) Representação do Dígrafo a partir da Matriz de Incidência.
-   (18) **Determinação do Grafo Subjacente (OPC= 0,5 ponto)**
<!-- -   (19) Busca em largura. -->

---

## 👨‍💻 Autores
- **Felipe Freitas Lopes**
- **Giliardo Júlio de Medeiros Júnior**
- **Ianco Soares Oliveira**
- **Kaio Eduardo Alves de Lima**
- **[COLOQUEM SEUS NOMES EM ORDEM ALFABÉTICA AQUI]**
