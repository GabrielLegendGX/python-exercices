from random import randint
import time 
lista = list()
n = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, n):
    for i in range(0, 6):
        time.sleep(0.2)
        num = randint(1, 60)
        if num in lista:
            novo = randint(1, 60)
            lista.append(novo)
        else:
            lista.append(num)
    lista.sort()
    print(f'Jogo {c + 1}: {lista}')
    lista.clear()