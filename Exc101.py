nascimento=int(input('Em que ano você nasceu? '))
nascimento=2022- nascimento
while True:
    if nascimento >=65:
        print(f'Você tem {nascimento} anos, voto opcional ')
        break
    if nascimento >=18:
        print(f'você tem {nascimento} anos, Voto obrigatorio')
        break
    if nascimento <=17:
        print(f' você tem {nascimento} anos, Não vota')
        break



#65+ anos voto opcional