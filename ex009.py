# Criação de um nó (O Vagão)
class No:
    def __init__(self, valor):
        self._valor = valor
        self._proximo = None

    @property
    def valor(self):
        return self._valor
    
    @property
    def proximo(self):
        return self._proximo
    
    @proximo.setter
    def proximo(self, novo_valor):
        self._proximo = novo_valor


# Criação da ListaEncadeada (A Estação)
class ListaEncadeada:
    def __init__(self):
        self._cabeca = None
        self._tamanho = 0

    @property
    def cabeca(self):
        return self._cabeca
    
    @cabeca.setter
    def cabeca(self, novo_no):
        self._cabeca = novo_no

    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, valor):
        self._tamanho = valor

    #Método para adicionar nó no inicio
    def adicionar_inicio(self, novo_valor):
        novo_no = No(novo_valor)
        
        if self.tamanho == 0:
            self.cabeca = novo_no
        else:
            novo_no.proximo = self.cabeca 
            self.cabeca = novo_no 
            
        self._tamanho += 1

    #Método para adicionar nó no final
    def adicionar_final(self, novo_valor):
        novo_no = No(novo_valor)
        if self.tamanho == 0:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    #Método para remover nó no inicio
    def remover_inicio(self):
        if self.tamanho == 0:
            return "Lista Vazia."
        else:
            atual = self.cabeca
            self.cabeca = self.cabeca.proximo
            atual.proximo = None
            self.tamanho -= 1

    #Método para remover nó no final
    def remover_final(self):
        if self.tamanho == 0:
            return "Lista Vazia."
        elif self.tamanho == 1:
            self.cabeca = None
            self.tamanho -= 1
        else:
            atual = self.cabeca
            while atual.proximo.proximo is not None:
                atual = atual.proximo
            atual.proximo = None
            self.tamanho -= 1

    def adicionar_meio(self, valor, posicao:int):
        novo_no = No(valor)
        if self.tamanho == 0:
            self.cabeca = novo_no
        elif self.tamanho == 1:
            self.cabeca.proximo = novo_no
        else:
            n = 1
            atual = self.cabeca
            while n < posicao:
                atual = atual.proximo
                n += 1
            salvador = atual.proximo
            novo_no.proximo = salvador
            atual.proximo = novo_no
        self.tamanho += 1

    def remover_meio(self, posicao:int):
        if self.tamanho == 0:
            return "Lista Vazia"
        elif self.tamanho == 1:
            self.cabeca = None
            self.tamanho -= 1
        elif (self.tamanho - 1) >= posicao and self.tamanho > 1:
            atual = self.cabeca
            n = 1
            while n < posicao:
                atual = atual.proximo
                n += 1
            salvador = atual.proximo.proximo
            atual.proximo = salvador
            self.tamanho -= 1
        else:
            return "Índice maior do que a quantidade de valores da lista."
        
    #Método Universal de Adicionar
    def inserir(self, valor, posicao:int):
        if posicao <= 0 or self.tamanho == 0:
            self.adicionar_inicio(valor)
        elif posicao >= self.tamanho:
            self.adicionar_final(valor)
        else:
            self.adicionar_meio(valor, posicao)

    #Método Universal de Remover
    def remover(self, posicao:int):
        if posicao <= 0 or self.tamanho == 0:
            self.remover_inicio()
        elif posicao >= self.tamanho:
            self.remover_final()
        else:
            self.remover_meio(posicao)
            
    def __str__(self):
        atual = self.cabeca
        texto = ""
        while atual is not None:
            texto += f"[{atual.valor}] -> "
            atual = atual.proximo
        return texto + "None"
    
def main():
    minha_lista = ListaEncadeada()

    minha_lista.inserir(10, 0)
    minha_lista.inserir(40, 3)
    minha_lista.inserir(50, 4)
    minha_lista.inserir(20, 1)
    minha_lista.inserir(30, 2)
    minha_lista.remover(1)
    minha_lista.remover(2)

    print("Minha Lista Encadeada:")
    print(minha_lista)
    print(f"Tamanho total: {minha_lista.tamanho}")

if __name__ == "__main__":
    main()