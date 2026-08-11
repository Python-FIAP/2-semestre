#Area do retangulo
def area_retangular(altura:float, largura:float) -> float:
    """
    Calcula area de um retangulo
    :param altura: altura do retangulo
    :param largura: largura do retangulo
    :return: area do retangulo
    """
    if altura <= 0 or largura <= 0:
        #return 0
        raise ValueError('A altura e largura deve ser positivo.')
    area = largura * altura
    return area

print(area_retangular(5, 10))
print(area_retangular(12, 1))
