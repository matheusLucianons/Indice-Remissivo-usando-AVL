# 📚 Índice Remissivo com Árvore AVL em Python

Este projeto implementa um índice remissivo de palavras a partir de um documento de texto em língua portuguesa, utilizando uma Árvore AVL como estrutura de dados principal.
O objetivo é demonstrar a aplicação prática de estruturas de dados balanceadas para indexação, busca e análise eficiente de informações textuais.

# Funcionalidades

📖 Construção automática de índice remissivo

🌳 Inserção de palavras em Árvore AVL (auto-balanceada)

🔍 Busca eficiente de palavras

📏 Cálculo do medidor de equilíbrio (ME) de um nó

🔤 Listagem alfabética das palavras indexadas

📊 Identificação da palavra mais frequente

⏱️ Medição do tempo de construção do índice

🔁 Contabilização do número de rotações da AVL

# 🧠 Tecnologias e Conceitos Utilizados

-Python 3

-Estruturas de Dados

-Árvores Binárias de Busca

-Árvores AVL

-Recursividade

-Manipulação de arquivos .txt

-Processamento de texto (normalização, remoção de acentos)

-Análise de desempenho

# 📁 Estrutura do Projeto
📂 indice-remissivo-avl/

 ├── no.py                # Estrutura do nó da árvore
 
 ├── avl.py               # Implementação da Árvore AVL
 
 ├── main.py              # Execução principal do projeto
 
 ├── texto_origem.txt     # Texto base para indexação
 
 ├── indice_remissivo.txt # Arquivo gerado com o índice
 
 └── README.md

# 📄 Arquivo de Entrada

texto_origem.txt

Texto em português com múltiplas linhas

Usado como base para a construção do índice remissivo

# 📑 Arquivo de Saída

indice_remissivo.txt

Contém:

Palavras em ordem alfabética

Linhas de ocorrência

Estatísticas finais do processamento

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com fins acadêmicos, visando consolidar conhecimentos sobre árvores AVL, balanceamento automático e organização eficiente de dados textuais.

Ele demonstra como estruturas de dados clássicas podem ser aplicadas para resolver problemas reais de indexação e busca.

# 📌 Observações

-Palavras são tratadas sem distinção entre maiúsculas e minúsculas

-Acentos são removidos para padronização

-Palavras com apenas um caractere são desconsideradas

-Linhas repetidas para uma mesma palavra são registradas apenas uma vez

# 👨‍💻 Autor

Projeto desenvolvido para a disciplina de Estruturas de Dados II, utilizando Python, VSCode e Github.
