valores = []




while True:
    n = int(input("Digite um número: "))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado com sucesso! ")
    else:
        print("Valor ja foi adicionado, não será adicionado novamente.")
    resposta = str(input("Quer Continuar ? [S/N} ")).strip().upper()
    if "N" in resposta:
        break


print(sorted(valores))
