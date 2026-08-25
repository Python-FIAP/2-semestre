#7. Use list comprehension para criar uma lista com os quadrados dos números de 1 a 10.
quadrados = [n ** 2 for n in range(1, 11)]
print(quadrados)

#7a. Peça o numero inicial ao usuario, peça o numero final
#Usando list comprehension, calcule os quadrados dos números entre
#o numero inicial e o numero final
inicial = int(input('Digite o numero inicial: '))
final = int(input('Digite o numero final: '))
quadrados = [n ** 2 for n in range(inicial, final + 1)]
print(quadrados)

#8.Dada a lista numeros = [3, 8, 15, 22, 7, 40, 11] , use list comprehension para criar uma
#nova lista contendo apenas os números pares
numeros = [3, 8, 15, 22, 7, 40, 11]
pares = [n for n in numeros if n % 2 == 0]
print(pares)

#9. Dada a lista numeros = [3, 8, 15, 22, 7] , use list comprehension com expressão
#condicional ( if / else dentro da expressão) para criar uma lista com a string "par" ou
# "ímpar" correspondente a cada número, na mesma ordem
numeros = [3, 8, 15, 22, 7]
par_ou_impar = ['par' if n % 2 == 0 else 'ímpar' for n in numeros]
print(par_ou_impar)

#10.Você recebeu uma matriz de produtos, no mesmo formato usado no projeto de fundo
# ( [nome, preco, estoque] ):
# NOME, PRECO, ESTOQUE = 0, 1, 2
# produtos = [
# ["Caderno", 12.50, 5],
# ["Caneta", 2.30, 100],
# ["Mochila", 89.90, 3],
# ["Estojo", 15.00, 8],
# ]
# Use list comprehension para criar uma lista apenas com os nomes dos produtos que têm
# estoque menor que 10.
NOME, PRECO, ESTOQUE = 0, 1, 2
produtos = [
    ["Caderno", 12.50, 5],
    ["Caneta", 2.30, 100],
    ["Mochila", 89.90, 3],
    ["Estojo", 15.00, 8],
]
nomes = [produto[NOME] for produto in produtos if produto[ESTOQUE] < 10]
print(nomes)