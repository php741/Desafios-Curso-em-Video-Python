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
print("-=" *30)
print(f"[{(matriz[0][0])}][{(matriz[0][1])}][{(matriz[0][2])}]")
print(f"[{(matriz[1][0])}][{(matriz[1][1])}][{(matriz[1][2])}]")
print(f"[{(matriz[2][0])}][{(matriz[2][1])}][{(matriz[2][2])}]")
print("-=" *30)
soma = 0
for p in matriz:
    for s in p:
        if s % 2 == 0:
            soma = soma + s
print(f"A soma dos valores pares é {soma}")
stc = (matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])
print(f"A soma da terceira coluna é {stc}")
mv = 0
if (matriz[1][0]) > (matriz[1][1]) and  (matriz[1][0]) > (matriz[1][2]):
    mv = (matriz[1][0])
elif (matriz[1][1]) > (matriz[1][0]) and  (matriz[1][1]) > (matriz[1][2]):
    mv = (matriz[1][1])
elif (matriz[1][2]) > (matriz[1][0]) and (matriz[1][2]) > (matriz[1][1]):
    mv =  (matriz[1][2])
print(f"O maior valor da segunda linha é {mv}")
print("-=" *30)



