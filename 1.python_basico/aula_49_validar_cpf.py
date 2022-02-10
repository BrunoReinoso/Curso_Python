exemplo_cpf = '158.108.477-30'

comeco, final = exemplo_cpf.split('-')

comeco = comeco.split('.')

numeros = []

for i in range(0,3):
    digitos = list(comeco[i])
    numeros.append(int(digitos[0]))
    numeros.append(int(digitos[1]))
    numeros.append(int(digitos[2]))

soma_comeco = 0

for indice, regressiva in enumerate(range(10,1,-1)):
    soma_comeco += numeros[indice] * regressiva

conta_1 = 11 - (soma_comeco % 11)
digito_1 = 0 if conta_1 > 9 else conta_1
numeros.append(digito_1)

final = list(final)
final[0], final[1] = int(final[0]), int(final[1])

soma_final = 0

for indice, regressiva in enumerate(range(11,1,-1)):
    soma_final += numeros[indice] * regressiva

conta_2 = 11 - (soma_final % 11)
digito_2 = 0 if conta_2 > 9 else conta_2

if final[0] == digito_1 and final[1] == digito_2:
    print(f"Cpf {exemplo_cpf} validado com sucesso.")
else:
    print(f"O Cpf {exemplo_cpf} não pode ser validado.")