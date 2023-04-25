d = float(input("Qual a ditância da sua viagem em Km? "))
if d <= 200:
    valor = d * 0.5
else:
    valor = d * 0.45
print("A sua passagem vai custar R${}".format(valor))
