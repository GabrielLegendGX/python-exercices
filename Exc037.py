n = int(input('Digite um número:'))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Digite sua opção:'))

if opção == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))

elif opção == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))

elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))

else:
    print('Essa opção não existe....')