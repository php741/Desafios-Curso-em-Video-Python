def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) Mostra o calculo ou não o calculo.
    :return: retorna o valor do fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f"{c}" , end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


print(fatorial(5, show=True))
