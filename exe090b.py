aluno = {"nome":"", "media": 0, "situacao": ""}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Qual foi a média de {aluno['nome']}?"))
if aluno['media'] >= 7:
    aluno['situacao'] = "Aprovado"
elif aluno['media'] < 7 and aluno['media'] >= 5:
    aluno['situacao'] = "Recuperação"
else:
    if aluno['media'] < 5:
        aluno['situacao'] = "Reprovado"
print(f"Nome é igual {aluno['nome']} a média é igual a {aluno['media']} e a situação é igual a {aluno['situacao']} ")









