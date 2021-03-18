import random
a1=input('Digite o nome do primeiro aluno: ')
a2=input('Digite o nome do segundo aluno: ')
a3=input('Digite o nome do terceiro aluno: ')
a4=input('Digite o nome do quarto aluno: ')
sorteio=[a1,a2,a3,a4]
escolhido=random.choice(sorteio)
print('O aluno sorteado para apagar o quadro foi {}'.format(escolhido))



#import random
#num= random.randint(1, 4)
#aluno= random.Random ('Murilo Gabriel, Julia, Jack')
#print('o {} {} foi o sorteado'.format(aluno, num))