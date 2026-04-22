#Primeira questão de árvore da lista da faculdade

#Importando Árvore Binária
from ex020 import Arvore_Binaria

#Proposta de exercício
"""
Escreva uma função que retorne a soma de todos os
valores de uma árvore binária. A função deve receber como
parâmetro o endereço da raiz da árvore.
"""

#Função da soma dos valores da Árvore
def soma_arvore(arvore):
    if arvore.root is None:
        return 0
    else:
        return 

#Programa Principal
def main():
    arvore = Arvore_Binaria()
    arvore.root = 1
    arvore.root.esq = 2
    arvore.root.dir = 3

    esquerda = arvore.root.esq
    direita = arvore.root.dir
    
    print(arvore.root.dado)
    print(esquerda)
    print(direita)
    print(soma_arvore(arvore))

if __name__ == "__main__":
    main()