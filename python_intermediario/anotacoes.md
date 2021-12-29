# Seção 3: Python Intermediário 

Quando não se sabe quantos argumentos a função irá receber, pode-se usar <b>*args</b> como parâmetro. <br>

Pode-se usar o desempacotamento de listas como em <b>print(*lista)</b>, que irá printar todos os valores dentro da mesma. <br>

<b>*args e **kargs</b> são chamados assim por convenção e se diferem pois o primeiro recebe argumentos não nomeados e o segundo recebe os nomeados. <br>

Caso não se tenha certeza da existência de um valor em <b>**kwargs</b> recomenda-se a utilização de <b>get()</b> para o código não retornar um erro caso ela não exista. Sendo sua utilização dada por exemplo como: <b>kwargs.get('idade')</b>. <br>