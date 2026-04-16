#Fazendo exercício 2 da faculdade sobre recursividade

#Função
def fibonacci_recursivo(posicao):
    if posicao == 1:
        return 0
    elif posicao == 2:
        return 1
    
    return fibonacci_recursivo(posicao - 1) + fibonacci_recursivo(posicao - 2)

#Programa Principal
def main():
    posicao = 5
    print(fibonacci_recursivo(posicao))

if __name__ == "__main__":
    main()