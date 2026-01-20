# 📚 Índice Remissivo com Árvore AVL em Python

## 📌 Introdução

Este projeto tem como objetivo desenvolver um **índice remissivo de palavras** a partir de um documento de texto em língua portuguesa, utilizando uma **Árvore AVL** como estrutura de dados principal.

O problema consiste em organizar as palavras extraídas de um texto extenso de forma **ordenada alfabeticamente**, associando cada palavra às **linhas em que ela aparece**, sem repetição de linhas para uma mesma palavra. Além disso, o sistema deve permitir **operações eficientes de inserção, busca e análise**, mesmo para grandes volumes de dados.

Para resolver esse problema, foi utilizada a **Árvore AVL**, uma árvore binária de busca auto-balanceada, garantindo desempenho **O(log n)** nas operações principais. A estrutura da árvore permite manter o índice sempre ordenado, dispensando ordenações adicionais.

---

## 🧠 Estruturas de Dados Utilizadas

- **Árvore AVL**
  - Estrutura principal para armazenamento das palavras
  - Responsável pelo balanceamento automático
- **Conjunto (`set`)**
  - Utilizado para evitar duplicação de linhas para uma mesma palavra
- **Dicionário (`dict`)**
  - Utilizado para organizar e escrever o índice final
- **Recursividade**
  - Aplicada nas operações de inserção, busca e percursos da árvore

---

## 📄 Documentação do Código

O projeto foi desenvolvido de forma modular, organizado nos seguintes arquivos:

# 📁 Estrutura do Projeto
📂 indice-remissivo-avl/

 ├── no.py                # Estrutura do nó da árvore
 
 ├── avl.py               # Implementação da Árvore AVL
 
 ├── main.py              # Execução principal do projeto
 
 ├── texto_origem.txt     # Texto base para indexação
 
 ├── indice_remissivo.txt # Arquivo gerado com o índice
 
 └── README.md


### 🔹 `no.py`

Define a estrutura do **nó da Árvore AVL**.  
Cada nó armazena:
- A palavra indexada
- Um conjunto com as linhas em que a palavra aparece
- Referência para o filho esquerdo
- Referência para o filho direito
- A altura do nó, necessária para o cálculo do balanceamento

---

### 🔹 `avl.py`

Implementa a **Árvore AVL**, contendo:
- Inserção de palavras na árvore
- Atualização das alturas dos nós
- Cálculo do fator de balanceamento
- Rotações simples e duplas para manter a árvore balanceada
- Busca eficiente de palavras
- Percurso em ordem para geração do índice remissivo
- Contador do número total de rotações realizadas

---

### 🔹 `main.py`

Arquivo responsável pela execução do projeto.  
Suas principais responsabilidades são:
- Leitura do arquivo `texto_origem.txt`
- Extração das palavras utilizando expressões regulares
- Normalização das palavras (minúsculas e remoção de acentos)
- Inserção das palavras na Árvore AVL juntamente com o número da linha
- Contabilização do total de palavras, palavras distintas e palavras descartadas
- Medição do tempo de construção do índice
- Escrita do índice remissivo no arquivo `indice_remissivo.txt`
- Busca de palavras na árvore
- Identificação da palavra mais frequente

---

## ▶️ Exemplos de Uso

### 🔍 Construção do índice

Para construir o índice remissivo, execute o arquivo principal:

```bash
python main.py
```
O índice será construído automaticamente a partir do arquivo texto_origem.txt, e o arquivo indice_remissivo.txt será gerado contendo as palavras em ordem alfabética.

🔎 Busca de uma palavra

Exemplo de busca por uma palavra na árvore AVL:

buscarPalavra(arvore, "exemplo")

Saída esperada:

A palavra 'exemplo' foi encontrada.
O medidor de equilíbrio é 0.
A palavra aparece nas linhas: [3, 15, 42]

Caso a palavra não seja encontrada:

A palavra 'exemplo' não foi encontrada.

📏 Medidor de Equilíbrio (ME)

Durante a busca, o programa calcula o Medidor de Equilíbrio (ME), definido como a diferença entre a quantidade de nós da subárvore esquerda e da subárvore direita do nó encontrado.

- ME = 0 → nó balanceado

- ME ≠ 0 → nó não perfeitamente balanceado

- Palavra não encontrada → mensagem apropriada

📊 Palavra mais frequente

O programa também identifica a palavra que aparece em mais linhas distintas no texto:

palavraMaisFrequente(arvore)

Exemplo de saída:

A palavra mais frequente é 'dados', que aparece em 27 linhas.

📌 Observações Finais

- Não há distinção entre letras maiúsculas e minúsculas

- Acentos são removidos para padronização

- Palavras com apenas um caractere são desconsideradas

- Linhas repetidas para a mesma palavra são armazenadas apenas uma vez

- A Árvore AVL garante eficiência mesmo para textos extensos

👨‍💻 Autor

Projeto desenvolvido para a disciplina de Estruturas de Dados II, utilizando Python, VSCode e GitHub.
