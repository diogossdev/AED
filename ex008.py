#Exercício --- Verificador de Palíndromos
from ex007 import Deque

#função de verificação
def verificar_palindromo(palavra:str):
    lista_palavra = Deque()

    for i in palavra:
        lista_palavra.adicionar_tras(i)
  
    while lista_palavra.tamanho() > 1:
        palavra_frente = lista_palavra.remover_frente()
        palavra_tras = lista_palavra.remover_tras()

        if palavra_frente != palavra_tras:
            return False
    return True


## Programa Principal
palavra = input('Digite uma palavra: ')

if verificar_palindromo(palavra):
    print(f'A palavra {palavra} é um palíndromo!')
else:
    print(f'A palavra {palavra} não é um palíndromo.')
