import random
nc = random.randint(0, 9)
nt = 0
n = nc + 1
while n != nc:
    n = int(input(("Insira um valor de 0 a 9: ")))
    nt = nt + 1
print(" O computador pensou no número {} e você digitiou o número {}, foram necessárias {} tentativas!".format(nc, n, nt))


