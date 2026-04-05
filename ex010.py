#Criando PilhaEncadeada e PilhaEncadeada a partir da ListaEncadeada
from ex009 import ListaEncadeada

class PilhaEncadeada:
    def __init__(self):
        self._motor = ListaEncadeada()

    @property
    def motor(self):
        return self._motor
    
    def ehVazia(self):
        if self.motor.tamanho == 0:
            return True
        else:
            return False
    
    def empilhar(self, valor):
        self.motor.adicionar_inicio(valor)
        return "Empilhado com sucesso!"

    def desempilhar(self):
        if self.ehVazia():
            return True
        else:
            valor = self.topo()
            self.motor.remover_inicio()
            return valor

    def topo(self):
        if self.ehVazia():
            return "Pilha Vazia."
        else:
            return str(self.motor.cabeca.valor)
        
    def tamanho_pilha(self):
        return self.motor.tamanho
    
    def esvaziar_pilha(self):
        if self.ehVazia():
            return "Pilha já vazia."
        else:
            self.motor.cabeca = None
            self.motor.tamanho = 0
            return "Pilha limpa com sucesso."

    def __str__(self):
        if self.ehVazia():
            return "Pilha Vazia no momento."
        else:
            return str(self.motor)
    
class FilaEncadeada:
    def __init__(self):
        self._motor = ListaEncadeada()

    @property
    def motor(self):
        return self._motor
    
    def ehVazio(self):
        if self.tamanho() == 0:
            return True
        else:
            return False
    
    def inserir(self, valor):
        self.motor.adicionar_final(valor)
        return "Valor adicionado com sucesso!"

    def exibir_primeiro(self):
        if self.ehVazio():
            return "Fila Vazia."
        else:
            return self.motor.cabeca.valor

    def remover(self):
        if self.ehVazio():
            return "A fila já está vazia."
        else:
            self.motor.remover_inicio()
            return "Valor removido com sucesso!"
            #Se precisar retornar o valor, terei que fazer a cauda do último valor de ListaEncadeada

    def tamanho(self):
        return self.motor.tamanho
    
    def esvaziar_fila(self):
        if self.ehVazio():
            return "A fila já está vazia."
        else:
            self.motor.tamanho = 0
            self.motor.cabeca = None
            return "Fila esvaziada com sucesso!"

    def __str__(self):
        if self.ehVazio():
            return "Fila sem elementos."
        else: 
            return str(self.motor)
    
#Programa Principal
def main():
    objeto = PilhaEncadeada()
    objeto.empilhar(10)
    objeto.empilhar(20)
    objeto.empilhar(40)
    objeto.desempilhar()
    objeto.empilhar(30)
    print(objeto)

    fila = FilaEncadeada()
    fila.inserir(10)
    fila.inserir(20)
    fila.inserir(40)
    fila.remover()
    fila.inserir(30)
    print(fila)

if __name__ == "__main__":
    main()
