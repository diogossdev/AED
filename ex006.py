#Exercício da Batata Quente
from ex003 import Fila

#função da batata quente
def batata_quente(nomes:list, num_passes:int):
    fila = Fila()
    for i in nomes:
        fila.adicionar(i)
    while fila.tamanho() > 1:
        for i in range(num_passes):
            fila.adicionar(fila.topo())
            fila.remover()
        fila.remover()
    return fila.topo()

#Programa Principal
lista = []

quantidade_nomes = int(input('Digite a quantidade de participantes da batata quente: '))
for i in range(1, quantidade_nomes + 1):
    nome = input(f'Digite o nome do participante {i} da competição: ')
    lista.append(nome)

num_passes = int(input('Muito bem! Agora digite o número de voltas que cada rodada terá: '))

print("Perfeito, agora executando brincadeira!")
print(f"O ganhador da batata quente foi {batata_quente(lista, num_passes)}!")
