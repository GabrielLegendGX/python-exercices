numeros=list()
from random import randint
def sorteia():
    for c in range(1,6):
        numeros.append(randint(0,10))

def somaPar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(soma)
sorteia()
print(numeros)
print('A soma dos valores pares é')
somaPar(numeros)