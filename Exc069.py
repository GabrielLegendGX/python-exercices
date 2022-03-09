maioridade=0
homen=0
mulhermaior=0
while True:
    idade=int(input('Digite a sua idade '))
    if idade >= 18:
        maioridade+=1
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Digite o seu sexo [M/F]')).upper().strip()[0]
        if sexo == 'M':
            homen+=1
        elif sexo == 'F' and idade < 20:
            mulhermaior+=1
    continua=' '
    while continua not in 'SN':
        continua=str(input('Deseja continua: [S/N]')).strip().upper()[0] 
    if continua == 'N':
        break
print("""Foram cadastradas {} pessoas com mais de 18 anos
Foram cadastrados {} homens
Tem {} mulheres com menos de 20 anos""".format(maioridade,homen,mulhermaior))