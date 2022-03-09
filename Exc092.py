dados=dict()
nome=str(input('Nome: '))
nasc=int(input('Ano que nasceu: '))
while True:
    carteira=int(input('Numero da certeira de trabalho(Se não tiver digite 0) '))
    if carteira==0:
        print(f'O nome é {nome}')
        print(f'Tem {2021-nasc} anos')
        break
    else:
        ano=int(input('Ano de contratação '))
        salario=float(input('salario R$ '))
    dados={'nomee':nome, 'idade':2021-nasc, 'Ctps':carteira, 'Salario':salario, 'Aposentadoria': (2021-ano)+35, 'ano':ano}
    print(f'O nome é {dados["nomee"]}')
    print(f'Tem {dados["idade"]} anos')
    print(f'O numero da carteira é {dados["Ctps"]}')
    print(f'O salario é {dados["Salario"]}')
    print(f'Foi contratado em {dados["ano"]}')
    print(f'Vai aposentar com {dados["Aposentadoria"]} anos')
    break

'''nome=str(input('Nome: '))
nasc=int(input('Ano que nasceu: '))
carteira=int(input('Numero da certeira de trabalho(Se não tiver digite 0) '))
ano=2021-nasc
while True:
    if carteira == 0:
        print(f'Nome é {nome}')
        print(f'Tem {ano} anos')
        break
    else:
        ano_contratação=int(input('Ano que foi contratado '))
        salario=float(input('Salarío '))
        print(f'Nome é {nome}')
        print(f'Tem {ano} anos')
        print(f'Foi contratado no ano de {ano_contratação}')
        print(f'Ganha {salario} por mês ')

        aposentadoria=(2021-ano_contratação) + 35
        if ano_contratação > aposentadoria:
            print(f'Você ainda não pode aposentar e vai aposentar com {aposentadoria} anos')
            break
        else:
            print(f'Você já pode aposentar, idade pra aposentar {aposentadoria} anos  ')
            break
'''