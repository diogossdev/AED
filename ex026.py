#Exercitando o uso de recursividade com Listas Encadeadas

#Importando Lista Encadeada
from ex009 import ListaEncadeada

#Função de inverter Lista Encadeada
def inverter_lista(atual):
    if atual.proximo is not None:
        inverter_lista(atual.proximo)

    print(f"{atual.valor}")
    return

#Programa Principal
def main():
    lista = ListaEncadeada()
    lista.adicionar_final(10)
    lista.adicionar_final(20)
    lista.adicionar_final(30)
    lista.adicionar_final(40)
    print(lista)
    inverter_lista(lista.cabeca)

if __name__ == "__main__":
    main()