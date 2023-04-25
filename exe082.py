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
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os valores digitados foram {lista}')
print(f"os valores pares foram {pares}")
print(f"Os valores impares foram {impares}")