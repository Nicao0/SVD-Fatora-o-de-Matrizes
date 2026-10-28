# SVD (Decomposição em Valores Singulares) e Fatoração de Matrizes

***

## 1. O Conceito Matemático do SVD
A Fatoração de Matrizes e o SVD buscam decompor uma matriz grande e complexa em matrizes menores para descobrir padrões ocultos (fatores latentes) nos dados. A decomposição matemática exata do SVD transforma uma matriz `A` no produto de três matrizes:

`A = U × Σ × V^T`

*   **U**: Indica a participação das linhas originais (ex: palavras) nos conceitos latentes.
*   **Σ**: Matriz diagonal que indica a importância (peso) de cada conceito latente identificado.
*   **V^T**: Indica a participação das colunas originais (ex: documentos) nos conceitos latentes.

---

## 2. Aplicação 1: Análise Semântica Latente em Textos (Trabalho 1)
O SVD é utilizado para identificar os principais temas em uma coleção de textos não rotulados, como manchetes de notícias. 

*   **Matriz Termo-Documento (A):** As linhas representam as palavras-chave (substantivos e verbos) e as colunas representam os documentos (manchetes).
*   **Identificação de Temas Latentes:** O algoritmo agrupa palavras que aparecem juntas. No exemplo analisado, o SVD separou as manchetes em um tema dominante de "Inflação" (economia) e um tema secundário de "Jogador" (esportes).
*   **O Papel dos Verbos de Ação:** Substantivos isolados podem ser ambíguos, mas a combinação com verbos (ex: "bolsa/sobe", "jogador/marca") é fundamental para o algoritmo distinguir claramente a qual tema o documento pertence.

---

## 3. Aplicação 2: Sistemas de Recomendação (Trabalho 2)
Plataformas como Netflix e Amazon utilizam uma variação da Fatoração de Matrizes (filtragem colaborativa) para sugerir itens aos usuários.

*   **Matriz de Utilidade (R):** As linhas representam os usuários e as colunas representam os itens (filmes). Esta matriz é extremamente esparsa (cheia de vazios), pois um usuário avalia apenas uma pequena fração do catálogo.
*   **Fatores Latentes:** Em vez do SVD tradicional, o modelo decompõe a matriz `R` em duas matrizes densas: a Matriz de Usuários (`P`) e a Matriz de Itens (`Q`).
*   **Previsão de Notas:** Para prever a nota que um usuário `u` daria a um filme `i`, calcula-se o produto escalar entre o perfil do usuário e as características do filme:

`r_ui = p_u × q_i`

*   **Treinamento do Modelo:** Como há muitos dados ausentes, o modelo "aprende" minimizando o erro entre as notas previstas e as notas reais conhecidas, utilizando técnicas de otimização (como Gradiente Descendente Estocástico) e regularização para evitar o overfitting.
