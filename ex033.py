#Fazendo exercício de Árvore Binária (Implementando Função)

#Importando Árvore Binária
from ex031 import ArvoreBinaria

#Exercício Proposto
"""
Escreva uma função que imprima todos os elementos de
uma árvore binária que estão em um nó folha. A função
deve receber como parâmetro o endereço da raiz da árvore.
"""

#Implementando Função de retornar valores
def valores_no(raiz):
    if raiz is not None:
        #Fazendo o percorrimento usando o método "em-ordem"
        valores_no(raiz.esquerda)
        if raiz.esquerda is None and raiz.direita is None:
            print(raiz)
        valores_no(raiz.direita)

#Testando Função
#Programa Principal
def main():
    arvore = ArvoreBinaria()
    arvore.raiz = 10
    arvore.raiz.esquerda = 20
    arvore.raiz.direita = 30

    p = arvore.raiz.esquerda
    q = arvore.raiz.direita

    p.esquerda = 40
    p.direita = 50

    q.esquerda = 60
    q.direita = 70

    valores_no(arvore.raiz) #Deve retornar apenas os nós que não possuem filhos (40, 50, 60, 70)

if __name__ == "__main__":
    main()