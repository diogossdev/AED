#Realocando ListaEncadeada para novos exercícios

#Criando Nó novamente
class No:
    def __init__(self, valor):
        self._valor = valor
        self._proximo = None

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor

    @property
    def proximo(self):
        return self._proximo
    
    @proximo.setter
    def proximo(self, novo_proximo):
        self._proximo = novo_proximo

#Adicionando Lista Encadeada com novas implementações
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

    #Método para adicionar valores usando a posição
    def adicionar_posicao(self, valor, posicao:int):
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

    #Método para obter posição a partir de conteúdo (valor)
    def trocarValorPeloIndice(self, valor):
        if self.ehVazia():
            return "Não há elementos na lista para ser visto."
        else:
            atual = self.cabeca
            posicao = 0
            while atual is not None:
                if atual.valor == valor:
                    return posicao
                else:
                    posicao += 1
                    atual = atual.proximo
            return "Não há elementos com esse valor dado."

    #Método para obter valor a partir da posição
    def trocarIndicePeloValor(self, posicao):
        if self.ehVazia():
            return "Não há elementos na lista para ser visto."
        else:
            atual = self.cabeca
            posicao_atual = 0
            while atual is not None:
                if posicao_atual == posicao:
                    return atual.valor
                else:
                    posicao_atual += 1
                    atual = atual.proximo
            return "Não há elementos na lista com o índice dado."

    #Método para verificar se a lista está vazia
    def ehVazia(self):
        if self.tamanho == 0:
            return True
        else:
            return False
        
    #Método para esvaziar a lista (zerar ela novamente)
    def limpar_lista(self):
        self.cabeca = None
        self.tamanho = 0

    #Método de remover usando o índice (posição)
    def remover_posicao(self, posicao:int):
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
        
    #Método de remover usando o conteúdo (valor)
    def remover_valor(self, valor):
        if self.tamanho == 0:
            return "Lista Vazia"
        
        atual = self.cabeca
        caminhante_anterior = self.cabeca

        if atual.valor == valor:
            self.remover_inicio()
            return "Valor removido com sucesso!"
        else:
            atual = atual.proximo

        while atual is not None:
            if atual.valor == valor and atual.proximo is not None:
                referencia = atual.proximo
                caminhante_anterior.proximo = referencia
                self.tamanho -= 1
                return "Valor removido com Sucesso!"
            elif atual.valor == valor and atual.proximo is None:
                self.remover_final()
                return "Valor removido com sucesso!"
            else:
                atual = atual.proximo
                caminhante_anterior = caminhante_anterior.proximo

        return "Esse valor não existe na lista atualmente."
      
    def __str__(self):
        atual = self.cabeca
        texto = ""
        while atual is not None:
            texto += f"[{atual.valor}] -> "
            atual = atual.proximo
        return texto + "None"
    

#Programa Principal
def main():
    objeto = ListaEncadeada()
    objeto.adicionar_final(10)
    objeto.adicionar_final(20)
    objeto.adicionar_final(30)
    objeto.adicionar_final(40)
    print(objeto.trocarIndicePeloValor(0))


if __name__ == "__main__":
    main()