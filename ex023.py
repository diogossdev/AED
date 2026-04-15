#Treinando diferença entre funções recursivas e iterativas

#Fazendo exercício de fatorial para compreender melhor a recursividade

#Função recursiva de fatorial
def fatorial_recursivo(valor:int) -> int:
    if valor <= 1:
        return 1
    
    return valor*(fatorial_recursivo(valor-1))

#Função iterativa de fatorial
def fatorial_iterativo(valor:int) -> int:
    valor_final = 1
    for i in range(1, (valor + 1)):
        valor_final *= i
    return valor_final

#Programa Principal
def main():
    valor = 4
    print(fatorial_iterativo(valor))
    print(fatorial_recursivo(valor))

if __name__ == "__main__":
    main()