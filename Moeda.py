from math import fabs


def dobro(n):
    return n*2
def metade(n):
    return n/2
def aumenta10(n):
    return n+(n*10/100)
def reduz13(n):
    return n-(n*5/100)
def resumo(n,p1,p):
    print('-'*20)
    print('Resumo do Valor')
    print('-'*20)
    print(f'O dobro é         R${n*2}')
    print(f'A metade é        R${n/2}')
    print(f'{p1}% de Aumento: R${n*(1+(p1/100))}')
    print(f'{p} % de Redução:  R${n*(1-(p/100))}')

