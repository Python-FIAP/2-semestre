#Lambda.
#Função anonima (pequena - de uma linha só - função inline).
#A lambda é uma função anonima, ou seja, uma função sem nome.
#Ela é usada para criar funções pequenas e simples.
#Que podem ser passadas como argumentos para outras funções.

def dobro(n: int) -> int:
    '''
    Calcula o dobro de um número.


    :param n: Número inteiro.
    :return: Dobro do número.
    '''
    return n * 2

#uso
print(dobro(4))

#transformar em lambda
#sintaxe lambda <argumentos/parametros> : <expressão de retorno>
#lambda SEMPRE TEM O RETURN
ldobro = lambda n: n * 2
print(ldobro(79))
#o uso mais comum
print((lambda n: n * 2)(67))

#Lambda condicional
#Tem um IF embutido

#Função que decide qual o maior de 2 numeros
def maior(x: int, y: int) -> int:
    if x > y:
        return x
    else:
        return y
#uso
print(maior(y=6, x=7)) #<= parametros nomeados

#transformando em lambda
lambda x,y: x if x > y else y

#não é o uso mais comum
lmaior = lambda x,y: x if x > y else y
print(lmaior(6, 7))
#uso mais comum
print((lambda x,y: x if x > y else y)(6, 9))

#posso usar o print dentro da lambda
#mas com cuidado
lmenor = lambda x,y: print(x) if x < y else print(y)
xpto = lmenor(4, 2)
# print(lmenor(6, 9)) #<= retorna None

#a melhor solução
lmenor = lambda x,y: f'o número menor é {x}' \
    if x < y else \
    f'Entre {x} e {y} o menor é {y}'
print(lmenor(4, 2))

#Map é uma funcionalidade do python que permite aplicar
#uma função em todos os elementos de uma coleção

def dobro(n: int) -> int:
    return n * 2
numeros = [33.5, 21, 3, 4, 5]

#da maneira roots
dobrados = []
for n in numeros:
    dobrados.append(dobro(n))
print(numeros)
print(dobrados)
print('\nCom map')
#com map
#sintaxe map(função, iterável/coleção)
#1o uso criando uma lista de números dobrados
dobrados2 = list(map(dobro, numeros))
print(dobrados2)
#2o uso direto no print
print(list(map(dobro, numeros))) #<= retorna um map object

#utilizando o ldobro abaixo, como eu faria o map?
ldobro = lambda n: n * 2
dobrado3 = list(map(ldobro, numeros))
print(dobrado3)

#o jeito mais pythoneiro
print(list(map((lambda n: n * 3), [23, 4, 867, - 4])))