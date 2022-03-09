def leiaint(n):
    while True:
        try:
            n=input('Digite um numero ')
            if n.isnumeric()==True:
                print(f'O numero informado foi {n}')
                break
            else: 
                print('\033[1;37;41mColoque um valor inteiro.\033[m ')
        except (KeyboardInterrupt):
            print('O usuario preferiu não digitar esse numero')
            break

n= leiaint('Digite um numero ')
