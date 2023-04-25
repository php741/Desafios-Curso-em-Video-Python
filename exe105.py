def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: notas(quantas quiser)
    :param sit: Boa, Razoavel ou ruim
    :return: dicionário contendo a maior nota, a menor e a média e a situação se sit=True
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = "Boa"
        elif r["media"] >=5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = "ruim"
    return r

resposta = notas(3, 5, 3, 7, 9 , 8,  sit=True)
print(resposta)
help(notas)




