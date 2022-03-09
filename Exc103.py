def status(gol=0, nome='<Desconhecido>'): 
    if nome == '':
        nome= '<Desconhecido>'
    if gol == '':
        gol='0'
    print(f'O jogador {nome} tem {gol} gols no campeonato')
gols=str(input('Gols '))
jogador=str(input('Nome '))
status(gols,jogador)
