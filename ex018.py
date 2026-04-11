#Exercício de Listas Encadeadas fazendo elas "conversarem entre si"

#Importando Lista Encadeada feita no exercício 16
from ex016 import ListaEncadeada
#Importando a biblioteca random para uso de valores aleatórios
from random import randint

'''
Utilizando a classe Lista criada na questão 1, faça um programa que:
a) crie quatro listas (L1, L2, L3 e L4);
b) insira sequencialmente, na lista L1, 10 números inteiros obtidos de
forma randômica (entre 0 e 99);
c) idem para a lista L2;
d) concatene as listas L1 e L2, armazenando o resultado na lista L3;
e) armazene na lista L4 os elementos da lista L3 (na ordem inversa);
f) exiba as listas L1, L2, L3 e L4.
'''

#Programa Principal
def main():
    lista1 = ListaEncadeada()
    lista2 = ListaEncadeada()
    lista3 = ListaEncadeada()
    lista4 = ListaEncadeada()


    #criando valores aleatórios
    for i in range(10):
        lista1.adicionar_final(randint(0, 99))
        lista2.adicionar_final(randint(0, 99))

    #gerando caminhante
    atual_1 = lista1.cabeca
    atual_2 = lista2.cabeca

    #criando lista3 a partir dos valores da lista1 e lista2
    for i in range(10):
        lista3.adicionar_final(atual_1.valor)
        lista3.adicionar_final(atual_2.valor)
        atual_1 = atual_1.proximo
        atual_2 = atual_2.proximo

    #Lógica de inversão da lista3 e gerando a partir disso a lista4
    contador = 19
    for i in range(20):
        #Poderia ter usado o método adicionar_inicio() para deixar mais performático, mas só pensei depois
        lista4.adicionar_final(lista3.trocarIndicePeloValor(contador))
        contador -= 1

    #Exibindo valores das 4 listas
    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)

if __name__ == "__main__":
    main()