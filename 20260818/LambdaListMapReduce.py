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