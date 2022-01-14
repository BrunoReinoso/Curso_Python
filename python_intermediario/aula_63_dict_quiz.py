questoes = {
    "Questão 1": {
        "pergunta": "Quanto é 5 * 5?",
        "respostas": {"a": "10", "b": "15", "c": "20", "d": "25"},
        "certa": "d",
    },
    "Questão 2": {
        "pergunta": "Em que ano estamos?",
        "respostas": {"a": "2020", "b": "2021", "c": "2022", "d": "2023"},
        "certa": "c",
    },
    "Questão 3": {
        "pergunta": "Qual é a capital do Tocantins?",
        "respostas": {"a": "Palmas", "b": "Fortaleza", "c": "Cuiabá", "d": "Teresina"},
        "certa": "a",
    },
    "Questão 4": {
        "pergunta": "Quais são as 3 cores primárias?",
        "respostas": {
            "a": "Vermelho, amarelo e azul",
            "b": "Verde, amarelo e azul",
            "c": "Azul, amarelo e laranja",
            "d": "Azul, branco e vermelho",
        },
        "certa": "a",
    },
    "Questão 5": {
        "pergunta": "Qual é a capital do Azerbaijão?",
        "respostas": {"a": "Xirvam", "b": "Aldabil", "c": "Baku", "d": "Ganja"},
        "certa": "c",
    },
}
numero_de_questoes = 0
respostas_corretas = 0

print("Digite a LETRA correspondente a sua resposta.")

for quest, conteudo in questoes.items():
    print(quest, conteudo["pergunta"], sep=" - ")
    numero_de_questoes += 1

    for letra, info in conteudo["respostas"].items():
        print(letra, info, sep=") ")
    resposta = input("Sua resposta: ")

    if resposta == conteudo["certa"]:
        respostas_corretas += 1
        print(f"Resposta correta! Você tem {respostas_corretas} ponto(s)")
    else:
        print(f"Resposta incorreta! Você tem {respostas_corretas} ponto(s)")
    print()

print(f"Você fez {respostas_corretas}/{numero_de_questoes}.")
porcentagem = respostas_corretas / numero_de_questoes * 100
print(f"Portanto, você acertou: {porcentagem}% do teste.")
