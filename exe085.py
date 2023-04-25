lista = []
pares = []
impares = []
n = 0
for c in range(1, 8):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
lista.append(pares)
lista.append(impares)
print(sorted(lista[0]))
print(sorted(lista[1]))
