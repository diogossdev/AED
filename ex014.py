#Exercício dos guichês
from ex010 import FilaEncadeada
from ex009 import ListaEncadeada

#Funções
def adicionar_cliente(clientes, contador):
    clientes.inserir(contador)

def atender_cliente(guiches, clientes):
    if clientes.tamanho() == 0:
        return "Sem Clientes"
    else:
        atual = guiches.cabeca
        while atual is not None: 
            if atual.valor == 0:
                atual.valor = clientes.exibir_primeiro()
                clientes.remover()
                return True
            else:
                atual = atual.proximo
        return False

def limpar_guiche(guiches):
    atual = guiches.cabeca
    while atual is not None:
        if atual.valor == 0:
            atual = atual.proximo
        else:
            atual.valor = 0
            return True
    return False
        
def monitorar_fila(clientes):
    quantidade = clientes.tamanho()
    return f"Existem {quantidade} clientes na fila atualmente."

def monitorar_guiches(guiches):
    guiches_cheios = 0
    guiches_vazios = 0
    atual = guiches.cabeca
    while atual is not None:
        if atual.valor == 0:
            guiches_vazios += 1
            atual = atual.proximo
        else:
            guiches_cheios += 1
            atual = atual.proximo
    return f"Temos atualmente {guiches_vazios} guichês vazios e {guiches_cheios} guichês cheios!"
        
def proxima_senha(clientes):
    if clientes.tamanho() == 0:
        return "Não há clientes na fila e não há próxima senha."
    else:
        return f"A próxima senha a ser chamada será {clientes.exibir_primeiro()}"

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
            adicionar_cliente(clientes, contador)
            contador += 1
            print("Cliente adicionado com sucesso!")
        elif verificador == 2:
            tem_guiche = atender_cliente(guiches, clientes)
            if tem_guiche == True:
                print("Cliente indo para atendimento com sucesso!")
            elif tem_guiche == False:
                print("Todos os guichês já estavam ocupados.")
            else:
                print("Não haviam clientes na fila.")
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
            print(proxima_senha(clientes))
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