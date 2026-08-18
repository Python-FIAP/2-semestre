#Dada a lista precos = [100.0, 250.0, 39.90] , use map com uma função lambda para gerar
#uma nova lista com 10% de desconto aplicado a cada preço
preços = [100.0, 250.0, 39.90]
descontos = print(list(map(lambda n: n * round(0.9, 2), preços)))