#Treinando o uso de recursividade com PilhaEncadeada

#Importando PilhaEncadeada
from ex010 import PilhaEncadeada

#Proposta do Exercício
'''
O Problema: Você tem uma Pilha com os valores [Topo: 30, 20, 10 :Fundo].
Se você der um print(pilha), ela mostra de cima para baixo (30, depois 20, depois 10).
Seu chefe pediu para você criar uma função que imprima os valores do Fundo para o Topo (10, 20, 30).

As Regras:

Você NÃO pode usar o "Motor" (ListaEncadeada) diretamente. Você só pode usar as regras da Pilha: empilhar, desempilhar e ehVazia.

Você NÃO pode criar uma segunda pilha, nem uma lista auxiliar do Python, nem usar laço while ou for.

Você DEVE usar uma Função Recursiva.

No final, a Pilha tem que voltar a ter os mesmos elementos que tinha antes (você não pode destruir a pilha no processo).
'''

#Função de Inverter PilhaEncadeada
def inversor_pilha(pilha:object) -> object:
    if pilha.ehVazia():
        return 
    
    valor_guardado = pilha.desempilhar()

    inversor_pilha(pilha)

    print(valor_guardado)
    #Fazendo ela voltar ao estado original
    pilha.empilhar(valor_guardado)

#Programa Principal
def main():
    pilha = PilhaEncadeada()
    pilha.empilhar(10)
    pilha.empilhar(20)
    pilha.empilhar(30)
    pilha.empilhar(40)
    print(pilha)
    inversor_pilha(pilha)
    print(pilha)

if __name__ == "__main__":
    main()