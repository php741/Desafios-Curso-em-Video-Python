lista = []
pares= []
impares = []
resposta = ""
while True:
    n =int(input("Digite um valor: "))
    resposta = str(input("Quer continuar? [S/N]")).strip().upper()
    lista.append(n)
    if "N" in resposta:
        break
for p in lista:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print(f'Os valores digitados foram {lista}')
print(f"os valores pares foram {pares}")
print(f"Os valores impares foram {impares}")