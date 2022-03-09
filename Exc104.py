def leiaint(n):
    while True:
        n=input('Digite um numero ')
        if n.isnumeric()==True:
            print(f'O numero informado foi {n}')
            break
        else:
            print('\033[1;37;41mColoque um valor inteiro.\033[m ')
n= leiaint('Digite um numero ')