#Exercício de Sistema de Atendimento de Clínica (Prioridades)
from ex003 import Fila

#Programa Principal
fila_normal = Fila()
fila_prioridade = Fila()

fila_normal.adicionar('Diogo')
fila_normal.adicionar('Vivi')
fila_normal.adicionar('Kaique')
fila_normal.adicionar('Juju')

fila_prioridade.adicionar('Titã')
fila_prioridade.adicionar('Aurora')
fila_prioridade.adicionar('Floquinha')
fila_prioridade.adicionar('Marceline')
fila_prioridade.adicionar('Tom-Tom')
fila_prioridade.adicionar('Lua')
fila_prioridade.adicionar('Nina')

while fila_normal.ehVazio() == False or fila_prioridade.ehVazio() == False:
    print(f'fila normal atualmente: {fila_normal.dados}')
    print(f'fila prioritária atualmente: {fila_prioridade.dados}')

    #condicional para impedir do programa chamar o método remover inutilmente
    if fila_normal.ehVazio() != True:
        fila_normal.remover()
    if fila_prioridade.ehVazio() != True:
        fila_prioridade.remover()
    if fila_prioridade.ehVazio() != True:
        fila_prioridade.remover()

print('Fila vazia. Pacientes atendidos com sucesso!')
