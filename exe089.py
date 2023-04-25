lista = []
temp = []
while True:
    temp.append(str(input("Insira o nome do aluno: ")))
    temp.append(float(input("Insira a primeira nota: ")))
    temp.append(float(input("Insira a segunda nota: ")))
    media = (temp[1] + temp[2]) / 2
    temp.append(media)
    lista.append(temp[:])
    temp.clear()
    resposta = str(input("Quer continuar? [S/N]")).strip().upper()
    if "N" in resposta:
        break
print(f"{'No':<10} {'Nome':<10} {'Média':>10}")
for n in range(0, len(lista)):
    print(f" {n:<10} {lista[n][0]:<10} {lista[n][3]:>10}")
while True:
    resp = int(input("Quer ver as notas de qual aluno? [999 interrompe]:"))
    if resp == 999:
        break
    print(f"As notas de {lista[resp][0]} foram {lista[resp][1]} e {lista[resp][2]}")
