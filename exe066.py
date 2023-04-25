n = 0
s = 0
c = 0
while True:
    n = int(input("Digite um valor: "))
    c += 1
    if n == 999:
        break
    s += n
print(f"A Soma dos números digitados é {s} e foram digitados {c} números.")