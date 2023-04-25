lista = []
for c in range(0, 5):
    lista.append(int(input("Digite um número :")))
maiorvalor = max(lista)
menorvalor = min(lista)
print(f"Você digitiou os valores {lista}")
for m, v in enumerate(lista):
    if v == maiorvalor:
        print(f"O maior valor é {max(lista)}, na posição {m}")
    elif v == menorvalor:
        print(f"O menor valor é {min(lista)} na posição {m}")

