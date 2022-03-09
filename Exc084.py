lista=list()
listatemp=list()
nome=list()
peso=list()
while True:
    nomee=str(input('Qual é o seu nome? '))
    nome.append(nomee)
    listatemp.append(nomee)
    kg=float(input('Qual é o seu peso? '))
    peso.append(kg)
    listatemp.append(kg)
    continua=str(input('Deseja contnuar? [S/N] ')).upper().split()[0]
    while continua not in 'SN':
        continua=str(input('Opção invalida [S/N] ')).upper().split()[0]
    if continua=='N':
        break
    lista.append(listatemp)
    listatemp.clear
print(f'Foi cadastrada {len(nome)} pessoas ')
maior=max(peso)
menor=min(peso)
print(f'A pessoa mais pesada tem KG {maior}')
print(f'A pessoa mais leve tem KG {menor}')