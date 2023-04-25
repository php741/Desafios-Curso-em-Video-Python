import random
s = 0
escolha = ''
x = 0
print("Vamos jogar par ou impar! ")
while True:
    n = int(input("Escolha um número: "))
    comp = random.randint(0, 10)
    s = n + comp
    escolha = str(input("Você quer par ou ímpar, [P/I]: ")).strip().upper()
    if escolha == "P" and s % 2 == 0:
        print(" Você escolheu {} e o computador escolheu {}".format(n, comp))
        print("Parabéns Você venceu!")
        x = x + 1
    elif escolha == "I" and s % 2 == 0:
        print(" Você escolheu {} e o computador escolheu {}".format(n, comp))
        print("Você perdeu!")
        break
    elif escolha == "P" and s % 2 != 0 :
        print(" Você escolheu {} e o computador escolheu {}".format(n, comp))
        print("Você perdeu!")
        break
    elif  escolha == "I" and s % 2 != 0:
        print(" Você escolheu {} e o computador escolheu {}".format(n, comp))
        print("Parabéns Você venceu!")
        x = x + 1
print(" Você ganhou {} vezes!".format(x))


