#Exerício 1 da faculdade de recursividade

#Proposta do exercício
"""
Escreva uma função recursiva que calcule X^N, onde X é um número
real e N é um inteiro não negativo. Essa função pode ser definida
da seguinte forma:
"""

#Função de calcular a potência de um valor pelo seu expoente
def potencia(numero:int, expoente:int) -> int:
    if expoente < 0:
        return False
    if expoente == 0:
        return 1
    
    produto = numero * potencia(numero, (expoente - 1))

    return produto

#Programa Principal
def main():
    numero = 5
    expoente = 3
    print(potencia(numero, expoente))

if __name__ == "__main__":
    main()