expressao = ""
cont = 0
expressao = (input("Digite a expressão: "))
for c in expressao:
    if c == '(':
        cont = cont + 1
    if c == ')':
        cont = cont - 1
    if cont < 0:
        break
if cont == 0:
    print("Expressão Valida!")
else:
    print("Expressão inválida!")
print(cont)



