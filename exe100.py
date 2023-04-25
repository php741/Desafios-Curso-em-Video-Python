from random import randint
def sorteio(t, p):
    for c in range(0, 5):
        n = randint(0, 100)
        t.append(n)
        if n % 2 == 0:
            p.append(n)


t = []
p = []
sorteio(t, p)
print(f"Sorteando 5 valores da lista: {t}")
print(f'A soma dos valores pares {p} é igual a {sum(p)}')




