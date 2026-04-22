#Fazendo exercício 3 da faculdade sobre recursividade

#Importando ListaEncadeada
from ex009 import ListaEncadeada

#Proposta de Exercício 
"""
Escreva uma função recursiva que retorne a soma dos elementos de
uma lista de números.
"""

#Função de somar valores da Lista
def soma_lista(lista:list):
    if lista.cabeca is None:
        return 0
    
    valor_atual = lista.cabeca.valor
    lista.remover_inicio()
    return valor_atual + (soma_lista(lista))

#Programa Principal
def main():
    lista = ListaEncadeada()
    lista.adicionar_final(1)
    lista.adicionar_final(2)
    lista.adicionar_final(3)
    lista.adicionar_final(4)
    lista.adicionar_final(5)
    print(soma_lista(lista)) #Deve retornar 15

if __name__ == "__main__":
    main()