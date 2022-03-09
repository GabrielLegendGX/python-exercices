primeiro=int(input('Digite o primeiro termo: '))
razão=int(input('Razão: '))
decimo= primeiro
cont=1
total=0
mais=10
while mais!=0:
    total=total + mais
    while cont <= total:
        print('{}'.format(decimo),end='-> ')
        decimo+=razão
        cont+=1
    mais=int(input('\nQuantos termos você quer saber a mais? '))
print('A progressão terminou com {} termos mostrado'.format(total))