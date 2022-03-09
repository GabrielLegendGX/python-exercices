tabu=0
negativo='-'
while True:
    n=int(input('Digite um numero '))
    if n < 0:
        print('Tabuada Encerrada')
        break
    if n !=negativo:
        for c in range (1,11):
            resu= c * n
            print('{} X {}  = {}'.format(n, c , resu))
