tupla = ("zero", "um", "dois", "três", "quatro", " cinco",
         "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
         "dezoito", "dezenove", "vinte")
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n1 = 0
tamanho = len(tupla)
while True:
    n1 = int(input("Digite um número de 0 a 20: "))
    while n1 not in lista:
        n1 = int(input("Número invalido, por favor digite novamente: "))
    print("Você digitou o número {}".format(tupla[n1]))
    break
