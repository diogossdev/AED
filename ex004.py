#Exercício de inversor de Filas

from ex003 import Fila, Pilha

#Primeira tentativa
'''def inverter_fila(fila:list):
    alterador = Pilha()
    contador = -1
    for i in range(0, fila.tamanho()):
        valor_invertido = fila.dados[contador]
        contador -= 1
        alterador.empilhar(valor_invertido)
    return alterador.itens'''

#Segunda tentativa corrigindo Encapsulamento
def inverter_fila(fila:list):
    alterador = Pilha()
    lista_alterada = []
    for i in range(0, fila.tamanho()):
        alterador.empilhar(fila.topo())
        fila.remover()

    for i in range(0, alterador.tamanho()):
        valor_invertido = alterador.desempilhar()
        lista_alterada.append(valor_invertido)

    return lista_alterada

#Programa Principal
fila = Fila()
fila.adicionar(10)
fila.adicionar(20)
fila.adicionar(30)
fila.adicionar(40)
fila.adicionar(50)
fila.adicionar(60)
print(inverter_fila(fila))