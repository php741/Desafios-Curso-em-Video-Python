from datetime import datetime

dic = {'nome': '', 'ctt': 0, "ano": 0, "sal": 0, "aposentadoria": 0, 'nasc': 0, 'idade': 0}



dic['nome'] = str(input("Nome: "))
dic['nasc'] = int(input("Ano de nascimento: "))
dic['idade'] = (datetime.now().year - dic['nasc'])
dic['ctt'] = int(input("Carteira de Trabalho: "))
if dic['ctt'] == 0:
    print(f"- Nome tem o valor {dic['nome']}  idade tem o valor {dic['idade']}")
else:
    dic['ano'] = int(input("Ano de contratação: "))
    dic['sal'] = float(input("Salário: "))
    dic['aposentadoria'] = dic['ano'] + 30 - dic['nasc']
    for k, v in dic.items():
        print(f'  {k} tem o valor  {v}')


