#Crie uma função lambda chamada par ou impar que recebe um número inteiro e retorna uma string
# indicando se o número é par ou ímpar.
par_ou_impar = lambda n: f'{n} é par' if n %2 == 0 else f'{n} é ímpar'
print(par_ou_impar(6))
print(par_ou_impar(7))