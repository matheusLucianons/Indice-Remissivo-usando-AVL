import re
import unicodedata
from time import time
from avl import ArvoreAVL

# Funções auxiliares

def remover_acentos(texto):
    # Remove acentos de uma string
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def extrair_palavras(linha):
    # Extrai palavras de uma linha de texto, ignorando pontuação.
    return re.findall(r"\b[a-zA-ZÀ-ÿ]+\b", linha)

# Construção do índice

def construir_indice(nome_arquivo):
    arvore = ArvoreAVL()

    total_palavras = 0
    palavras_distintas = set()
    palavras_descartadas = 0

    inicio = time()

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            palavras_linha = extrair_palavras(linha)

            for palavra in palavras_linha:
                total_palavras += 1

                palavra = palavra.lower()
                palavra = remover_acentos(palavra)

                # Palavra já vista antes?
                if palavra in palavras_distintas:
                    palavras_descartadas += 1
                else:
                    palavras_distintas.add(palavra)

                # Inserção na AVL
                arvore.raiz = arvore.inserir(arvore.raiz, palavra, numero_linha)

    fim = time()
    tempo_construcao = fim - inicio

    return (
        arvore,
        total_palavras,
        len(palavras_distintas),
        palavras_descartadas,
        tempo_construcao
    )

# Geração do índice em arquivo

def escrever_indice(arvore, nome_arquivo, total_palavras,
                    total_palavras_distintas, palavras_descartadas,
                    tempo_construcao):

    resultado = []
    arvore.em_ordem(arvore.raiz, resultado)

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        for palavra, linhas in resultado:
            linhas_str = ", ".join(str(l) for l in linhas)
            f.write(f"{palavra} {linhas_str}\n")

        f.write("\n")
        f.write(f"Total de palavras: {total_palavras}\n")
        f.write(f"Total de palavras distintas: {total_palavras_distintas}\n")
        f.write(f"Total de palavras descartadas: {palavras_descartadas}\n")
        f.write(f"Total de rotações executadas: {arvore.rotacoes}\n")
        f.write(f"Tempo de construção do índice usando árvore AVL: "
                f"{tempo_construcao:.3f}s\n")

# Programa principal

def main():
    print("Construindo índice remissivo...\n")

    (
        arvore,
        total_palavras,
        total_palavras_distintas,
        palavras_descartadas,
        tempo_construcao
    ) = construir_indice("texto_origem.txt")

    escrever_indice(
        arvore,
        "indice_remissivo.txt",
        total_palavras,
        total_palavras_distintas,
        palavras_descartadas,
        tempo_construcao
    )

    print("Índice remissivo gerado com sucesso!\n")

    # Busca exata + Medidor de Equilíbrio
    palavra_busca = "algoritmo"
    resultado_me = arvore.medidor_equilibrio(palavra_busca)

    if resultado_me == -1:
        print(f"A palavra '{palavra_busca}' não foi encontrada.")
    elif resultado_me == 0:
        print(f"A palavra '{palavra_busca}' foi encontrada "
              f"e o medidor de equilíbrio é 0.")
    else:
        _, me = resultado_me
        print(f"A palavra '{palavra_busca}' foi encontrada "
              f"e o medidor de equilíbrio é {me}.")

    # Busca por prefixo
    prefixo = "alg"
    palavras_prefixo = []
    arvore.buscar_prefixo(arvore.raiz, prefixo, palavras_prefixo)

    print(f"\nPalavras que começam com '{prefixo}':")
    print(sorted(palavras_prefixo))

    # Palavra mais frequente
    palavra, freq = arvore.palavra_mais_frequente()
    if palavra:
        print(f"\nPalavra mais frequente: '{palavra}' "
              f"(aparece em {freq} linhas)")
    else:
        print("\nNenhuma palavra encontrada.")

    # Exemplo de remoção
    print("\nExemplo de remoção:")
    removido = arvore.remover_linha(palavra_busca, 1)
    if removido:
        print(f"Linha 1 removida da palavra '{palavra_busca}'.")
    else:
        print(f"Não foi possível remover a linha da palavra '{palavra_busca}'.")

if __name__ == "__main__":
    main()