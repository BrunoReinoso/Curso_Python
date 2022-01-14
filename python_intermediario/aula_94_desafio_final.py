import os

def valida_cnpj():
    os.system("clear") or None
    cnpj = list((input("Digite aqui o CNPJ em questão: ")))
    cnpj = [x for x in cnpj if x.isnumeric()]

    if len(cnpj) != 14:
        input(
            f"O CNPJ digitado tem {len(cnpj)} números.\nA quantidade correta é 14.\nPor favor, tente novamente."
        )
        return

    cnpj = [int(x) for x in cnpj]
    *cnpj, final_1, final_2 = cnpj

    if analisa_digito(cnpj, final_1, 5):
        cnpj.append(final_1)
        if analisa_digito(cnpj, final_2, 6):
            cnpj.append(final_2)
        else:
            return
    else:
        return

    input(f'O CNPJ {monta_cnpj(cnpj)} é válido!')

def analisa_digito(cnpj, numero, multiplicador):
    somador = 0

    for c in cnpj:
        somador += c * multiplicador
        multiplicador -= 1
        if multiplicador < 2:
            multiplicador = 9

    formula = 11 - (somador % 11)

    if formula > 9:
        digito = 0
    else:
        digito = formula

    if digito != numero:
        input('CNPJ inválido!')
        return False

    else:
        return True

def monta_cnpj(cnpj):
    contador = 0
    string = ''

    for c in cnpj:
        string += str(c)

        if contador == 1 or contador == 4:
            string += '.'
        elif contador == 7:
            string += '/'
        elif contador == 11:
            string += '-'
        contador += 1

    return string

if __name__ == "__main__":

    while True:
        valida_cnpj()
