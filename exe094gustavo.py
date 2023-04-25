galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo? [M/F]")).strip().upper()
        if pessoa['sexo'] in "MF":
            break
    print("Erro!! Digite apenas M ou F!")
    pessoa['dade'] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
        if resp in "SN":
            break
        print("Erro!! Resonda apenas S ou N!:")
        if resp == "N":
            break
media = soma / len(galera)
