#Exercício de Inversor de Palavras

#Classe Pilha
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
    
#Função para pegar string e inverter a palavra
def inversor(string:str) -> str:
    lista_string = Pilha()
    for i in string:
        lista_string.empilhar(i)

    lista_invertida = ""
    for i in range(lista_string.tamanho()):
        lista_invertida += lista_string.desempilhar()

    return lista_invertida

##Programa Principal
palavra = input('Digite a palavra que será invertida: ')
print(f"A palavra invertida é {inversor(palavra)}!")
        


