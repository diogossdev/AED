#Implementando uma Fila na prática
class Fila:
    def __init__(self):
        self._dados = []

    @property
    def dados(self):
        return self._dados
    
    def __str__(self):
        return f"{self.dados}"
    
    def adicionar(self, valor):
        self.dados.append(valor)

    def remover(self):
        if self.ehVazio():
            return "ERRO --- Fila Vazia"
        else:
            return self.dados.pop(0)
    
    def ehVazio(self):
        return len(self.dados) == 0
    
    def tamanho(self):
        return len(self.dados)
    
    def topo(self):
        if self.ehVazio():
            return "ERRO --- Fila Vazia"
        else:
            return self.dados[0]
        
#Deixando Pilha aqui para Modularização nos exercícios
class Pilha:
    def __init__(self):
        self._itens = []

    @property
    def itens(self):
        return self._itens

    def __str__(self):
        return f"{self._itens}"
    
    def limpar_pilha(self):
        self._itens = []
    
    def empilhar(self, novo_item):
        self._itens.append(novo_item)

    def desempilhar(self):
        if len(self._itens) == 0:
            return f"ERRO --- não há itens na lista para ser removido."
        else:
            return self._itens.pop()
        
    def ehVazia(self):
        return len(self._itens) == 0

    def topo(self):
        if len(self._itens) == 0:
            return f"ERRO --- não há topo na lista (sem itens)"
        else:
            return self._itens[len(self._itens) - 1]
        
    def tamanho(self):
        return len(self._itens)