#Primeiro exemplo de recursividade

#Função recursiva
def somar_ate_n(n:int):
    if n <= 1:
        return n
    else:
        return (n + somar_ate_n(n-1))
        #resultado deu 15... isso deve indicar que ele guarda o valor de todas as funções até chegar na pausa.
    
#Programa Principal
def main():
    print(somar_ate_n(5))

if __name__ == "__main__":
    main()