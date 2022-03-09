numero=int(input('Digite um numero que você quer saber a tabuada: '))
for c in range (1,11):
    resu= c * numero
    print('{} X {}  = {}'.format(numero, c , resu))
     
#ou

"""numero=int(input('Digite um numero que você quer saber a tabuada: '))
for c in range (1,11):
    resu= c * numero
    print(f'{numero} X {c}  = {resu}')
"""