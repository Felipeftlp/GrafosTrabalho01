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
- **`utils.py`**: Módulo com funções auxiliares e de conversão, como `matriz -> lista` e `lista -> matriz`.
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

### A Implementar 🚧

#### A. Para GRAFOS (Não-Direcionados)
-   (5) Função que calcula o grau de cada vértice.
-   (6) Função que determina se dois vértices são adjacentes.
-   (7) Função que determina o número total de vértices.
-   (8) Função que determina o número total de arestas.
-   (9) Inclusão de um novo vértice usando Lista de Adjacências e Matriz de Adjacências.
-   (10) Exclusão de um vértice existente usando Lista de Adjacências e Matriz de Adjacências.
-   (11) Função que determina se um grafo é conexo ou não.
-   (12) **Determinar se um grafo é bipartido (OPC = 1,0 ponto)**
-   (13) Busca em Largura, a partir de um vértice específico.
-   (14) Busca em Profundidade, com determinação de arestas de retorno, a partir de um vértice específico.
-   (15) Determinação de articulações e blocos (biconectividade), utilizando obrigatoriamente a função *lowpt*.

#### B. Para DÍGRAFOS (Direcionados)
-   (16) Representação do Dígrafo a partir da Matriz de Adjacências.
-   (17) Representação do Dígrafo a partir da Matriz de Incidência.
-   (18) **Determinação do Grafo Subjacente (OPC= 0,5 ponto)**
-   (19) Busca em largura.
-   (20) Busca em profundidade, com determinação de profundidade de entrada e de saída de cada vértice, e arestas de árvore, retorno, avanço e cruzamento.

---

## 👨‍💻 Autores
- **Felipe Freitas Lopes**
- **[COLOQUEM SEUS NOMES EM ORDEM ALFABÉTICA AQUI]**
