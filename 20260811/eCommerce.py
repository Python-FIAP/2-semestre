#1a cadastrar produto
#parametros: catalogo, produto, valor, quantidade
#Exemplo depois de cadastrar
#[('Camiseta Azul', 89.90, 50)], [('Cachecol', 35.00, 30)]
NOME = 0
PRECO = 1
ESTOQUE = 2

# catalogo = []
# def cadastrar_produto(catalogo, nome, preco, estoque):
#    nome = input("Digite seu produto: ")
#    preco = float(input("Insira o valor do produto: "))
#    estoque = float(input("Insira a quantia em estoque: "))
#
#    produto = [nome, preco, estoque]
#    catalogo.append(produto)
# cadastrar_produto(catalogo, NOME, PRECO, ESTOQUE)
# cadastrar_produto(catalogo, NOME, PRECO, ESTOQUE)
# print(catalogo)

def cadastrar_produto(catalogo:list[list[object]],
                      nome:str, preco:float, estoque:int) -> list[list[object]]:
    """Cadastra um produto em um catalogo
    Params:
    :catalogo: lista de produtos
    :nome: nome do produto
    :preco: preco do produto
    :estoque: quantia em estoque

    return:lista de produtos cadastrados"""


    catalogo.append([nome, preco, estoque])
    return catalogo

#2a funcao
#Exibir o que esta no catalogo
#Exemplo: Camiseta Azul - R$89.90 (estoque:50)

loja = [['Camiseta Azul', 89.90, 50], ['Tenis Runner',349.99, 80]]

def exibir_catalogo(catalogo:list[list[object]]) -> None:
    for produto in catalogo:
        print(f'{produto[NOME]} - R${produto[PRECO]:.2f} (estoque: {produto[ESTOQUE]})')
exibir_catalogo(loja)



# loja = []
# produto = input("Insira o nome do produto: ")
# valor = float(input("Insira o valor do produto: "))
# qtde = int(input("Insira a quantia de produtos: "))
# cadastrar_produto(loja,produto,valor,qtde)
# print(produto, valor, qtde)
