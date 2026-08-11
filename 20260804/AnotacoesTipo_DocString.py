# python possui tipagens dinamicas, por exemplo:
x = 10
print(type(x))  # <class 'int'>

nome = "paulo"
print(type(nome))  # <class 'str'>

# type hints ajuda a definir o tipo de dados esperados nas variaveis.
# porem ele apenas ajuda, ou seja o python nao impede que seja atribuido
# um valor de outro tipo de dados.

nome: str = "paulo"
print(type(nome))

nome = 123
print(type(nome))

preco : float

preco = 7.8
print(type(preco))
#todos os tipos de dados são aceitos no type hints
#int, float, bool, str, list
disponivel : bool = True
print(type(disponivel))

#o tipo de uso mais importante é quando definimos funções
#quando definimos o tipo de dados esperado como parametro e tambem o tipo
#de retorno da função, estamos definindo a
#ASSINATURA da função
#isso é importante para disponibilizarmos essas funções, por exemplo
#como API

def calcular_total(preco : float, quantidade:int) -> float:
    return preco * quantidade

print(calcular_total(preco, 2))
print(calcular_total(preco, 3))

#e quando a função não tem retorno?
def exibir_produto(produto: str, preco: float) -> None:
    print(f"{produto} - {preco}")

exibir_produto('Leite',8.9)

#mas o tipo list?
def somar_precos(preco: list) -> float:
    return

#revisão de list
#--> tipo de dados do composto
minhaLista:list = ['cafe', 'chantilly', 'biscoito']
print(minhaLista)
dadosPessoais: list = ['Moita', 54, 'Masculino']
print(dadosPessoais)
print(f'Nome: {dadosPessoais[0]}')
print(f'Idade: {dadosPessoais[1]}')
print(f'Sexo5: {dadosPessoais[2]}')
dadosPessoais.append('Engenheiro')
print(dadosPessoais)
print('\nImprimindo a lista elemento a elemento')
for item in dadosPessoais:
    print(item)

#mas e o tipo list??
#vamos aplicar a lista usando type hint em funções
#def somor_precos (precos: list) -> float:
#    total: float = 0
#fale que o tota é um float sem falar que é um float]
#total = 0.0
#    for preco in precos:
#        total += preco
#    return total
#print('\nSomando precos')
#print(f'total: {somar_precos([10, 20, 30])}')
#print(preco)
#def criar_produto(produto: str, preco: float, quantidade: int) -> list:
#    return [produto, preco, quantidade]
#print(f'\nCriar Estoque')
#print(t'Estoque: {criar_produto('Leite), 8.9, 0}')
