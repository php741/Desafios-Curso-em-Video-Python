from random import randint
from time import sleep
lista = []
jogo = []
n1 = int(input("Quantos jogos você quer que sorteie: "))
for j in range(1, n1+1):
    for n in range(1, 7):
        n2 = randint(1, 60)
        if n2 not in jogo:
            jogo.append(n2)
    lista.append(jogo[:])
    jogo.clear()
print("-"*30)
print("MEGA SENA DO PEDRINHO" )
print("-"*30)
for c in range(0, n1):
    print(lista[c])
    sleep(1)
print("-"*30)
print("BOA SORTE!!")

