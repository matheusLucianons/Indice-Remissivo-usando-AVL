📚 Índice Remissivo com Árvore AVL em Python
---
Introdução
---
Este projeto tem como objetivo desenvolver um índice remissivo de palavras a partir de um documento de texto em língua portuguesa, utilizando uma Árvore AVL como estrutura de dados principal.

O problema consiste em organizar as palavras extraídas de um texto extenso de forma ordenada alfabeticamente, associando cada palavra às linhas em que ela aparece, sem repetição de linhas para uma mesma palavra. Além disso, o sistema deve permitir operações eficientes de inserção, busca e análise, mesmo para grandes volumes de dados.

Para resolver esse problema, foi utilizada a Árvore AVL, uma árvore binária de busca auto-balanceada, garantindo desempenho O(log n) nas operações principais. A estrutura da árvore permite manter o índice sempre ordenado, dispensando ordenações adicionais.

Estruturas de Dados Utilizadas
---
◦Árvore AVL
   -Estrutura principal para armazenamento das palavras
   -Responsável pelo balanceamento automático

◦Lista
   -Utilizada para armazenar as linhas associadas a cada palavra, sem repetição

◦Conjunto (set)
   -Utilizado para contabilizar palavras distintas e palavras descartadas (estatísticas)

◦Recursividade
   -Aplicada nas operações de inserção, busca, remoção e percursos da árvore

Documentação do Código
---
O projeto foi desenvolvido de forma modular, organizado nos seguintes arquivos:

📁 Estrutura do Projeto
---
indice-remissivo-avl/

├── no.py # Estrutura do nó da árvore

├── avl.py # Implementação da Árvore AVL

├── main.py # Execução principal do projeto

├── texto_origem.txt # Texto base para indexação

├── indice_remissivo.txt # Arquivo gerado com o índice

└── README.md

🔹 no.py
---
Define a estrutura do nó da Árvore AVL.
Cada nó armazena:

◦A palavra indexada

◦Uma lista com as linhas em que a palavra aparece (sem duplicação)

◦Referência para o filho esquerdo

◦Referência para o filho direito

◦A altura do nó, necessária para o cálculo do balanceamento

A classe também contém métodos auxiliares para adicionar e remover linhas associadas à palavra.

🔹 avl.py
---
◦Implementa a Árvore AVL, contendo:

◦Inserção de palavras na árvore

◦Atualização das alturas dos nós

◦Cálculo do fator de balanceamento

◦Rotações simples e duplas para manter a árvore balanceada

◦Busca eficiente de palavras

◦Remoção de palavras e de linhas específicas

◦Percurso em ordem para geração do índice remissivo

◦Busca por prefixo

◦Identificação da palavra mais frequente

◦Contador do número total de rotações realizadas

🔹 main.py
---
Arquivo responsável pela execução do projeto.
Suas principais responsabilidades são:

◦Leitura do arquivo texto_origem.txt

◦Extração das palavras utilizando expressões regulares

◦Normalização das palavras (conversão para minúsculas e remoção de acentos)

◦Inserção das palavras na Árvore AVL juntamente com o número da linha

◦Contabilização do total de palavras, palavras distintas e palavras descartadas

◦Medição do tempo de construção do índice

◦Escrita do índice remissivo no arquivo indice_remissivo.txt

◦Execução de buscas e análises adicionais sobre a árvore

Exemplos de Uso
Construção do índice
---
Para construir o índice remissivo, execute o arquivo principal:

python main.py

O índice será construído automaticamente a partir do arquivo texto_origem.txt, e o arquivo indice_remissivo.txt será gerado contendo as palavras em ordem alfabética, seguidas das linhas em que aparecem.

Busca de uma palavra
---
Exemplo de busca exata por uma palavra na árvore AVL:

resultado = arvore.buscar(arvore.raiz, "exemplo")

Caso a palavra seja encontrada, é possível analisar sua posição na árvore e as linhas associadas.
Caso contrário, o sistema informa que a palavra não existe no índice.

Medidor de Equilíbrio (ME)
---
Durante a busca, o programa calcula o Medidor de Equilíbrio (ME), definido como a diferença entre a quantidade de nós da subárvore esquerda e da subárvore direita do nó encontrado.

◦ME = 0 → nó perfeitamente balanceado

◦ME ≠ 0 → nó não perfeitamente balanceado

◦Palavra não encontrada → mensagem apropriada

Esse medidor é utilizado apenas para fins de análise estrutural da árvore.

Palavra mais frequente
---
O programa também identifica a palavra que aparece em maior número de linhas distintas no texto:

palavra, freq = arvore.palavra_mais_frequente()

Exemplo de saída:

Palavra mais frequente: dados (aparece em 27 linhas)

Exemplo de remoção
---
O sistema permite remover uma ocorrência específica de uma palavra em determinada linha.
Caso a palavra fique sem nenhuma linha associada, o nó é removido da árvore mantendo o balanceamento.

Observações Finais
---
◦Não há distinção entre letras maiúsculas e minúsculas

◦Acentos são removidos para padronização

◦Linhas repetidas para a mesma palavra são armazenadas apenas uma vez

◦O índice é gerado automaticamente em ordem alfabética

◦A Árvore AVL garante eficiência mesmo para textos extensos

Métricas de desempenho, como tempo de execução e número de rotações, são apresentadas ao final da execução

Autor
---
Projeto desenvolvido por Matheus Luciano para a disciplina de Estruturas de Dados II, utilizando Python, VS Code e GitHub.
