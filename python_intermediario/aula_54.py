#  1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.


def fsaudacao(saudacao, nome):
    print(saudacao, nome)


s, n = "Oi", "Eduarda"

fsaudacao("Olá", "Bruno")
fsaudacao(s, n)

#  2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.


def fsoma(n1, n2, n3):
    print(n1 + n2 + n3)


n1, n2, n3 = 5, 3, 4

fsoma(1, 2, 3)
fsoma(n1, n2, n3)

#  3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual.
#  Retorne o valor do primeiro número somado do aumento do percentual do mesmo.


def fpercentual(numero, percent):
    return numero * (1 + percent / 100)


numero = 2
percent = 10

print(fpercentual(100, 20))
print(fpercentual(numero, percent))

#  4 - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5, return buzz.
#  Se o parâmetro da função for divisível por 5 e por 3, reotrne FizzBuzz, caso contrário retorne o número enviado.


def Fizz_Buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n

n = 30

print(Fizz_Buzz(10))
print(Fizz_Buzz(n))