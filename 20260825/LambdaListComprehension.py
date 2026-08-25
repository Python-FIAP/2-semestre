print('Revisão Map')
def dobro (n:int) -> int:
    return n * 2


numeros = [7, 87, 90, -23, 4, 0]
print(numeros)
numeros_dobrados = list(map(dobro, numeros))
print(numeros_dobrados)

def multi (n:int, m:int) -> int:
    return n * m

numeros = [7, 87, 90, -23, 4, 0]
print(numeros)
multiplicadores = [2, 3, 4, 5, 6, 7]
multiplicados = list(map(multi, numeros, multiplicadores))
print(multiplicados)





print('\nList Comprehension')
#feito para simplificar o map
#retorna uma lista
print('\nSem o list comprehension')
numeros = [7, 87, 90, -23, 4, 0]
dobrados = []
for n in numeros:
    dobrados.append(n * 2)

print(dobrados)
print('\nCom o list comprehension')
dobrados2 = [n * 2 for n in numeros]
print(dobrados2)


print('\nList Comprehension e condicional')
numeros = [7, 87, 90, -23, 4, 0]
dobradospositivos = [n * 2 for n in numeros if n > 0]
print(dobradospositivos)

print('\nList Comprehension e condicional e else')
numeros = [7, 87, 90, -23, 4, 0]
dobradospositivosquadradosnegativos = \
    [n * 2 if n > 0 else n+100 for n in numeros]
print(dobradospositivosquadradosnegativos)