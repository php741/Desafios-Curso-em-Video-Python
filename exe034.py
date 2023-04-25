sal = float(input("Qual o valor do seu salario? "))
if sal > 1250:
    print("O seu aumento será de R${}.".format(sal * 10/100 ))
    print("O seu novo salário é R${}.".format(sal + (sal*10/100)))
else:
    print("O seu aumento será de R${}.".format(sal * 15/100))
    print("O seu novo salário é de R${}.".format(sal + (sal * 15/100)))

