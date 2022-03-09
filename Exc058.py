import random
pc = random.randint(1, 10)
acertou= False
palpite=0 #VER QUANTAS TENTATIVAS
print('Pensei em um numero de 1 a 10 tente adivinhar ele ')
while not acertou:
    vc=int(input('Digite um numero -> '))
    palpite += 1
    if vc==pc:
        acertou=True
    else:
        if vc < pc:
            print('Mais...')
        else:
            print('Menos...')
print('Você acertou com {} Tentativas'.format(palpite))