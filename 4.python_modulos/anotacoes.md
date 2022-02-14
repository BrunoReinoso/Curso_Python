# Seção 5: Módulos Python - os, datetime, sys, json, csv, selenium, pillow e mais 

``if __name__ == '__main__'`` é utilizado para rodar um código quando aquele módulo (arquivo) for executado diretamente, ou seja, quando for importado por outro módulo aquela parte do código não será executada. Dessa forma, se naquele trecho tiver algum teste ou algo desnecessário para os demais arquivos ele não irá impactar nos mesmos. Para isso também é possível criar uma função ``main()`` como é feito em outras linguagens de programação.

O módulo ``datetime`` é muito rico, e possui diversas utilidades. É possível comparar datas e, além disso, com a utilização do ``timedelta`` é possível alterar datas com "operações matemáticas". 

O módulo ``os`` nos permite usar funcionalidades que são relacionadas ao sistema operacional.

O módulo ``sys`` pode ser utilizado para verificar o sistema operacional, além de outras funções.

O módulo ``shutils`` nos permite trabalhar com arquivos e pastas de forma mais abrangente, com diversas funcionalidades para isto.

O módulo ``fnmatch`` pode ser usado para verificar extensão de arquivos.

``JSON`` é um formato de troca de dados entre sistemas e programas muito leve e de fácil utilização. Em python, podemos importar o módulo ``json`` justamente para trabalhar com esse tipo de dado. 

``CSV`` é um formato de arquivo normalmente utilizado em planilhas. Para manipular arquivos desse tipo devemos importar o módutlo de mesmo nome.

O módulo ``random`` nos permite trabalhar com números aleatórios. Permite gerar números aleatórios, embaralhar listas, sortear elementos de listas, gerar senhas, etc.

O módulo ``string`` nos permite manipular strings de diversas formas, inclusive alterar o texto a partir de um template base.

