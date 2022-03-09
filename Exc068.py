from random import randint
vitoria=0
while True:
    jogador=int(input('Digite um Numero '))
    computador=randint(1, 10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Impar ou Par? [I/P]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} total de {total}')
    if tipo == 'P':
        if total %2 == 0:
            print('Você venceu ')
            vitoria += 1 
        else:
            break
    if tipo == 'I':
        if total %2 == 1:
            print('Você venceu')
            vitoria+=1
        else:
            print('Você perdeu')
            break
print(f'Você venceu {vitoria} vezes ')


#total % 2 == 0 par 
#total % 2 == 1 impar