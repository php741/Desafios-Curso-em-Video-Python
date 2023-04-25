from random import randint
from operator import itemgetter
from time import sleep


jogadores = {"jogador1": randint(1, 6),
       "jogador2": randint(1, 6),
       "jogador3": randint(1, 6),
       "jogador4": randint(1, 6)}
ranking = []
print(f"Valores Sorteados!!")
for k, v in jogadores.items():
       print(f"O jogador {k} tirou {v}")
       sleep(0.7)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("==RANKING==")
for i, v in enumerate(ranking):
       print(f"  {i+1} lugar  {v[0]} com {v[1]}")



