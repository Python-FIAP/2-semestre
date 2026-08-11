def mostrar_informacoes(nome:str, idade:int, cidade:str) -> None:
    print(f'Nome: {nome}, Idade: {idade}, Cidade: {cidade}')

    mostrar_informacoes('Eduardo', 19, 'São Paulo')
    mostrar_informacoes('Abacatudo', 67, 'São Paulo')

    def mostrar_informacoes1(nome:str, idade:int, cidade:str = 'Não Informada') -> None:
        print(f'{nome} - Idade: {idade}, Cidade: {cidade}')
    mostrar_informacoes1('Moranguete', 42)

    def mostrar_informacoes2(nome:str, idade:int, cidade:str = 'Nâo Informada') -> None:
        print(f'{nome} - Idade: {idade}, Cidade: {cidade}')
    mostrar_informacoes2('Sigma', 999)
    pessoa = mostrar_informacoes2('Pessoa', 42)
    print(f'')
