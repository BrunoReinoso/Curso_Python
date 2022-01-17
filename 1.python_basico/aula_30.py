def par_ou_impar():
    numero = input("Digite um número inteiro: ")

    try:
        if numero.isnumeric:
            numero = int(numero)
        
            if numero % 2 == 0:
                print("Par!")
            else:
                print("Ímpar")
    except:
        print("Por favor, digite um número inteiro! ")

def saudacao():
    h = input("Digite a hora atual no formato 0-23 (apenas a hora): ")

    try:
        h = int(h)
        if h >= 0 and h <= 11:
            print("Bom dia!")
        elif h <= 17:
            print("Boa tarde!")
        elif h <= 23:
            print("Boa noite!")
        else:
            print("Valor fora da faixa solicitada!")
    except:
        print("Por favor, digite um número inteiro!")

def tamanho_nome():
    nome = input("Digite seu nome: ")
    tamanho = len(nome)

    if tamanho <= 4:
        print("Seu nome é curto")
    elif tamanho <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande!")


if __name__ == '__main__':
    #par_ou_impar()
    saudacao()
    #tamanho_nome()