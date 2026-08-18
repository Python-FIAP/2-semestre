# Dada a lista numeros = [2, 3, 4, 5] , use reduce (com uma função def chamada
# multiplicar ) para calcular o produto de todos os números da lista.
from functools import reduce
def multiplicar(x: int, y: int) -> int:
    return x * y
numeros = [2, 3, 4, 5]
print(reduce(multiplicar, numeros))