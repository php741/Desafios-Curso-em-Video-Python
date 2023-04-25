print("Gerador de PA")
print("-=" *10)
pt = int(input("Qual o primeiro termo: "))
rz = int(input("Qual a razão da PA? "))
c = 1
termo = pt
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print("{}-->".format(termo), end='')
        c = c + 1
        termo = termo + rz
    print("PAUSA")
    mais = int(input('Quantos termos a mais você quer ver? '))
print("Você visualizou {} termos no total.".format(total))





