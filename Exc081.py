num=list()
while True:
    n=int(input('Digite um numero -> '))
    num.append(n)

    escolha=str(input('deseja continuar?[S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha= str(input('Opção invalida, digite novamente [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
if 5 in num:
    print('O numero 5 foi encontrado na lista')
else:
    print('O numero 5 não foi encontrado na lista')
num.sort(reverse=True)
print(f'Os numeros em forma decrescente {num}')