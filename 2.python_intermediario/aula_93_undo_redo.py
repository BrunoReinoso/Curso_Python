import os

lista_de_tarefas, lista_undo, lista_redo = [], [], []
undo = 0

def le_comando(lista_original):
    print(f"Lista atual: {(list(enumerate(lista_original)))}\n")
    print(
        "1 - Adicionar tarefa.\n"
        + "2 - Remover tarefa.\n"
        + "3 - Undo.\n"
        + "4 - Redo.\n"
        + "0 - Sair\n"
    )
    comando = input("Digite o comando que gostaria de executar: ")
    return comando

def adiciona(lista_original, lista_anterior):
    tarefa = input("Escreva a tarefa que gostaria de adicionar: ")
    lista_anterior = lista_original.copy()
    lista_original.append(tarefa)
    input(f'Tarefa "{tarefa}" adicionada com sucesso.')
    return lista_original, lista_anterior

def remove(lista_original, lista_anterior):
    if lista_original == []:
        input("Lista vazia. Não é possível remover nenhum item.")
    else:
        tarefa = int(input("Escreva o índice da tarefa que gostaria de remover: "))
        try:
            existe = lista_original[tarefa]
            lista_anterior = lista_original.copy()
            lista_original.pop(tarefa)
            input(f'Tarefa "{tarefa}" removida com sucesso.')
        except:
            input(f"Não foi possível remover a tarefa requisitada.")
    return lista_original, lista_anterior

def funcao_undo(lista_original, lista_anterior, lista_posterior, fez_undo):
    if fez_undo == 0:
        lista_posterior = lista_original.copy()
        lista_original = lista_anterior.copy()
        fez_undo = 1
    else:
        input("Você não pode voltar esta ação no momento.")
    return lista_original, lista_anterior, lista_posterior, fez_undo

def funcao_redo(lista_original, lista_posterior, fez_undo):
    if fez_undo == 1:
        lista_original = lista_posterior.copy()
        fez_undo = 0
    else:
        input("Você não pode voltar esta ação no momento.")
    return lista_original, lista_posterior, fez_undo

if __name__ == '__main__':
    
    while True:
        os.system("clear") or None
        comando = le_comando(lista_de_tarefas)

        if comando == "1":
            lista_de_tarefas, lista_undo = adiciona(lista_de_tarefas, lista_undo)

        elif comando == "2":
            lista_de_tarefas, lista_undo = remove(lista_de_tarefas, lista_undo)

        elif comando == "3":
            lista_de_tarefas, lista_undo, lista_redo, undo = funcao_undo(lista_de_tarefas, lista_undo, lista_redo, undo)

        elif comando == "4":
            lista_de_tarefas, lista_redo, undo = funcao_redo(lista_de_tarefas, lista_redo, undo)

        elif comando == "0":
            input("Você optou por sair.")
            break

        else:
            input(f'O comando "{comando}" não foi reconhecido.')
