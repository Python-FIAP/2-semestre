#Funcoes outros temas

#Parametros

def calcular_media (python:float, webdev:float, frontend:float,) ->float:
    """
    Calcula a media de python, webdev, frontend
    Args
        :param python: nota de python
        :param frontend: nota de frontend
        :param webdev: nota de webdev

        :return: media de python, webdev, frontend

    """
    return (python + webdev + frontend) / 3

#durante o uso definimos se a passagem de parametro sera nomeada ou posiciona
media = calcular_media(9, 8, 9.5)
#racional posicional
#1 posição a nota 9 se refere a nota de python
#2 posição a nota se refere a nota de webdev
#3 posição a nota se refere a nota de frontend
print(f'Media {media:.1f}')

#parametros nomeados
media = calcular_media(9, 8, 9.5)
print(f'Media {media:.1f}')

#cuidado com a mistura
# media = calcular_media(python=9.5, 8, 7)
# print(f'Media {media:.1f}')

#funciona parametro posicional na frente de nomeado
media = calcular_media(python=9.5, webdev=8, frontend=8.5)
print(f'Media {media:.1f}')
