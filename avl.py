from no import No
class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.rotacoes = 0

# Funções auxiliares AVL

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def atualizar_altura(self, no):
        no.altura = 1 + max(self.altura(no.esquerda),
                            self.altura(no.direita))

# Rotações

    def rotacao_direita(self, y):
        self.rotacoes += 1

        x = y.esquerda
        t2 = x.direita

        x.direita = y
        y.esquerda = t2

        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x

    def rotacao_esquerda(self, x):
        self.rotacoes += 1

        y = x.direita
        t2 = y.esquerda

        y.esquerda = x
        x.direita = t2

        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y

# Inserção

    def inserir(self, no, palavra, linha):
        if not no:
            return No(palavra, linha)

        if palavra < no.palavra:
            no.esquerda = self.inserir(no.esquerda, palavra, linha)
        elif palavra > no.palavra:
            no.direita = self.inserir(no.direita, palavra, linha)
        else:
            # Palavra já existe => adiciona linha
            no.adicionar_linha(linha)
            return no

        self.atualizar_altura(no)
        balance = self.fator_balanceamento(no)

        # Casos de desbalanceamento
        if balance > 1 and palavra < no.esquerda.palavra:
            return self.rotacao_direita(no)

        if balance < -1 and palavra > no.direita.palavra:
            return self.rotacao_esquerda(no)

        if balance > 1 and palavra > no.esquerda.palavra:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        if balance < -1 and palavra < no.direita.palavra:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

# Busca exata

    def buscar(self, no, palavra):
        if not no or no.palavra == palavra:
            return no

        if palavra < no.palavra:
            return self.buscar(no.esquerda, palavra)

        return self.buscar(no.direita, palavra)

# Remoção de nó AVL

    def _minimo(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def remover_no(self, no, palavra):
        if not no:
            return no

        if palavra < no.palavra:
            no.esquerda = self.remover_no(no.esquerda, palavra)
        elif palavra > no.palavra:
            no.direita = self.remover_no(no.direita, palavra)
        else:
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda

            temp = self._minimo(no.direita)
            no.palavra = temp.palavra
            no.linhas = temp.linhas
            no.direita = self.remover_no(no.direita, temp.palavra)

        self.atualizar_altura(no)
        balance = self.fator_balanceamento(no)

        # Rebalanceamento
        if balance > 1 and self.fator_balanceamento(no.esquerda) >= 0:
            return self.rotacao_direita(no)

        if balance > 1 and self.fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        if balance < -1 and self.fator_balanceamento(no.direita) <= 0:
            return self.rotacao_esquerda(no)

        if balance < -1 and self.fator_balanceamento(no.direita) > 0:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

# Remoção por linha

    def remover_linha(self, palavra, linha):
        no = self.buscar(self.raiz, palavra)
        if not no:
            return False

        removido = no.remover_linha(linha)
        if removido and len(no.linhas) == 0:
            self.raiz = self.remover_no(self.raiz, palavra)

        return removido

# Percurso em ordem

    def em_ordem(self, no, resultado):
        if no:
            self.em_ordem(no.esquerda, resultado)
            resultado.append((no.palavra, sorted(no.linhas)))
            self.em_ordem(no.direita, resultado)

# Busca por prefixo

    def buscar_prefixo(self, no, prefixo, resultado):
        if not no:
            return

        if no.palavra.startswith(prefixo):
            resultado.append(no.palavra)

        if prefixo <= no.palavra:
            self.buscar_prefixo(no.esquerda, prefixo, resultado)

        if prefixo >= no.palavra[:len(prefixo)]:
            self.buscar_prefixo(no.direita, prefixo, resultado)

# Medidor de Equilíbrio (ME)

    def contar_nos(self, no):
        if not no:
            return 0
        return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)

    def medidor_equilibrio(self, palavra):
        no = self.buscar(self.raiz, palavra)
        if not no:
            return -1

        me = self.contar_nos(no.esquerda) - self.contar_nos(no.direita)
        if me == 0:
            return 0
        return 1, me

# Palavra mais frequente

    def palavra_mais_frequente(self):
        resultado = {"palavra": None, "freq": 0}

        def percorrer(no):
            if no:
                if len(no.linhas) > resultado["freq"]:
                    resultado["palavra"] = no.palavra
                    resultado["freq"] = len(no.linhas)
                percorrer(no.esquerda)
                percorrer(no.direita)
                
        percorrer(self.raiz)
        return resultado["palavra"], resultado["freq"]