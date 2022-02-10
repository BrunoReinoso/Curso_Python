string = '0123456789012345678901234567890123456789012345678901234567890123456789'
aux = 10

posi_inicio = [n for n in range(0, len(string), aux)]
posi_fim = [(n, n + aux) for n in range(0, len(string), aux)]

lista = [string[n: n + aux] for n in range(0, len(string), aux)]
raw = [f'string[{n}: {n + aux}]' for n in range(0, len(string), aux)]
juntar = '.'.join(lista)

print(posi_inicio)
print(posi_fim,'\n')
print(raw)
print(lista,'\n')
print(juntar)