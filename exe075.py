n1 = (int(input("Insira o primeiro número: ")),
        int(input("Insira o segundo número: ")),
        int(input("Insira mais um número: ")),
        int(input("Insira o ultimo número: ")))
print("Você digitou os valores {}".format(n1))
print(f"Voce digitou o número 9, {n1.count(9)} vezes")
if 3 in n1:
    print(f"O valor 3 apareceu primeiro na posição {n1.index(3) +1} ")
else:
    print("O número 3 não foi digitado")
print(f"O número par digitado foi ", end="")
for n in n1:
    if n % 2 == 0:
        print(f"{n}, ", end="")



