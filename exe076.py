produtos = ("Porsch", 100000, "Casa na florida", 300000, "Casa na Scicilia", 150000, "Sistema de automação", 5000,
            "Arquiteto", 15000, "Tesla", 45000)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}$', end="")
    else:
        print(f"{produtos[item]:>7}")