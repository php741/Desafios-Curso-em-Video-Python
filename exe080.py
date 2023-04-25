valores = []
for c in range(0, 5):
    x = int(input(f"Digite um valor: "))
    if c == 0 or x > valores[-1]:
        valores.append(x)
        print("Valor adicionao ao final da lista...")
    else:
        pos = 0
        while pos < len(valores):
            if pos <= valores[-1]:
                valores.insert(pos, x)
                print(f"Valor adicionado na posição {pos} ")
                break



print(valores)
