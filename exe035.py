a = int(input("Insira o valor da primeira reta :"))
b = int(input("Insira o valor da segunda reta: "))
c = int(input("Insira o valor da terceira reta: "))
if (b -c) < a < b + c and (a - c) < b < a + b and (a - b) < c < a + b :
    print("Sim, é possivel formar um triangulo com essas retas!")
if (a == b and b == c) and ((b -c) < a < b + c and (a - c) < b < a + b and (a - b) < c < a + b):
    print('é um triangulo equilátero!')

elif (a == b and b != c) and ((b -c) < a < b + c and (a - c) < b < a + b and (a - b) < c < a + b):
    print('É um triângulo isóceles!')
elif ((b -c) < a < b + c and (a - c) < b < a + b and (a - b) < c < a + b) and (a !=b and b !=c):
    print('É um triângulo escaleno!')
else:
    print("Não é possivel formar um triangulo com essas retas!")