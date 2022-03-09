galera=list()
pessoas=dict()
media=list()
while True:
    pessoas.clear
    pessoas['Nome']=str(input('Nome: '))
    pessoas['Sexo']=str(input('Sexo[M/F] ')).upper().strip()[0]
    if pessoas['Sexo'] not in 'MF':
        pessoas['Sexo']=str(input('Sexo[M/F] ')).upper().strip()[0]       
    pessoas['Idade']=int(input('Idade '))
    media.append(pessoas['Idade'])
    continua=str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    galera.append(pessoas.copy())
    while continua not in 'SN':
        continua=str(input('Opção invalida, tente novamente (S/N)')).upper()[0]
    if continua == 'N':
        break
                # != é diferente    
print(f'Foram cadastrados {len(galera)} pessoas')
media=sum(media) / len(galera)
print(f'A media de idade foi {media}')
print('Pessoas do sexo feminino são')
for p in galera:
    if pessoas['Sexo'] in 'F':
        print(p)
print('As pessoas que está em cima da media é ')
for p in galera:
    if p['Idade'] >= media:
        print(p)