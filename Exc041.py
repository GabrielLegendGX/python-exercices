a=int(input('Em ano você nasceu? '))
ano=2021-a
if ano<=9:
    print('O atleta tem {} anos\nCategoria: Mirim'.format(ano))
elif ano<=14:
    print('O atleta tem {} anos\nCategoria: INFANTIL '.format(ano))
elif ano<=19:
    print('O atleta tem {} anos\nCategoria: JUNIOR '.format(ano))
elif ano<=25:
    print('O atleta tem {} anos\nCategoria: SÊNIOR'.format(ano))
else:
    print('O atleta tem {} anos\nCategoria: MATER'.format(ano))


#9 anos MIRIM
#14 anos INFANTIL
#19 anos JUNIOR
#25 anos SÊNIOR
#Mais MASTER