n1=int(input('Digite um valor-> '))
n2=int(input('Digite outro valor->'))
opção=0
print('-=-'*10)
while opção != 6:
    print("""    [ 1 ] Somar
    [ 2 ] Subtrair
    [ 3 ] Multiplicar
    [ 4 ] Maior
    [ 5 ] Novos numeros
    [ 6 ] Sair do programa""")
    opção=int(input('Qual é a sua opção? '))
    if 1==opção:
        opção=n1+n2
        print('A soma entre {} e {} é igual a {}'.format(n1,n2,opção))
    elif 2==opção:
        opção=n1-n2
        print('A subtração entre {} e {} é igual a {}'.format(n1,n1,opção))

    elif 3==opção:
        opção=n1*n2
        print('A multiplicação ente {} e {} é igual a {}'.format(n1,n2,opção))
    elif 4==opção:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('Entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif 5==opção:
        print('informe os valores novamente')
        n1=int(input('Digite um valor-> '))
        n2=int(input('Digite outro valor->'))
    
    else:
        print('Opção invalida')
    print('-=-'*10)
print('Valeu falou')