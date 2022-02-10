# Seção 2: Python Básico 

Por convenção, os padrões usados em Python são: ``snake_case`` para qualquer coisa e ``PascalCase`` para classes.

Pep8 pede 2 espaços pra comentário do lado do código .

Docstring é usado para documentação.

A função ``type()`` retorna o tipo da variável.	

// divisão inteira <br>
** potência <br>
% resto da divisão <br>


## Detalhes print
* ``print('esse \'texto\' é um teste')`` printa normal, a barra ignora as aspas (caractere de escape) <br>
* `` print(r’teste \n (str).’)`` o “r” faz tudo dentro das aspas ser texto (raw) <br>
* `` print(f’{nome} tem {peso} kgs’) `` “f string” <br>
* `` {variável:.2f} `` printa com duas casas decimais <br>
* `` print(’{} tem {:2f} kgs’.format(nome, peso)) `` <br>
* `` print(’{0} tem {1} kgs’.format(nome, peso)) `` <br>
* `` print(’{n} tem {p} kgs’.format(n = nome,  p = peso)) `` 

* ``sep=’-‘`` separador de argumentos no print

* ``end=’‘`` tira a quebra de linha automática 

A função ``input()`` serve para receber dados pelo usuário em forma de string.

Os operadores lógicos são: `` and, or, not, in`` e ``not in``.

A função ``len()`` retorna a quantidade de caracteres da string passada (levando em consideração espaços) em forma de inteiro.

O Python possui várias funções built-in úteis. (olhar documentação da linguagem)

``Try/Except`` são interessantes em alguns casos.

## Formatando valores com modificadores
``:s`` - strings <br>
``:d`` - inteiros <br>
``:f`` - float <br>
``:(caractere)(> ou < ou ^)(quantidade)(tipo)``
* ``>`` - add esquerda
* ``<`` - add direita
* ``^`` - posiciona no centro <br>

(Há funções semelhantes às opções abaixo.) <br>
* Exemplos: <br> ``print(f'{nome:#^50}')`` irá posicionar o nome no centro e adicionar # na esquerda e na direita até completar 50 caracteres. <br>
``nome_formatado = '{:#^50}'.format(nome)`` fará algo semelhante.

Pode-se acessar o último valor de uma lista ou string se usarmos negativos, por exemplo: ``texto[-1]`` 

Pode-se fatiar a string de acordo com o desejado fazendo algo como ``texto[2:6]`` que irá pegar do caractere 2 ao 5 pois o 6 não é incluído. 

Pode-se pular caracteres usando ``texto[0::2]`` que irá do caractere 0 ao último pulando de 2 em 2. 

Uma maneira interessante de inverter uma lista é fazer ``lista = [ : : -1]``. 

Algumas funções que podemos usar em listas são: ``append, insert, pop, del, clear, extend, +, min, max e range. `` 

``split(), join() e strip()``  são funções built-ins relacionadas a strings e listas.

`` enumerate() ``  é uma tupla que retorna, normalmente, um índice e o respectivo valor na lista. 

O desempacotamento de lista funciona como o exemplo abaixo:
```python
lista = [1, 2, 3, 4, 5, 9] 
n1, n2, *_ = lista
```
Onde definiremos duas novas variáveis com os dois primeiros valores e guardamos o resto na variável ' _ ' por conta do uso do *. 

A troca de valores entre variáveis é bem simples em python, podendo ser usada da forma: `` x, y, z = z, x, y `` 

O ternário no python funciona como o exemplo abaixo: 
```python
idade = 18
acesso = "Pode acessar" if idade >= 18 else "Não pode acessar" 
```


 