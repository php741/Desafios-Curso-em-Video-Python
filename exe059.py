n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
op = int(input(" [1] Somar \n [2] multiplica \n [3] novos números \n [4] sair do programa"))

if op == 1:
    print(" {} + {} = {}".format(n1, n2, n1 + n2))
elif op == 2:
    print('{} x {} = {}'.format(n1, n2, n1*n2))
elif op == 3:
     n1 = int(input("Insira o primeiro valor: "))
     n2 = int(input("Insira o segundo valor: "))
     op = int(input(" [1] Somar \n [2] multiplica \n [3] novos números \n [4] sair do programa"))
     if op == 1:
         print(" {} + {} = {}".format(n1, n2, n1 + n2))
     elif op == 2:
         print('{} x {} = {}'.format(n1, n2, n1 * n2))
     elif op == 3:
         n1 = int(input("Insira o primeiro valor: "))
         n2 = int(input("Insira o segundo valor: "))
         op = int(input(" [1] Somar \n [2] multiplica \n [3] novos números \n [4] sair do programa"))
     elif op == 4:
         print("Tchau! até a proxima!")
elif op == 4:
     print("Tchau! até a proxima!")