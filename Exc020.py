import random
print('QUEM VAI APRESENTAR PRIMEIRO O TRABALHO?')
a1=input('Digite o nome do primeiro grupo:')
a2=input('Digite o nome do segundo grupo:')
a3=input('Digite o nome do terceiro grupo:')
a4=input('Digite o nome do quarto grupo:')
grupos=[a1,a2,a3,a4]
random.shuffle(grupos)
print('A ordem de apresentação vai ser')
print(grupos)
