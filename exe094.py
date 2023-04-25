dic = {}
temp = []
somamulheres = 0
numpessoas = 0
somaidade = 0
mediaidade = 0
while True:
    dic['nome'] = str(input("NOME: "))
    sexo = str(input("SEXO [M/F]: ")).strip().upper()
    if sexo not in "MF":
        sexo = str(input("Você digitiou errado, por favor digite novamente somente [M/F]")).strip().upper()
    if sexo in 'F':
        somamulheres += 1
    if sexo in "MF":
        dic['sexo]'] = sexo
        numpessoas = numpessoas + 1
        idade = int(input("idade:"))
        somaidade = somaidade + idade
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp not in 'SN':
        print("Por favor digite novamente, somente [S/N]")
    if resp in 'N':
        break
mediaidade = somaidade / numpessoas


