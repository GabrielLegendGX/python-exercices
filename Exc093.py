gols=list()
nome=str(input('Qual é o nome do jogador? '))
partidas=int(input(f'Quantas partidas {nome} jogou? '))
dicionario={'Jogador':nome, 'jogos': partidas}
for c in range (1,partidas+1):
    gols.append(int(input(f'Quantos gols na partida {c} ')))
    tot_gol = sum(gols)
print('=+'* 30)
print(dicionario, end=' ')
print(f'Gols {gols},Total gols  {tot_gol}')
print('=+'* 30)
print(f'O campo nome tem o valor {dicionario["Jogador"]}')
print(f'O campo gol tem o valor {gols}')
print(f'O campo total tem o valor {tot_gol}')
print('=+'* 30)
for c in range(1,partidas+1):
    print(f'Na partida {c} ele fez {gols[1-c]} gols')
print(f'Ele fez {tot_gol} no total')
print('=+'* 30)
'''print(f'{dicionario["Jogador"]}')
print(f'{dicionario["jogos"]}')
print(f'{dicionario["Gol"]}') '''