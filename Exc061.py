primeiro=int(input('Digite o primeiro termo: '))
razão=int(input('Razão: '))
decimo= primeiro
cont=1
while cont <= 10:
    print('{}'.format(decimo),end='-> ')
    decimo+=razão
    cont+=1
print('Fim')