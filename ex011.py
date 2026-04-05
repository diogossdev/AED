#Exercício de interação do usuário com a PilhaEncadeada
from ex010 import PilhaEncadeada

#Programa Principal

def main():
    pilha = PilhaEncadeada()
    while True:
        acao = int(input('''
        --- EDITOR DE PILHA ---
        [1] -- Empilhar
        [2] -- Desempilhar
        [3] -- Exibir Elemento do Topo
        [4] -- Exibir a Pilha
        [5] -- Tamanho da Pilha
        [6] -- Esvaziar a Pilha
        [0] -- Sair
        Digite sua opção: '''))

        if acao == 1:
            valor_empilhar = input('Digite o que será empilhado: ')
            print(pilha.empilhar(valor_empilhar))
        elif acao == 2:
            print(pilha.desempilhar())
        elif acao == 3:
            print(pilha.topo())
        elif acao == 4:
            print(pilha)
        elif acao == 5:
            print(pilha.tamanho_pilha())
        elif acao == 6:
            print(pilha.esvaziar_pilha())
        elif acao == 0:
            print('Saindo do programa!')
            break
        else:
            print('Ação não reconhecida. Tente novamente com valores válidos.')

if __name__ == "__main__":
    main()