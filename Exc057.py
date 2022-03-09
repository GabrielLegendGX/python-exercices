sexo=str(input('Digite se usexo [M/F]')).upper()[0]
while sexo not in 'MF':
    sexo=str(input('Sexo invalido, coloque M ou F: ')).upper()[0]
print('Sexo {} registrado com seucesso'.format(sexo))
    