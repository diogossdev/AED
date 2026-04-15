#Treinando diferença entre funções recursivas e iterativas

#Fazendo exercício de Fibonacci para compreender melhor a recursividade

#Função recursiva de fatorial (retorna a lista dos primeiros n valores de fibonacci usando valor)
def fibonacci_iterativo(valor):
    lista = []
    for i in range(valor):
        if len(lista) < 2:
            lista.append(i)
        else:
            lista.append(lista[-1] + lista[-2])
    
    return lista

#Função iterativa de fatorial (retorna o valor do fibonacci dado a posição)
def fibonacci_recursivo(valor):
    if valor == 1:
        return 0
    elif valor == 2:
        return 1
    return fibonacci_recursivo(valor - 1) + fibonacci_recursivo(valor - 2)


#Programa Principal
def main():
    valores_fibonacci = 6 #Deve retornar 0, 1, 1, 2, 3, 5
    print(fibonacci_iterativo(valores_fibonacci))
    print(fibonacci_recursivo(valores_fibonacci))

if __name__ == "__main__":
    main()