maior=0
menor=11
from random import randint
numeros=randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10)
for item in numeros:
    if item == 1:
        maior=item
        menor=item
    else:
        if item > maior:
            maior = item
        if item < menor:
            menor = item
print(f'os numeros sorteados foi {numeros}')
print(f'o menor valor é {menor}')
print(f'o maior valor é {maior}')
        
print(f'O maior foi {max(numeros)}')
print(f'O menor foi {min(numeros)}')


'''umeros=randint(1,10)
A=randint(1, 10)
B=randint(1, 10)
C=randint(1, 10)
D=randint(1, 10)
E=randint(1, 10)
'''