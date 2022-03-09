gols=list()
lista=list()
Jogador=dict()
while True:
    Jogador['nome']=input(str('Qual é o nome do jogador?'))
    partidas=int(input(f'Quantas partidas {Jogador["nome"]} jogou? '))
    for c in range (1,partidas+1):
        Jogador['gols']=(int(input(f'Quantos gols na partida {c} ')))
        gols.append(Jogador['gols'])
        tot_gol = sum(gols)
    continua=str(input('Deseja continua? [S/N]' )).upper().strip()[0]
    if continua == 'N':
        lista.append(Jogador)
        Jogador.clear()
        break
print('=+'* 30)
print(gols)
print(Jogador)
print(tot_gol)
print(lista)

#while True:
#   jogador=int(input('Coloque o numero do jogador que você quer ver, para finalizar digite [999] '))
#  print(['jogador'])