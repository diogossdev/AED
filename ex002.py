#Exercício de Validador de Parênteses Balanceados

#Classe Pilha
class Pilha:
    def __init__(self):
        self._itens = []

    def __str__(self):
        return f"{self._itens}"
    
    @property
    def pilha(self):
        return self._itens
    
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
    
#Função de Balanceamento
def verifica_parenteses(expressao:str) -> bool:
    verificador = Pilha()
    for i in expressao:
        if i == ')' and verificador.tamanho() == 0:
            return False
        elif i == '(':
            verificador.empilhar(i)
        else:
            verificador.desempilhar()
        
    if verificador.tamanho() > 0:
        return False
    else:
        return True
    
#Programa Principal
teste = input('Digite seus parênteses: ')
verificador = verifica_parenteses(teste)

if verificador:
    print('parênteses abertos e fechados com sucesso!')
else:
    print('ERRO --- parênteses errados')