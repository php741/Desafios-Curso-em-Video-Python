matriz = []
primeira =[]
segunda = []
terceira = []
for c in range(0, 3):
    primeira.append(int(input(f"Digite um número para a posição [0, {c} ]")))
for c in range(0, 3):
    segunda.append(int(input(f"Digite um número para a posição [1, {c} ]")))
for c in range(0, 3):
    terceira.append(int(input(f"Digite um número para a posição [2, {c} ]")))
matriz.append(primeira)
matriz.append(segunda)
matriz.append(terceira)
for c in range(0, 3):
    print(f"[{(matriz[0][c])}]", end="")
print("\n")
for c in range(0, 3):
    print(f"[{(matriz[1][c])}]", end="")
print("\n")
for c in range(0, 3):
    print(f"[{(matriz[2][c])}]", end="")