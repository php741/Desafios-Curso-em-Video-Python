maiores = homens = mulhermenor = idade = 0
sexo = ""
resposta = ""
while True:
    idade = int(input("Informe sua idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Informe seu sexo [F/M]: ")).strip().upper()[0]
    if sexo == "F" and idade < 20:
        mulhermenor = mulhermenor + 1
    if sexo == "M":
        homens = homens + 1
    if idade > 18:
        maiores = maiores + 1
    resposta = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if resposta == "N":
        break

print("{} são maiores de 18 anos, {} são homens e {} mulheres tem menos de 20 anos".format(maiores, homens, mulhermenor))

