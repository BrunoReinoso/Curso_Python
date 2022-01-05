# Seção 3: Python Intermediário 

Quando não se sabe quantos argumentos a função irá receber, pode-se usar <b>*args</b> como parâmetro. <br>

Pode-se usar o desempacotamento de listas como em <b>print(*lista)</b>, que irá printar todos os valores dentro da mesma. <br>

<b>*args e **kargs</b> são chamados assim por convenção e se diferem pois o primeiro recebe argumentos não nomeados e o segundo recebe os nomeados. <br>

Caso não se tenha certeza da existência de um valor em <b>**kwargs</b> recomenda-se a utilização de <b>get()</b> para o código não retornar um erro caso ela não exista. Sendo sua utilização dada por exemplo como: <b>kwargs.get('idade')</b>. <br>

Pode-se utilizar funções lambda/anônimas para passarmos parâmetros para outras funções. Um exemplo seria ao ordenarmos uma lista de listas, que poderia ser feita como: <b> lista.sort(key=lambda :item: item[1])</b>. <br>

Pode-se ordenar uma lista com <b>.sort()</b> ou com <b>sorted()</b>, sendo que a primeira modifica a ordem da lista e a segunda apenas trabalha junto com a função <b>print()</b> para demonstrar determinada lista ordenada. <br>

Tuplas são semelhantes à listas, porém a princípio não podem ser alteradas. Para isto, seria necessário convertê-las para listas. <br>

Em alguns pontos, dicionários são bem semelhantes à listas. Pode-se criar um dicionário de duas formas: <br>
--> <b>d = {'chave1': 'valor da chave', 'chave2': 'valor'}</b> <br>
--> <b>d = dict(chave1 = 'valor', chave2 = ' valor)</b> <br>
Dicionários têm as funções <b>keys()</b>,<b>values()</b> e <b>items()</b>.
Dicionários podem ser desempacotados assim como listas. <br>
Não é possível copiar um dicionário da mesma forma que copiamos o valor de uma variável para outra. Para isto é necessário utilizar a função <b>copy.deepcopy()</b>.

Sets são a representação de conjuntos em python. Funcionam de forma semelhante às listas, porém não há como acessar seus elementos via índice. Não possuem uma ordem específica, não admitem elementos duplicados e também possuem funções específicas.<br>
<b>|</b> = união <br>
<b>&</b> = interseção <br>
<b>-</b> = elementos apenas no set da esquerda <br> 
<b>^</b> = todos - interseção <br>

List Comprehension é uma forma diferente de construção de lista. Ela se utiliza de loopings para montar seus valores internos. Um exemplo seria: <b> lista2 = [variavel for variavel in lista1)]</b>