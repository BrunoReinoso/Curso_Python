# Seção 4: Python Orientado a Objetos 

## Classes

Classes são uma forma de retratar coisas do mundo real como objetos dentro do código. A ideia é criar uma abstração de algo que iremos descrever. Após criado este modelo, com variáveis e métodos, pode-se utilizar instâncias do mesmo como um tipo de dado. <br>
Por exemplo, uma classe 'Pessoa' poderia ter atributos, como 'nome', 'idade', 'altura', e métodos como 'falando', 'correndo', 'comendo'. <br>
Exemplo: <br>
```python
classe Pessoa:
    def __init__(self, nome, idade, comendo = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
    
    def comer(self, alimento):
        if self.comendo:
            print (f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
```
Para utilizarmos uma classe precisamos definir um objeto, uma instância, daquela classe. Além disso, é preciso dizer quais são os atributos do mesmo. tendo como exemplo a classe anterior:
```python
p1 = Pessoa ('Bruno', 25)
p2 = Pessoa ('Cleide', 53)
```
E para executar os métodos descritos:
```python
p1.comer('maçã')
p1.parar_comer()
```
Métodos de instância, métodos de classe e métodos estáticos têm cada um sua função e forma específica de serem utilizados. Pode-se pensar da seguinte forma: <br>
1 - Caso receba a palavra ``self`` dentro do método ele será de instância. <br>
```python
def parar_comer(self):
    if not self.comendo:
        print(f'{self.nome} não está comendo.')
        return
    print(f'{self.nome} parou de comer.')
    self.comendo = False
```
2 - Caso use a classe em si dentro do método (``cls``) será um método de classe. <br>
```python
@classmethod
def ano_nascimento(cls, nome, ano_nascimento):
    idade = cls.ano_atual - ano_nascimento
    return cls(nome, idade)
```
3 - Caso não precise nem de ``self`` e nem de ``cls`` dentro do método, pode ser um método estático.
```python
@staticmethod
def gera_id()
    rand = randint(0, 1000)
    return rand
```
Métodos ``getters`` e ``setters`` são uma forma de proteção para os atributos da classe. Sua vantagem é que podem ser utilizados após a classe já estar pronta, sem necessitar de alterações no código já criado. Pode-se criar filtros ou transformar dados a partir destes métodos. Sua utilização se dá da seguinte forma:
```python
#Getter
@property
def preco(self):
    return self._preco

#Setter
@preco.setter
def preco(self,valor):
    if isinstance(valor, str):
        valor = float(valor.replace('R$', ''))

    self._preco = valor
```
Obs: tomar cuidado para não causar recursividade nos getters e setters!

O encapsulamento em python funciona de forma diferente de outras linguagens orientadas a objeto. No caso específicode python, ele funciona como uma forma de convenção. De forma que: <br>
var -> publico <br>
_var -> recomendado não mexer <br>
__var -> fortemente recomendado não mexer <br>
Para acessar um atributo ``__var`` pode-se usar ``_NOMECLASSE__var``. 

## Relacionamento entre classes

``Associação`` - acontece quando utilizamos uma classe em conjunto com outra porém sendo as duas independentes entre si. Acontece como no exemplo de "escritor" e "caneta", onde o escritor e a caneta podem ser objetos com variáveis e métodos únicos, ou seja, vistos separadamente.

``Agregação`` - pode ser considerada uma associação porém pelo menos uma das classes em questão não funciona bem separadamente. Acontece como no exemplo de "carrinho de compras" e "produto", onde as duas podem existir separadamente porém a "carrinho de compras" depende, de certa forma, de produtos.

``Composição`` - é uma classe que será diretamente ligada à outra, sendo usada naquela situação em específico. Acontece como no exemplo de "endereço" e "cliente", onde um cliente pode ter vários endereços e aqueles endereços são dele em específico.

``Herança Simples`` - é quando uma classe herda os atributos e métodos de outra classe. Como acontece no exemplo da classe "Cliente", que herdaria a classe "Pessoa". Para isso bastaria passar como argumento "Pessoa" na hora de criação da classe "Cliente":
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    pass
```
É possível reescrever/soprepor um método criado na "classe mãe" caso se crie um método de mesmo nome na classe que recebe a herança da mesma.<br>
No caso de construtores, é importante verificar se os atributos da "classe mãe" seriam usados, pois ao criar um construtor na classe filha ele automaticamente sobrepõem o anterior. Neste caso, a solução é a seguinte:
```python
class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
```
``Herança Múltipla`` - é quando uma classe herda os atributos e métodos de mais de uma classe diretamente. Nesse caso é importante salientar que a ordem dos argumentos importa, tendo como ordem de prioridade da esquerda para a direita. Portanto, caso existam métodos com o mesmo nome, o python irá considerar o primeiro. Apesar dessa ressalva, esse tipo de herança funciona de forma semelhante à herança simples.

``Classes Abstratas`` - São classes que servem de base para criação de outras classes. Elas forçam que as classes filhas implementem determinado método abstrato que foi criado. Desta forma, ao invés de criarmos o método completo na classe mãe, este método deverá ser refeito nas classes filhas de acordo com a necessidade. Não é possível instanciar uma classe abstrata, isso retornará um erro! Para criarmos uma classe abstrata com um método abstrato devemos seguir algo como:
```python
from abc import ABC, abstractmethod

class Exemplo(ABC):
    @abstractmethod
    def abstrato(self):
        pass
```