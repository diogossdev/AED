#Treinando recursividade com Lista Encadeada

#Importando a Lista Encadeada
from ex010 import FilaEncadeada

#Função para inverter Fila
def inverter_fila(fila):
    if fila.ehVazio():
        return
    
    guardar_valor = fila.exibir_primeiro()
    fila.remover()

    inverter_fila(fila)

    fila.inserir(guardar_valor)
    print(fila)


#Programa Principal
def main():
    fila = FilaEncadeada()
    fila.inserir(10)
    fila.inserir(20)
    fila.inserir(30)
    fila.inserir(40)
    print(fila)
    inverter_fila(fila)

if __name__ == "__main__":
    main()