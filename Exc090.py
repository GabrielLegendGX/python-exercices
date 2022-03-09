nome_aluno=str(input('Nome: '))
media_aluno=float(input('Média: '))
escola={'nome':nome_aluno,
'media':media_aluno}
print(f'Nome é igual {escola["nome"]}')
print(f'Média é igual a {escola["media"]} ')
if media_aluno <=4.9:
    print('Situação é igual a Reprovado')
else:
    print('Situação é igual a Aprovado')