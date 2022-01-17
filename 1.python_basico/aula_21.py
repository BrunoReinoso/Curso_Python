nome = 'Bruno'
idade = 25
altura = 1.60
peso = 73.00
ano_atual = 2021

imc = peso / altura**2
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura:.2f}m de altura e pesa {peso:.2f}kgs.')
print('O imc de {} é {:.2f}'.format(nome, imc))
print('{} nasceu em {}'.format(nome, ano_nascimento))