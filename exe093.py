dic = {}
dic['nome'] = str(input("Qual o nome do jogador? "))
gols = []
totalp = int(input(f"Quantos jogos o {dic['nome']} jogou? "))
for n in range(1, totalp + 1):
    gols.append(int(input(f"Quantos gols o {dic['nome']} fez na partida {n}?")))
dic["gols"] = gols

soma = 0
for n in gols:
    soma = soma + n
dic['soma'] = soma
print("-=" * 30)
print(dic)
print("-=" * 30)
for k, v in dic.items():
    print(f"O campo {k} tem o valor {v}")

print("-=" * 30)
print(f"O Jogador {dic['nome']} jogou {totalp} partidas!")
for i, v in enumerate(dic['gols']):
    print(f" na partida {i + 1} fez {v} gols.")


