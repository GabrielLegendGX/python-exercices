print('CAIXA ELETRONICO')
valor=int(input('Que valor você quer sacar?'))
total=valor
ced=50
totalced=0
while True:
    if total >=ced:
        total -=ced
        totalced+=1
    else:
        if totalced > 0:
            print(f'Total de {totalced} notas de {ced}')
        if ced == 50:
            ced=20
            totalced=0
        elif ced == 20:
            ced=10
            totalced=0
        elif ced == 10:
            ced=1
            totalced=0
        else:
            break
        
