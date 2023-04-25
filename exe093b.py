jogador = {'nome': '', 'gols': 0, 'total':0 }
jogadores = []
gols = []
partidas = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input("Qual o nome do Jogador? "))
    partidas = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
    for n in range(1, partidas + 1):
        gols.append( int(input(f"Quantos gols o {jogador['nome']} fez na {n}a partida? ")))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    resp = str(input("Quer Continuar? [S/N]")).upper()[0]
    if resp not in "SN":
        resp = str(input("Somente S ou N")).upper()[0]
    if resp == "N":
        break
print("-=" *30)
print('cod', end="")
for p in jogador.keys():
    print(f"{p:<15}", end="")
print()

for k, v in enumerate(jogadores):
    print(f" {k:>3}", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("_" * 30)
while True:
    resp = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if resp == 999:
        break
    elif resp >= len(jogadores):
        resp = int(input("codigo inexistente, favor digitar um codigo válido: "))
    else:
        print(f" Levantamento do jogador {jogadores[resp]['nome']}")
        for i, g in enumerate(jogadores[resp]['gols']):
            print(f"No {i+1}o jogo {jogadores[resp]['nome']} fez {g} gols ")
            

