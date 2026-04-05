#Refazendo exercício do Palíndromo com Pilha Encadeada
from ex010 import PilhaEncadeada

def verificar_palindromo(texto:str) -> bool:
    pilha = PilhaEncadeada()
    texto_normal = ''
    texto_invertido = ''
    for letra in texto:
        #poderia usar a função isalnum(), mas decidi deixar essa minha primeira ideia de solução.
        if ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122 or ord(letra) >= 48 and ord(letra) <= 57:
            texto_normal += letra
            pilha.empilhar(letra) 
    for i in range(0, pilha.tamanho_pilha()):
       texto_invertido += pilha.desempilhar()
    if texto_normal.lower() == texto_invertido.lower():
        return True
    else: 
        return False

#Programa Principal
def main():
    string = input('Digite a string e direi se ela é palíndroma: ')
    valor = verificar_palindromo(string)
    if valor:
        print('Ela é um palíndromo!')
    else:
        print('Ela não é um palíndromo.')

if __name__ == "__main__":
    main()