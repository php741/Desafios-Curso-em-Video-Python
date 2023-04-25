def ficha(jog="desconhecido", gol=0):
    print(f"O jogador {jog} fez {gol} gol(s). ")


n = str(input("Qual o nome do jogador:"))
g = str(input("gols: "))
if g.isnumeric():
     g = int(g)
else :
    g = 0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)