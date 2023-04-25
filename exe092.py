from datetime import datetime
dados = {}
dados['nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados["ctps]"] = int(input("Cateira de trabalho [0 não tem]: "))
if dados['ctps'] != 0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados["salario"] = float(input("Salário: "))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - datetime.now().year) + dados['idade']
print(dados)
