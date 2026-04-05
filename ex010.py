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
            return "Lista Vazia."
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
            return "Lista Vazia no momento."
        else:
            return str(self.motor)
    
class FilaEncadeada:
    def __init__(self):
        self._motor = ListaEncadeada()

    @property
    def motor(self):
        return self._motor
    
    def adicionar(self, valor):
        self.motor.adicionar_inicio(valor)

    def remover(self):
        self.motor.remover_final()

    def __str__(self):
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
    fila.adicionar(10)
    fila.adicionar(20)
    fila.adicionar(40)
    fila.remover()
    fila.adicionar(30)
    print(fila)

if __name__ == "__main__":
    main()
