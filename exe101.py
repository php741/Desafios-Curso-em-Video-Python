
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return (f'Com {idade} anos, Não Vota!!')
    elif 16 <= idade < 18 or idade >= 65:
        return (f'Com {idade} anos, o Voto é Opcional!')
    else:
         return (f"Com {idade} anos, o voto é OBRIGATORIO")


ano = int(input("Em que ano você nasceu? "))
print(voto(ano))