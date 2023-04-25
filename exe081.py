lista = []
resposta = ""
while True:
    lista.append(int(input("Digite um valor: ")))
    resposta = str(input("Quer continuar? [S/N]")).strip().upper()
    if "N" in resposta:
        break
print(f"foram digitados {len(lista)} valores")
print(f"O valores digitados em ordem foram: {sorted(lista)}")
if 5 in lista:
    print("O valor 5 foi digitado")
else:
    print("O valor 5 não foi digitado")