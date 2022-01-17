from itertools import zip_longest

lista_1 = [1, 5, 13, 24, 2]
lista_2 = [7, 6, 8]

# esperado: [8, 11, 21]
# forma completa (bônus): [8, 11, 21, 24,2]

lista_3 = list([x + y for x, y in zip_longest(lista_1, lista_2, fillvalue=0)])

print(lista_3)