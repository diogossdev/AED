#Exercício de interação do usuário com Fila Encadeada
from ex010 import FilaEncadeada

#Programa Principal
def main():
    fila = FilaEncadeada()
    while True:
        acao = int(input('''
        --- EDITOR DE FILA ---
        [1] -- Inserir
        [2] -- Remover
        [3] -- Exibir Primeiro
        [4] -- Exibir a Fila
        [5] -- Tamanho da Fila
        [6] -- Esvaziar a Fila
        [0] -- Sair
        Digite sua opção: '''))

        if acao == 1:
            valor_empilhar = input('Digite o que será acrescentado na fila: ')
            print(fila.inserir(valor_empilhar))
        elif acao == 2:
            print(fila.remover())
        elif acao == 3:
            print(fila.exibir_primeiro())
        elif acao == 4:
            print(fila)
        elif acao == 5:
            print(fila.tamanho())
        elif acao == 6:
            print(fila.esvaziar_fila())
        elif acao == 0:
            print('Saindo do programa!')
            break
        else:
            print('Ação não reconhecida. Tente novamente com valores válidos.')

if __name__ == "__main__":
    main()
