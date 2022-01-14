# 1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.

def func1(*args):
    return args

def func2():
    return 

print(func1(func2))

# 2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
#     Faça a função 1 executar duas funções que recebam um número diferente de argumentos.

def func1_2(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def soma(n1, n2):
    n3 = n1 + n2
    return n3

def nome(nome):
    return nome

executando1 = func1_2(soma, n1=2, n2=3)
executando2 = func1_2(nome, 'bruno')

print(executando1, executando2)