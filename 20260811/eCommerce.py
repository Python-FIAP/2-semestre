# ecommerce.py
# Projeto de fundo - E-commerce simples
# Atividade avaliativa (conteúdo até a Aula 03): login de usuário e menus
# diferenciados.
#
# Complete as funções marcadas com TODO. Não altere as funções já prontas
# (elas vêm da Aula 03 e continuam funcionando exatamente como antes).

from functools import reduce

# ============================================================
# CONSTANTES
# ============================================================

# Índices de cada campo dentro da lista que representa um produto.
NOME = 0
PRECO = 1
ESTOQUE = 2

# TODO: crie as constantes de posição para a lista que representa um
# usuário ([nome, email, senha]). Siga o mesmo padrão usado acima para
# produtos (NOME_USUARIO, EMAIL, SENHA).


# ============================================================
# SISTEMA — produtos (prontas desde a Aula 03, não alterar)
# ============================================================


def cadastrar_produto(
    catalogo: list[list[object]],
    nome: str,
    preco: float,
    estoque: int = 0,
) -> list[list[object]]:
    """Cadastra um novo produto no catálogo.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        nome: nome do produto a ser cadastrado.
        preco: preço unitário do produto.
        estoque: quantidade disponível em estoque. Padrão: 0 (produto
            cadastrado sem estoque inicial).

    Returns:
        O catálogo atualizado, incluindo o novo produto.
    """
    produto: list[object] = [nome, preco, estoque]
    catalogo.append(produto)
    return catalogo


def atualizar_estoque(
    catalogo: list[list[object]],
    nome_produto: str,
    quantidade: int,
) -> list[list[object]]:
    """Atualiza a quantidade em estoque de um produto já cadastrado.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        nome_produto: nome do produto cujo estoque será atualizado.
        quantidade: quantidade a ser somada ao estoque atual (pode ser
            negativa, para representar uma saída de estoque).

    Returns:
        O catálogo atualizado. Se o produto não for encontrado, o
        catálogo é retornado sem alterações.
    """
    for produto in catalogo:
        if produto[NOME] == nome_produto:
            produto[ESTOQUE] += quantidade
            return catalogo
    print(f"Produto '{nome_produto}' não encontrado no catálogo.")
    return catalogo


def exibir_catalogo(catalogo: list[list[object]]) -> None:
    """Exibe todos os produtos cadastrados no catálogo.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].

    Returns:
        None. Apenas imprime os produtos no console.
    """
    for produto in catalogo:
        print(
            f"{produto[NOME]} - R$ {produto[PRECO]:.2f} "
            f"(estoque: {produto[ESTOQUE]})"
        )


def listar_nomes_produtos(catalogo: list[list[object]]) -> list[str]:
    """Lista os nomes de todos os produtos cadastrados no catálogo.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].

    Returns:
        Uma lista com os nomes dos produtos, na mesma ordem do catálogo.
    """
    return [produto[NOME] for produto in catalogo]


def aplicar_reajuste_precos(
    catalogo: list[list[object]],
    percentual: float,
) -> list[list[object]]:
    """Aplica um reajuste percentual ao preço de todos os produtos.

    Gera um novo catálogo (nova matriz) com os preços reajustados,
    sem alterar o catálogo original.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        percentual: percentual de reajuste a ser aplicado. Valores
            positivos aumentam o preço, valores negativos representam
            desconto (ex.: -10 aplica 10% de desconto).

    Returns:
        Um novo catálogo, com os preços reajustados e o nome/estoque
        de cada produto preservados.
    """
    fator = 1 + (percentual / 100)
    return [
        [produto[NOME], round(produto[PRECO] * fator, 2), produto[ESTOQUE]]
        for produto in catalogo
    ]


def calcular_valor_total_estoque(catalogo: list[list[object]]) -> float:
    """Calcula o valor total investido em estoque.

    Soma, para cada produto, o valor de preco * estoque, usando reduce.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].

    Returns:
        O valor total investido em estoque (soma de preco * estoque de
        todos os produtos). Devolve 0.0 se o catálogo estiver vazio.
    """
    return reduce(
        lambda total, produto: total + produto[PRECO] * produto[ESTOQUE],
        catalogo,
        0.0,
    )


# ============================================================
# SISTEMA — produtos (implemente aqui)
# ============================================================


def listar_produtos_baixo_estoque(
    catalogo: list[list[object]],
    limite: int = 10,
) -> list[str]:
    """Lista os nomes dos produtos com estoque abaixo de um limite.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        limite: quantidade mínima de estoque considerada "segura".
            Produtos com estoque menor que esse valor entram no
            resultado. Padrão: 10.

    Returns:
        Uma lista com os nomes dos produtos cujo estoque está abaixo do
        limite informado.
    """
    # TODO: implemente usando list comprehension com condição (visto na
    # Aula 03). Não use um laço "for" tradicional com "if" dentro dele.
    pass


# ============================================================
# SISTEMA — usuários (implemente aqui)
# ============================================================


def cadastrar_usuario(
    usuarios: list[list[str]],
    nome: str,
    email: str,
    senha: str,
) -> list[list[str]]:
    """Cadastra um novo usuário, se o e-mail ainda não estiver em uso.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
            Cada usuário é representado como [nome, email, senha].
        nome: nome do usuário.
        email: e-mail do usuário (deve ser único).
        senha: senha do usuário.

    Returns:
        A lista de usuários atualizada. Se o e-mail já existir, a lista
        é retornada sem alterações.
    """
    # TODO: implemente. Use email_existe para checar duplicidade antes
    # de cadastrar.
    pass


def email_existe(usuarios: list[list[str]], email: str) -> bool:
    """Verifica se já existe um usuário cadastrado com o e-mail informado.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
            Cada usuário é representado como [nome, email, senha].
        email: e-mail a ser verificado.

    Returns:
        True se o e-mail já estiver cadastrado, False caso contrário.
    """
    # TODO: implemente.
    pass


def fazer_login(
    usuarios: list[list[str]],
    email: str,
    senha: str,
) -> list[str] | None:
    """Verifica as credenciais e retorna o usuário correspondente.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
            Cada usuário é representado como [nome, email, senha].
        email: e-mail informado no login.
        senha: senha informada no login.

    Returns:
        A lista do usuário [nome, email, senha] se as credenciais
        conferirem, ou None caso contrário.
    """
    # TODO: implemente.
    pass


# ============================================================
# MENUS (implemente aqui)
# ============================================================


def menu_cadastrar_usuario(usuarios: list[list[str]]) -> list[list[str]]:
    """Pede nome, e-mail e senha ao usuário e chama cadastrar_usuario.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.

    Returns:
        A lista de usuários atualizada.
    """
    # TODO: implemente.
    pass


def menu_login(usuarios: list[list[str]]) -> list[str] | None:
    """Pede e-mail e senha, chama fazer_login e informa o resultado.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.

    Returns:
        O usuário logado (lista [nome, email, senha]) se o login deu
        certo, ou None caso contrário.
    """
    # TODO: implemente.
    pass


def menu_produtos(catalogo: list[list[object]]) -> None:
    """Exibe o catálogo de produtos.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.

    Returns:
        None.
    """
    # TODO: implemente (chame exibir_catalogo).
    pass


def menu_logout() -> None:
    """Informa que o logout foi realizado com sucesso.

    Returns:
        None.
    """
    # TODO: implemente.
    pass


def menu_usuario_nao_logado(
    usuarios: list[list[str]],
    catalogo: list[list[object]],
) -> str | list[str] | None:
    """Menu mostrado a quem ainda não fez login.

    Opções: cadastrar usuário, fazer login, ver produtos, sair.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
        catalogo: matriz (lista de listas) com os produtos do e-commerce.

    Returns:
        "SAIR" se o usuário escolheu sair, o usuário logado (lista) se o
        login deu certo, ou None caso contrário.
    """
    # TODO: implemente.
    pass


def menu_usuario_logado(
    usuario_logado: list[str],
    catalogo: list[list[object]],
) -> str | list[str] | None:
    """Menu mostrado a quem já está logado.

    Opções: ver produtos, logout, sair.

    Args:
        usuario_logado: usuário atualmente logado ([nome, email, senha]).
        catalogo: matriz (lista de listas) com os produtos do e-commerce.

    Returns:
        "SAIR" se o usuário escolheu sair, None se fez logout, ou o
        próprio usuario_logado caso continue logado.
    """
    # TODO: implemente.
    pass


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":
    # Catálogo inicial de produtos (você pode reaproveitar os dados da
    # Aula 03 ou cadastrar os seus).
    catalogo: list[list[object]] = []
    catalogo = cadastrar_produto(catalogo, "Camiseta Azul", 59.90, 120)
    catalogo = cadastrar_produto(catalogo, "Tênis Runner", 199.90, 60)
    catalogo = cadastrar_produto(catalogo, "Boné Preto", 39.90, 50)

    usuarios: list[list[str]] = []
    usuario_logado: list[str] | None = None

    # TODO: implemente o loop principal (while True) do programa.
    # Enquanto usuario_logado for None, chame menu_usuario_nao_logado.
    # Caso contrário, chame menu_usuario_logado.
    # Trate o retorno "SAIR" para encerrar o loop.
