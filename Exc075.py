usuario=int(input('Digite um valor ')),int(input('Digite outro valor ')),int(input('Digite mais um valor ')),int(input('Digite o ultimo valo '))
print(f'Você digitou os valores {usuario}')
print(f'O valor 9 apareceu {usuario.count(9)} vezes')
if 3 in usuario:
    print(f'O numero 3 apareceu na posição {usuario.index(3)+1}')
else:
    print('Não tem valor 3 ')
print('Os valores pares foram',end=' ')
for c in usuario:
    if c % 2 ==0:
        print(f' {c}',end = '' )





'''
for tot in usuario:
    if tot == 9:
        nove+=1
print(f'O numero 9 apareceu {nove} vezes')

for tot in enumerate(usuario):
    if tot == 3:
        usuario.index(3)
    else:
        print('O tres não apareceu')
'''

