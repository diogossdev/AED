#Criação de um deque para aprender
class Deque:
    def __init__(self):
        self._dados = []

    @property
    def dados(self):
        return self._dados
    
    def __str__(self):
        return f"{self.dados}"

    def adicionar_frente(self, novo_dado):
        self.dados.insert(0, novo_dado)

    def adicionar_tras(self, novo_dado):
        self.dados.append(novo_dado)

    def remover_frente(self):
        if self.ehVazio():
            return "ERRO --- Deque Vazio"
        else:
            return self.dados.pop(0)
    
    def remover_tras(self):
        if self.ehVazio():
            return "ERRO --- Deque Vazio"
        else:
            return self.dados.pop()
    
    def ehVazio(self):
        return len(self.dados) == 0
    
    def topo(self):
        if self.ehVazio():
            return "ERRO --- Deque Vazio"
        else:
            return self.dados[0]
        
    def final(self):
        if self.ehVazio():
            return "ERRO --- Deque Vazio"
        else:
            return self.dados[-1] 
    
    def tamanho(self):
        return len(self.dados)
