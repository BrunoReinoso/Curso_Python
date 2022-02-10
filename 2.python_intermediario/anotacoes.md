# Seção 3: Python Intermediário 

## Args & kargs

Quando não se sabe quantos argumentos a função irá receber, pode-se usar ``*args``como parâmetro. 

Pode-se usar o desempacotamento de listas como em ``print(*lista)``, que irá printar todos os valores dentro da mesma. 

``*args e **kargs`` são chamados assim por convenção e se diferem pois o primeiro recebe argumentos não nomeados e o segundo recebe os nomeados. 

Caso não se tenha certeza da existência de um valor em ``**kwargs`` recomenda-se a utilização de ``get()`` para o código não retornar um erro caso ela não exista. Sendo sua utilização dada por exemplo como: ``kwargs.get('idade')``. 

## Funções, listas, tuplas, dicionários e sets

Pode-se utilizar funções lambda/anônimas para passarmos parâmetros para outras funções. Um exemplo seria ao ordenarmos uma lista de listas, que poderia ser feita como: `` lista.sort(key=lambda :item: item[1])``.

Pode-se ordenar uma lista com ``.sort()`` ou com ``sorted()``, sendo que a primeira modifica a ordem da lista e a segunda apenas trabalha junto com a função ``print()`` para printar determinada lista ordenada.

Tuplas são semelhantes à listas, porém a princípio não podem ser alteradas. Para isto, seria necessário convertê-las para listas.

Em alguns pontos, dicionários são bem semelhantes à listas. Pode-se criar um dicionário de duas formas:
```python
d = {'chave1': 'valor da chave', 'chave2': 'valor'}
d = dict(chave1 = 'valor', chave2 = ' valor)
```

Dicionários têm as funções ``keys()``,``values()`` e ``items()``.
Dicionários podem ser desempacotados assim como listas. <br>
Não é possível copiar um dicionário da mesma forma que copiamos o valor de uma variável para outra. Para isto é necessário utilizar a função ``copy.deepcopy()``.

Sets são a representação de conjuntos em python. Funcionam de forma semelhante às listas, porém não há como acessar seus elementos via índice. Não possuem uma ordem específica, não admitem elementos duplicados e também possuem funções específicas.<br>
``|`` = união <br>
``&`` = interseção <br>
``-`` = elementos apenas no set da esquerda <br> 
``^`` = todos - interseção <br>

List Comprehension é uma forma diferente de construção de lista. Ela se utiliza de loopings para montar seus valores internos. Um exemplo seria: `` lista2 = [variavel for variavel in lista1)]`` 

``zip()`` é utilizado para unir dois iteráveis (listas por exemplo) de acordo com a menor lista. No caso de ``zip_logest() (from itertools import zip_longest)`` a função levará em consideração o maior iterável. 

A função ``round()`` serve para arredondar um valor de acordo com a quantidade de casas decimais desejadas. Por exemplo: ``round(valor, 2)``.

A função ``round() (from itertools import count)`` é um contador, podendo ser utilizada de diferentes formas. Um exemplo seria ``round(start=1, step=2)`` que irá retornar os valores de 2 em 2  partir de 1 sempre que ela for chamada. 

Outras funções interessantes e que tem relação com contadores são: ``combinations, permutations e product (todas importadas de intertools).`` <br>
Combinação - ordem não importa, não repete valor único. <br>
Permutação - ordem importa, não repete valor único. <br>
Produto - ordem importa, repete valores únicos 

Para usar a função ``groupby() (intertools)`` de forma correta é importante utilizar a função ``sort()`` antes, e ordenar de acordo com o dado que deseja agrupar. Um exemplo seria:<br> `` 
ordena = lambda item: item ['nota'] <br>
alunos.sort(key=ordena)<br>
alunos_agrupados = groupy(alunos, ordena) ``

A função `` tee() (intertools)`` é utilizada para fazer cópias de um iterador. 

A função `` map() `` trabalha em cima de uma função e iteráveis. Ou seja, ela passa determinada função em cada elemento do iterável passado como argumento. No caso de listas, é muito similar à list comprehension. Exemplo: 
```python
nova_lista = map(lambda x: x*2, lista) 
```
No caso de dicionários, a utilização desta função é mais justificável. 

A função `` filter() `` trabalha em cima de uma função e iteráveis. Ela retorna um iterável dado pelo resultado True retornado função passada, removendo os demais. Exemplo:  
```python
nova_lista = filter(lambda p: p[p'preco'] > 50, produtos)
``` 

A função ``reduce() (from functools import reduce)`` trabalha em cima de acumulador, função e iteráveis. Funciona para acumular valores. 

``try, exception e finally`` são utilizadas para rodar o código mesmo quando há um erro no mesmo. Podem ser utilizadas de diversas formas e funcionam similarmente a ``if e else`` em questão de identação. Além de ser possível ser utilizada com ``else``.

## Arquivos

Pode-se abrir um documento da forma: ``file = open('abc.txt', 'w+')`` (no caso, para escrita.) <br>
Há várias opções, de acordo com o desejado, para serem passadas como segundo parâmetro da função ``open()``. Dependerá se queremos ler ou escrever no arquivo em questão.

Muitas pessoas utilizam o bloco ``try`` para abrir arquivos e o ``finally`` para fechar, porém não é a forma mais recomendada. No caso do python, pode-se utilizar um gerenciador de contexto para isso. A vantagem é que, após executar os comandos, ele irá fechar o arquivo automaticamente. <br>
Exemplo: `` with open('exemplo.txt', 'w') as file:``

Para lermos e escrevermos no arquivo podemos usar de diversas opções, como: ``write(), read(), readline(), readlines(), etc.`` <br>
Uma questão interessante é que, após executar os comandos de leitura, o python irá posicionar o "cursor" no final da leitura. Ou seja, caso queiramos ler ou alterar algo que já foi "passado", teremos que voltar algumas posições (normalmente ao início). Para isto, usamos a função ``seek()``, como no exemplo: ``file.seek(0,0)``. 

Funções decoradoras são aquelas que que trabalham em cima de outras funções afim de modificá-las. Normalmente são utilizadas por bibliotecas ou criadas quando iremos rodar um mesmo comando em diversas funções. Exemplo de criação:
```python
def decoradora(funcao):
    def timer(*args, **kwargs):
        start = time()
        resultado = funcao(*args, **kwargs)
        end = time()
        tempo = (end - start) * 1000
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        return resultado
    return decoradora
```
Em python há uma forma simples de executar esse tipo de função, que seria decorando a outra. Por exemplo: 
```python
@decoradora
def funcao(): (...) 
```

