#Exercício de Verificação de machos e fêmeas

#Importando lista encadeada do exercício 16
from ex016 import ListaEncadeada

'''
Utilizando a classe Lista criada na questão 1, faça um programa que leia
o nome e o sexo de vários animais. Se o animal for do sexo masculino,
insira o seu nome em uma lista chamada MACHOS. Caso contrário, insira
o nome numa lista chamada FEMEAS. Escolha uma condição de parada
para a entrada de dados a seu gosto. Ao final, devem ser exibidas as
duas listas criadas.
'''

#Programa Principal
def main():
    quantidade = int(input("Digite quantos animais serão catalogados: "))
    machos = ListaEncadeada()
    femeas = ListaEncadeada()

    for i in range(quantidade):
            print(f" --- Catalogando o {i+1}° animal ---")
            while True:
                nome = input("Digite o nome do animal: ")
                sexo = input("Digite o sexo do animal (M para Macho e F para Fêmea): ").upper()
                if sexo == "M":
                    machos.adicionar_final(nome)
                    break
                elif sexo == "F":
                    femeas.adicionar_final(nome)
                    break
                else:
                    print("Valor errado. Tente novamente.")
                    
    print(f"Lista de animais machos: {machos}")
    print((f"Lista de animais femeas: {femeas}"))

if __name__ == "__main__":
    main()