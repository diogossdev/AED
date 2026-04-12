#Exercício 19 de AED sobre Listas Encadeadas

#Importando a ListaEncadeada do exercício 16
from ex016 import ListaEncadeada

'''
Uma maneira usual de se representar um conjunto é pela lista de seus
elementos. Supondo esta representação, escreva funções para as
operações usuais de conjunto: união, interseção, diferença e pertinência.
'''

#Funções

#Função de Pertinência
def pertinencia(valor, conjunto:object):
    if type(conjunto.trocarValorPeloIndice(valor)) == int:
        return True
    else:
        return False
    
#Função de União
def uniao(conjuntoA:object, conjuntoB:object):
    uniao = ListaEncadeada()
    atualA = conjuntoA.cabeca
    atualB = conjuntoB.cabeca

    while atualA is not None:
        uniao.adicionar_inicio(atualA.valor)
        atualA = atualA.proximo

    while atualB is not None:
        if pertinencia(atualB.valor, uniao) == False:
            uniao.adicionar_inicio(atualB.valor)
        atualB = atualB.proximo

    return uniao

#Função de Interseção
def intersecao(conjuntoA:object, conjuntoB:object):
    intersecao = ListaEncadeada()
    atualA = conjuntoA.cabeca
    
    while atualA is not None:
        if pertinencia(atualA.valor, conjuntoB):
            intersecao.adicionar_inicio(atualA.valor)
        atualA = atualA.proximo

    return intersecao

#Função de Diferença
def diferenca(conjuntoA:object, conjuntoB:object):
    diferenca = ListaEncadeada()
    atualA = conjuntoA.cabeca
    
    while atualA is not None:
        if pertinencia(atualA.valor, conjuntoB) == False:
            diferenca.adicionar_inicio(atualA.valor)
        atualA = atualA.proximo

    return diferenca
        
#Programa Principal
def main():
    conjuntoA = ListaEncadeada()
    conjuntoB = ListaEncadeada()
    conjuntoA.adicionar_inicio(1)
    conjuntoA.adicionar_inicio(2)
    conjuntoA.adicionar_inicio(3)
    conjuntoA.adicionar_inicio(4)
    conjuntoB.adicionar_inicio(3)
    conjuntoB.adicionar_inicio(5)
    conjuntoB.adicionar_inicio(4)
    conjuntoB.adicionar_inicio(7)
    
    #A pertinência entre o valor 3 do conjunto A deve dar True em relação ao conjunto B
    print(pertinencia(3, conjuntoB))

    #A pertinência entre o valor 2 do conjunto A deve dar False em relação ao conjunto B
    print(pertinencia(2, conjuntoB))

    #A união deve retornar os valores 5, 7, 1, 2, 3 e 4
    print(uniao(conjuntoA, conjuntoB))

    #A interseção deve retornar os valores 3 e 4
    print(intersecao(conjuntoA, conjuntoB))

    #A diferença entre A e B deve retornar os valores 1 e 2
    print(diferenca(conjuntoA, conjuntoB))

if __name__ == "__main__":
    main()