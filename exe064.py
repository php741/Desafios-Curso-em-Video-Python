n = 0
soma = 0
while n != 999:
    n = int(input(" Digite um número, [999 para parar]: "))
    soma = soma + n
    if n == 999:
        soma = soma - 999
        print(" a Soma dos números digitados é {}.".format(soma))