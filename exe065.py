maior = menor = num = soma = media = 0
contador = 0
resposta = "S"

while resposta in "S":
    num = int(input('Insira um valor: '))
    contador = contador + 1
    soma = soma + num
    if contador == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Quer continuar? [S/N]')).strip().upper()
media = soma / contador



print("A média entre os valor foi {}, o maior número é {} e o menor número é {}.".format(media, maior, menor))



