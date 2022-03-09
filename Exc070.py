total=0
milpila=0
menor=0
cont=0
while True:
    produto=str(input('Qual é o nome do produto? '))
    valor=float(input('Qual é o valor do produto?R$ '))
    cont +=1
    total +=valor
    if valor > 1000:
        milpila += 1
    if cont ==1 or valor < menor:
        menor=valor
        barato=produto
    continua=' '
    while continua not in 'SN':
        continua=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print(f'o total da compra foi {total}')
print(f'Temos {milpila} que custa mais de R$1000')
print(f'o produto mais barato foi {barato} custando {menor}')


         
"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário 
vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato."""