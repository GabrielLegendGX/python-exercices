dias=int(input('Quantos dias alugado? '))
km=float(input('Quantos km foi percorrido? '))
total= (dias * 60) + (km * 0.15)
print('O valor total a se pagar é {}'.format(total)) 

#ou

dia=int(input('Quantos dias alugado? '))
distancia=float(input('Quantos km for percurrido? '))
x=dia*60
z=distancia*0.15
print('o total a se pagar é {}'.format(x + z))