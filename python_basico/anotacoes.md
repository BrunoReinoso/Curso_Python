# Seção 2: Python Básico 

Pep8 pede 2 espaços pra comentário do lado do código .

Docstring é usado para documentação.

A função <b>type()</b> retorna o tipo da variável.	

// divisão inteira <br>
** potência <br>
% resto da divisão <br>


## Detalhes print
* <b>print('esse \'texto\' é um teste')</b> printa normal, a barra ignora as aspas (caractere de escape) <br>
* <b> print(r’teste \n (str).’)</b> o “r” faz tudo dentro das aspas ser texto (raw) <br>
* <b> print(f’{nome} tem {peso} kgs’) </b> “f string” <br>
* <b> {variável:.2f} </b> printa com duas casas decimais <br>
* <b> print(’{} tem {:2f} kgs’.format(nome, peso)) </b> <br>
* <b> print(’{0} tem {1} kgs’.format(nome, peso)) </b> <br>
* <b> print(’{n} tem {p} kgs’.format(n = nome,  p = peso)) </b> 

* <b>sep=’-‘</b> separador de argumentos no print

* <b>end=’‘</b> tira a quebra de linha automática <br><br>

A função <b>input()</b> serve para receber dados pelo usuário em forma de string.

Os operadores lógicos são: <b> and, or, not, in</b> e <b>not in</b>.

A função <b>len()</b> retorna a quantidade de caracteres da string passada (levando em consideração espaços) em forma de inteiro.

O Python possui várias funções built-in úteis. (olhar documentação da linguagem)

<b>Try/Except</b> são interessantes em alguns casos.

## Formatando valores com modificadores
<b>:s</b> - strings</b> <br>
<b>:d</b> - inteiros <br>
<b>:f</b> - float <br>
<b>:(caractere)(> ou < ou ^)(quantidade)(tipo)</b>
* <b>></b> - add esquerda
* <b><</b> - add direita
* <b>^</b> - posiciona no centro <br>

(Há funções semelhantes às opções abaixo.) <br>
* Exemplos: <br> <b>print(f'{nome:#^50}')</b> irá posicionar o nome no centro e adicionar # na esquerda e na direita até completar 50 caracteres. <br>
<b>nome_formatado = '{:#^50}'.format(nome)</b> fará algo semelhante.
<br>

Pode-se acessar o último valor de uma lista ou string se usarmos negativos, por exemplo: <b>texto[-1]</b> <br>

Pode-se fatiar a string de acordo com o desejado fazendo algo como <b>texto[2:6]</b> que irá pegar do caractere 2 ao 5 pois o 6 não é incluído. <br>

Pode-se pular caracteres usando <b>texto[0::2]</b> que irá do caractere 0 ao último pulando de 2 em 2. <br>

Uma maneira interessante de inverter uma lista é fazer <b>lista = [ : : -1]</b>. <br>

Algumas funções que podemos usar em listas são: <b>append, insert, pop, del, clear, extend, +, min, max e range. </b> <br>

<b>split(), join() e strip()</b>  são funções built-ins relacionadas a strings e listas.<br>

<b> enumerate() </b>  é uma tupla que retorna, normalmente, um índice e o respectivo valor na lista. <br>

O desempacotamento de lista funciona como o exemplo abaixo: <br>
<b>lista = [1, 2, 3, 4, 5, 9] <br>
n1, n2, *_ = lista</b> <br>
Onde definiremos duas novas variáveis com os dois primeiros valores e guardamos o resto na variável ' _ ' por conta do uso do *. <br>

A troca de valores entre variáveis é bem simples em python, podendo ser usada da forma: <br>
<b> x, y, z = z, x, y </b> <br>

O ternário no python funciona como o exemplo abaixo: <br><b>
idade = 18 <br>
acesso = "Pode acessar" if idade >= 18 else "Não pode acessar" </b><br>


 