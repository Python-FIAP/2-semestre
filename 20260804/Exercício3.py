##Implemente a função soma_dos_quadrados que receba
# dois numeros e devolve a soma dos seus quadrados.
# Você pode tentar reutilizar a função quadrado definida anteriormente para facilitar a implementação.


def soma_dos_quadrados(num1, num2) -> int:
    return (num1 ** 2) + (num2 ** 2)


num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
print(f'A soma dos quadrados é: {soma_dos_quadrados(num1, num2)}')
