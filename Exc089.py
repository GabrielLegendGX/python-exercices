lista=list()
lista_temporaria=list()
notas=list()
notas_separadas=list()
num=0
while True:
    nome=str(input('Nome: '))
    num +=1
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    notas_separadas.append(nota1)
    notas_separadas.append(nota2)
    conta=(nota1+nota2) / 2#MEDIA
    notas.append(conta)

    lista_temporaria.append(nome)
    lista_temporaria.append(nota1)
    lista_temporaria.append(nota2)
    lista.append(lista_temporaria[:])
    lista_temporaria.clear()
    continua=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continua not in 'SN':
        continua=str(input('Opção invalida, deseja continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
contador=0
print('x-'*25)
print('Num\t NOME \t\tMEDIA ')
for p in lista:
    contador+=1
    print(f'{contador - 1}',end='\t')
    print(f'{p[0]}',end='\t\t')
    print(p[1])
print('x-'*25)
while True:
    aluno=int(input('Coloque o numero do aluno que você quer ver[digite 999 para encerrar o programa] '))
    if aluno == 999:
        break
    else:
        print(lista[aluno])
print('volte sempre')