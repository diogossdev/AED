#Exercício dos guichês
from ex010 import FilaEncadeada
from ex009 import ListaEncadeada

'''Quando voltar --- corrgir funções e anotar principais erros + fazer novos exercícios de fixação
    Tomar cuidado com caminhante - loop de ponteiros infinitos - atribuições erradas - lógica incompleta e falha
'''

#Funções
def adicionar_cliente(clientes, contador):
    clientes.inserir(contador)

def atender_cliente(guiches, clientes):
    atual = guiches.cabeca
    if atual.valor == 0:
        atual.valor = clientes.cabeca.valor
        clientes.remover()
        return True
    else:
        if atual.proximo == None:
            return False
        else:
            atual.proximo

def limpar_guiche(guiches):
    atual = guiches
    while True:
        if atual.cabeca.valor == 0 and atual.cabeca.proximo != None:
            atual.cabeca.proximo
        elif atual.cabeca.valor != 0:
            atual.cabeca.valor = 0
            return True
        else:
            return False
        
def monitorar_fila(clientes):
    quantidade = clientes.tamanho()
    return f"Existem {quantidade} clientes na fila atualmente."

def monitorar_guiches(guiches):
    guiches_cheios = 0
    guiches_vazios = 0
    atual = guiches.cabeca
    while atual is not None:
        if atual.cabeca.valor == 0:
            guiches_vazios += 1
            atual.proximo
        else:
            guiches_cheios += 1
            atual.proximo
    return f"Temos atualmente {guiches_vazios} guichês vazios e {guiches_cheios} cheios!"
        
def proxima_senha(clientes):
    return f"A senha atual é {clientes.cabeca.valor} e a próxima senha é {clientes.cabeca.proximo.valor}"

#Programa Principal
def main():
    guiches = ListaEncadeada()
    quantidade_guiches = int(input("Quantos guichês a empresa terá? "))
    for i in range(quantidade_guiches):
        guiches.adicionar_final(0)

    clientes = FilaEncadeada()
    contador = 1

    while True:
        verificador = int(input('''
        Digite o número para realizar o que irá acontecer:
        1- novo cliente para fila;
        2- atender cliente da fila;
        3- limpar guichê (cliente atendido);
        4- monitorar fila atualmente;
        5- monitorar guichês atualmente;
        6- número da próxima senha;
        7- pedir para sair.
        Número: '''))

        if verificador == 1:
            adicionar_cliente(contador)
            contador += 1
            print("Cliente adicionado com sucesso!")
        elif verificador == 2:
            tem_guiche = atender_cliente(guiches, clientes)
            if tem_guiche:
                print("cliente indo para atendimento com sucesso!")
            else:
                print("Todos os guichês estavam já ocupados.")
        elif verificador == 3:
            limpando_guiche = limpar_guiche(guiches)
            if limpando_guiche:
                print("Guichê limpo com suceso!")
            else:
                print("Todos os guichês já estão vazios!")
        elif verificador == 4:
            print(monitorar_fila(clientes))
        elif verificador == 5:
            print(monitorar_guiches(guiches))
        elif verificador == 6:
            proxima_senha(clientes)
        elif verificador == 7:
            if limpar_guiche(guiches) == False and clientes.tamanho() == 0:
                break
            else:
                print("ERRO --- Ainda há clientes no sistema ---")
        else:
            print("Valor Inválido. Digite novamente.")

    print("programa terminado com sucesso!")

if __name__ == "__main__":
    main()