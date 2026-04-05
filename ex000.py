#Criação de uma pilha para entender a lógica
class Pilha:
    def __init__(self):
        self._itens = []

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

    def topo(self):
        if len(self._itens) == 0:
            return f"ERRO --- não há topo na lista (sem itens)"
        else:
            return self._itens[len(self._itens) - 1]
        
    def tamanho(self):
        return len(self._itens)

## Programa Principal

#Testando se a pilha deu certo
objeto = Pilha()
objeto.empilhar(10)
objeto.empilhar(20)
objeto.empilhar(30)
objeto.desempilhar()
objeto.empilhar(12)
objeto.limpar_pilha()
print(objeto)
print(objeto.topo())