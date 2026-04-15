#Treinando o uso de recursividade com PilhaEncadeada

#Importando PilhaEncadeada
from ex010 import PilhaEncadeada

#Proposta do Exercício
'''
Crie uma função recursiva chamada somar_pilha(pilha).
Ela deve retornar a soma de todos os números dentro da pilha, sem usar o tamanho e sem usar laços while/for.
E o mais importante: após somar, a pilha tem que voltar ao seu estado original.
'''

#Função de Inverter PilhaEncadeada
def somar_pilha(pilha):
    if pilha.ehVazia():
        return 0
    
    valor_guardado = int(pilha.desempilhar())

    valor_funcao = somar_pilha(pilha)

    pilha.empilhar(valor_guardado)

    soma = valor_guardado + valor_funcao
    return soma

#Programa Principal
def main():
    pilha = PilhaEncadeada()
    pilha.empilhar(10)
    pilha.empilhar(20)
    pilha.empilhar(30) #Precisa retornar 60

    print(f"A soma dos valores da pilha é {somar_pilha(pilha)}.")

if __name__ == "__main__":
    main()