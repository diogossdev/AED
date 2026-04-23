#Fazendo exercício de Árvore Binária (implementando função)

#Importando Árvore Binária
from ex031 import ArvoreBinaria

#Exercício Proposto
"""
Escreva uma função que retorne a soma de todos os
valores de uma árvore binária. A função deve receber como
parâmetro o endereço da raiz da árvore.
"""

#Fazendo Função de somar valores da árvore
def somar_nos(raiz:object):
    if raiz is None:
        return 0
    else:
        valores_esquerda = somar_nos(raiz.esquerda)
        valores_direita = somar_nos(raiz.direita)

        return raiz.valor + valores_esquerda + valores_direita
    
#Testando Função
#Programa Principal
def main():
    arvore = ArvoreBinaria()
    arvore.raiz = 10
    arvore.raiz.esquerda = 20
    arvore.raiz.direita = 30
    print(arvore.contar_nos(arvore.raiz))
    print(somar_nos(arvore.raiz)) #Precisa retornar 60

if __name__ == "__main__":
    main()