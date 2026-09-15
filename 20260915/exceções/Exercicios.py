#1ex
# Leia um número inteiro digitado pelo usuário e imprima o seu quadrado (o número elevado
# ao quadrado). Trate ValueError caso o valor informado não seja um número inteiro.
try:
    numero = int(input('Digite um número inteiro: '))
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}.")
except ValueError:
    print('O valor informado não é um número inteiro.')

#2ex
#Elabore um algoritmo que leia dois números e imprima qual é o maior e qual é o menor. Se
# eles forem iguais, lance uma exceção explicando o motivo e trate essa exceção, encerrando a
# comparação de forma controlada (sem travar o programa).