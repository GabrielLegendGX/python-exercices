compras=('Caderno',10.00,'Lapis',0.50,'Celular',500.00,'Livro',50.50,'Cubo Magico',25.90,'Teclado',150.00)
print(30*'-=')
print('Listagem de preços')
print(30*'-=')
for c in range(0,len(compras)):
    if c % 2 == 0:
        print(f'{compras[c]:.<40}',end=' ')
    else:
        c % 2 == 1
        print(f'R$ {compras[c]:>6.2f}')