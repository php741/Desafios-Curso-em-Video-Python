pessoas = {'nome':'', 'sexo':'', 'idade':''}
totmulher = []
listpessoas = []
soma = 0
mediaidade = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: "))
    pessoas['sexo'] = str(input("Sexo [M/F]")).strip().upper()
    if pessoas['sexo'] not in "FM":
        pessoas['sexo'] = str(input("Você digitiou errado. Use somente M ou F")).strip().upper()
    pessoas['idade'] = int(input("Idade: "))
    listpessoas.append(pessoas.copy())
    soma += pessoas['idade']
    if pessoas['sexo'] == "F":
        totmulher.append(pessoas.copy())
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == "N":
        break
    if resp not in "SN":
        resp = str(input("Você digitiou errado. somente S ou N "))
mediaidade = soma / len(listpessoas)

print("-=" *30)
print(f"Ao todo temos {len(listpessoas)} pessoas cadastradas.")
print(f"A média de idade é {mediaidade:.2f}")

print(f"As mulheres cadastradas foram {totmulher}")

for p in listpessoas:
    if p['idade'] > mediaidade:
        print(f"As Pessoas com idade acima da média foram {p['nome']} ")
print("-=" *30)

