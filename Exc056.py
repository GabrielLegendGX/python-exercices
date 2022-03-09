somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
mulher20=0
for c in range (1,5):
    print('____{} Pessoa____'.format(c))
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).upper()
    somaidade += idade 
    if c == 1 and sexo in 'M': 
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'F' and idade < 20:
        mulher20 += 1

mediaidade= somaidade/4
print('A media de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho,maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos '.format(mulher20))