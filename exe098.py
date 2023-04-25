from time import sleep
def pg(a, b, c=-1):
    if a > b:
        for a in range(a, b - 1, -c):
            print(f"{a} ", end="")
            sleep(0.2)
            return a, b, c

    else:
        for a in range(a, b+1, c):
            print(f"{a} ", end="")
            sleep(0.2)
            return a, b, c


    print()
    print("-=" * 30)


pg(1, 10, 1)
pg(10, 0, 2)

print("agora é sua vez de realizar a contage!!")
a = int(input("Inicio: "))
b = int(input("Fim: "))
c = int(input("Passo: "))
if c == 0:
    pg(a, b, c=-1)
else:
    pg(a, b, c)



