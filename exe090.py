dados = {"nome":"", "idade": 0}
dados["nome"] = str(input("Nome: "))
dados["média"] = float(input(f"Qual foi a média de {dados['nome']} "))
print(f"O nome é igual a {dados['nome']}, a média é igual a {dados['média']}")
if dados["média"] >= 7:
    print('A situação é aprovado')
else:
    print("A situação é reprovado.")