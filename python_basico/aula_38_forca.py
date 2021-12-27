palavra_secreta = "reinoso"
letras_certas_digitadas = []
letras_erradas_digitadas = []
chances = 3

print("Palavra secreta: " + "*" * len(palavra_secreta))

while chances > 0:

    print(f"Você tem {chances} chances.")
    letra_digitada = input("Digite sua tentativa: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
    elif (
        letra_digitada in palavra_secreta
        and letra_digitada not in letras_certas_digitadas
    ):
        print(f"A letra {letra_digitada} está na palavra secreta!")
        letras_certas_digitadas.append(letra_digitada)
    elif (
        letra_digitada in letras_certas_digitadas
        or letra_digitada in letras_erradas_digitadas
    ):
        print(f"A letra {letra_digitada} já foi digitada!")
    else:
        letras_erradas_digitadas.append(letra_digitada)
        chances -= 1
        print(f"A letra {letra_digitada} não está na palavra secreta!")

    palavra_temporaria = ""
    for letra in palavra_secreta:
        if letra in letras_certas_digitadas:
            palavra_temporaria += letra
        else:
            palavra_temporaria += '*'

    
    if palavra_temporaria == palavra_secreta:
        break

    print(f"Letras certas digitadas: {letras_certas_digitadas}")
    print(f"A palavra temporária é: {palavra_temporaria}")

if chances == 0:
    print(f'Suas chances chegaram a {chances}! Você perdeu o jogo.')
    print(f'A palavra secreta era {palavra_secreta}.')
else:
    print(f'Parabéns, você consegui acertar a palavra {palavra_secreta} com {chances} chance(s) restante(s)!')