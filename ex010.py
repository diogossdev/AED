#Criando PilhaEncadeada e PilhaEncadeada a partir da ListaEncadeada
from ex009 import ListaEncadeada

class PilhaEncadeada:
    def __init__(self):
        self._motor = ListaEncadeada()

    @property
    def motor(self):
        return self._motor
    
    def empilhar(self, valor):
        self.motor.adicionar_inicio(valor)

    def desempilhar(self):
        self.motor.remover_inicio()

    def __str__(self):
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
