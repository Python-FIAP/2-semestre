#Crie uma função (com def , não lambda) chamada para_maiuscula que receba um texto e
#devolva o mesmo texto em letras maiúsculas. Depois, use map para aplicar essa função a
#toda a lista nomes = ["ana", "bruno", "carla"] .
def para_maiuscula(texto: str) -> str:
    return texto.upper()
nomes = ["ana", "bruno", "carla"]
print(list(map(para_maiuscula, nomes)))