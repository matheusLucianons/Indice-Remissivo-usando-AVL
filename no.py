class No:
    
    # Classe que representa um nó da árvore AVL.
    # Cada nó armazena uma palavra do índice remissivo e a lista de linhas em que essa palavra aparece.

    def __init__(self, palavra, linha):
        self.palavra = palavra              # Palavra armazenada no nó
        self.linhas = [linha]               # Lista de linhas (sem repetição)
        self.esquerda = None                # Filho à esquerda
        self.direita = None                 # Filho à direita
        self.altura = 1                     # Altura do nó (AVL)

    def adicionar_linha(self, linha):
        # Adiciona uma linha à lista de linhas da palavra, garantindo que não haja duplicação.
        # Retorna True se a linha foi adicionada, False se já existia.
        if linha not in self.linhas:
            self.linhas.append(linha)
            return True
        return False

    def remover_linha(self, linha):
        # Remove uma linha da lista de linhas da palavra.
        # Retorna True se a linha foi removida, False se a linha não existia.
        if linha in self.linhas:
            self.linhas.remove(linha)
            return True
        return False