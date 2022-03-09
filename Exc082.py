valores=list()
impares=list()
pares=list()
while True:
    n = int(input('Digite um numero '))
    valores.append(n)
    escolha=str(input('deseja continuar?[S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha= str(input('Opção invalida, digite novamente [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
for c,v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {valores}')
print(f'Os numeros pares são {pares}')
print(f'Os numeros impares são {impares}')