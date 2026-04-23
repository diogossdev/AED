#Criando minha própria árvore binária

#Nó da Árvore Binária
class No:
    def __init__(self, valor):
        self._valor = valor
        self._esquerda = None
        self._direita = None
        self._pai = None

    #Propriedades do Nó esquerdo
    @property
    def esquerda(self):
        return self._esquerda
    @esquerda.setter
    def esquerda(self, nova_esquerda):
        self._esquerda = No(nova_esquerda)
        self._esquerda._pai = self

    #Propriedades do Nó direito
    @property
    def direita(self):
        return self._direita
    @direita.setter
    def direita(self, nova_direita):
        self._direita = No(nova_direita)
        self._direita._pai = self

    #Propriedades do Nó Pai
    @property
    def pai(self):
        return self._pai
    @pai.setter
    def pai(self, novo_pai):
        self._pai = novo_pai
        
    #Propriedade do Valor de um Nó
    @property
    def valor(self):
        return self._valor
    
    def __str__(self):
        return f"{self.valor}"
    

#Criando a Estrutura de Dados --- Árvore Binária
class ArvoreBinaria:
    def __init__(self):
        self._raiz = None

    #Propriedades da raiz
    @property
    def raiz(self):
        return self._raiz
    @raiz.setter
    def raiz(self, valor_raiz):
        self._raiz = No(valor_raiz)

    def pre_ordem(self, no_raiz):
        if no_raiz is not None:
            print(no_raiz)
            self.pre_ordem(no_raiz.esquerda)
            self.pre_ordem(no_raiz.direita)

    def em_ordem(self, no_raiz):
        if no_raiz is not None:
            self.em_ordem(no_raiz.esquerda)
            print(no_raiz)
            self.em_ordem(no_raiz.direita)

    def pos_ordem(self, no_raiz):
        if no_raiz is not None:
            self.pos_ordem(no_raiz.esquerda)
            self.pos_ordem(no_raiz.direita)
            print(no_raiz)

    #Métodos de contar nós
    def contar_nos(self, no_raiz):
        if no_raiz is None:
            return 0
        else:
            contar_nos_esquerda = self.contar_nos(no_raiz.esquerda)
            contar_nos_direita = self.contar_nos(no_raiz.direita)
            return 1 + contar_nos_esquerda + contar_nos_direita
        
    #Método de somar valores numéricos
    def somar_valores(self, no_raiz):
        if no_raiz is None:
            return 0
        else:
            valores_esquerda = self.somar_valores(no_raiz.esquerda)
            valores_direita = self.somar_valores(no_raiz.direita)
            return no_raiz.valor + valores_esquerda + valores_direita
        
    #Método para verificar se um nó é esquerda
    def ehEsquerda(self, no):
        if no.pai is None:
            return False
        else:
            if no is no.pai.esquerda:
                return True
            else:
                return False
            
    #Método para verificar se um nó é direita
    def ehDireita(self, no):
        if no.pai is None:
            return False
        else:
            if no is no.pai.direita:
                return True
            else:
                return False
        
    #Método de buscar o irmão de algum nó
    def valor_irmao(self, no):
        if no.pai is None:
            return None
        else:
            if self.ehEsquerda(no):
                return no.pai.direita
            else:
                return no.pai.esquerda

#Programa Principal
def main():
    arvore = ArvoreBinaria()
    arvore.raiz = 10
    arvore.raiz.esquerda = 20
    arvore.raiz.direita = 30

    no_esquerdo = arvore.raiz.esquerda
    no_direito = arvore.raiz.direita

    no_esquerdo.esquerda = 40
    no_esquerdo.direita = 50
    no_direito.esquerda = 60

    arvore.em_ordem(arvore.raiz)
    print(arvore.contar_nos(arvore.raiz)) #deve retornar 6
    print(arvore.somar_valores(arvore.raiz)) #deve retornar 210

    #Verificando métodos que usa o pai
    print(arvore.ehEsquerda(no_esquerdo)) #deve retornar True
    print(arvore.ehEsquerda(no_direito)) #deve retornar False
    print(arvore.ehDireita(no_direito)) #deve retonar True
    print(arvore.ehDireita(no_esquerdo)) #deve retornar False
    print(arvore.ehDireita(arvore.raiz)) #deve retornar False

    print(arvore.valor_irmao(arvore.raiz)) #deve retornar None
    print(arvore.valor_irmao(no_direito)) #deve retornar 20
    print(arvore.valor_irmao(no_esquerdo)) #deve retornar 30
    print(arvore.valor_irmao(no_direito.esquerda)) #deve retornar None

if __name__ == "__main__":
    main()
            